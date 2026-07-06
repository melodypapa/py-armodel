"""Phase H: comprehensive tests for complex orchestrator methods in ARXMLParser.

Each test directly invokes orchestrator methods on ARXMLParser with minimal XML snippets,
lifting coverage on complex orchestrators for SWC internal behavior, runnable entities,
RTE events, data types, value specifications, system mappings, and ECUC values.

This file tests orchestrator methods that coordinate multiple sub-handlers.
"""

import logging
import xml.etree.ElementTree as ET
from unittest.mock import MagicMock

import pytest

from armodel.models import AUTOSAR
from armodel.models import ApplicationSwComponentType
from armodel.models import CompositionSwComponentType
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


# ==================== SwcInternalBehavior Orchestrator ====================


class TestSwcInternalBehaviorOrchestrator:
    """Exercise readSwcInternalBehavior full orchestrator and sub-handlers."""

    def test_readSwcInternalBehavior_minimal(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip("<SHORT-NAME>bh</SHORT-NAME>", root_tag="SWC-INTERNAL-BEHAVIOR")
        parser.readSwcInternalBehavior(element, behavior)
        assert behavior.getShortName() == "bh"

    def test_readSwcInternalBehavior_with_events(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<EVENTS>"
            "<TIMING-EVENT><SHORT-NAME>te</SHORT-NAME><PERIOD>0.1</PERIOD></TIMING-EVENT>"
            "</EVENTS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getTimingEvents()) == 1

    def test_readSwcInternalBehavior_with_runnables(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<RUNNABLES>"
            "<RUNNABLE-ENTITY><SHORT-NAME>run1</SHORT-NAME><SYMBOL>Run1</SYMBOL></RUNNABLE-ENTITY>"
            "</RUNNABLES>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getRunnableEntities()) == 1

    def test_readSwcInternalBehavior_with_per_instance_memories(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<PER-INSTANCE-MEMORYS>"
            "<PER-INSTANCE-MEMORY><SHORT-NAME>mem1</SHORT-NAME><TYPE>uint8</TYPE></PER-INSTANCE-MEMORY>"
            "</PER-INSTANCE-MEMORYS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getPerInstanceMemories()) == 1

    def test_readSwcInternalBehavior_with_port_api_options(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<PORT-API-OPTIONS>"
            "<PORT-API-OPTION>"
            "<ENABLE-TAKE-ADDRESS>true</ENABLE-TAKE-ADDRESS>"
            "<PORT-REF DEST='P-PORT-PROTOTYPE'>/port</PORT-REF>"
            "</PORT-API-OPTION>"
            "</PORT-API-OPTIONS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getPortAPIOptions()) == 1

    def test_readSwcInternalBehavior_with_explicit_inter_runnable_variables(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<EXPLICIT-INTER-RUNNABLE-VARIABLES>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>var1</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</EXPLICIT-INTER-RUNNABLE-VARIABLES>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getExplicitInterRunnableVariables()) == 1

    def test_readSwcInternalBehavior_with_service_dependencies(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<SERVICE-DEPENDENCYS>"
            "<SWC-SERVICE-DEPENDENCY><SHORT-NAME>dep1</SHORT-NAME></SWC-SERVICE-DEPENDENCY>"
            "</SERVICE-DEPENDENCYS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getSwcServiceDependencies()) == 1

    def test_readSwcInternalBehavior_with_shared_parameters(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<SHARED-PARAMETERS>"
            "<PARAMETER-DATA-PROTOTYPE><SHORT-NAME>param1</SHORT-NAME></PARAMETER-DATA-PROTOTYPE>"
            "</SHARED-PARAMETERS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getSharedParameters()) == 1

    def test_readSwcInternalBehavior_with_included_mode_declaration_group_sets(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "<PREFIX>prefix</PREFIX>"
            "<MODE-DECLARATION-GROUP-REFS>"
            "<MODE-DECLARATION-GROUP-REF DEST='MODE-DECLARATION-GROUP'>/mg</MODE-DECLARATION-GROUP-REF>"
            "</MODE-DECLARATION-GROUP-REFS>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SETS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getIncludedModeDeclarationGroupSets()) == 1

    def test_readSwcInternalBehaviorArTypedPerInstanceMemories_creates(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<AR-TYPED-PER-INSTANCE-MEMORYS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>mem</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</AR-TYPED-PER-INSTANCE-MEMORYS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehaviorArTypedPerInstanceMemories(element, behavior)
        assert len(behavior.getArTypedPerInstanceMemories()) == 1

    def test_readSwcInternalBehavior_with_handleTerminationAndRestart(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<HANDLE-TERMINATION-AND-RESTART>support</HANDLE-TERMINATION-AND-RESTART>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert behavior.getHandleTerminationAndRestart() is not None

    def test_readSwcInternalBehavior_with_supportsMultipleInstantiation(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<SUPPORTS-MULTIPLE-INSTANTIATION>true</SUPPORTS-MULTIPLE-INSTANTIATION>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert behavior.getSupportsMultipleInstantiation().getValue() is True

    def test_readSwcInternalBehavior_full_orchestration(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<SHORT-NAME>bh</SHORT-NAME>"
            "<EVENTS>"
            "<TIMING-EVENT><SHORT-NAME>te</SHORT-NAME><PERIOD>0.1</PERIOD></TIMING-EVENT>"
            "</EVENTS>"
            "<RUNNABLES>"
            "<RUNNABLE-ENTITY><SHORT-NAME>run</SHORT-NAME><SYMBOL>Run</SYMBOL></RUNNABLE-ENTITY>"
            "</RUNNABLES>"
            "<PER-INSTANCE-MEMORYS>"
            "<PER-INSTANCE-MEMORY><SHORT-NAME>mem</SHORT-NAME><TYPE>uint8</TYPE></PER-INSTANCE-MEMORY>"
            "</PER-INSTANCE-MEMORYS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        parser.readSwcInternalBehavior(element, behavior)
        assert len(behavior.getTimingEvents()) == 1
        assert len(behavior.getRunnableEntities()) == 1
        assert len(behavior.getPerInstanceMemories()) == 1


# ==================== Service Needs Handlers ====================


class TestServiceNeedsHandlers:
    """Exercise all service needs types."""

    def test_readNvBlockNeeds_full(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>nvNeeds</SHORT-NAME>"
            "<CALC-RAM-BLOCK-CRC>true</CALC-RAM-BLOCK-CRC>"
            "<CHECK-STATIC-BLOCK-ID>true</CHECK-STATIC-BLOCK-ID>"
            "<N-DATA-SETS>3</N-DATA-SETS>"
            "<N-ROM-BLOCKS>2</N-ROM-BLOCKS>",
            root_tag="NV-BLOCK-NEEDS",
        )
        needs = dependency.createNvBlockNeeds("nvNeeds")
        parser.readNvBlockNeeds(element, needs)
        assert needs.getCalcRamBlockCrc().getValue() is True
        assert needs.getNDataSets().getValue() == 3

    def test_readDiagnosticCommunicationManagerNeeds_sets_callbackType(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>diagNeeds</SHORT-NAME>"
            "<SERVICE-REQUEST-CALLBACK-TYPE>callback</SERVICE-REQUEST-CALLBACK-TYPE>",
            root_tag="DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS",
        )
        needs = dependency.createDiagnosticCommunicationManagerNeeds("diagNeeds")
        parser.readDiagnosticCommunicationManagerNeeds(element, needs)
        assert needs.getServiceRequestCallbackType().getValue() == "callback"

    def test_readDiagnosticRoutineNeeds_sets_ridNumber(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>routineNeeds</SHORT-NAME>"
            "<DIAG-ROUTINE-TYPE>routine</DIAG-ROUTINE-TYPE>"
            "<RID-NUMBER>0x0100</RID-NUMBER>",
            root_tag="DIAGNOSTIC-ROUTINE-NEEDS",
        )
        needs = dependency.createDiagnosticRoutineNeeds("routineNeeds")
        parser.readDiagnosticRoutineNeeds(element, needs)
        assert needs.getRidNumber().getValue() == 0x0100

    def test_readDiagnosticValueNeeds_sets_didNumber(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>valueNeeds</SHORT-NAME>"
            "<DATA-LENGTH>8</DATA-LENGTH>"
            "<DIAGNOSTIC-VALUE-ACCESS>read</DIAGNOSTIC-VALUE-ACCESS>"
            "<DID-NUMBER>0xF190</DID-NUMBER>",
            root_tag="DIAGNOSTIC-VALUE-NEEDS",
        )
        needs = dependency.createDiagnosticValueNeeds("valueNeeds")
        parser.readDiagnosticValueNeeds(element, needs)
        assert needs.getDidNumber().getValue() == 0xF190

    def test_readDiagnosticEventNeeds_sets_udsDtcNumber(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>eventNeeds</SHORT-NAME>"
            "<DTC-KIND>kind</DTC-KIND>"
            "<UDS-DTC-NUMBER>0x1234</UDS-DTC-NUMBER>",
            root_tag="DIAGNOSTIC-EVENT-NEEDS",
        )
        needs = dependency.createDiagnosticEventNeeds("eventNeeds")
        parser.readDiagnosticEventNeeds(element, needs)
        assert needs.getUdsDtcNumber().getValue() == 0x1234

    def test_readDiagnosticEventInfoNeeds_sets_dtcKind(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>eventInfoNeeds</SHORT-NAME>"
            "<DTC-KIND>kind</DTC-KIND>"
            "<UDS-DTC-NUMBER>0x5678</UDS-DTC-NUMBER>",
            root_tag="DIAGNOSTIC-EVENT-INFO-NEEDS",
        )
        needs = dependency.createDiagnosticEventInfoNeeds("eventInfoNeeds")
        parser.readDiagnosticEventInfoNeeds(element, needs)
        assert needs.getDtcKind().getValue() == "kind"

    def test_readCryptoServiceNeeds_sets_maxKeyLength(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>cryptoNeeds</SHORT-NAME>"
            "<MAXIMUM-KEY-LENGTH>256</MAXIMUM-KEY-LENGTH>",
            root_tag="CRYPTO-SERVICE-NEEDS",
        )
        needs = dependency.createCryptoServiceNeeds("cryptoNeeds")
        parser.readCryptoServiceNeeds(element, needs)
        assert needs.getMaximumKeyLength().getValue() == 256

    def test_readEcuStateMgrUserNeeds_minimal(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip("<SHORT-NAME>ecuStateNeeds</SHORT-NAME>", root_tag="ECU-STATE-MGR-USER-NEEDS")
        needs = dependency.createEcuStateMgrUserNeeds("ecuStateNeeds")
        parser.readEcuStateMgrUserNeeds(element, needs)
        assert needs.getShortName() == "ecuStateNeeds"

    def test_readDtcStatusChangeNotificationNeeds_sets_dtcFormatType(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SHORT-NAME>dtcNeeds</SHORT-NAME>"
            "<DTC-FORMAT-TYPE>format</DTC-FORMAT-TYPE>",
            root_tag="DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
        )
        needs = dependency.createDtcStatusChangeNotificationNeeds("dtcNeeds")
        parser.readDtcStatusChangeNotificationNeeds(element, needs)
        assert needs.getDtcFormatType().getValue() == "format"

    def test_readDltUserNeeds_minimal(self, parser):
        from armodel.models import SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip("<SHORT-NAME>dltNeeds</SHORT-NAME>", root_tag="DLT-USER-NEEDS")
        needs = dependency.createDltUserNeeds("dltNeeds")
        parser.readDltUserNeeds(element, needs)
        assert needs.getShortName() == "dltNeeds"

    def test_readDiagEventDebounceMonitorInternal_minimal(self, parser):
        from armodel.models import DiagnosticEventNeeds, SwcServiceDependency, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        event_needs = dependency.createDiagnosticEventNeeds("eventNeeds")
        element = _snip("<SHORT-NAME>debounce</SHORT-NAME>", root_tag="DIAG-EVENT-DEBOUNCE-MONITOR-INTERNAL")
        monitor = event_needs.createDiagEventDebounceMonitorInternal("debounce")
        parser.readDiagEventDebounceMonitorInternal(element, monitor)
        assert monitor.getShortName() == "debounce"


# ==================== Runnable Entity Orchestrator ====================


class TestRunnableEntityOrchestrator:
    """Exercise readRunnableEntity full orchestrator and all variable access types."""

    def test_readRunnableEntity_minimal(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip("<SHORT-NAME>run</SHORT-NAME><SYMBOL>Run</SYMBOL>", root_tag="RUNNABLE-ENTITY")
        parser.readRunnableEntity(element, runnable)
        assert runnable.getSymbol().getValue() == "Run"

    def test_readRunnableEntity_with_dataReceivePointByArguments(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<DATA-RECEIVE-POINT-BY-ARGUMENTS>"
            "<VARIABLE-ACCESS><SHORT-NAME>rp</SHORT-NAME></VARIABLE-ACCESS>"
            "</DATA-RECEIVE-POINT-BY-ARGUMENTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getDataReceivePointByArguments()) == 1

    def test_readRunnableEntity_with_dataReceivePointByValues(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<DATA-RECEIVE-POINT-BY-VALUES>"
            "<VARIABLE-ACCESS><SHORT-NAME>rpv</SHORT-NAME></VARIABLE-ACCESS>"
            "</DATA-RECEIVE-POINT-BY-VALUES>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getDataReceivePointByValues()) == 1

    def test_readRunnableEntity_with_dataReadAccesses(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<DATA-READ-ACCESSS>"
            "<VARIABLE-ACCESS><SHORT-NAME>ra</SHORT-NAME></VARIABLE-ACCESS>"
            "</DATA-READ-ACCESSS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getDataReadAccesses()) == 1

    def test_readRunnableEntity_with_dataWriteAccesses(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<DATA-WRITE-ACCESSS>"
            "<VARIABLE-ACCESS><SHORT-NAME>wa</SHORT-NAME></VARIABLE-ACCESS>"
            "</DATA-WRITE-ACCESSS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getDataWriteAccesses()) == 1

    def test_readRunnableEntity_with_dataSendPoints(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<DATA-SEND-POINTS>"
            "<VARIABLE-ACCESS><SHORT-NAME>sp</SHORT-NAME></VARIABLE-ACCESS>"
            "</DATA-SEND-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getDataSendPoints()) == 1

    def test_readRunnableEntity_with_writtenLocalVariables(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<WRITTEN-LOCAL-VARIABLES>"
            "<VARIABLE-ACCESS><SHORT-NAME>wlv</SHORT-NAME></VARIABLE-ACCESS>"
            "</WRITTEN-LOCAL-VARIABLES>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getWrittenLocalVariables()) == 1

    def test_readRunnableEntity_with_readLocalVariables(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<READ-LOCAL-VARIABLES>"
            "<VARIABLE-ACCESS><SHORT-NAME>rlv</SHORT-NAME></VARIABLE-ACCESS>"
            "</READ-LOCAL-VARIABLES>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getReadLocalVariables()) == 1

    def test_readRunnableEntity_with_synchronousServerCallPoint(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<SERVER-CALL-POINTS>"
            "<SYNCHRONOUS-SERVER-CALL-POINT>"
            "<SHORT-NAME>scp</SHORT-NAME>"
            "<TIMEOUT>1.0</TIMEOUT>"
            "</SYNCHRONOUS-SERVER-CALL-POINT>"
            "</SERVER-CALL-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getSynchronousServerCallPoint()) == 1

    def test_readRunnableEntity_with_asynchronousServerCallPoint(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<SERVER-CALL-POINTS>"
            "<ASYNCHRONOUS-SERVER-CALL-POINT>"
            "<SHORT-NAME>acp</SHORT-NAME>"
            "<TIMEOUT>1.0</TIMEOUT>"
            "</ASYNCHRONOUS-SERVER-CALL-POINT>"
            "</SERVER-CALL-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getAsynchronousServerCallPoint()) == 1

    def test_readRunnableEntity_with_internalTriggeringPoints(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<INTERNAL-TRIGGERING-POINTS>"
            "<INTERNAL-TRIGGERING-POINT><SHORT-NAME>itp</SHORT-NAME></INTERNAL-TRIGGERING-POINT>"
            "</INTERNAL-TRIGGERING-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(list(runnable.getInternalTriggeringPoints())) == 1

    def test_readRunnableEntity_with_modeAccessPoints(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<MODE-ACCESS-POINTS>"
            "<MODE-ACCESS-POINT></MODE-ACCESS-POINT>"
            "</MODE-ACCESS-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getModeAccessPoints()) == 1

    def test_readRunnableEntity_with_modeSwitchPoints(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<MODE-SWITCH-POINTS>"
            "<MODE-SWITCH-POINT><SHORT-NAME>msp</SHORT-NAME></MODE-SWITCH-POINT>"
            "</MODE-SWITCH-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getModeSwitchPoints()) == 1

    def test_readRunnableEntity_with_parameterAccesses(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<PARAMETER-ACCESSS>"
            "<PARAMETER-ACCESS><SHORT-NAME>pa</SHORT-NAME></PARAMETER-ACCESS>"
            "</PARAMETER-ACCESSS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getParameterAccesses()) == 1

    def test_readRunnableEntity_with_arguments(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<ARGUMENTS>"
            "<RUNNABLE-ENTITY-ARGUMENT><SYMBOL>arg1</SYMBOL></RUNNABLE-ENTITY-ARGUMENT>"
            "</ARGUMENTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getArguments()) == 1

    def test_readRunnableEntity_with_asynchronousServerCallResultPoints(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS>"
            "<ASYNCHRONOUS-SERVER-CALL-RESULT-POINT>"
            "<SHORT-NAME>asrp</SHORT-NAME>"
            "</ASYNCHRONOUS-SERVER-CALL-RESULT-POINT>"
            "</ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert len(runnable.getAsynchronousServerCallResultPoints()) == 1

    def test_readRunnableEntity_with_canBeInvokedConcurrently(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SHORT-NAME>run</SHORT-NAME>"
            "<CAN-BE-INVOKED-CONCURRENTLY>true</CAN-BE-INVOKED-CONCURRENTLY>",
            root_tag="RUNNABLE-ENTITY",
        )
        parser.readRunnableEntity(element, runnable)
        assert runnable.getCanBeInvokedConcurrently().getValue() is True


# ==================== RTE Event Handlers ====================


class TestRteEventHandlers:
    """Exercise all RTE event types."""

    def test_readTimingEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createTimingEvent("te")
        element = _snip(
            "<SHORT-NAME>te</SHORT-NAME>"
            "<PERIOD>0.1</PERIOD>"
            "<OFFSET>0.05</OFFSET>",
            root_tag="TIMING-EVENT",
        )
        parser.readTimingEvent(element, event)
        assert event.getPeriod().getValue() == 0.1
        assert event.getOffset().getValue() == 0.05

    def test_readOperationInvokedEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createOperationInvokedEvent("oe")
        element = _snip(
            "<SHORT-NAME>oe</SHORT-NAME>"
            "<OPERATION-IREF>"
            "<CONTEXT-P-PORT-REF DEST='P-PORT-PROTOTYPE'>/port</CONTEXT-P-PORT-REF>"
            "<TARGET-PROVIDED-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/op</TARGET-PROVIDED-OPERATION-REF>"
            "</OPERATION-IREF>",
            root_tag="OPERATION-INVOKED-EVENT",
        )
        parser.readOperationInvokedEvent(element, event)
        assert event.getOperationIRef() is not None

    def test_readDataReceivedEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createDataReceivedEvent("dre")
        element = _snip(
            "<SHORT-NAME>dre</SHORT-NAME>"
            "<DATA-IREF>"
            "<CONTEXT-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rport</CONTEXT-R-PORT-REF>"
            "<TARGET-DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/data</TARGET-DATA-ELEMENT-REF>"
            "</DATA-IREF>",
            root_tag="DATA-RECEIVED-EVENT",
        )
        parser.readDataReceivedEvent(element, event)
        assert event.getDataIRef() is not None

    def test_readSwcModeSwitchEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createSwcModeSwitchEvent("mse")
        element = _snip(
            "<SHORT-NAME>mse</SHORT-NAME>"
            "<ACTIVATION>enable</ACTIVATION>"
            "<MODE-IREFS>"
            "<MODE-IREF>"
            "<CONTEXT-PORT-REF DEST='R-PORT-PROTOTYPE'>/port</CONTEXT-PORT-REF>"
            "</MODE-IREF>"
            "</MODE-IREFS>",
            root_tag="SWC-MODE-SWITCH-EVENT",
        )
        parser.readSwcModeSwitchEvent(element, event)
        assert event.getActivation().getValue() == "enable"

    def test_readInternalTriggerOccurredEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createInternalTriggerOccurredEvent("ito")
        element = _snip(
            "<SHORT-NAME>ito</SHORT-NAME>"
            "<EVENT-SOURCE-REF DEST='INTERNAL-TRIGGERING-POINT'>/itp</EVENT-SOURCE-REF>",
            root_tag="INTERNAL-TRIGGER-OCCURRED-EVENT",
        )
        parser.readInternalTriggerOccurredEvent(element, event)
        assert event.getEventSourceRef().getValue() == "/itp"

    def test_readInitEvent_minimal(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createInitEvent("ie")
        element = _snip("<SHORT-NAME>ie</SHORT-NAME>", root_tag="INIT-EVENT")
        parser.readInitEvent(element, event)
        assert event.getShortName() == "ie"

    def test_readAsynchronousServerCallReturnsEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createAsynchronousServerCallReturnsEvent("ascr")
        element = _snip(
            "<SHORT-NAME>ascr</SHORT-NAME>"
            "<EVENT-SOURCE-REF DEST='ASYNCHRONOUS-SERVER-CALL-POINT'>/acp</EVENT-SOURCE-REF>",
            root_tag="ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT",
        )
        parser.readAsynchronousServerCallReturnsEvent(element, event)
        assert event.getEventSourceRef().getValue() == "/acp"

    def test_readModeSwitchedAckEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createModeSwitchedAckEvent("msa")
        element = _snip(
            "<SHORT-NAME>msa</SHORT-NAME>"
            "<EVENT-SOURCE-REF DEST='MODE-SWITCH-POINT'>/msp</EVENT-SOURCE-REF>",
            root_tag="MODE-SWITCHED-ACK-EVENT",
        )
        parser.readModeSwitchedAckEvent(element, event)
        assert event.getEventSourceRef().getValue() == "/msp"

    def test_readBackgroundEvent_minimal(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createBackgroundEvent("be")
        element = _snip("<SHORT-NAME>be</SHORT-NAME>", root_tag="BACKGROUND-EVENT")
        parser.readBackgroundEvent(element, event)
        assert event.getShortName() == "be"

    def test_readDataSendCompletedEvent_full(self, parser):
        from armodel.models import SwcInternalBehavior, ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        event = behavior.createDataSendCompletedEvent("dsc")
        element = _snip(
            "<SHORT-NAME>dsc</SHORT-NAME>"
            "<EVENT-SOURCE-REF DEST='DATA-SEND-POINT'>/dsp</EVENT-SOURCE-REF>",
            root_tag="DATA-SEND-COMPLETED-EVENT",
        )
        parser.readDataSendCompletedEvent(element, event)
        assert event.getEventSourceRef().getValue() == "/dsp"


# ==================== SwComponentType Deep Handlers ====================


class TestSwComponentTypeDeepHandlers:
    """Exercise port groups, com specs, composition orchestrators."""

    def test_readSwComponentTypePortGroups_creates_group(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        element = _snip(
            "<PORT-GROUPS>"
            "<PORT-GROUP><SHORT-NAME>pg</SHORT-NAME></PORT-GROUP>"
            "</PORT-GROUPS>",
            root_tag="APPLICATION-SW-COMPONENT-TYPE",
        )
        parser.readSwComponentTypePortGroups(element, swc)
        assert len(swc.getPortGroups()) == 1

    def test_readPortGroupInnerGroupIRefs_adds_ref(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        port_group = swc.createPortGroup("pg")
        element = _snip(
            "<INNER-GROUP-IREFS>"
            "<INNER-GROUP-IREF>"
            "<TARGET-REF DEST='PORT-GROUP'>/pg2</TARGET-REF>"
            "</INNER-GROUP-IREF>"
            "</INNER-GROUP-IREFS>",
            root_tag="PORT-GROUP",
        )
        parser.readPortGroupInnerGroupIRefs(element, port_group)
        assert len(port_group.getInnerGroupIRefs()) == 1

    def test_readPortGroupOuterPortRefs_adds_ref(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        port_group = swc.createPortGroup("pg")
        element = _snip(
            "<OUTER-PORTS>"
            "<PORT-PROTOTYPE-REF-CONDITIONAL>"
            "<PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/port</PORT-PROTOTYPE-REF>"
            "</PORT-PROTOTYPE-REF-CONDITIONAL>"
            "</OUTER-PORTS>",
            root_tag="PORT-GROUP",
        )
        parser.readPortGroupOuterPortRefs(element, port_group)
        assert len(port_group.getOuterPortRefs()) == 1

    def test_readPPortPrototype_with_providedComSpecs(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        port = swc.createPPortPrototype("pport")
        element = _snip(
            "<SHORT-NAME>pport</SHORT-NAME>"
            "<PROVIDED-COM-SPECS>"
            "<NONQUEUED-SENDER-COM-SPEC>"
            "<DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/data</DATA-ELEMENT-REF>"
            "</NONQUEUED-SENDER-COM-SPEC>"
            "</PROVIDED-COM-SPECS>",
            root_tag="P-PORT-PROTOTYPE",
        )
        parser.readPPortPrototype(element, port)
        assert len(port.getProvidedComSpecs()) == 1

    def test_readRPortPrototype_with_requiredComSpecs(self, parser):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        port = swc.createRPortPrototype("rport")
        element = _snip(
            "<SHORT-NAME>rport</SHORT-NAME>"
            "<REQUIRED-COM-SPECS>"
            "<NONQUEUED-RECEIVER-COM-SPEC>"
            "<DATA-ELEMENT-REF DEST='VARIABLE-DATA-PROTOTYPE'>/data</DATA-ELEMENT-REF>"
            "</NONQUEUED-RECEIVER-COM-SPEC>"
            "</REQUIRED-COM-SPECS>",
            root_tag="R-PORT-PROTOTYPE",
        )
        parser.readRPortPrototype(element, port)
        assert len(port.getRequiredComSpecs()) == 1

    def test_readCompositionSwComponentTypeComponents_creates(self, parser):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        element = _snip(
            "<COMPONENTS>"
            "<SW-COMPONENT-PROTOTYPE><SHORT-NAME>proto</SHORT-NAME></SW-COMPONENT-PROTOTYPE>"
            "</COMPONENTS>",
            root_tag="COMPOSITION-SW-COMPONENT-TYPE",
        )
        parser.readCompositionSwComponentTypeComponents(element, comp)
        assert len(comp.getComponents()) == 1

    def test_readCompositionSwComponentTypeSwConnectors_assembly(self, parser):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        element = _snip(
            "<CONNECTORS>"
            "<ASSEMBLY-SW-CONNECTOR><SHORT-NAME>conn</SHORT-NAME></ASSEMBLY-SW-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="COMPOSITION-SW-COMPONENT-TYPE",
        )
        parser.readCompositionSwComponentTypeSwConnectors(element, comp)
        assert len(comp.getAssemblySwConnectors()) == 1

    def test_readCompositionSwComponentTypeSwConnectors_delegation(self, parser):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        element = _snip(
            "<CONNECTORS>"
            "<DELEGATION-SW-CONNECTOR>"
            "<SHORT-NAME>conn</SHORT-NAME>"
            "<INNER-PORT-IREF>"
            "<R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/comp</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rport</TARGET-R-PORT-REF>"
            "</R-PORT-IN-COMPOSITION-INSTANCE-REF>"
            "</INNER-PORT-IREF>"
            "</DELEGATION-SW-CONNECTOR>"
            "</CONNECTORS>",
            root_tag="COMPOSITION-SW-COMPONENT-TYPE",
        )
        parser.readCompositionSwComponentTypeSwConnectors(element, comp)
        assert len(comp.getDelegationSwConnectors()) == 1

    def test_readAssemblySwConnector_full(self, parser):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        connector = comp.createAssemblySwConnector("conn")
        element = _snip(
            "<SHORT-NAME>conn</SHORT-NAME>"
            "<PROVIDER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/proto1</CONTEXT-COMPONENT-REF>"
            "<TARGET-P-PORT-REF DEST='P-PORT-PROTOTYPE'>/pport</TARGET-P-PORT-REF>"
            "</PROVIDER-IREF>"
            "<REQUESTER-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/proto2</CONTEXT-COMPONENT-REF>"
            "<TARGET-R-PORT-REF DEST='R-PORT-PROTOTYPE'>/rport</TARGET-R-PORT-REF>"
            "</REQUESTER-IREF>",
            root_tag="ASSEMBLY-SW-CONNECTOR",
        )
        parser.readAssemblySwConnector(element, connector)
        assert connector.getProviderIRef() is not None
        assert connector.getRequesterIRef() is not None

    def test_readSwComponentPrototype_sets_typeTRef(self, parser):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        proto = comp.createSwComponentPrototype("proto")
        element = _snip(
            "<SHORT-NAME>proto</SHORT-NAME>"
            "<TYPE-TREF DEST='APPLICATION-SW-COMPONENT-TYPE'>/swc</TYPE-TREF>",
            root_tag="SW-COMPONENT-PROTOTYPE",
        )
        parser.readSwComponentPrototype(element, proto)
        assert proto.getTypeTRef().getValue() == "/swc"


# ==================== Port Interface Handlers ====================


class TestPortInterfaceHandlers:
    """Exercise sender/receiver, client/server, and other port interfaces."""

    def test_readSenderReceiverInterface_full(self, parser):
        from armodel.models import SenderReceiverInterface

        sr_if = SenderReceiverInterface(parent=_autosar_root(), short_name="sr_if")
        element = _snip(
            "<SHORT-NAME>sr_if</SHORT-NAME>"
            "<IS-SERVICE>true</IS-SERVICE>"
            "<DATA-ELEMENTS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>data</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</DATA-ELEMENTS>",
            root_tag="SENDER-RECEIVER-INTERFACE",
        )
        parser.readSenderReceiverInterface(element, sr_if)
        assert sr_if.getIsService().getValue() is True
        assert len(sr_if.getDataElements()) == 1

    def test_readClientServerInterface_full(self, parser):
        from armodel.models import ClientServerInterface

        cs_if = ClientServerInterface(parent=_autosar_root(), short_name="cs_if")
        element = _snip(
            "<SHORT-NAME>cs_if</SHORT-NAME>"
            "<OPERATIONS>"
            "<CLIENT-SERVER-OPERATION><SHORT-NAME>op</SHORT-NAME></CLIENT-SERVER-OPERATION>"
            "</OPERATIONS>"
            "<POSSIBLE-ERRORS>"
            "<APPLICATION-ERROR><SHORT-NAME>err</SHORT-NAME></APPLICATION-ERROR>"
            "</POSSIBLE-ERRORS>",
            root_tag="CLIENT-SERVER-INTERFACE",
        )
        parser.readClientServerInterface(element, cs_if)
        assert len(cs_if.getOperations()) == 1
        assert len(cs_if.getPossibleErrors()) == 1

    def test_readParameterInterface_full(self, parser):
        from armodel.models import ParameterInterface

        param_if = ParameterInterface(parent=_autosar_root(), short_name="param_if")
        element = _snip(
            "<SHORT-NAME>param_if</SHORT-NAME>"
            "<PARAMETERS>"
            "<PARAMETER-DATA-PROTOTYPE><SHORT-NAME>param</SHORT-NAME></PARAMETER-DATA-PROTOTYPE>"
            "</PARAMETERS>",
            root_tag="PARAMETER-INTERFACE",
        )
        parser.readParameterInterface(element, param_if)
        assert len(param_if.getParameters()) == 1

    def test_readNvDataInterface_full(self, parser):
        from armodel.models import NvDataInterface

        nv_if = NvDataInterface(parent=_autosar_root(), short_name="nv_if")
        element = _snip(
            "<SHORT-NAME>nv_if</SHORT-NAME>"
            "<NV-DATAS>"
            "<VARIABLE-DATA-PROTOTYPE><SHORT-NAME>nvdata</SHORT-NAME></VARIABLE-DATA-PROTOTYPE>"
            "</NV-DATAS>",
            root_tag="NV-DATA-INTERFACE",
        )
        parser.readNvDataInterface(element, nv_if)
        assert len(nv_if.getNvDatas()) == 1

    def test_readModeSwitchInterface_full(self, parser):
        from armodel.models import ModeSwitchInterface

        mode_if = ModeSwitchInterface(parent=_autosar_root(), short_name="mode_if")
        element = _snip(
            "<SHORT-NAME>mode_if</SHORT-NAME>"
            "<MODE-GROUP>"
            "<SHORT-NAME>mg</SHORT-NAME>"
            "<TYPE-TREF DEST='MODE-DECLARATION-GROUP'>/mg</TYPE-TREF>"
            "</MODE-GROUP>",
            root_tag="MODE-SWITCH-INTERFACE",
        )
        parser.readModeSwitchInterface(element, mode_if)
        assert len(mode_if.getModeGroups()) == 1

    def test_readClientServerOperation_with_arguments(self, parser):
        from armodel.models import ClientServerInterface

        cs_if = ClientServerInterface(parent=_autosar_root(), short_name="cs_if")
        op = cs_if.createOperation("op")
        element = _snip(
            "<SHORT-NAME>op</SHORT-NAME>"
            "<ARGUMENTS>"
            "<ARGUMENT-DATA-PROTOTYPE><SHORT-NAME>arg</SHORT-NAME><DIRECTION>IN</DIRECTION></ARGUMENT-DATA-PROTOTYPE>"
            "</ARGUMENTS>",
            root_tag="CLIENT-SERVER-OPERATION",
        )
        parser.readClientServerOperation(element, op)
        assert len(op.getArguments()) == 1

    def test_readArgumentDataPrototype_sets_direction(self, parser):
        from armodel.models import ClientServerInterface

        cs_if = ClientServerInterface(parent=_autosar_root(), short_name="cs_if")
        op = cs_if.createOperation("op")
        arg = op.createArgumentDataPrototype("arg")
        element = _snip(
            "<SHORT-NAME>arg</SHORT-NAME>"
            "<DIRECTION>IN</DIRECTION>"
            "<SERVER-ARGUMENT-IMPL-POLICY>use</SERVER-ARGUMENT-IMPL-POLICY>",
            root_tag="ARGUMENT-DATA-PROTOTYPE",
        )
        parser.readArgumentDataPrototype(element, arg)
        assert arg.getDirection().getValue() == "IN"


# ==================== DataType and Compu Handlers ====================


class TestDataTypeAndCompuHandlers:
    """Exercise data types, CompuMethod, DataConstr, Unit, SwBaseType."""

    def test_readCompuMethod_full(self, parser):
        from armodel.models import CompuMethod

        method = CompuMethod(parent=_autosar_root(), short_name="cm")
        element = _snip(
            "<SHORT-NAME>cm</SHORT-NAME>"
            "<UNIT-REF DEST='UNIT'>/unit</UNIT-REF>"
            "<COMPU-INTERNAL-TO-PHYS>"
            "<COMPU-SCALES>"
            "<COMPU-SCALE>"
            "<SHORT-LABEL>scale1</SHORT-LABEL>"
            "<LOWER-LIMIT>0</LOWER-LIMIT>"
            "<UPPER-LIMIT>10</UPPER-LIMIT>"
            "<COMPU-CONST><VT>value1</VT></COMPU-CONST>"
            "</COMPU-SCALE>"
            "</COMPU-SCALES>"
            "</COMPU-INTERNAL-TO-PHYS>",
            root_tag="COMPU-METHOD",
        )
        parser.readCompuMethod(element, method)
        assert method.getUnitRef().getValue() == "/unit"

    def test_readDataConstr_full(self, parser):
        from armodel.models import DataConstr

        constr = DataConstr(parent=_autosar_root(), short_name="dc")
        element = _snip(
            "<SHORT-NAME>dc</SHORT-NAME>"
            "<DATA-CONSTR-RULES>"
            "<DATA-CONSTR-RULE>"
            "<CONSTR-LEVEL>1</CONSTR-LEVEL>"
            "<INTERNAL-CONSTRS>"
            "<LOWER-LIMIT>0</LOWER-LIMIT>"
            "<UPPER-LIMIT>100</UPPER-LIMIT>"
            "</INTERNAL-CONSTRS>"
            "</DATA-CONSTR-RULE>"
            "</DATA-CONSTR-RULES>",
            root_tag="DATA-CONSTR",
        )
        parser.readDataConstr(element, constr)
        assert len(constr.getDataConstrRules()) == 1

    def test_readUnit_full(self, parser):
        from armodel.models import Unit

        unit = Unit(parent=_autosar_root(), short_name="unit")
        element = _snip(
            "<SHORT-NAME>unit</SHORT-NAME>"
            "<DISPLAY-NAME>m/s</DISPLAY-NAME>"
            "<FACTOR-SI-TO-UNIT>1.0</FACTOR-SI-TO-UNIT>"
            "<OFFSET-SI-TO-UNIT>0.0</OFFSET-SI-TO-UNIT>",
            root_tag="UNIT",
        )
        parser.readUnit(element, unit)
        assert unit.getDisplayName().getValue() == "m/s"

    def test_readSwBaseType_full(self, parser):
        from armodel.models import SwBaseType

        base_type = SwBaseType(parent=_autosar_root(), short_name="bt")
        element = _snip(
            "<SHORT-NAME>bt</SHORT-NAME>"
            "<BASE-TYPE-SIZE>32</BASE-TYPE-SIZE>"
            "<BASE-TYPE-ENCODING>UNSIGNED</BASE-TYPE-ENCODING>"
            "<BYTE-ORDER>LITTLE-ENDIAN</BYTE-ORDER>",
            root_tag="SW-BASE-TYPE",
        )
        parser.readSwBaseType(element, base_type)
        assert base_type.getBaseTypeDefinition().getBaseTypeSize().getValue() == 32

    def test_readApplicationPrimitiveDataType_full(self, parser):
        from armodel.models import ApplicationPrimitiveDataType

        data_type = ApplicationPrimitiveDataType(parent=_autosar_root(), short_name="apdt")
        element = _snip(
            "<SHORT-NAME>apdt</SHORT-NAME>"
            "<SW-DATA-DEF-PROPS>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL>"
            "<BASE-TYPE-REF DEST='SW-BASE-TYPE'>/bt</BASE-TYPE-REF>"
            "</SW-DATA-DEF-PROPS-CONDITIONAL>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</SW-DATA-DEF-PROPS>",
            root_tag="APPLICATION-PRIMITIVE-DATA-TYPE",
        )
        parser.readApplicationPrimitiveDataType(element, data_type)
        assert data_type.getSwDataDefProps() is not None

    def test_readApplicationRecordDataType_full(self, parser):
        from armodel.models import ApplicationRecordDataType

        data_type = ApplicationRecordDataType(parent=_autosar_root(), short_name="ardt")
        element = _snip(
            "<SHORT-NAME>ardt</SHORT-NAME>"
            "<ELEMENTS>"
            "<APPLICATION-RECORD-ELEMENT><SHORT-NAME>elem</SHORT-NAME></APPLICATION-RECORD-ELEMENT>"
            "</ELEMENTS>",
            root_tag="APPLICATION-RECORD-DATA-TYPE",
        )
        parser.readApplicationRecordDataType(element, data_type)
        assert len(data_type.getApplicationRecordElements()) == 1

    def test_readImplementationDataType_full(self, parser):
        from armodel.models import ImplementationDataType

        data_type = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SHORT-NAME>idt</SHORT-NAME>"
            "<SUB-ELEMENTS>"
            "<IMPLEMENTATION-DATA-TYPE-ELEMENT><SHORT-NAME>se</SHORT-NAME></IMPLEMENTATION-DATA-TYPE-ELEMENT>"
            "</SUB-ELEMENTS>"
            "<TYPE-EMITTER>emitter</TYPE-EMITTER>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        parser.readImplementationDataType(element, data_type)
        assert len(data_type.getSubElements()) == 1

    def test_readSwRecordLayout_full(self, parser):
        from armodel.models import SwRecordLayout

        layout = SwRecordLayout(parent=_autosar_root(), short_name="srl")
        element = _snip(
            "<SHORT-NAME>srl</SHORT-NAME>"
            "<SW-RECORD-LAYOUT-GROUP>"
            "<SHORT-LABEL>group</SHORT-LABEL>"
            "<CATEGORY>cat</CATEGORY>"
            "</SW-RECORD-LAYOUT-GROUP>",
            root_tag="SW-RECORD-LAYOUT",
        )
        parser.readSwRecordLayout(element, layout)
        assert layout.getSwRecordLayoutGroup() is not None

    def test_readSwAddrMethod_full(self, parser):
        from armodel.models import SwAddrMethod

        method = SwAddrMethod(parent=_autosar_root(), short_name="sam")
        element = _snip(
            "<SHORT-NAME>sam</SHORT-NAME>"
            "<MEMORY-ALLOCATION-KEYWORD-POLICY>policy</MEMORY-ALLOCATION-KEYWORD-POLICY>"
            "<OPTIONS>"
            "<OPTION>opt1</OPTION>"
            "</OPTIONS>"
            "<SECTION-INITIALIZATION-POLICY>init</SECTION-INITIALIZATION-POLICY>"
            "<SECTION-TYPE>type</SECTION-TYPE>",
            root_tag="SW-ADDR-METHOD",
        )
        parser.readSwAddrMethod(element, method)
        assert method.getMemoryAllocationKeywordPolicy().getValue() == "policy"


# ==================== Value Specification Handlers ====================


class TestValueSpecificationHandlers:
    """Exercise all value specification types."""

    def test_getApplicationValueSpecification_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>avs</SHORT-LABEL>"
            "<CATEGORY>cat</CATEGORY>"
            "<SW-VALUE-CONT>"
            "<UNIT-REF DEST='UNIT'>/unit</UNIT-REF>"
            "<SW-VALUES-PHYS>"
            "<V>1.0</V>"
            "</SW-VALUES-PHYS>"
            "</SW-VALUE-CONT>",
            root_tag="APPLICATION-VALUE-SPECIFICATION",
        )
        spec = parser.getApplicationValueSpecification(element)
        assert spec.getCategory().getValue() == "cat"

    def test_getNumericalValueSpecification_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>nvs</SHORT-LABEL>"
            "<VALUE>42</VALUE>",
            root_tag="NUMERICAL-VALUE-SPECIFICATION",
        )
        spec = parser.getNumericalValueSpecification(element)
        assert spec.getValue().getValue() == 42

    def test_getTextValueSpecification_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>tvs</SHORT-LABEL>"
            "<VALUE>text</VALUE>",
            root_tag="TEXT-VALUE-SPECIFICATION",
        )
        spec = parser.getTextValueSpecification(element)
        assert spec.getValue().getValue() == "text"

    def test_getArrayValueSpecification_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>avs</SHORT-LABEL>"
            "<ELEMENTS>"
            "<NUMERICAL-VALUE-SPECIFICATION><VALUE>1</VALUE></NUMERICAL-VALUE-SPECIFICATION>"
            "<NUMERICAL-VALUE-SPECIFICATION><VALUE>2</VALUE></NUMERICAL-VALUE-SPECIFICATION>"
            "</ELEMENTS>",
            root_tag="ARRAY-VALUE-SPECIFICATION",
        )
        spec = parser.getArrayValueSpecification(element)
        assert len(spec.getElements()) == 2

    def test_getConstantReference_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>cr</SHORT-LABEL>"
            "<CONSTANT-REF DEST='CONSTANT-SPECIFICATION'>/const</CONSTANT-REF>",
            root_tag="CONSTANT-REFERENCE",
        )
        spec = parser.getConstantReference(element)
        assert spec.getConstantRef().getValue() == "/const"

    def test_getRecordValueSpecification_full(self, parser):
        element = _snip(
            "<SHORT-LABEL>rvs</SHORT-LABEL>"
            "<FIELDS>"
            "<NUMERICAL-VALUE-SPECIFICATION><SHORT-LABEL>f1</SHORT-LABEL><VALUE>1</VALUE></NUMERICAL-VALUE-SPECIFICATION>"
            "</FIELDS>",
            root_tag="RECORD-VALUE-SPECIFICATION",
        )
        spec = parser.getRecordValueSpecification(element)
        assert len(spec.getFields()) == 1


# ==================== System and Mapping Handlers ====================


class TestSystemAndMappingHandlers:
    """Exercise system orchestrator, mappings, and fibex refs."""

    def test_readSystem_full(self, parser):
        from armodel.models import System

        system = System(parent=_autosar_root(), short_name="sys")
        element = _snip(
            "<SHORT-NAME>sys</SHORT-NAME>"
            "<ECU-EXTRACT-VERSION>1.0</ECU-EXTRACT-VERSION>"
            "<FIBEX-ELEMENTS>"
            "<FIBEX-ELEMENT-REF-CONDITIONAL>"
            "<FIBEX-ELEMENT-REF DEST='CAN-CLUSTER'>/can</FIBEX-ELEMENT-REF>"
            "</FIBEX-ELEMENT-REF-CONDITIONAL>"
            "</FIBEX-ELEMENTS>"
            "<MAPPINGS>"
            "<SYSTEM-MAPPING><SHORT-NAME>sm</SHORT-NAME></SYSTEM-MAPPING>"
            "</MAPPINGS>",
            root_tag="SYSTEM",
        )
        parser.readSystem(element, system)
        assert system.getEcuExtractVersion().getValue() == "1.0"
        assert len(system.getFibexElementRefs()) == 1
        assert len(system.getMappings()) == 1

    def test_readSystemMapping_full(self, parser):
        from armodel.models import System, SystemMapping

        system = System(parent=_autosar_root(), short_name="sys")
        mapping = system.createSystemMapping("sm")
        element = _snip(
            "<SHORT-NAME>sm</SHORT-NAME>"
            "<DATA-MAPPINGS>"
            "<SENDER-RECEIVER-TO-SIGNAL-MAPPING>"
            "<COMMUNICATION-DIRECTION>in</COMMUNICATION-DIRECTION>"
            "<SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/sig</SYSTEM-SIGNAL-REF>"
            "</SENDER-RECEIVER-TO-SIGNAL-MAPPING>"
            "</DATA-MAPPINGS>"
            "<SW-MAPPINGS>"
            "<SWC-TO-ECU-MAPPING><SHORT-NAME>swcEcu</SHORT-NAME></SWC-TO-ECU-MAPPING>"
            "</SW-MAPPINGS>"
            "<ECU-RESOURCE-MAPPINGS>"
            "<ECU-MAPPING><SHORT-NAME>ecuMap</SHORT-NAME></ECU-MAPPING>"
            "</ECU-RESOURCE-MAPPINGS>"
            "<SW-IMPL-MAPPINGS>"
            "<SWC-TO-IMPL-MAPPING><SHORT-NAME>swcImpl</SHORT-NAME></SWC-TO-IMPL-MAPPING>"
            "</SW-IMPL-MAPPINGS>",
            root_tag="SYSTEM-MAPPING",
        )
        parser.readSystemMapping(element, mapping)
        assert len(mapping.getDataMappings()) == 1
        assert len(mapping.getSwMappings()) == 1
        assert len(mapping.getEcuResourceMappings()) == 1
        assert len(mapping.getSwImplMappings()) == 1

    def test_readSwcToEcuMapping_full(self, parser):
        from armodel.models import System, SystemMapping

        system = System(parent=_autosar_root(), short_name="sys")
        mapping = system.createSystemMapping("sm")
        swc_mapping = mapping.createSwcToEcuMapping("swcEcu")
        element = _snip(
            "<SHORT-NAME>swcEcu</SHORT-NAME>"
            "<COMPONENT-IREFS>"
            "<COMPONENT-IREF>"
            "<TARGET-REF DEST='SW-COMPONENT-PROTOTYPE'>/proto</TARGET-REF>"
            "</COMPONENT-IREF>"
            "</COMPONENT-IREFS>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ecu</ECU-INSTANCE-REF>",
            root_tag="SWC-TO-ECU-MAPPING",
        )
        parser.readSwcToEcuMapping(element, swc_mapping)
        assert swc_mapping.getEcuInstanceRef().getValue() == "/ecu"

    def test_readEcuMapping_full(self, parser):
        from armodel.models import System, SystemMapping

        system = System(parent=_autosar_root(), short_name="sys")
        mapping = system.createSystemMapping("sm")
        ecu_mapping = mapping.createECUMapping("ecuMap")
        element = _snip(
            "<SHORT-NAME>ecuMap</SHORT-NAME>"
            "<ECU-INSTANCE-REF DEST='ECU-INSTANCE'>/ecuInst</ECU-INSTANCE-REF>"
            "<ECU-REF DEST='ECU'>/ecu</ECU-REF>",
            root_tag="ECU-MAPPING",
        )
        parser.readEcuMapping(element, ecu_mapping)
        assert ecu_mapping.getEcuInstanceRef().getValue() == "/ecuInst"

    def test_readSwcToImplMapping_full(self, parser):
        from armodel.models import System, SystemMapping

        system = System(parent=_autosar_root(), short_name="sys")
        mapping = system.createSystemMapping("sm")
        impl_mapping = mapping.createSwcToImplMapping("swcImpl")
        element = _snip(
            "<SHORT-NAME>swcImpl</SHORT-NAME>"
            "<COMPONENT-IMPLEMENTATION-REF DEST='SWC-IMPLEMENTATION'>/impl</COMPONENT-IMPLEMENTATION-REF>"
            "<COMPONENT-IREFS>"
            "<COMPONENT-IREF>"
            "<TARGET-REF DEST='SW-COMPONENT-PROTOTYPE'>/proto</TARGET-REF>"
            "</COMPONENT-IREF>"
            "</COMPONENT-IREFS>",
            root_tag="SWC-TO-IMPL-MAPPING",
        )
        parser.readSwcToImplMapping(element, impl_mapping)
        assert impl_mapping.getComponentImplementationRef().getValue() == "/impl"

    def test_readGateway_full(self, parser):
        from armodel.models import Gateway

        gateway = Gateway(parent=_autosar_root(), short_name="gw")
        element = _snip(
            "<SHORT-NAME>gw</SHORT-NAME>"
            "<ECU-REF DEST='ECU-INSTANCE'>/ecu</ECU-REF>"
            "<I-PDU-MAPPINGS>"
            "<I-PDU-MAPPING>"
            "<SOURCE-I-PDU-REF DEST='I-PDU'>/ipdu1</SOURCE-I-PDU-REF>"
            "</I-PDU-MAPPING>"
            "</I-PDU-MAPPINGS>"
            "<SIGNAL-MAPPINGS>"
            "<I-SIGNAL-MAPPING>"
            "<SOURCE-SIGNAL-REF DEST='I-SIGNAL'>/sig1</SOURCE-SIGNAL-REF>"
            "</I-SIGNAL-MAPPING>"
            "</SIGNAL-MAPPINGS>",
            root_tag="GATEWAY",
        )
        parser.readGateway(element, gateway)
        assert gateway.getEcuRef().getValue() == "/ecu"
        assert len(gateway.getIPduMappings()) == 1
        assert len(gateway.getSignalMappings()) == 1


# ==================== ECUC Def and Value Handlers ====================


class TestEcucDefAndValueHandlers:
    """Exercise ECUC value collection, module configuration values, and container values."""

    def test_readEcucValueCollection_full(self, parser):
        from armodel.models import EcucValueCollection

        collection = EcucValueCollection(parent=_autosar_root(), short_name="evc")
        element = _snip(
            "<SHORT-NAME>evc</SHORT-NAME>"
            "<ECU-EXTRACT-REF DEST='SYSTEM'>/sys</ECU-EXTRACT-REF>"
            "<ECUC-VALUES>"
            "<ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL>"
            "<ECUC-MODULE-CONFIGURATION-VALUES-REF DEST='ECUC-MODULE-CONFIGURATION-VALUES'>/values</ECUC-MODULE-CONFIGURATION-VALUES-REF>"
            "</ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL>"
            "</ECUC-VALUES>",
            root_tag="ECUC-VALUE-COLLECTION",
        )
        parser.readEcucValueCollection(element, collection)
        assert collection.getEcuExtractRef().getValue() == "/sys"
        assert len(collection.getEcucValueRefs()) == 1

    def test_readEcucModuleConfigurationValues_full(self, parser):
        from armodel.models import EcucModuleConfigurationValues

        values = EcucModuleConfigurationValues(parent=_autosar_root(), short_name="emcv")
        element = _snip(
            "<SHORT-NAME>emcv</SHORT-NAME>"
            "<DEFINITION-REF DEST='ECUC-MODULE-DEF'>/def</DEFINITION-REF>"
            "<MODULE-DESCRIPTION-REF DEST='BSW-MODULE-DESCRIPTION'>/desc</MODULE-DESCRIPTION-REF>"
            "<IMPLEMENTATION-CONFIG-VARIANT>variant</IMPLEMENTATION-CONFIG-VARIANT>"
            "<CONTAINERS>"
            "<ECUC-CONTAINER-VALUE><SHORT-NAME>container</SHORT-NAME></ECUC-CONTAINER-VALUE>"
            "</CONTAINERS>",
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        parser.readEcucModuleConfigurationValues(element, values)
        assert values.getDefinitionRef().getValue() == "/def"
        assert len(values.getContainers()) == 1

    def test_readEcucContainerValue_full(self, parser):
        from armodel.models import EcucModuleConfigurationValues, EcucContainerValue

        values = EcucModuleConfigurationValues(parent=_autosar_root(), short_name="emcv")
        container = values.createContainer("container")
        element = _snip(
            "<SHORT-NAME>container</SHORT-NAME>"
            "<DEFINITION-REF DEST='ECUC-PARAM-CONF-CONTAINER-DEF'>/def</DEFINITION-REF>"
            "<PARAMETER-VALUES>"
            "<ECUC-NUMERICAL-PARAM-VALUE>"
            "<DEFINITION-REF DEST='ECUC-INTEGER-PARAM-DEF'>/paramDef</DEFINITION-REF>"
            "<VALUE>42</VALUE>"
            "</ECUC-NUMERICAL-PARAM-VALUE>"
            "</PARAMETER-VALUES>"
            "<REFERENCE-VALUES>"
            "<ECUC-REFERENCE-VALUE>"
            "<DEFINITION-REF DEST='ECUC-REFERENCE-DEF'>/refDef</DEFINITION-REF>"
            "<VALUE-REF DEST='ECUC-CONTAINER-VALUE'>/ref</VALUE-REF>"
            "</ECUC-REFERENCE-VALUE>"
            "</REFERENCE-VALUES>"
            "<SUB-CONTAINERS>"
            "<ECUC-CONTAINER-VALUE><SHORT-NAME>sub</SHORT-NAME></ECUC-CONTAINER-VALUE>"
            "</SUB-CONTAINERS>",
            root_tag="ECUC-CONTAINER-VALUE",
        )
        parser.readEcucContainerValue(element, container)
        assert container.getDefinitionRef().getValue() == "/def"
        assert len(container.getParameterValues()) == 1
        assert len(container.getReferenceValues()) == 1
        assert len(container.getSubContainers()) == 1

    def test_getEcucNumericalParamValue_full(self, parser):
        element = _snip(
            "<DEFINITION-REF DEST='ECUC-INTEGER-PARAM-DEF'>/def</DEFINITION-REF>"
            "<VALUE>100</VALUE>",
            root_tag="ECUC-NUMERICAL-PARAM-VALUE",
        )
        param = parser.getEcucNumericalParamValue(element)
        assert param.getValue().getValue() == 100

    def test_getEcucTextualParamValue_full(self, parser):
        element = _snip(
            "<DEFINITION-REF DEST='ECUC-STRING-PARAM-DEF'>/def</DEFINITION-REF>"
            "<VALUE>text</VALUE>",
            root_tag="ECUC-TEXTUAL-PARAM-VALUE",
        )
        param = parser.getEcucTextualParamValue(element)
        assert param.getValue().getValue() == "text"

    def test_getEcucReferenceValue_full(self, parser):
        element = _snip(
            "<DEFINITION-REF DEST='ECUC-REFERENCE-DEF'>/def</DEFINITION-REF>"
            "<VALUE-REF DEST='ECUC-CONTAINER-VALUE'>/ref</VALUE-REF>",
            root_tag="ECUC-REFERENCE-VALUE",
        )
        ref = parser.getEcucReferenceValue(element)
        assert ref.getValueRef().getValue() == "/ref"


# ==================== Life Cycle and Variant Handlers ====================


class TestLifeCycleAndVariantHandlers:
    """Exercise life cycle info set, predefined variant, flat map, flat instance descriptor."""

    def test_readLifeCycleInfoSet_full(self, parser):
        from armodel.models import LifeCycleInfoSet

        info_set = LifeCycleInfoSet(parent=_autosar_root(), short_name="lcis")
        element = _snip(
            "<SHORT-NAME>lcis</SHORT-NAME>"
            "<DEFAULT-LC-STATE-REF DEST='LIFE-CYCLE-STATE'>/state</DEFAULT-LC-STATE-REF>"
            "<LIFE-CYCLE-INFOS>"
            "<LIFE-CYCLE-INFO>"
            "<LC-OBJECT-REF DEST='SWC-IMPLEMENTATION'>/obj</LC-OBJECT-REF>"
            "<LC-STATE-REF DEST='LIFE-CYCLE-STATE'>/lcs</LC-STATE-REF>"
            "</LIFE-CYCLE-INFO>"
            "</LIFE-CYCLE-INFOS>",
            root_tag="LIFE-CYCLE-INFO-SET",
        )
        parser.readLifeCycleInfoSet(element, info_set)
        assert info_set.getDefaultLcStateRef().getValue() == "/state"
        assert len(info_set.getLifeCycleInfos()) == 1

    def test_readLifeCycleInfo_full(self, parser):
        from armodel.models import LifeCycleInfo

        info = LifeCycleInfo()
        element = _snip(
            "<LC-OBJECT-REF DEST='SWC-IMPLEMENTATION'>/obj</LC-OBJECT-REF>"
            "<LC-STATE-REF DEST='LIFE-CYCLE-STATE'>/state</LC-STATE-REF>"
            "<USE-INSTEAD-REFS>"
            "<USE-INSTEAD-REF DEST='SWC-IMPLEMENTATION'>/other</USE-INSTEAD-REF>"
            "</USE-INSTEAD-REFS>",
            root_tag="LIFE-CYCLE-INFO",
        )
        parser.readLifeCycleInfo(element, info)
        assert info.getLcObjectRef().getValue() == "/obj"
        assert len(info.getUseInsteadRefs()) == 1

    def test_readFlatMap_full(self, parser):
        from armodel.models import FlatMap

        flat_map = FlatMap(parent=_autosar_root(), short_name="fm")
        element = _snip(
            "<SHORT-NAME>fm</SHORT-NAME>"
            "<INSTANCES>"
            "<FLAT-INSTANCE-DESCRIPTOR><SHORT-NAME>fid</SHORT-NAME></FLAT-INSTANCE-DESCRIPTOR>"
            "</INSTANCES>",
            root_tag="FLAT-MAP",
        )
        parser.readFlatMap(element, flat_map)
        assert len(flat_map.getInstances()) == 1

    def test_readFlatInstanceDescriptor_full(self, parser):
        from armodel.models import FlatMap, FlatInstanceDescriptor

        flat_map = FlatMap(parent=_autosar_root(), short_name="fm")
        desc = flat_map.createFlatInstanceDescriptor("fid")
        element = _snip(
            "<SHORT-NAME>fid</SHORT-NAME>"
            "<UPSTREAM-REFERENCE-IREF>"
            "<BASE-REF DEST='SW-COMPONENT-PROTOTYPE'>/base</BASE-REF>"
            "<TARGET-REF DEST='RUNNABLE-ENTITY'>/target</TARGET-REF>"
            "</UPSTREAM-REFERENCE-IREF>",
            root_tag="FLAT-INSTANCE-DESCRIPTOR",
        )
        parser.readFlatInstanceDescriptor(element, desc)
        assert desc.getUpstreamReferenceIRef() is not None


# ==================== Implementations Handlers ====================


class TestImplementationsHandlers:
    """Exercise code/artifact descriptors, resource consumption, implementations."""

    def test_readCodeDescriptor_full(self, parser):
        from armodel.models import SwcImplementation

        impl = SwcImplementation(parent=_autosar_root(), short_name="impl")
        element = _snip(
            "<CODE-DESCRIPTORS>"
            "<CODE>"
            "<SHORT-NAME>code</SHORT-NAME>"
            "<ARTIFACT-DESCRIPTORS>"
            "<AUTOSAR-ENGINEERING-OBJECT>"
            "<SHORT-LABEL>obj</SHORT-LABEL>"
            "<CATEGORY>cat</CATEGORY>"
            "</AUTOSAR-ENGINEERING-OBJECT>"
            "</ARTIFACT-DESCRIPTORS>"
            "</CODE>"
            "</CODE-DESCRIPTORS>",
            root_tag="SWC-IMPLEMENTATION",
        )
        parser.readCodeDescriptor(element, impl)
        assert len(impl.getCodeDescriptors()) == 1

    def test_readSwcImplementation_full(self, parser):
        from armodel.models import SwcImplementation

        impl = SwcImplementation(parent=_autosar_root(), short_name="impl")
        element = _snip(
            "<SHORT-NAME>impl</SHORT-NAME>"
            "<BEHAVIOR-REF DEST='SWC-INTERNAL-BEHAVIOR'>/bh</BEHAVIOR-REF>"
            "<PROGRAMMING-LANGUAGE>C</PROGRAMMING-LANGUAGE>"
            "<SW-VERSION>1.0</SW-VERSION>"
            "<VENDOR-ID>1</VENDOR-ID>",
            root_tag="SWC-IMPLEMENTATION",
        )
        parser.readSwcImplementation(element, impl)
        assert impl.getBehaviorRef().getValue() == "/bh"
        assert impl.getProgrammingLanguage().getValue() == "C"

    def test_readBswImplementation_full(self, parser):
        from armodel.models import BswImplementation

        impl = BswImplementation(parent=_autosar_root(), short_name="bswImpl")
        element = _snip(
            "<SHORT-NAME>bswImpl</SHORT-NAME>"
            "<BEHAVIOR-REF DEST='BSW-INTERNAL-BEHAVIOR'>/bh</BEHAVIOR-REF>"
            "<AR-RELEASE-VERSION>4.0</AR-RELEASE-VERSION>"
            "<VENDOR-API-INFIX>api</VENDOR-API-INFIX>"
            "<VENDOR-SPECIFIC-MODULE-DEF-REFS>"
            "<VENDOR-SPECIFIC-MODULE-DEF-REF DEST='BSW-MODULE-DESCRIPTION'>/mod</VENDOR-SPECIFIC-MODULE-DEF-REF>"
            "</VENDOR-SPECIFIC-MODULE-DEF-REFS>",
            root_tag="BSW-IMPLEMENTATION",
        )
        parser.readBswImplementation(element, impl)
        assert impl.getBehaviorRef().getValue() == "/bh"
        assert impl.getArReleaseVersion().getValue() == "4.0"

    def test_readResourceConsumption_full(self, parser):
        from armodel.models import SwcImplementation

        impl = SwcImplementation(parent=_autosar_root(), short_name="impl")
        element = _snip(
            "<RESOURCE-CONSUMPTION>"
            "<SHORT-NAME>rc</SHORT-NAME>"
            "<MEMORY-SECTIONS>"
            "<MEMORY-SECTION>"
            "<SHORT-NAME>ms</SHORT-NAME>"
            "<ALIGNMENT>8</ALIGNMENT>"
            "<SIZE>1024</SIZE>"
            "</MEMORY-SECTION>"
            "</MEMORY-SECTIONS>"
            "<STACK-USAGES>"
            "<ROUGH-ESTIMATE-STACK-USAGE>"
            "<SHORT-NAME>stack</SHORT-NAME>"
            "<MEMORY-CONSUMPTION>512</MEMORY-CONSUMPTION>"
            "</ROUGH-ESTIMATE-STACK-USAGE>"
            "</STACK-USAGES>"
            "</RESOURCE-CONSUMPTION>",
            root_tag="SWC-IMPLEMENTATION",
        )
        parser.readResourceConsumption(element, impl)
        assert impl.getResourceConsumption() is not None

    def test_readSwcBswMapping_full(self, parser):
        from armodel.models import SwcBswMapping

        mapping = SwcBswMapping(parent=_autosar_root(), short_name="mapping")
        element = _snip(
            "<SHORT-NAME>mapping</SHORT-NAME>"
            "<BSW-BEHAVIOR-REF DEST='BSW-INTERNAL-BEHAVIOR'>/bswBh</BSW-BEHAVIOR-REF>"
            "<SWC-BEHAVIOR-REF DEST='SWC-INTERNAL-BEHAVIOR'>/swcBh</SWC-BEHAVIOR-REF>"
            "<RUNNABLE-MAPPINGS>"
            "<SWC-BSW-RUNNABLE-MAPPING>"
            "<BSW-ENTITY-REF DEST='BSW-SCHEDULABLE-ENTITY'>/bswEnt</BSW-ENTITY-REF>"
            "<SWC-RUNNABLE-REF DEST='RUNNABLE-ENTITY'>/swcRun</SWC-RUNNABLE-REF>"
            "</SWC-BSW-RUNNABLE-MAPPING>"
            "</RUNNABLE-MAPPINGS>",
            root_tag="SWC-BSW-MAPPING",
        )
        parser.readSwcBswMapping(element, mapping)
        assert mapping.getBswBehaviorRef().getValue() == "/bswBh"
        assert mapping.getSwcBehaviorRef().getValue() == "/swcBh"


# ==================== Timing and Execution Order Handlers ====================


class TestTimingAndExecutionOrderHandlers:
    """Exercise SwcTiming, TimingExtension, ExecutionOrderConstraint."""

    def test_readSwcTiming_full(self, parser):
        from armodel.models import SwcTiming

        timing = SwcTiming(parent=_autosar_root(), short_name="timing")
        element = _snip(
            "<SHORT-NAME>timing</SHORT-NAME>"
            "<TIMING-REQUIREMENTS>"
            "<EXECUTION-ORDER-CONSTRAINT>"
            "<SHORT-NAME>eoc</SHORT-NAME>"
            "<ORDERED-ELEMENTS>"
            "<EOC-EXECUTABLE-ENTITY-REF>"
            "<SHORT-NAME>entity</SHORT-NAME>"
            "</EOC-EXECUTABLE-ENTITY-REF>"
            "</ORDERED-ELEMENTS>"
            "</EXECUTION-ORDER-CONSTRAINT>"
            "</TIMING-REQUIREMENTS>",
            root_tag="SWC-TIMING",
        )
        parser.readSwcTiming(element, timing)
        assert len(timing.getTimingRequirements()) == 1

    def test_readExecutionOrderConstraint_full(self, parser):
        from armodel.models import SwcTiming

        timing = SwcTiming(parent=_autosar_root(), short_name="timing")
        element = _snip(
            "<SHORT-NAME>eoc</SHORT-NAME>"
            "<ORDERED-ELEMENTS>"
            "<EOC-EXECUTABLE-ENTITY-REF>"
            "<SHORT-NAME>entity</SHORT-NAME>"
            "<SUCCESSOR-REFS>"
            "<SUCCESSOR-REF DEST='EOC-EXECUTABLE-ENTITY-REF'>/succ</SUCCESSOR-REF>"
            "</SUCCESSOR-REFS>"
            "</EOC-EXECUTABLE-ENTITY-REF>"
            "</ORDERED-ELEMENTS>",
            root_tag="EXECUTION-ORDER-CONSTRAINT",
        )
        parser.readExecutionOrderConstraint(element, timing)
        assert len(timing.getTimingRequirements()) == 1


# ==================== Port Interface Mapping Handlers ====================


class TestPortInterfaceMappingHandlers:
    """Exercise PortInterfaceMappingSet, variable/parameter mapping, client/server operation mapping."""

    def test_readPortInterfaceMappingSet_full(self, parser):
        from armodel.models import PortInterfaceMappingSet

        mapping_set = PortInterfaceMappingSet(parent=_autosar_root(), short_name="pims")
        element = _snip(
            "<SHORT-NAME>pims</SHORT-NAME>"
            "<PORT-INTERFACE-MAPPINGS>"
            "<VARIABLE-AND-PARAMETER-INTERFACE-MAPPING>"
            "<SHORT-NAME>vpm</SHORT-NAME>"
            "</VARIABLE-AND-PARAMETER-INTERFACE-MAPPING>"
            "<CLIENT-SERVER-INTERFACE-MAPPING>"
            "<SHORT-NAME>csim</SHORT-NAME>"
            "</CLIENT-SERVER-INTERFACE-MAPPING>"
            "<MODE-INTERFACE-MAPPING>"
            "<SHORT-NAME>mim</SHORT-NAME>"
            "</MODE-INTERFACE-MAPPING>"
            "</PORT-INTERFACE-MAPPINGS>",
            root_tag="PORT-INTERFACE-MAPPING-SET",
        )
        parser.readPortInterfaceMappingSet(element, mapping_set)
        assert len(mapping_set.getPortInterfaceMappings()) == 3

    def test_readVariableAndParameterInterfaceMapping_full(self, parser):
        from armodel.models import PortInterfaceMappingSet

        mapping_set = PortInterfaceMappingSet(parent=_autosar_root(), short_name="pims")
        mapping = mapping_set.createVariableAndParameterInterfaceMapping("vpm")
        element = _snip(
            "<SHORT-NAME>vpm</SHORT-NAME>"
            "<DATA-MAPPINGS>"
            "<DATA-PROTOTYPE-MAPPING>"
            "<FIRST-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/first</FIRST-DATA-PROTOTYPE-REF>"
            "<SECOND-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/second</SECOND-DATA-PROTOTYPE-REF>"
            "</DATA-PROTOTYPE-MAPPING>"
            "</DATA-MAPPINGS>",
            root_tag="VARIABLE-AND-PARAMETER-INTERFACE-MAPPING",
        )
        parser.readVariableAndParameterInterfaceMapping(element, mapping)
        assert len(mapping.getDataMappings()) == 1

    def test_readClientServerInterfaceMapping_full(self, parser):
        from armodel.models import PortInterfaceMappingSet

        mapping_set = PortInterfaceMappingSet(parent=_autosar_root(), short_name="pims")
        mapping = mapping_set.createClientServerInterfaceMapping("csim")
        element = _snip(
            "<SHORT-NAME>csim</SHORT-NAME>"
            "<OPERATION-MAPPINGS>"
            "<CLIENT-SERVER-OPERATION-MAPPING>"
            "<FIRST-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/first</FIRST-OPERATION-REF>"
            "<SECOND-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/second</SECOND-OPERATION-REF>"
            "</CLIENT-SERVER-OPERATION-MAPPING>"
            "</OPERATION-MAPPINGS>",
            root_tag="CLIENT-SERVER-INTERFACE-MAPPING",
        )
        parser.readClientServerInterfaceMapping(element, mapping)
        assert len(mapping.getOperationMappings()) == 1

    def test_readModeInterfaceMapping_full(self, parser):
        from armodel.models import PortInterfaceMappingSet

        mapping_set = PortInterfaceMappingSet(parent=_autosar_root(), short_name="pims")
        mapping = mapping_set.createModeInterfaceMapping("mim")
        element = _snip(
            "<SHORT-NAME>mim</SHORT-NAME>"
            "<MODE-MAPPING>"
            "<FIRST-MODE-GROUP-REF DEST='MODE-GROUP'>/first</FIRST-MODE-GROUP-REF>"
            "<SECOND-MODE-GROUP-REF DEST='MODE-GROUP'>/second</SECOND-MODE-GROUP-REF>"
            "</MODE-MAPPING>",
            root_tag="MODE-INTERFACE-MAPPING",
        )
        parser.readModeInterfaceMapping(element, mapping)
        assert mapping.getModeMapping() is not None


# ==================== Additional Coverage Tests ====================


class TestAdditionalOrchestratorCoverage:
    """Additional tests for edge cases and warning scenarios."""

    def test_readSwcInternalBehaviorEvents_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        element = _snip(
            "<EVENTS><UNSUPPORTED-EVENT><SHORT-NAME>ue</SHORT-NAME></UNSUPPORTED-EVENT></EVENTS>",
            root_tag="SWC-INTERNAL-BEHAVIOR",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehaviorEvents(element, behavior)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readSwcServiceDependencyServiceNeeds_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        dependency = behavior.createSwcServiceDependency("dep")
        element = _snip(
            "<SERVICE-NEEDS><UNSUPPORTED-NEEDS><SHORT-NAME>un</SHORT-NAME></UNSUPPORTED-NEEDS></SERVICE-NEEDS>",
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcServiceDependencyServiceNeeds(element, dependency)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readRunnableEntityServerCallPoints_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ApplicationSwComponentType

        swc = ApplicationSwComponentType(parent=_autosar_root(), short_name="swc")
        behavior = swc.createSwcInternalBehavior("bh")
        runnable = behavior.createRunnableEntity("run")
        element = _snip(
            "<SERVER-CALL-POINTS><UNSUPPORTED-POINT><SHORT-NAME>up</SHORT-NAME></UNSUPPORTED-POINT></SERVER-CALL-POINTS>",
            root_tag="RUNNABLE-ENTITY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityInternalBehaviorServerCallPoint(element, runnable)
        assert "Unsupported" in caplog.text

    def test_readSystemMappingDataMappings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import System, SystemMapping

        system = System(parent=_autosar_root(), short_name="sys")
        mapping = system.createSystemMapping("sm")
        element = _snip(
            "<DATA-MAPPINGS><UNSUPPORTED-MAPPING><SHORT-NAME>um</SHORT-NAME></UNSUPPORTED-MAPPING></DATA-MAPPINGS>",
            root_tag="SYSTEM-MAPPING",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingDataMappings(element, mapping)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readPortInterfaceMappings_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import PortInterfaceMappingSet

        mapping_set = PortInterfaceMappingSet(parent=_autosar_root(), short_name="pims")
        element = _snip(
            "<PORT-INTERFACE-MAPPINGS><UNSUPPORTED-MAPPING><SHORT-NAME>um</SHORT-NAME></UNSUPPORTED-MAPPING></PORT-INTERFACE-MAPPINGS>",
            root_tag="PORT-INTERFACE-MAPPING-SET",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readPortInterfaceMappings(element, mapping_set)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readEcucModuleConfigurationValuesContainers_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import EcucModuleConfigurationValues

        values = EcucModuleConfigurationValues(parent=_autosar_root(), short_name="emcv")
        element = _snip(
            "<CONTAINERS><UNSUPPORTED-CONTAINER><SHORT-NAME>uc</SHORT-NAME></UNSUPPORTED-CONTAINER></CONTAINERS>",
            root_tag="ECUC-MODULE-CONFIGURATION-VALUES",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEcucModuleConfigurationValuesContainers(element, values)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readCompositionSwComponentTypeSwConnectors_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import CompositionSwComponentType

        comp = CompositionSwComponentType(parent=_autosar_root(), short_name="comp")
        element = _snip(
            "<CONNECTORS><UNSUPPORTED-CONNECTOR><SHORT-NAME>uc</SHORT-NAME></UNSUPPORTED-CONNECTOR></CONNECTORS>",
            root_tag="COMPOSITION-SW-COMPONENT-TYPE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readCompositionSwComponentTypeSwConnectors(element, comp)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readImplementationDataTypeSubElements_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ImplementationDataType

        data_type = ImplementationDataType(parent=_autosar_root(), short_name="idt")
        element = _snip(
            "<SUB-ELEMENTS><UNSUPPORTED-ELEMENT><SHORT-NAME>ue</SHORT-NAME></UNSUPPORTED-ELEMENT></SUB-ELEMENTS>",
            root_tag="IMPLEMENTATION-DATA-TYPE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readImplementationDataTypeSubElements(element, data_type)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readClientServerInterfaceOperations_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ClientServerInterface

        cs_if = ClientServerInterface(parent=_autosar_root(), short_name="cs_if")
        element = _snip(
            "<OPERATIONS><UNSUPPORTED-OP><SHORT-NAME>uo</SHORT-NAME></UNSUPPORTED-OP></OPERATIONS>",
            root_tag="CLIENT-SERVER-INTERFACE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerInterfaceOperations(element, cs_if)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)

    def test_readSenderReceiverInterfaceDataElements_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SenderReceiverInterface

        sr_if = SenderReceiverInterface(parent=_autosar_root(), short_name="sr_if")
        element = _snip(
            "<DATA-ELEMENTS><UNSUPPORTED-ELEM><SHORT-NAME>ue</SHORT-NAME></UNSUPPORTED-ELEM></DATA-ELEMENTS>",
            root_tag="SENDER-RECEIVER-INTERFACE",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderReceiverInterfaceDataElements(element, sr_if)
        assert any("Unsupported" in r.getMessage() for r in caplog.records)


# ===========================================================================
# Merged from test_arxml_parser_swc_behavior_gaps.py
# Tests for SwcInternalBehavior ServiceNeeds, Events, and related handlers.
# ===========================================================================


def _make_service_dependency():
    """Create a SwcServiceDependency for service-needs tests."""
    from armodel.models import ApplicationSwComponentType
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    behavior = app.createSwcInternalBehavior("Behavior")
    return behavior.createSwcServiceDependency("Dep")


def _make_swc_behavior():
    """Create a minimal SwcInternalBehavior for event tests."""
    from armodel.models import ApplicationSwComponentType
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    return app.createSwcInternalBehavior("Behavior")


class TestSwcServiceDependencyServiceNeeds:
    """Tests for readSwcServiceDependencyServiceNeeds branches."""

    @pytest.mark.parametrize("tag", [
        "DIAGNOSTIC-COMMUNICATION-MANAGER-NEEDS",
        "DIAGNOSTIC-ROUTINE-NEEDS",
        "DIAGNOSTIC-VALUE-NEEDS",
        "DIAGNOSTIC-EVENT-NEEDS",
        "DIAGNOSTIC-EVENT-INFO-NEEDS",
        "CRYPTO-SERVICE-NEEDS",
        "ECU-STATE-MGR-USER-NEEDS",
        "DTC-STATUS-CHANGE-NOTIFICATION-NEEDS",
        "DLT-USER-NEEDS",
    ])
    def test_service_needs_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_service_dependency()
        element = _snip(
            f"""
            <SERVICE-NEEDS>
                <{tag}>
                    <SHORT-NAME>Need</SHORT-NAME>
                </{tag}>
            </SERVICE-NEEDS>
            """,
        )
        parser.readSwcServiceDependencyServiceNeeds(element, dep)
        needs = dep.getServiceNeeds()
        assert len(needs) == 1
        assert needs[0].getShortName() == "Need"

    def test_nv_block_needs_branch(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_service_dependency()
        element = _snip(
            """
            <SERVICE-NEEDS>
                <NV-BLOCK-NEEDS>
                    <SHORT-NAME>NvNeed</SHORT-NAME>
                </NV-BLOCK-NEEDS>
            </SERVICE-NEEDS>
            """,
        )
        parser.readSwcServiceDependencyServiceNeeds(element, dep)
        needs = dep.getServiceNeeds()
        assert len(needs) == 1
        assert needs[0].getShortName() == "NvNeed"

    def test_unknown_service_needs_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        dep = _make_service_dependency()
        element = _snip(
            """
            <SERVICE-NEEDS>
                <UNKNOWN-NEEDS>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-NEEDS>
            </SERVICE-NEEDS>
            """,
        )
        warning_parser.readSwcServiceDependencyServiceNeeds(element, dep)
        assert len(dep.getServiceNeeds()) == 0


class TestIncludedDataTypeSets:
    """Tests for getIncludedDataTypeSets (L778-786)."""

    def test_with_data_type_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <INCLUDED-DATA-TYPE-SETS>
                <INCLUDED-DATA-TYPE-SET>
                    <DATA-TYPE-REFS>
                        <DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/dt/Type1</DATA-TYPE-REF>
                    </DATA-TYPE-REFS>
                </INCLUDED-DATA-TYPE-SET>
            </INCLUDED-DATA-TYPE-SETS>
            """,
        )
        result = parser.getIncludedDataTypeSets(element)
        assert len(result) == 1
        assert len(result[0].getDataTypeRefs()) == 1

    def test_empty_returns_empty_list(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getIncludedDataTypeSets(element)
        assert result == []


class TestSwcInternalBehaviorEvents:
    """Tests for readSwcInternalBehaviorEvents branches."""

    @pytest.mark.parametrize("tag", [
        "INTERNAL-TRIGGER-OCCURRED-EVENT",
        "INIT-EVENT",
        "ASYNCHRONOUS-SERVER-CALL-RETURNS-EVENT",
        "MODE-SWITCHED-ACK-EVENT",
        "BACKGROUND-EVENT",
        "DATA-SEND-COMPLETED-EVENT",
    ])
    def test_event_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = _make_swc_behavior()
        element = _snip(
            f"""
            <EVENTS>
                <{tag}>
                    <SHORT-NAME>Event</SHORT-NAME>
                </{tag}>
            </EVENTS>
            """,
        )
        parser.readSwcInternalBehaviorEvents(element, behavior)
        event = behavior.getEvent("Event")
        assert event is not None
        assert event.getShortName() == "Event"

    def test_unknown_event_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        behavior = _make_swc_behavior()
        element = _snip(
            """
            <EVENTS>
                <UNKNOWN-EVENT>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-EVENT>
            </EVENTS>
            """,
        )
        warning_parser.readSwcInternalBehaviorEvents(element, behavior)


class TestSwPointerTargetProps:
    """Tests for getSwPointerTargetProps and readSwPointerTargetProps."""

    def test_get_sw_pointer_target_props_with_data(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <SW-POINTER-TARGET-PROPS>
                <TARGET-CATEGORY>VALUE</TARGET-CATEGORY>
            </SW-POINTER-TARGET-PROPS>
            """,
        )
        result = parser.getSwPointerTargetProps(element, "SW-POINTER-TARGET-PROPS")
        assert result is not None
        assert result.getTargetCategory() is not None

    def test_get_sw_pointer_target_props_empty(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getSwPointerTargetProps(element, "SW-POINTER-TARGET-PROPS")
        assert result is None

    def test_read_sw_pointer_target_props(self, parser):
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = SwDataDefProps()
        element = _snip(
            """
            <SW-POINTER-TARGET-PROPS>
                <TARGET-CATEGORY>VALUE</TARGET-CATEGORY>
            </SW-POINTER-TARGET-PROPS>
            """,
        )
        parser.readSwPointerTargetProps(element, parent)
        assert parent.swPointerTargetProps is not None
        assert parent.swPointerTargetProps.getTargetCategory() is not None

    def test_read_sw_pointer_target_props_empty(self, parser):
        from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
            SwDataDefProps,
        )
        AUTOSAR.getInstance().setARRelease("R23-11")
        parent = SwDataDefProps()
        element = _snip("")
        parser.readSwPointerTargetProps(element, parent)
        assert parent.swPointerTargetProps is None


class TestParameterInAtomicSWCTypeInstanceRef:
    """Tests for getParameterInAtomicSWCTypeInstanceRef (L1278-1283)."""

    def test_with_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
                <PORT-PROTOTYPE-REF DEST="P-PORT-PROTOTYPE">/pp/Port</PORT-PROTOTYPE-REF>
                <ROOT-PARAMETER-DATA-PROTOTYPE-REF DEST="PARAMETER-DATA-PROTOTYPE">/pdp/Param</ROOT-PARAMETER-DATA-PROTOTYPE-REF>
            </PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF>
            """,
        )
        result = parser.getParameterInAtomicSWCTypeInstanceRef(
            element, "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"
        )
        assert result is not None
        assert result.getPortPrototypeRef() is not None

    def test_without_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getParameterInAtomicSWCTypeInstanceRef(
            element, "PARAMETER-IN-ATOMIC-SWC-TYPE-INSTANCE-REF"
        )
        assert result is None


class TestModeGroupIRef:
    """Tests for getModeGroupIRef (L1386-1392)."""

    def test_p_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                    <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/pp/Port</CONTEXT-P-PORT-REF>
                    <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
                </P-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = parser.getModeGroupIRef(element, "MODE-GROUP-IREF")
        assert result is not None

    def test_r_mode_group_iref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
                    <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/rp/Port</CONTEXT-R-PORT-REF>
                    <TARGET-MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</TARGET-MODE-GROUP-REF>
                </R-MODE-GROUP-IN-ATOMIC-SWC-INSTANCE-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = parser.getModeGroupIRef(element, "MODE-GROUP-IREF")
        assert result is not None

    def test_unknown_mode_group_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-IREF>
                <UNKNOWN-MODE-GROUP-REF>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-MODE-GROUP-REF>
            </MODE-GROUP-IREF>
            """,
        )
        result = warning_parser.getModeGroupIRef(element, "MODE-GROUP-IREF")
        assert result is None


# ===========================================================================
# Merged from test_arxml_parser_system_mapping_gaps.py
# Tests for SystemMapping and Type Mapping handlers (L5373-5421).
# ===========================================================================


def _make_system_mapping():
    """Create a SystemMapping with a MagicMock parent for data-mapping tests."""
    from unittest.mock import MagicMock
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate import SystemMapping
    return SystemMapping(parent=MagicMock(), short_name="TestSystemMapping")


# ==================== readSenderRecRecordElementMapping (L5373-5377) ====================


class TestReadSenderRecRecordElementMapping:
    """Cover readSenderRecRecordElementMapping optional ref handling."""

    def test_sets_all_optional_refs_when_present(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordElementMapping,
        )
        mapping = SenderRecRecordElementMapping()
        element = _snip("""
            <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
            <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
        """)
        parser.readSenderRecRecordElementMapping(element, mapping)
        assert mapping.getApplicationRecordElementRef() is not None
        assert mapping.getApplicationRecordElementRef().getValue() == "/App/Rec1"
        assert mapping.getImplementationRecordElementRef() is not None
        assert mapping.getImplementationRecordElementRef().getValue() == "/Impl/Rec1"
        assert mapping.getSystemSignalRef() is not None
        assert mapping.getSystemSignalRef().getValue() == "/Sig/S1"

    def test_keeps_refs_none_when_absent(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordElementMapping,
        )
        mapping = SenderRecRecordElementMapping()
        element = _snip("")
        parser.readSenderRecRecordElementMapping(element, mapping)
        assert mapping.getApplicationRecordElementRef() is None
        assert mapping.getImplementationRecordElementRef() is None
        assert mapping.getSystemSignalRef() is None


# ==================== readSenderRecArrayTypeMappingRecordElementMapping (L5379-5387) ====================


class TestReadSenderRecArrayTypeMappingRecordElementMapping:
    """Cover SENDER-REC-RECORD-ELEMENT-MAPPING branch and warning branch."""

    def test_reads_sender_rec_record_element_mapping(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordElementMapping,
            SenderRecRecordTypeMapping,
        )
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        mappings = mapping.getRecordElementMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SenderRecRecordElementMapping)
        assert mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"

    def test_unsupported_record_element_mapping_raises(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordTypeMapping,
        )
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)

    def test_unsupported_record_element_mapping_logs_warning(self, warning_parser, caplog):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordTypeMapping,
        )
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        assert any("Unsupported RecordElementMapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getRecordElementMappings() == []

    def test_empty_record_element_mappings(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordTypeMapping,
        )
        mapping = SenderRecRecordTypeMapping()
        element = _snip("<RECORD-ELEMENT-MAPPINGS></RECORD-ELEMENT-MAPPINGS>")
        parser.readSenderRecArrayTypeMappingRecordElementMapping(element, mapping)
        assert mapping.getRecordElementMappings() == []


# ==================== readSenderRecRecordTypeMapping (L5389-5391) ====================


class TestReadSenderRecRecordTypeMapping:
    """Cover readSenderRecRecordTypeMapping delegation."""

    def test_delegates_to_composite_and_array_type_mapping(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderRecRecordTypeMapping,
        )
        mapping = SenderRecRecordTypeMapping()
        element = _snip("""
            <RECORD-ELEMENT-MAPPINGS>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec2</APPLICATION-RECORD-ELEMENT-REF>
                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec2</IMPLEMENTATION-RECORD-ELEMENT-REF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S2</SYSTEM-SIGNAL-REF>
                </SENDER-REC-RECORD-ELEMENT-MAPPING>
            </RECORD-ELEMENT-MAPPINGS>
        """)
        parser.readSenderRecRecordTypeMapping(element, mapping)
        mappings = mapping.getRecordElementMappings()
        assert len(mappings) == 2
        assert mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"
        assert mappings[1].getSystemSignalRef().getValue() == "/Sig/S2"


# ==================== readSenderReceiverToSignalGroupMappingTypeMapping (L5393-5402) ====================


class TestReadSenderReceiverToSignalGroupMappingTypeMapping:
    """Cover SENDER-REC-RECORD-TYPE-MAPPING branch and warning branch."""

    def test_reads_sender_rec_record_type_mapping(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalGroupMapping,
            SenderRecRecordTypeMapping,
        )
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <SENDER-REC-RECORD-TYPE-MAPPING>
                    <RECORD-ELEMENT-MAPPINGS>
                        <SENDER-REC-RECORD-ELEMENT-MAPPING>
                            <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                            <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                            <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                        </SENDER-REC-RECORD-ELEMENT-MAPPING>
                    </RECORD-ELEMENT-MAPPINGS>
                </SENDER-REC-RECORD-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        type_mapping = mapping.getTypeMapping()
        assert type_mapping is not None
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert len(type_mapping.getRecordElementMappings()) == 1
        assert type_mapping.getRecordElementMappings()[0].getSystemSignalRef().getValue() == "/Sig/S1"

    def test_unsupported_type_mapping_raises(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalGroupMapping,
        )
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <UNKNOWN-TYPE-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)

    def test_unsupported_type_mapping_logs_warning(self, warning_parser, caplog):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalGroupMapping,
        )
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("""
            <TYPE-MAPPING>
                <UNKNOWN-TYPE-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-TYPE-MAPPING>
            </TYPE-MAPPING>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        assert any("Unsupported Type Mapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getTypeMapping() is None

    def test_no_type_mapping_child_keeps_none(self, parser):
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalGroupMapping,
        )
        mapping = SenderReceiverToSignalGroupMapping()
        element = _snip("")
        parser.readSenderReceiverToSignalGroupMappingTypeMapping(element, mapping)
        assert mapping.getTypeMapping() is None


# ==================== readSystemMappingDataMappings (L5409-5421) ====================


class TestReadSystemMappingDataMappings:
    """Cover SENDER-RECEIVER-TO-SIGNAL-MAPPING and SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING branches + warning."""

    def test_reads_sender_receiver_to_signal_mapping(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                    <COMMUNICATION-DIRECTION>IN</COMMUNICATION-DIRECTION>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                        <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Cmp/Comp/sw1</CONTEXT-COMPONENT-REF>
                        <CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/Cmp/Comp/port1</CONTEXT-PORT-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Iface/If/de1</TARGET-DATA-PROTOTYPE-REF>
                    </DATA-ELEMENT-IREF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-RECEIVER-TO-SIGNAL-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 1
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalMapping,
        )
        assert isinstance(data_mappings[0], SenderReceiverToSignalMapping)
        assert data_mappings[0].getSystemSignalRef().getValue() == "/Sig/S1"
        assert data_mappings[0].getCommunicationDirection().getValue() == "IN"
        assert data_mappings[0].getDataElementIRef() is not None

    def test_reads_sender_receiver_to_signal_group_mapping(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                        <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Cmp/Comp/sw1</CONTEXT-COMPONENT-REF>
                        <CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/Cmp/Comp/port1</CONTEXT-PORT-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Iface/If/de1</TARGET-DATA-PROTOTYPE-REF>
                    </DATA-ELEMENT-IREF>
                    <SIGNAL-GROUP-REF DEST="SIGNAL-GROUP">/Sig/Group1</SIGNAL-GROUP-REF>
                    <TYPE-MAPPING>
                        <SENDER-REC-RECORD-TYPE-MAPPING>
                            <RECORD-ELEMENT-MAPPINGS>
                                <SENDER-REC-RECORD-ELEMENT-MAPPING>
                                    <APPLICATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/App/Rec1</APPLICATION-RECORD-ELEMENT-REF>
                                    <IMPLEMENTATION-RECORD-ELEMENT-REF DEST="RECORD-ELEMENT">/Impl/Rec1</IMPLEMENTATION-RECORD-ELEMENT-REF>
                                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                                </SENDER-REC-RECORD-ELEMENT-MAPPING>
                            </RECORD-ELEMENT-MAPPINGS>
                        </SENDER-REC-RECORD-TYPE-MAPPING>
                    </TYPE-MAPPING>
                </SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 1
        from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DataMapping import (
            SenderReceiverToSignalGroupMapping,
            SenderRecRecordTypeMapping,
        )
        assert isinstance(data_mappings[0], SenderReceiverToSignalGroupMapping)
        assert data_mappings[0].getSignalGroupRef().getValue() == "/Sig/Group1"
        assert data_mappings[0].getDataElementIRef() is not None
        type_mapping = data_mappings[0].getTypeMapping()
        assert type_mapping is not None
        assert isinstance(type_mapping, SenderRecRecordTypeMapping)
        assert len(type_mapping.getRecordElementMappings()) == 1

    def test_reads_both_signal_and_signal_group_mappings(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                    </DATA-ELEMENT-IREF>
                    <SYSTEM-SIGNAL-REF DEST="SYSTEM-SIGNAL">/Sig/S1</SYSTEM-SIGNAL-REF>
                </SENDER-RECEIVER-TO-SIGNAL-MAPPING>
                <SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
                    <DATA-ELEMENT-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/Cmp/Comp</CONTEXT-COMPOSITION-REF>
                    </DATA-ELEMENT-IREF>
                    <SIGNAL-GROUP-REF DEST="SIGNAL-GROUP">/Sig/Group1</SIGNAL-GROUP-REF>
                </SENDER-RECEIVER-TO-SIGNAL-GROUP-MAPPING>
            </DATA-MAPPINGS>
        """)
        parser.readSystemMappingDataMappings(element, mapping)
        data_mappings = mapping.getDataMappings()
        assert len(data_mappings) == 2

    def test_unsupported_data_mapping_raises(self, parser):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </DATA-MAPPINGS>
        """)
        with pytest.raises(NotImplementedError):
            parser.readSystemMappingDataMappings(element, mapping)

    def test_unsupported_data_mapping_logs_warning(self, warning_parser, caplog):
        mapping = _make_system_mapping()
        element = _snip("""
            <DATA-MAPPINGS>
                <UNKNOWN-MAPPING>
                    <SHORT-NAME>X</SHORT-NAME>
                </UNKNOWN-MAPPING>
            </DATA-MAPPINGS>
        """)
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingDataMappings(element, mapping)
        assert any("Unsupported Data Mapping" in rec.getMessage() for rec in caplog.records)
        assert mapping.getDataMappings() == []

    def test_empty_data_mappings(self, parser):
        mapping = _make_system_mapping()
        element = _snip("<DATA-MAPPINGS></DATA-MAPPINGS>")
        parser.readSystemMappingDataMappings(element, mapping)
        assert mapping.getDataMappings() == []


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestRoleBasedDataTypeAssignment:
    def test_getRoleBasedDataTypeAssignment_with_role(self, parser):
        element = _snip(
            "<ROLE>MyRole</ROLE>"
            "<USED-IMPLEMENTATION-DATA-TYPE-REF "
            'DEST="IMPLEMENTATION-DATA-TYPE">/dt/Impl</USED-IMPLEMENTATION-DATA-TYPE-REF>',
            root_tag="ROLE-BASED-DATA-TYPE-ASSIGNMENT",
        )
        result = parser.getRoleBasedDataTypeAssignment(element)
        assert result.getRole() is not None
        assert result.getRole().getValue() == "MyRole"
        assert result.getUsedImplementationDataTypeRef() is not None
        assert result.getUsedImplementationDataTypeRef().getValue() == "/dt/Impl"

    def test_getRoleBasedDataTypeAssignment_empty(self, parser):
        element = _snip("", root_tag="ROLE-BASED-DATA-TYPE-ASSIGNMENT")
        result = parser.getRoleBasedDataTypeAssignment(element)
        assert result.getRole() is None
        assert result.getUsedImplementationDataTypeRef() is None

    def test_readServiceDependency_with_role_based_data_type_assignment(
        self, parser
    ):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Dep"
        )
        element = _snip(
            "<ASSIGNED-DATA-TYPES>"
            "<ROLE-BASED-DATA-TYPE-ASSIGNMENT>"
            "<ROLE>r</ROLE>"
            "</ROLE-BASED-DATA-TYPE-ASSIGNMENT>"
            "</ASSIGNED-DATA-TYPES>",
            root_tag="SERVICE-DEPENDENCY",
        )
        parser.readServiceDependency(element, dep)
        assert len(dep.getAssignedDataTypes()) == 1

    def test_readServiceDependency_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Dep"
        )
        element = _snip(
            "<ASSIGNED-DATA-TYPES><BAD/></ASSIGNED-DATA-TYPES>",
            root_tag="SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readServiceDependency(element, dep)
        assert any("Unsupported assigned data type" in r.getMessage()
                   for r in caplog.records)


# ==================== SwcServiceDependency assigned ports/data (L623, L631, L776) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestSwcServiceDependencyAssigned:
    def test_readAssignedData_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Swsd"
        )
        element = _snip(
            "<ASSIGNED-DATAS><BAD/></ASSIGNED-DATAS>",
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcServiceDependencyAssignedData(
                element, dep
            )
        assert any("Unsupported assigned data" in r.getMessage()
                   for r in caplog.records)

    def test_readAssignedPorts_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import SwcServiceDependency
        dep = SwcServiceDependency(
            parent=_autosar_root(), short_name="Swsd"
        )
        element = _snip(
            "<ASSIGNED-PORTS><BAD/></ASSIGNED-PORTS>",
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcServiceDependencyAssignedPorts(
                element, dep
            )
        assert any("Unsupported assigned ports" in r.getMessage()
                   for r in caplog.records)

    def test_readSwcInternalBehaviorServiceDependencies_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        element = _snip(
            "<SERVICE-DEPENDENCYS><BAD/></SERVICE-DEPENDENCYS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehaviorServiceDependencies(
                element, behavior
            )
        assert any("Unsupported Service Dependencies" in r.getMessage()
                   for r in caplog.records)


# ==================== SwcInternalBehavior IncludedModeDeclarationGroupSet (L813, L840, L845-848) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestSwcInternalBehaviorIncludedModeDeclaration:
    def test_readIncludedModeDeclarationGroupSets_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS><BAD/></INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSwcInternalBehaviorIncludedModeDeclarationGroupSets(
                element, behavior
            )
        assert any("Unsupported IncludedModeDeclarationGroupSet"
                   in r.getMessage() for r in caplog.records)

    def test_readAtomicSwComponentTypeSwcInternalBehavior_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        element = _snip(
            "<INTERNAL-BEHAVIORS><BAD/></INTERNAL-BEHAVIORS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readAtomicSwComponentTypeSwcInternalBehavior(
                element, app
            )
        assert any("Unsupported Internal Behaviors" in r.getMessage()
                   for r in caplog.records)

    def test_getIncludedModeDeclarationGroupSets_returns_groups(
        self, parser
    ):
        element = _snip(
            "<INCLUDED-MODE-DECLARATION-GROUP-SETS>"
            "<INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "<MODE-DECLARATION-GROUP-REFS>"
            '<MODE-DECLARATION-GROUP-REF DEST="MODE-DECLARATION-GROUP">/mdg</MODE-DECLARATION-GROUP-REF>'
            "</MODE-DECLARATION-GROUP-REFS>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SET>"
            "</INCLUDED-MODE-DECLARATION-GROUP-SETS>"
        )
        result = parser.getIncludedModeDeclarationGroupSets(element)
        assert len(result) == 1


# ==================== BswInternalBehavior addIncludedModeDeclarationGroupSet (L1025) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestRunnableEntityGaps:
    def test_readModeSwitchPointModeGroupIRef_sets_ref(self, parser):
        from armodel.models import ModeSwitchPoint
        point = ModeSwitchPoint(parent=MagicMock(), short_name="Msp")
        element = _snip(
            "<MODE-GROUP-IREF>"
            "<CONTEXT-IREF>"
            '<CONTEXT-PORT-REF DEST="P-PORT-PROTOTYPE">/pp</CONTEXT-PORT-REF>'
            "<TARGET-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/t</TARGET-REF>"
            "</CONTEXT-IREF>"
            "<TARGET-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/t</TARGET-REF>"
            "</MODE-GROUP-IREF>"
        )
        parser.readModeSwitchPointModeGroupIRef(element, point)
        assert point.getModeGroupIRef() is not None

    def test_readRunnableEntityModeSwitchPoints_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<MODE-SWITCH-POINTS><BAD/></MODE-SWITCH-POINTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityModeSwitchPoints(
                element, entity
            )
        assert any("Unsupported Mode Switch Point" in r.getMessage()
                   for r in caplog.records)

    def test_readRunnableEntityArguments_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<ARGUMENTS><BAD/></ARGUMENTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityArguments(element, entity)
        assert any("Unsupported Arguments of runnable entity"
                   in r.getMessage() for r in caplog.records)

    def test_readRunnableEntityModeAccessPoints_unsupported_warns(
        self, warning_parser, caplog
    ):
        app = ApplicationSwComponentType(
            parent=_autosar_root(), short_name="App"
        )
        behavior = app.createSwcInternalBehavior("Beh")
        entity = behavior.createRunnableEntity("R")
        element = _snip(
            "<MODE-ACCESS-POINTS><BAD/></MODE-ACCESS-POINTS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readRunnableEntityModeAccessPoints(
                element, entity
            )
        assert any("Unsupported Mode Access Point" in r.getMessage()
                   for r in caplog.records)


# ==================== SwDataDefPros InvalidValue (L1827) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestGetValueSpecification:
    def test_application_value_specification(self, parser):
        element = _snip(
            "<APPLICATION-VALUE-SPECIFICATION>"
            "<SHORT-LABEL>lbl</SHORT-LABEL>"
            "</APPLICATION-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "APPLICATION-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_record_value_specification(self, parser):
        element = _snip(
            "<RECORD-VALUE-SPECIFICATION>"
            "<FIELDS/>"
            "</RECORD-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "RECORD-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_array_value_specification(self, parser):
        element = _snip(
            "<ARRAY-VALUE-SPECIFICATION>"
            "<ELEMENTS/>"
            "</ARRAY-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "ARRAY-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_text_value_specification(self, parser):
        element = _snip(
            "<TEXT-VALUE-SPECIFICATION>"
            "<VALUE>txt</VALUE>"
            "</TEXT-VALUE-SPECIFICATION>"
        )
        result = parser.getValueSpecification(
            element, "TEXT-VALUE-SPECIFICATION"
        )
        assert result is not None

    def test_constant_reference(self, parser):
        element = _snip(
            '<CONSTANT-REFERENCE>'
            '<CONSTANT-REF DEST="CONSTANT-SPECIFICATION">/c</CONSTANT-REF>'
            '</CONSTANT-REFERENCE>'
        )
        result = parser.getValueSpecification(
            element, "CONSTANT-REFERENCE"
        )
        assert result is not None

    def test_unsupported_warns(self, warning_parser, caplog):
        # L2697: notImplemented logs in warning mode. The subsequent
        # return is a known bug (unbound value_spec), so we catch it.
        element = _snip("<UNKNOWN/>")
        with caplog.at_level(logging.ERROR):
            with pytest.raises(UnboundLocalError):
                warning_parser.getValueSpecification(
                    element, "UNKNOWN"
                )
        assert any("Unsupported RecordValueSpecificationField"
                   in r.getMessage() for r in caplog.records)


# ==================== EndToEndProtections (L2835-2839) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestSystemMappingGaps:
    def _make_system(self):
        pkg = _autosar_root().createARPackage("Pkg")
        return pkg.createSystem("Sys")

    def test_readSystemMappingSwMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<SW-MAPPINGS><BAD/></SW-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingSwMappings(
                element, mapping
            )
        assert any("Unsupported Sw Mapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappingEcuResourceMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<ECU-RESOURCE-MAPPINGS><BAD/></ECU-RESOURCE-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingEcuResourceMappings(
                element, mapping
            )
        assert any("Unsupported EcuResourceMapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappingSwImplMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        mapping = system.createSystemMapping("Sm")
        element = _snip(
            "<SW-IMPL-MAPPINGS><BAD/></SW-IMPL-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappingSwImplMappings(
                element, mapping
            )
        assert any("Unsupported SwImplMapping" in r.getMessage()
                   for r in caplog.records)

    def test_readSystemMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        system = self._make_system()
        element = _snip(
            "<MAPPINGS><BAD/></MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readSystemMappings(element, system)
        assert any("Unsupported Mapping" in r.getMessage()
                   for r in caplog.records)


# ==================== RootSwCompositionPrototype (L5496-5497) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestRootSwCompositionPrototype:
    def test_readRootSwCompositionPrototype_duplicate_warns(
        self, warning_parser, caplog
    ):
        system_pkg = _autosar_root().createARPackage("SysPkg")
        system = system_pkg.createSystem("Sys")
        proto = system.createRootSoftwareComposition("Root")
        AUTOSAR.getInstance().setRootSwCompositionPrototype(proto)
        element = _snip(
            "<ROOT-SOFTWARE-COMPOSITIONS>"
            "<ROOT-SW-COMPOSITION-PROTOTYPE>"
            "<SHORT-NAME>Root2</SHORT-NAME>"
            "</ROOT-SW-COMPOSITION-PROTOTYPE>"
            "</ROOT-SOFTWARE-COMPOSITIONS>"
        )
        with caplog.at_level(logging.WARNING):
            warning_parser.readRootSwCompositionPrototype(
                element, system
            )
        assert any("has already been set" in r.getMessage()
                   or "RootSwComposition" in r.getMessage()
                   for r in caplog.records)


# ==================== LifeCycleInfoSet (L5545) ====================



# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestClientServerInterfaceMapping:
    def test_readOperationMappings_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import ClientServerInterfaceMapping
        mapping = ClientServerInterfaceMapping(
            parent=MagicMock(), short_name="Csim"
        )
        element = _snip(
            "<OPERATION-MAPPINGS><BAD/></OPERATION-MAPPINGS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerInterfaceMappingOperationMappings(
                element, mapping
            )
        assert any("Unsupported Operation Mapping" in r.getMessage()
                   for r in caplog.records)


# ==================== DiagEventDebounceAlgorithm (L687-692) ====================

