"""Phase F: targeted tests for uncovered BSW handler methods in ARXMLParser.

Each test directly invokes a single BSW-related handler method on `ARXMLParser`
with a minimal XML snippet, lifting coverage on the BSW module description,
module entry, internal behavior, entities, events, call points and reception
policies (parser/arxml_parser.py lines 461-1148).

The dispatch tests in test_arxml_parser_dispatch.py only route these elements
to their handlers; Group E in test_arxml_parser_handlers.py covers a small
subset (readBswVariableAccess and the data send/receive points). This file
covers the remaining BSW surface.
"""

import logging
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


@pytest.fixture
def warning_parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


def _autosar_root():
    return AUTOSAR.getInstance()


# ==================== BswModuleDescription building blocks ====================


class TestBswModuleDescriptionHandlers:
    """Exercise the readBswModuleDescription orchestrator and its sub-readers."""

    def test_readBswModuleDescriptionImplementedEntryRefs_adds_ref(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e1</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, desc)
        assert len(desc.getImplementedEntryRefs()) == 1

    def test_readBswModuleDescriptionImplementedEntryRefs_empty_ref_skipped(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL></BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, desc)
        assert len(desc.getImplementedEntryRefs()) == 0

    def test_readModeDeclarationGroupPrototype_sets_type_tref(self, parser):
        from armodel.models import ModeDeclarationGroupPrototype

        proto = ModeDeclarationGroupPrototype(
            parent=_autosar_root(), short_name="mg"
        )
        element = _snip(
            "<SHORT-NAME>mg</SHORT-NAME>"
            "<TYPE-TREF DEST='MODE-DECLARATION-GROUP'>/tg</TYPE-TREF>",
            root_tag="MODE-DECLARATION-GROUP-PROTOTYPE",
        )
        parser.readModeDeclarationGroupPrototype(element, proto)
        assert proto.getTypeTRef().getValue() == "/tg"

    def test_readBswModuleDescriptionProvidedModeGroups_creates_group(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-MODE-GROUPS>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE><SHORT-NAME>pmg</SHORT-NAME></MODE-DECLARATION-GROUP-PROTOTYPE>"
            "</PROVIDED-MODE-GROUPS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionProvidedModeGroups(element, desc)
        assert len(desc.getProvidedModeGroups()) == 1

    def test_readBswModuleDescriptionProvidedModeGroups_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-MODE-GROUPS><BAD/></PROVIDED-MODE-GROUPS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionProvidedModeGroups(element, desc)
        assert any("Unsupported ProvidedModeGroup" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionRequiredModeGroups_creates_group(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-MODE-GROUPS>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE><SHORT-NAME>rmg</SHORT-NAME></MODE-DECLARATION-GROUP-PROTOTYPE>"
            "</REQUIRED-MODE-GROUPS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionRequiredModeGroups(element, desc)
        assert len(desc.getProvidedModeGroups()) == 1

    def test_readBswModuleDescriptionRequiredModeGroups_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-MODE-GROUPS><BAD/></REQUIRED-MODE-GROUPS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionRequiredModeGroups(element, desc)
        assert any("Unsupported RequiredModeGroup" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionReleasedTriggers_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<RELEASED-TRIGGERS>"
            "<TRIGGER><SHORT-NAME>rt</SHORT-NAME></TRIGGER>"
            "</RELEASED-TRIGGERS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionReleasedTriggers(element, desc)
        assert len(desc.getReleasedTriggers()) == 1

    def test_readBswModuleDescriptionReleasedTriggers_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<RELEASED-TRIGGERS><BAD/></RELEASED-TRIGGERS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionReleasedTriggers(element, desc)
        assert any("Unsupported Released Trigger" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionRequiredTriggers_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-TRIGGERS>"
            "<TRIGGER><SHORT-NAME>qt</SHORT-NAME></TRIGGER>"
            "</REQUIRED-TRIGGERS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionRequiredTriggers(element, desc)
        assert len(desc.getRequiredTriggers()) == 1

    def test_readBswModuleDescriptionRequiredTriggers_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-TRIGGERS><BAD/></REQUIRED-TRIGGERS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionRequiredTriggers(element, desc)
        assert any("Unsupported Required Trigger" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionProvidedDatas_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-DATAS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>pd</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</PROVIDED-DATAS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionProvidedDatas(element, desc)
        assert len(desc.getProvidedDatas()) == 1

    def test_readBswModuleDescriptionProvidedDatas_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-DATAS><BAD/></PROVIDED-DATAS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionProvidedDatas(element, desc)
        assert any("Unsupported Provided Data" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionRequiredDatas_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-DATAS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>rd</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</REQUIRED-DATAS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionRequiredDatas(element, desc)
        assert len(desc.getRequiredDatas()) == 1

    def test_readBswModuleDescriptionRequiredDatas_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-DATAS><BAD/></REQUIRED-DATAS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionRequiredDatas(element, desc)
        assert any("Unsupported Required Data" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionProvidedClientServerEntries_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-CLIENT-SERVER-ENTRYS>"
            "<BSW-MODULE-CLIENT-SERVER-ENTRY><SHORT-NAME>pce</SHORT-NAME></BSW-MODULE-CLIENT-SERVER-ENTRY>"
            "</PROVIDED-CLIENT-SERVER-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionProvidedClientServerEntries(element, desc)
        assert len(desc.getProvidedClientServerEntries()) == 1

    def test_readBswModuleDescriptionProvidedClientServerEntries_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<PROVIDED-CLIENT-SERVER-ENTRYS><BAD/></PROVIDED-CLIENT-SERVER-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionProvidedClientServerEntries(element, desc)
        assert any("Unsupported Provided Client Server Entry" in r.getMessage() for r in caplog.records)

    def test_readBswModuleDescriptionRequiredClientServerEntries_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-CLIENT-SERVER-ENTRYS>"
            "<BSW-MODULE-CLIENT-SERVER-ENTRY><SHORT-NAME>rce</SHORT-NAME></BSW-MODULE-CLIENT-SERVER-ENTRY>"
            "</REQUIRED-CLIENT-SERVER-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionRequiredClientServerEntries(element, desc)
        assert len(desc.getRequiredClientServerEntries()) == 1

    def test_readBswModuleDescriptionRequiredClientServerEntries_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<REQUIRED-CLIENT-SERVER-ENTRYS><BAD/></REQUIRED-CLIENT-SERVER-ENTRYS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionRequiredClientServerEntries(element, desc)
        assert any("Unsupported Required Client Server Entry" in r.getMessage() for r in caplog.records)

    def test_readBswModuleClientServerEntry_sets_attrs(self, parser):
        from armodel.models import BswModuleClientServerEntry

        entry = BswModuleClientServerEntry(parent=_autosar_root(), short_name="ce")
        element = _snip(
            "<SHORT-NAME>ce</SHORT-NAME>"
            "<ENCAPSULATED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ee</ENCAPSULATED-ENTRY-REF>"
            "<IS-REENTRANT>true</IS-REENTRANT>"
            "<IS-SYNCHRONOUS>false</IS-SYNCHRONOUS>",
            root_tag="BSW-MODULE-CLIENT-SERVER-ENTRY",
        )
        parser.readBswModuleClientServerEntry(element, entry)
        assert entry.getEncapsulatedEntryRef().getValue() == "/ee"
        assert entry.getIsReentrant().getValue() is True
        assert entry.getIsSynchronous().getValue() is False

    def test_readBswModuleDescription_minimal(self, warning_parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<SHORT-NAME>bswm</SHORT-NAME>"
            "<MODULE-ID>1</MODULE-ID>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        warning_parser.readBswModuleDescription(element, desc)
        assert desc.getModuleId().getValue() == 1

    def test_readBswModuleDescription_full_orchestration(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<SHORT-NAME>bswm</SHORT-NAME>"
            "<MODULE-ID>42</MODULE-ID>"
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e1</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>"
            "<PROVIDED-MODE-GROUPS>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE><SHORT-NAME>pmg</SHORT-NAME></MODE-DECLARATION-GROUP-PROTOTYPE>"
            "</PROVIDED-MODE-GROUPS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescription(element, desc)
        assert desc.getModuleId().getValue() == 42
        assert len(desc.getImplementedEntryRefs()) == 1
        assert len(desc.getProvidedModeGroups()) == 1

    def test_readBswModuleDescriptionBswInternalBehaviors_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<INTERNAL-BEHAVIORS>"
            "<BSW-INTERNAL-BEHAVIOR>"
            "<SHORT-NAME>bh</SHORT-NAME>"
            "</BSW-INTERNAL-BEHAVIOR>"
            "</INTERNAL-BEHAVIORS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        parser.readBswModuleDescriptionBswInternalBehaviors(element, desc)
        assert len(desc.getInternalBehaviors()) == 1

    def test_readBswModuleDescriptionBswInternalBehaviors_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        element = _snip(
            "<INTERNAL-BEHAVIORS><BAD/></INTERNAL-BEHAVIORS>",
            root_tag="BSW-MODULE-DESCRIPTION",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleDescriptionBswInternalBehaviors(element, desc)
        assert any("Unsupported Internal Behavior" in r.getMessage() for r in caplog.records)


# ==================== BswModuleEntry and SwServiceArg ====================


class TestBswModuleEntryHandlers:
    """Exercise readBswModuleEntry, readSwServiceArg, and the entry helpers."""

    def test_readSwServiceArg_minimal(self, parser):
        from armodel.models import SwServiceArg

        arg = SwServiceArg(parent=_autosar_root(), short_name="arg")
        element = _snip(
            "<SHORT-NAME>arg</SHORT-NAME>"
            "<DIRECTION>IN</DIRECTION>",
            root_tag="SW-SERVICE-ARG",
        )
        parser.readSwServiceArg(element, arg)
        assert arg.getDirection().getValue() == "IN"

    def test_readBswModuleEntryArguments_creates_arg(self, parser):
        from armodel.models import BswModuleEntry

        entry = BswModuleEntry(parent=_autosar_root(), short_name="ent")
        element = _snip(
            "<ARGUMENTS>"
            "<SW-SERVICE-ARG><SHORT-NAME>a1</SHORT-NAME></SW-SERVICE-ARG>"
            "</ARGUMENTS>",
            root_tag="BSW-MODULE-ENTRY",
        )
        parser.readBswModuleEntryArguments(element, entry)
        assert len(entry.getArguments()) == 1

    def test_readBswModuleEntryArguments_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswModuleEntry

        entry = BswModuleEntry(parent=_autosar_root(), short_name="ent")
        element = _snip(
            "<ARGUMENTS><BAD/></ARGUMENTS>",
            root_tag="BSW-MODULE-ENTRY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntryArguments(element, entry)
        assert any("Unsupported Argument" in r.getMessage() for r in caplog.records)

    def test_readBswModuleEntryReturnType_present(self, parser):
        from armodel.models import BswModuleEntry

        entry = BswModuleEntry(parent=_autosar_root(), short_name="ent")
        element = _snip(
            "<RETURN-TYPE><SHORT-NAME>ret</SHORT-NAME></RETURN-TYPE>",
            root_tag="BSW-MODULE-ENTRY",
        )
        parser.readBswModuleEntryReturnType(element, entry)
        assert entry.getReturnType() is not None
        assert entry.getReturnType().getShortName() == "ret"

    def test_readBswModuleEntryReturnType_absent_no_op(self, parser):
        from armodel.models import BswModuleEntry

        entry = BswModuleEntry(parent=_autosar_root(), short_name="ent")
        element = _snip("", root_tag="BSW-MODULE-ENTRY")
        parser.readBswModuleEntryReturnType(element, entry)
        assert entry.getReturnType() is None

    def test_readBswModuleEntry_full(self, parser):
        from armodel.models import BswModuleEntry

        entry = BswModuleEntry(parent=_autosar_root(), short_name="ent")
        element = _snip(
            "<SHORT-NAME>ent</SHORT-NAME>"
            "<IS-REENTRANT>true</IS-REENTRANT>"
            "<IS-SYNCHRONOUS>true</IS-SYNCHRONOUS>"
            "<SERVICE-ID>10</SERVICE-ID>"
            "<CALL-TYPE>SHARED</CALL-TYPE>"
            "<EXECUTION-CONTEXT>UNSPECIFIED</EXECUTION-CONTEXT>"
            "<SW-SERVICE-IMPL-POLICY>STANDARD</SW-SERVICE-IMPL-POLICY>"
            "<BSW-ENTRY-KIND>FUNCTION</BSW-ENTRY-KIND>"
            "<ARGUMENTS>"
            "<SW-SERVICE-ARG><SHORT-NAME>a1</SHORT-NAME></SW-SERVICE-ARG>"
            "</ARGUMENTS>"
            "<RETURN-TYPE><SHORT-NAME>r</SHORT-NAME></RETURN-TYPE>",
            root_tag="BSW-MODULE-ENTRY",
        )
        parser.readBswModuleEntry(element, entry)
        assert entry.getIsReentrant().getValue() is True
        assert entry.getServiceId().getValue() == 10
        assert entry.getCallType().getValue() == "SHARED"
        assert entry.getExecutionContext().getValue() == "UNSPECIFIED"
        assert entry.getSwServiceImplPolicy().getValue() == "STANDARD"
        assert entry.getBswEntryKind().getValue() == "FUNCTION"
        assert len(entry.getArguments()) == 1
        assert entry.getReturnType() is not None


# ==================== ExecutableEntity / InternalBehavior helpers ====================


class TestExecutableEntityAndInternalBehaviorHandlers:
    """Exercise readCanEnterExclusiveAreaRefs, readExecutableEntity,
    readInternalBehavior*, and readDataTypeMappingRefs."""

    def test_readCanEnterExclusiveAreaRefs_adds_refs(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        entity = behavior.createBswCalledEntity("e")
        element = _snip(
            "<CAN-ENTER-EXCLUSIVE-AREA-REFS>"
            "<CAN-ENTER-EXCLUSIVE-AREA-REF DEST='EXCLUSIVE-AREA'>/a1</CAN-ENTER-EXCLUSIVE-AREA-REF>"
            "</CAN-ENTER-EXCLUSIVE-AREA-REFS>",
            root_tag="ENTITY",
        )
        parser.readCanEnterExclusiveAreaRefs(element, entity)
        assert len(entity.getCanEnterExclusiveAreaRefs()) == 1

    def test_readExecutableEntity_sets_attrs(self, parser):
        from armodel.models import BswCalledEntity

        entity = BswCalledEntity(parent=_autosar_root(), short_name="e")
        element = _snip(
            "<SHORT-NAME>e</SHORT-NAME>"
            "<MINIMUM-START-INTERVAL>0.5</MINIMUM-START-INTERVAL>"
            "<SW-ADDR-METHOD-REF DEST='SW-ADDR-METHOD'>/m</SW-ADDR-METHOD-REF>",
            root_tag="ENTITY",
        )
        parser.readExecutableEntity(element, entity)
        assert entity.getMinimumStartInterval().getValue() == 0.5
        assert entity.getSwAddrMethodRef().getValue() == "/m"

    def test_readDataTypeMappingRefs_adds_refs(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<DATA-TYPE-MAPPING-REFS>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/m1</DATA-TYPE-MAPPING-REF>"
            "</DATA-TYPE-MAPPING-REFS>",
            root_tag="BH",
        )
        parser.readDataTypeMappingRefs(element, behavior)
        assert len(behavior.getDataTypeMappingRefs()) == 1

    def test_readDataTypeMappingRefs_missing_no_op(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip("", root_tag="BH")
        parser.readDataTypeMappingRefs(element, behavior)
        assert len(behavior.getDataTypeMappingRefs()) == 0

    def test_readInternalBehaviorConstantMemories_creates(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<CONSTANT-MEMORYS>"
            "<PARAMETER-DATA-PROTOTYPE><SHORT-NAME>cm</SHORT-NAME></PARAMETER-DATA-PROTOTYPE>"
            "</CONSTANT-MEMORYS>",
            root_tag="BH",
        )
        parser.readInternalBehaviorConstantMemories(element, behavior)
        assert len(behavior.getConstantMemories()) == 1

    def test_readInternalBehaviorConstantMemories_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<CONSTANT-MEMORYS><BAD/></CONSTANT-MEMORYS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readInternalBehaviorConstantMemories(element, behavior)
        assert any("Unsupported constant memories" in r.getMessage() for r in caplog.records)

    def test_readInternalBehaviorStaticMemories_creates(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<STATIC-MEMORYS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>sm</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</STATIC-MEMORYS>",
            root_tag="BH",
        )
        parser.readInternalBehaviorStaticMemories(element, behavior)
        assert len(behavior.getStaticMemories()) == 1

    def test_readInternalBehaviorStaticMemories_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<STATIC-MEMORYS><BAD/></STATIC-MEMORYS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readInternalBehaviorStaticMemories(element, behavior)
        assert any("Unsupported static memories" in r.getMessage() for r in caplog.records)

    def test_readInternalBehavior_full(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<EXCLUSIVE-AREAS>"
            "<EXCLUSIVE-AREA><SHORT-NAME>ea1</SHORT-NAME></EXCLUSIVE-AREA>"
            "</EXCLUSIVE-AREAS>"
            "<DATA-TYPE-MAPPING-REFS>"
            "<DATA-TYPE-MAPPING-REF DEST='DATA-TYPE-MAPPING-SET'>/m</DATA-TYPE-MAPPING-REF>"
            "</DATA-TYPE-MAPPING-REFS>",
            root_tag="BH",
        )
        parser.readInternalBehavior(element, behavior)
        assert len(behavior.getExclusiveAreas()) == 1
        assert len(behavior.getDataTypeMappingRefs()) == 1


# ==================== BswModuleEntity call points and trigger refs ====================


class TestBswModuleEntityHandlers:
    """Exercise readBswModuleEntity orchestrator + sub-readers for call points,
    trigger refs, activation points, and managed mode groups."""

    def test_readBswModuleEntityManagedModeGroups_adds_refs(self, parser):
        from armodel.models import BswInternalBehavior, BswSchedulableEntity

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<MANAGED-MODE-GROUPS>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/mg</MODE-DECLARATION-GROUP-PROTOTYPE-REF>"
            "</MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL>"
            "</MANAGED-MODE-GROUPS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityManagedModeGroups(element, entity)
        assert len(entity.getManagedModeGroupRefs()) == 1

    def test_readBswModuleEntityManagedModeGroups_empty_no_op(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<MANAGED-MODE-GROUPS>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL></MODE-DECLARATION-GROUP-PROTOTYPE-REF-CONDITIONAL>"
            "</MANAGED-MODE-GROUPS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityManagedModeGroups(element, entity)
        assert len(entity.getManagedModeGroupRefs()) == 0

    def test_readBswModuleEntityIssuedTriggerRefs_adds(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<ISSUED-TRIGGERS>"
            "<TRIGGER-REF-CONDITIONAL>"
            "<TRIGGER-REF DEST='TRIGGER'>/t1</TRIGGER-REF>"
            "</TRIGGER-REF-CONDITIONAL>"
            "</ISSUED-TRIGGERS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityIssuedTriggerRefs(element, entity)
        assert len(entity.getIssuedTriggerRefs()) == 1

    def test_readBswModuleEntityActivationPointRefs_adds(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<ACTIVATION-POINTS>"
            "<BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL>"
            "<BSW-INTERNAL-TRIGGERING-POINT-REF DEST='BSW-INTERNAL-TRIGGERING-POINT'>/itp</BSW-INTERNAL-TRIGGERING-POINT-REF>"
            "</BSW-INTERNAL-TRIGGERING-POINT-REF-CONDITIONAL>"
            "</ACTIVATION-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityActivationPointRefs(element, entity)
        assert len(entity.getActivationPointRefs()) == 1

    def test_readBswModuleCallPoint_minimal(self, parser):
        from armodel.models import BswAsynchronousServerCallPoint

        point = BswAsynchronousServerCallPoint(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<SHORT-NAME>cp</SHORT-NAME>",
            root_tag="BSW-ASYNCHRONOUS-SERVER-CALL-POINT",
        )
        parser.readBswModuleCallPoint(element, point)
        assert point.getShortName() == "cp"

    def test_readBswAsynchronousServerCallPoint_sets_ref(self, parser):
        from armodel.models import BswAsynchronousServerCallPoint

        point = BswAsynchronousServerCallPoint(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<SHORT-NAME>cp</SHORT-NAME>"
            "<CALLED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</CALLED-ENTRY-REF>",
            root_tag="BSW-ASYNCHRONOUS-SERVER-CALL-POINT",
        )
        parser.readBswAsynchronousServerCallPoint(element, point)
        assert point.getCalledEntryRef().getValue() == "/ent"

    def test_readBswSynchronousServerCallPoint_sets_ref(self, parser):
        from armodel.models import BswSynchronousServerCallPoint

        point = BswSynchronousServerCallPoint(parent=_autosar_root(), short_name="cp")
        element = _snip(
            "<SHORT-NAME>cp</SHORT-NAME>"
            "<CALLED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</CALLED-ENTRY-REF>",
            root_tag="BSW-SYNCHRONOUS-SERVER-CALL-POINT",
        )
        parser.readBswSynchronousServerCallPoint(element, point)
        assert point.getCalledEntryRef().getValue() == "/ent"

    def test_readBswModuleEntityCallPoints_async(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<CALL-POINTS>"
            "<BSW-ASYNCHRONOUS-SERVER-CALL-POINT><SHORT-NAME>acp</SHORT-NAME></BSW-ASYNCHRONOUS-SERVER-CALL-POINT>"
            "</CALL-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityCallPoints(element, entity)
        assert len(entity.getCallPoints()) == 1

    def test_readBswModuleEntityCallPoints_sync(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<CALL-POINTS>"
            "<BSW-SYNCHRONOUS-SERVER-CALL-POINT><SHORT-NAME>scp</SHORT-NAME></BSW-SYNCHRONOUS-SERVER-CALL-POINT>"
            "</CALL-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntityCallPoints(element, entity)
        assert len(entity.getCallPoints()) == 1

    def test_readBswModuleEntityCallPoints_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<CALL-POINTS><BAD/></CALL-POINTS>",
            root_tag="ENTITY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswModuleEntityCallPoints(element, entity)
        assert any("Unsupported Call Point" in r.getMessage() for r in caplog.records)

    def test_readBswModuleEntity_full(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        # Build a BswInternalBehavior + entity via the model API so the entity
        # has a fully-resolved short-name path for IMPLEMENTED-ENTRY-REF.
        behavior = desc.createBswInternalBehavior("bh")
        entity = behavior.createBswSchedulableEntity("e")
        element = _snip(
            "<SHORT-NAME>e</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</IMPLEMENTED-ENTRY-REF>"
            "<CALL-POINTS>"
            "<BSW-SYNCHRONOUS-SERVER-CALL-POINT><SHORT-NAME>scp</SHORT-NAME></BSW-SYNCHRONOUS-SERVER-CALL-POINT>"
            "</CALL-POINTS>"
            "<DATA-RECEIVE-POINTS>"
            "<BSW-VARIABLE-ACCESS><SHORT-NAME>rp</SHORT-NAME></BSW-VARIABLE-ACCESS>"
            "</DATA-RECEIVE-POINTS>"
            "<DATA-SEND-POINTS>"
            "<BSW-VARIABLE-ACCESS><SHORT-NAME>sp</SHORT-NAME></BSW-VARIABLE-ACCESS>"
            "</DATA-SEND-POINTS>",
            root_tag="ENTITY",
        )
        parser.readBswModuleEntity(element, entity)
        assert entity.getImplementedEntryRef().getValue() == "/ent"
        assert len(entity.getCallPoints()) == 1
        assert len(entity.getDataReceivePoints()) == 1
        assert len(entity.getDataSendPoints()) == 1


# ==================== BSW entities dispatch (Called/Schedulable/Interrupt) ====================


class TestBswEntityDispatch:
    """Exercise readBswCalledEntity, readBswSchedulableEntity,
    readBswInterruptEntity, and readBswInternalBehaviorEntities dispatch."""

    def test_readBswCalledEntity_minimal(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        entity = behavior.createBswCalledEntity("ce")
        element = _snip(
            "<SHORT-NAME>ce</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</IMPLEMENTED-ENTRY-REF>",
            root_tag="BSW-CALLED-ENTITY",
        )
        parser.readBswCalledEntity(element, entity)
        assert entity.getImplementedEntryRef().getValue() == "/ent"

    def test_readBswSchedulableEntity_minimal(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        entity = behavior.createBswSchedulableEntity("se")
        element = _snip(
            "<SHORT-NAME>se</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</IMPLEMENTED-ENTRY-REF>",
            root_tag="BSW-SCHEDULABLE-ENTITY",
        )
        parser.readBswSchedulableEntity(element, entity)
        assert entity.getImplementedEntryRef().getValue() == "/ent"

    def test_readBswInterruptEntity_sets_attrs(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        entity = behavior.createBswInterruptEntity("ie")
        element = _snip(
            "<SHORT-NAME>ie</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/ent</IMPLEMENTED-ENTRY-REF>"
            "<INTERRUPT-CATEGORY>CAT_1</INTERRUPT-CATEGORY>"
            "<INTERRUPT-SOURCE>EXT</INTERRUPT-SOURCE>",
            root_tag="BSW-INTERRUPT-ENTITY",
        )
        parser.readBswInterruptEntity(element, entity)
        assert entity.getInterruptCategory().getValue() == "CAT_1"
        assert entity.getInterruptSource().getValue() == "EXT"

    def test_readBswInternalBehaviorEntities_dispatches_all(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        element = _snip(
            "<ENTITYS>"
            "<BSW-CALLED-ENTITY><SHORT-NAME>ce</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e1</IMPLEMENTED-ENTRY-REF>"
            "</BSW-CALLED-ENTITY>"
            "<BSW-SCHEDULABLE-ENTITY><SHORT-NAME>se</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e2</IMPLEMENTED-ENTRY-REF>"
            "</BSW-SCHEDULABLE-ENTITY>"
            "<BSW-INTERRUPT-ENTITY><SHORT-NAME>ie</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e3</IMPLEMENTED-ENTRY-REF>"
            "</BSW-INTERRUPT-ENTITY>"
            "</ENTITYS>",
            root_tag="BH",
        )
        parser.readBswInternalBehaviorEntities(element, behavior)
        assert len(behavior.getBswCalledEntities()) == 1
        assert len(behavior.getBswSchedulableEntities()) == 1
        assert len(behavior.getBswInterruptEntities()) == 1

    def test_readBswInternalBehaviorEntities_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<ENTITYS><BAD/></ENTITYS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswInternalBehaviorEntities(element, behavior)
        assert any("Unsupported BswModuleEntity" in r.getMessage() for r in caplog.records)


# ==================== BSW Events ====================


class TestBswInternalBehaviorEventsDetailed:
    """Exercise readBswEvent, readBswScheduleEvent, all the BSW event types,
    and the readBswInternalBehaviorEvents dispatch."""

    def test_readBswEvent_sets_startsOnEventRef(self, parser):
        from armodel.models import BswModeSwitchEvent

        event = BswModeSwitchEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<STARTS-ON-EVENT-REF DEST='BSW-MODE-SENDER-POLICY'>/p</STARTS-ON-EVENT-REF>",
            root_tag="EV",
        )
        parser.readBswEvent(element, event)
        assert event.startsOnEventRef.getValue() == "/p"

    def test_readBswModeSwitchEvent_minimal(self, parser):
        from armodel.models import BswModeSwitchEvent

        event = BswModeSwitchEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<STARTS-ON-EVENT-REF DEST='X'>/p</STARTS-ON-EVENT-REF>",
            root_tag="BSW-MODE-SWITCH-EVENT",
        )
        parser.readBswModeSwitchEvent(element, event)
        assert event.startsOnEventRef.getValue() == "/p"

    def test_readBswTimingEvent_sets_period(self, parser):
        from armodel.models import BswTimingEvent

        event = BswTimingEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<PERIOD>0.1</PERIOD>",
            root_tag="BSW-TIMING-EVENT",
        )
        parser.readBswTimingEvent(element, event)
        assert event.getPeriod().getValue() == 0.1

    def test_readBswTimingEvent_missing_period_logs_warning(self, parser, caplog):
        from armodel.models import BswTimingEvent

        event = BswTimingEvent(parent=_autosar_root(), short_name="ev")
        element = _snip("<SHORT-NAME>ev</SHORT-NAME>", root_tag="BSW-TIMING-EVENT")
        with caplog.at_level(logging.WARNING):
            parser.readBswTimingEvent(element, event)
        assert event.getPeriod() is None
        assert any("invalid" in r.getMessage() for r in caplog.records)

    def test_readBswDataReceivedEvent_sets_dataRef(self, parser):
        from armodel.models import BswDataReceivedEvent

        event = BswDataReceivedEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<DATA-REF DEST='VARIABLE-DATA-PROTOTYPE'>/d</DATA-REF>",
            root_tag="BSW-DATA-RECEIVED-EVENT",
        )
        parser.readBswDataReceivedEvent(element, event)
        assert event.getDataRef().getValue() == "/d"

    def test_readBswInternalTriggerOccurredEvent_sets_source_ref(self, parser):
        from armodel.models import BswInternalTriggerOccurredEvent

        event = BswInternalTriggerOccurredEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<EVENT-SOURCE-REF DEST='BSW-INTERNAL-TRIGGERING-POINT'>/s</EVENT-SOURCE-REF>",
            root_tag="BSW-INTERNAL-TRIGGER-OCCURRED-EVENT",
        )
        parser.readBswInternalTriggerOccurredEvent(element, event)
        assert event.getEventSourceRef().getValue() == "/s"

    def test_readBswBackgroundEvent_minimal(self, parser):
        from armodel.models import BswBackgroundEvent

        event = BswBackgroundEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<STARTS-ON-EVENT-REF DEST='X'>/p</STARTS-ON-EVENT-REF>",
            root_tag="BSW-BACKGROUND-EVENT",
        )
        parser.readBswBackgroundEvent(element, event)
        assert event.startsOnEventRef.getValue() == "/p"

    def test_readBswExternalTriggerOccurredEvent_sets_trigger_ref(self, parser):
        from armodel.models import BswExternalTriggerOccurredEvent

        event = BswExternalTriggerOccurredEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<TRIGGER-REF DEST='TRIGGER'>/t</TRIGGER-REF>",
            root_tag="BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT",
        )
        parser.readBswExternalTriggerOccurredEvent(element, event)
        assert event.getTriggerRef().getValue() == "/t"

    def test_readBswOperationInvokedEvent_sets_entry_ref(self, parser):
        from armodel.models import BswOperationInvokedEvent

        event = BswOperationInvokedEvent(parent=_autosar_root(), short_name="ev")
        element = _snip(
            "<SHORT-NAME>ev</SHORT-NAME>"
            "<ENTRY-REF DEST='BSW-MODULE-CLIENT-SERVER-ENTRY'>/e</ENTRY-REF>",
            root_tag="BSW-OPERATION-INVOKED-EVENT",
        )
        parser.readBswOperationInvokedEvent(element, event)
        assert event.getEntryRef().getValue() == "/e"

    def test_readBswInternalBehaviorEvents_dispatches_all_types(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        element = _snip(
            "<EVENTS>"
            "<BSW-MODE-SWITCH-EVENT><SHORT-NAME>e1</SHORT-NAME></BSW-MODE-SWITCH-EVENT>"
            "<BSW-TIMING-EVENT><SHORT-NAME>e2</SHORT-NAME></BSW-TIMING-EVENT>"
            "<BSW-DATA-RECEIVED-EVENT><SHORT-NAME>e3</SHORT-NAME></BSW-DATA-RECEIVED-EVENT>"
            "<BSW-INTERNAL-TRIGGER-OCCURRED-EVENT><SHORT-NAME>e4</SHORT-NAME></BSW-INTERNAL-TRIGGER-OCCURRED-EVENT>"
            "<BSW-BACKGROUND-EVENT><SHORT-NAME>e5</SHORT-NAME></BSW-BACKGROUND-EVENT>"
            "<BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT><SHORT-NAME>e6</SHORT-NAME></BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT>"
            "<BSW-OPERATION-INVOKED-EVENT><SHORT-NAME>e7</SHORT-NAME></BSW-OPERATION-INVOKED-EVENT>"
            "</EVENTS>",
            root_tag="BH",
        )
        parser.readBswInternalBehaviorEvents(element, behavior)
        assert len(behavior.getBswModeSwitchEvents()) == 1
        assert len(behavior.getBswTimingEvents()) == 1
        assert len(behavior.getBswDataReceivedEvents()) == 1
        assert len(behavior.getBswInternalTriggerOccurredEvents()) == 1
        assert len(behavior.getBswBackgroundEvents()) == 1
        assert len(behavior.getBswExternalTriggerOccurredEvents()) == 1
        assert len(behavior.getBswOperationInvokedEvents()) == 1

    def test_readBswInternalBehaviorEvents_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<EVENTS><BAD/></EVENTS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswInternalBehaviorEvents(element, behavior)
        assert any("Unsupported BswModuleEntity" in r.getMessage() for r in caplog.records)


# ==================== BSW Mode Sender Policy & Reception Policies ====================


class TestBswReceptionAndApiOptions:
    """Exercise readBswApiOptions, reception policies, internal triggering
    points, getBswModeSenderPolicy, and readBswInternalBehaviorModeSenderPolicy."""

    def test_getBswModeSenderPolicy_full(self, parser):
        from armodel.models import BswModeSenderPolicy

        element = _snip(
            "<PROVIDED-MODE-GROUP-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/mg</PROVIDED-MODE-GROUP-REF>"
            "<QUEUE-LENGTH>3</QUEUE-LENGTH>",
            root_tag="BSW-MODE-SENDER-POLICY",
        )
        policy = parser.getBswModeSenderPolicy(element)
        assert isinstance(policy, BswModeSenderPolicy)
        assert policy.getProvidedModeGroupRef().getValue() == "/mg"
        assert policy.getQueueLength().getValue() == 3

    def test_readBswInternalBehaviorModeSenderPolicy_adds_policy(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<MODE-SENDER-POLICYS>"
            "<BSW-MODE-SENDER-POLICY>"
            "<PROVIDED-MODE-GROUP-REF DEST='X'>/mg</PROVIDED-MODE-GROUP-REF>"
            "<QUEUE-LENGTH>3</QUEUE-LENGTH>"
            "</BSW-MODE-SENDER-POLICY>"
            "</MODE-SENDER-POLICYS>",
            root_tag="BH",
        )
        parser.readBswInternalBehaviorModeSenderPolicy(element, behavior)
        assert len(behavior.getModeSenderPolicies()) == 1

    def test_readBswInternalBehaviorModeSenderPolicy_unsupported_raises(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<MODE-SENDER-POLICYS><BAD/></MODE-SENDER-POLICYS>",
            root_tag="BH",
        )
        with pytest.raises(Exception):
            parser.readBswInternalBehaviorModeSenderPolicy(element, behavior)

    def test_readBswInternalBehaviorModeSenderPolicy_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<MODE-SENDER-POLICYS><BAD/></MODE-SENDER-POLICYS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswInternalBehaviorModeSenderPolicy(element, behavior)
        assert any("Unsupported ModeSenderPolicy" in r.getMessage() for r in caplog.records)

    def test_readBswApiOptions_sets_enable_take_address(self, parser):
        from armodel.models import BswQueuedDataReceptionPolicy

        # Use concrete subclass (BswQueuedDataReceptionPolicy) since BswApiOptions is abstract.
        options = BswQueuedDataReceptionPolicy()
        element = _snip(
            "<ENABLE-TAKE-ADDRESS>true</ENABLE-TAKE-ADDRESS>",
            root_tag="OPTS",
        )
        parser.readBswApiOptions(element, options)
        assert options.getEnableTakeAddress().getValue() is True

    def test_readBswDataReceptionPolicy_sets_ref(self, parser):
        from armodel.models import BswQueuedDataReceptionPolicy

        # Use concrete subclass since BswDataReceptionPolicy is abstract.
        policy = BswQueuedDataReceptionPolicy()
        element = _snip(
            "<RECEIVED-DATA-REF DEST='VARIABLE-DATA-PROTOTYPE'>/d</RECEIVED-DATA-REF>",
            root_tag="P",
        )
        parser.readBswDataReceptionPolicy(element, policy)
        assert policy.getReceivedDataRef().getValue() == "/d"

    def test_readBswQueuedDataReceptionPolicy_sets_queue_length(self, parser):
        from armodel.models import BswQueuedDataReceptionPolicy

        policy = BswQueuedDataReceptionPolicy()
        element = _snip(
            "<RECEIVED-DATA-REF DEST='VARIABLE-DATA-PROTOTYPE'>/d</RECEIVED-DATA-REF>"
            "<QUEUE-LENGTH>5</QUEUE-LENGTH>",
            root_tag="P",
        )
        parser.readBswQueuedDataReceptionPolicy(element, policy)
        assert policy.getQueueLength().getValue() == 5

    def test_readBswInternalBehaviorReceptionPolicies_adds(self, parser):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<RECEPTION-POLICYS>"
            "<BSW-QUEUED-DATA-RECEPTION-POLICY>"
            "<QUEUE-LENGTH>1</QUEUE-LENGTH>"
            "</BSW-QUEUED-DATA-RECEPTION-POLICY>"
            "</RECEPTION-POLICYS>",
            root_tag="BH",
        )
        parser.readBswInternalBehaviorReceptionPolicies(element, behavior)
        assert len(behavior.getReceptionPolicies()) == 1

    def test_readBswInternalBehaviorReceptionPolicies_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<RECEPTION-POLICYS><BAD/></RECEPTION-POLICYS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswInternalBehaviorReceptionPolicies(element, behavior)
        assert any("Unsupported Reception Policies" in r.getMessage() for r in caplog.records)


# ==================== BswInternalTriggeringPoint & BswInternalBehavior orchestrator ====================


class TestBswInternalBehaviorOrchestrator:
    """Exercise readBswInternalTriggeringPoint, internal triggering points
    collection, and the full readBswInternalBehavior orchestrator."""

    def test_readBswInternalTriggeringPoint_minimal(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        point = behavior.createBswInternalTriggeringPoint("tp")
        element = _snip(
            "<SHORT-NAME>tp</SHORT-NAME>",
            root_tag="BSW-INTERNAL-TRIGGERING-POINT",
        )
        parser.readBswInternalTriggeringPoint(element, point)
        assert point.getShortName() == "tp"

    def test_readBswInternalBehaviorInternalTriggeringPoints_creates(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        element = _snip(
            "<INTERNAL-TRIGGERING-POINTS>"
            "<BSW-INTERNAL-TRIGGERING-POINT><SHORT-NAME>tp</SHORT-NAME></BSW-INTERNAL-TRIGGERING-POINT>"
            "</INTERNAL-TRIGGERING-POINTS>",
            root_tag="BH",
        )
        parser.readBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        assert len(behavior.getInternalTriggeringPoints()) == 1

    def test_readBswInternalBehaviorInternalTriggeringPoints_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import BswInternalBehavior

        behavior = BswInternalBehavior(parent=_autosar_root(), short_name="bh")
        element = _snip(
            "<INTERNAL-TRIGGERING-POINTS><BAD/></INTERNAL-TRIGGERING-POINTS>",
            root_tag="BH",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readBswInternalBehaviorInternalTriggeringPoints(element, behavior)
        assert any("Unsupported Internal Triggering Points" in r.getMessage() for r in caplog.records)

    def test_readBswInternalBehavior_full(self, parser):
        from armodel.models import BswModuleDescription

        desc = BswModuleDescription(parent=_autosar_root(), short_name="bswm")
        behavior = desc.createBswInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<ENTITYS>"
            "<BSW-SCHEDULABLE-ENTITY><SHORT-NAME>se</SHORT-NAME>"
            "<IMPLEMENTED-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/e</IMPLEMENTED-ENTRY-REF>"
            "</BSW-SCHEDULABLE-ENTITY>"
            "</ENTITYS>"
            "<EVENTS>"
            "<BSW-TIMING-EVENT><SHORT-NAME>te</SHORT-NAME><PERIOD>0.5</PERIOD></BSW-TIMING-EVENT>"
            "</EVENTS>"
            "<MODE-SENDER-POLICYS>"
            "<BSW-MODE-SENDER-POLICY>"
            "<PROVIDED-MODE-GROUP-REF DEST='X'>/mg</PROVIDED-MODE-GROUP-REF>"
            "<QUEUE-LENGTH>3</QUEUE-LENGTH>"
            "</BSW-MODE-SENDER-POLICY>"
            "</MODE-SENDER-POLICYS>",
            root_tag="BSW-INTERNAL-BEHAVIOR",
        )
        parser.readBswInternalBehavior(element, behavior)
        assert len(behavior.getBswSchedulableEntities()) == 1
        assert len(behavior.getBswTimingEvents()) == 1
        assert len(behavior.getModeSenderPolicies()) == 1


# ==================== Trigger (released/required) ====================


class TestTriggerHandlers:
    """Exercise readTrigger via the released/required trigger paths."""

    def test_readTrigger_minimal(self, parser):
        from armodel.models import Trigger

        trigger = Trigger(parent=_autosar_root(), short_name="t")
        element = _snip(
            "<SHORT-NAME>t</SHORT-NAME>",
            root_tag="TRIGGER",
        )
        parser.readTrigger(element, trigger)
        assert trigger.getShortName() == "t"


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestBswInternalBehaviorIncludedModeDeclarationGroupSet:
    def test_readBswInternalBehavior_adds_group_set(self, parser):
        from armodel.models import BswModuleDescription
        desc = BswModuleDescription(
            parent=_autosar_root(), short_name="Bsw"
        )
        behavior = desc.createBswInternalBehavior("Beh")
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "<MODE-DECLARATION-GROUP-REFS>"
            '<MODE-DECLARATION-GROUP-REF DEST="MODE-DECLARATION-GROUP">/mdg</MODE-DECLARATION-GROUP-REF>'
            "</MODE-DECLARATION-GROUP-REFS>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        parser.readBswInternalBehavior(element, behavior)
        assert len(behavior.getIncludedModeDeclarationGroupSets()) == 1


# ==================== ArtifactDescriptor / MemorySectionOptions / StackUsages (L1166, L1179-1180, L1209) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestCodeAndResourceConsumption:
    def test_readArtifactDescriptor_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import Code
        code = Code(parent=_autosar_root(), short_name="Code")
        element = _snip(
            "<ARTIFACT-DESCRIPTORS><BAD/></ARTIFACT-DESCRIPTORS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readArtifactDescriptor(element, code)
        assert any("Unsupported Artifact Descriptor" in r.getMessage()
                   for r in caplog.records)

    def test_readMemorySectionOptions_adds_options(self, parser):
        from armodel.models import MemorySection
        section = MemorySection(parent=MagicMock(), short_name="Sec")
        element = _snip(
            "<OPTIONS>"
            "<OPTION>OPT1</OPTION>"
            "<OPTION>OPT2</OPTION>"
            "</OPTIONS>"
        )
        parser.readMemorySectionOptions(element, section)
        assert len(section.getOptions()) == 2

    def test_readStackUsages_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcImplementation
        impl = SwcImplementation(parent=_autosar_root(), short_name="Impl")
        consumption = impl.createResourceConsumption("Rc")
        element = _snip(
            "<STACK-USAGES><BAD/></STACK-USAGES>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readStackUsages(element, consumption)
        assert any("Unsupported Stack Usages" in r.getMessage()
                   for r in caplog.records)


# ==================== RunnableEntity ModeSwitchPoints / Arguments (L1409, L1414-1416, L1429, L1437) ====================

