"""Phase D: targeted tests for uncovered internal parser methods.

Each test directly invokes an internal method on ARXMLParser with a minimal
XML snippet, lifting coverage on specific handler bodies that the dispatch
tests in test_arxml_parser_dispatch.py only route around.

Focus areas (from coverage report on arxml_parser.py):
- SDG / Sd / SdgCaption / SdgSdxRefs parsing (lines 250-323)
- DocRevision / Modification parsing (lines 293-323)
- _readVariableAccesses branching (lines 426-457)
"""

import pytest
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models import (
    AdminData,
    BswModuleDescription,
    DocRevision,
    RunnableEntity,
    Sdg,
)
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


def _snip(inner: str, root_tag: str = "ROOT") -> ET.Element:
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'>{inner}</{root_tag}>")


# ==================== SDG (Service Data Group) ====================


class TestSdgParsing:
    def test_getSdg_minimal(self, parser):
        element = _snip(
            "<SD GID='MyGroup'>value1</SD>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert isinstance(sdg, Sdg)

    def test_getSdg_with_caption(self, parser):
        element = _snip(
            "<SDG-CAPTION><SHORT-NAME>Caption1</SHORT-NAME></SDG-CAPTION>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_getSdg_with_nested_sdg(self, parser):
        element = _snip(
            "<SDG GID='Inner'><SD>x</SD></SDG>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_getSdg_with_sdx_refs(self, parser):
        element = _snip(
            "<SDX-REF DEST='SOMETHING'>/path/to/ref</SDX-REF>",
            root_tag="SDG",
        )
        sdg = parser.getSdg(element)
        assert sdg is not None

    def test_readAdminDataSdgs(self, parser):
        element = _snip(
            "<SDGS>"
            "<SDG GID='A'><SD>x</SD></SDG>"
            "<SDG GID='B'><SD>y</SD></SDG>"
            "</SDGS>"
        )
        admin = AdminData()
        parser.readAdminDataSdgs(element, admin)
        # Verify both SDGs added.
        assert len(admin.getSdgs()) == 2

    def test_readAdminDataSdgs_unsupported_tag_warns(self, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        element = _snip("<SDGS><UNKNOWN-SDG/></SDGS>")
        admin = AdminData()
        with caplog.at_level(logging.ERROR):
            p.readAdminDataSdgs(element, admin)
        assert any("Unsupported SDG" in r.getMessage() for r in caplog.records)


# ==================== Modification / DocRevision ====================


class TestRevisionParsing:
    def test_readDocRevision_minimal(self, parser):
        element = _snip(
            "<DATE>2024-01-01T00:00:00</DATE>"
            "<ISSUED-BY>alice</ISSUED-BY>"
            "<REVISION-LABEL>1.0.0</REVISION-LABEL>"
            "<STATE>released</STATE>",
            root_tag="DOC-REVISION",
        )
        revision = DocRevision()
        parser.readDocRevision(element, revision)
        assert revision.getIssuedBy().getValue() == "alice"
        assert revision.getState().getValue() == "released"

    def test_readDocRevision_with_modifications(self, parser):
        element = _snip(
            "<MODIFICATIONS>"
            "<MODIFICATION>"
            "<CHANGE><L-4>L-1</L-4></CHANGE>"
            "<REASON><L-4>R-1</L-4></REASON>"
            "</MODIFICATION>"
            "</MODIFICATIONS>",
            root_tag="DOC-REVISION",
        )
        revision = DocRevision()
        parser.readDocRevision(element, revision)
        # modification was added
        assert len(revision.getModifications()) == 1

    def test_readAdminDataDocRevisions(self, parser):
        element = _snip(
            "<DOC-REVISIONS>"
            "<DOC-REVISION>"
            "<ISSUED-BY>bob</ISSUED-BY>"
            "<REVISION-LABEL>2.0.0</REVISION-LABEL>"
            "</DOC-REVISION>"
            "</DOC-REVISIONS>"
        )
        admin = AdminData()
        parser.readAdminDataDocRevisions(element, admin)
        assert len(admin.getDocRevisions()) == 1

    def test_readAdminDataDocRevisions_unsupported_tag_warns(self, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        element = _snip("<DOC-REVISIONS><UNKNOWN/></DOC-REVISIONS>")
        admin = AdminData()
        with caplog.at_level(logging.ERROR):
            p.readAdminDataDocRevisions(element, admin)
        assert any("Unsupported DocRevision" in r.getMessage() for r in caplog.records)


# ==================== RxIdentifierRange ====================


class TestRxIdentifierRange:
    def test_getChildElementRxIdentifierRange(self, parser):
        # The method does find(element, "RX-IDENTIFIER-RANGE"), so element
        # must be the parent wrapper containing <RX-IDENTIFIER-RANGE>.
        element = _snip(
            "<RX-IDENTIFIER-RANGE>"
            "<LOWER-CAN-ID>0x100</LOWER-CAN-ID>"
            "<UPPER-CAN-ID>0x1FF</UPPER-CAN-ID>"
            "</RX-IDENTIFIER-RANGE>",
            root_tag="PARENT",
        )
        rng = parser.getChildElementRxIdentifierRange(element, "RX-IDENTIFIER-RANGE")
        assert rng is not None
        assert rng.getLowerCanId().getValue() == 256
        assert rng.getUpperCanId().getValue() == 511

    def test_getChildElementRxIdentifierRange_missing_returns_None(self, parser):
        element = _snip("<X/>")
        assert parser.getChildElementRxIdentifierRange(element, "ABSENT") is None


# ==================== _readVariableAccesses branching ====================


class TestReadVariableAccessesBranches:
    """Exercise each branch of _readVariableAccesses (arxml_parser.py:426)."""

    @pytest.fixture
    def runnable(self):
        return RunnableEntity(parent=None, short_name="R1")

    @pytest.mark.parametrize("key,creator_attr", [
        ("DATA-RECEIVE-POINT-BY-ARGUMENTS", "getDataReceivePointByArguments"),
        ("DATA-RECEIVE-POINT-BY-VALUES", "getDataReceivePointByValues"),
        ("DATA-READ-ACCESSS", "getDataReadAccesses"),
        ("DATA-WRITE-ACCESSS", "getDataWriteAccesses"),
        ("DATA-SEND-POINTS", "getDataSendPoints"),
        ("WRITTEN-LOCAL-VARIABLES", "getWrittenLocalVariables"),
        ("READ-LOCAL-VARIABLES", "getReadLocalVariables"),
    ])
    def test_branch(self, parser, runnable, key, creator_attr):
        element = _snip(
            f"<{key}>"
            f"<VARIABLE-ACCESS>"
            f"<SHORT-NAME>va1</SHORT-NAME>"
            f"</VARIABLE-ACCESS>"
            f"</{key}>",
            root_tag=key,
        )
        parser._readVariableAccesses(element, runnable, key)
        # Each branch creates one variable access on the runnable.
        created = getattr(runnable, creator_attr)()
        assert len(created) == 1, f"{key} did not produce a variable access"

    def test_unsupported_key_warns(self, runnable, caplog):
        import logging
        AUTOSAR.getInstance().new()
        p = ARXMLParser(options={"warning": True})
        # Match the double-wrap pattern from test_branch: outer ROOT contains
        # the <BAD-KEY> parent which itself wraps the VARIABLE-ACCESS.
        element = _snip(
            "<BAD-KEY><VARIABLE-ACCESS><SHORT-NAME>va</SHORT-NAME></VARIABLE-ACCESS></BAD-KEY>",
            root_tag="ROOT",
        )
        with caplog.at_level(logging.ERROR):
            p._readVariableAccesses(element, runnable, "BAD-KEY")
        assert any("Unsupported Variable Access" in r.getMessage() for r in caplog.records)


# ==================== readBswModuleDescriptionImplementedEntryRefs ====================


class TestBswModuleDescriptionImplementedEntryRefs:
    def test_reads_implemented_entry_refs(self, parser):
        bmd = BswModuleDescription(parent=None, short_name="Bmd1")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry1</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry2</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="ROOT",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, bmd)
        assert len(bmd.getImplementedEntryRefs()) == 2

    def test_skips_entries_without_ref(self, parser):
        bmd = BswModuleDescription(parent=None, short_name="Bmd1")
        element = _snip(
            "<PROVIDED-ENTRYS>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL/>"
            "<BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "<BSW-MODULE-ENTRY-REF DEST='BSW-MODULE-ENTRY'>/pkg/Entry</BSW-MODULE-ENTRY-REF>"
            "</BSW-MODULE-ENTRY-REF-CONDITIONAL>"
            "</PROVIDED-ENTRYS>",
            root_tag="ROOT",
        )
        parser.readBswModuleDescriptionImplementedEntryRefs(element, bmd)
        # Only one had a ref; the empty conditional should be skipped.
        assert len(bmd.getImplementedEntryRefs()) == 1
