"""Writer/reader round-trip tests for RunnableEntity (Table 7.3, p.528, R23-11).

Element order per the XSD RUNNABLE-ENTITY group: ARGUMENTS, ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS,
CAN-BE-INVOKED-CONCURRENTLY, DATA-READ-ACCESSS, DATA-RECEIVE-POINT-BY-ARGUMENTS,
DATA-RECEIVE-POINT-BY-VALUES, DATA-SEND-POINTS, DATA-WRITE-ACCESSS, EXTERNAL-TRIGGERING-POINTS,
INTERNAL-TRIGGERING-POINTS, MODE-ACCESS-POINTS, MODE-SWITCH-POINTS, PARAMETER-ACCESSS,
READ-LOCAL-VARIABLES, SERVER-CALL-POINTS, SYMBOL (C-IDENTIFIER), WAIT-POINTS,
WRITTEN-LOCAL-VARIABLES, VARIATION-POINT.

Round-trip counterpart: tests/test_armodel/parser/test_runnable_entity.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, CIdentifier
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ModeDeclarationGroup import ModeAccessPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RunnableEntityArgument import RunnableEntityArgument
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.Trigger import ExternalTriggeringPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _make_runnable():
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    behavior = swc.createSwcInternalBehavior("Behavior")
    return behavior.createRunnableEntity("Cyclic")


def _populate_all_wrappers(runnable):
    runnable.addArgument(RunnableEntityArgument())
    runnable.createAsynchronousServerCallResultPoint("Result1")
    runnable.setCanBeInvokedConcurrently(Boolean().setValue("true"))
    runnable.createDataReadAccess("Read1")
    runnable.createDataReceivePointByArgument("RecvArg")
    runnable.createDataReceivePointByValue("RecvVal")
    runnable.createDataSendPoint("Send1")
    runnable.createDataWriteAccess("Write1")
    runnable.addExternalTriggeringPoint(ExternalTriggeringPoint())
    runnable.createInternalTriggeringPoint("InternalTrig")
    runnable.addModeAccessPoint(ModeAccessPoint())
    runnable.createModeSwitchPoint("ModeSwitch1")
    runnable.createParameterAccess("Param1")
    runnable.createReadLocalVariable("ReadLocal")
    runnable.createAsynchronousServerCallPoint("Async1")
    runnable.createSynchronousServerCallPoint("Sync1")
    runnable.setSymbol(CIdentifier().setValue("SWC_Cyclic_Cyclic"))
    runnable.createWaitPoint("Wait1")
    runnable.createWrittenLocalVariable("WrittenLocal")
    return runnable


def test_write_element_order_matches_xsd_group():
    runnable = _populate_all_wrappers(_make_runnable())

    parent = ET.Element("RUNNABLES")
    ARXMLWriter().writeRunnableEntity(parent, runnable)

    element = parent.find("RUNNABLE-ENTITY")
    expected = [
        "ARGUMENTS",
        "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS",
        "CAN-BE-INVOKED-CONCURRENTLY",
        "DATA-READ-ACCESSS",
        "DATA-RECEIVE-POINT-BY-ARGUMENTS",
        "DATA-RECEIVE-POINT-BY-VALUES",
        "DATA-SEND-POINTS",
        "DATA-WRITE-ACCESSS",
        "EXTERNAL-TRIGGERING-POINTS",
        "INTERNAL-TRIGGERING-POINTS",
        "MODE-ACCESS-POINTS",
        "MODE-SWITCH-POINTS",
        "PARAMETER-ACCESSS",
        "READ-LOCAL-VARIABLES",
        "SERVER-CALL-POINTS",
        "SYMBOL",
        "WAIT-POINTS",
        "WRITTEN-LOCAL-VARIABLES",
    ]
    children = [child.tag for child in element if child.tag in expected]
    assert children == expected


def test_round_trip_preserves_field_values():
    _populate_all_wrappers(_make_runnable())

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, AUTOSAR.getInstance())
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)

        package_2 = document_2.getARPackages()[0]
        swc_2 = package_2.getReferrableElement("Swc")
        behavior_2 = swc_2.getReferrableElement("Behavior")
        runnable_2 = behavior_2.getReferrableElement("Cyclic")
        assert isinstance(runnable_2, RunnableEntity)

        assert runnable_2.getCanBeInvokedConcurrently() is not None
        assert runnable_2.getCanBeInvokedConcurrently().getValue() is True
        assert isinstance(runnable_2.getSymbol(), CIdentifier)
        assert runnable_2.getSymbol().getValue() == "SWC_Cyclic_Cyclic"
        assert len(runnable_2.getArguments()) == 1
        assert len(runnable_2.getAsynchronousServerCallResultPoints()) == 1
        assert len(runnable_2.getDataReadAccesses()) == 1
        assert runnable_2.getDataReadAccesses()[0].short_name == "Read1"
        assert len(runnable_2.getDataReceivePointByArguments()) == 1
        assert len(runnable_2.getDataReceivePointByValues()) == 1
        assert len(runnable_2.getDataSendPoints()) == 1
        assert runnable_2.getDataSendPoints()[0].short_name == "Send1"
        assert len(runnable_2.getDataWriteAccesses()) == 1
        assert len(runnable_2.getExternalTriggeringPoints()) == 1
        assert len(runnable_2.getInternalTriggeringPoints()) == 1
        assert runnable_2.getInternalTriggeringPoints()[0].short_name == "InternalTrig"
        assert len(runnable_2.getModeAccessPoints()) == 1
        assert len(runnable_2.getModeSwitchPoints()) == 1
        assert len(runnable_2.getParameterAccesses()) == 1
        assert runnable_2.getParameterAccesses()[0].short_name == "Param1"
        assert len(runnable_2.getReadLocalVariables()) == 1
        assert len(runnable_2.getServerCallPoints()) == 2
        assert len(runnable_2.getSynchronousServerCallPoint()) == 1
        assert runnable_2.getSynchronousServerCallPoint()[0].short_name == "Sync1"
        assert len(runnable_2.getAsynchronousServerCallPoint()) == 1
        assert runnable_2.getAsynchronousServerCallPoint()[0].short_name == "Async1"
        assert len(runnable_2.getWaitPoints()) == 1
        assert runnable_2.getWaitPoints()[0].short_name == "Wait1"
        assert len(runnable_2.getWrittenLocalVariables()) == 1
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_round_trip_empty_runnable_has_no_wrappers():
    _make_runnable()

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, AUTOSAR.getInstance())
        raw = open(file_path, encoding="utf-8").read()
        for tag in ["ARGUMENTS", "ASYNCHRONOUS-SERVER-CALL-RESULT-POINTS", "DATA-READ-ACCESSS", "DATA-SEND-POINTS", "SERVER-CALL-POINTS", "SYMBOL", "WAIT-POINTS", "WRITTEN-LOCAL-VARIABLES"]:
            assert "<%s" % tag not in raw

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        package_2 = document_2.getARPackages()[0]
        swc_2 = package_2.getReferrableElement("Swc")
        behavior_2 = swc_2.getReferrableElement("Behavior")
        runnable_2 = behavior_2.getReferrableElement("Cyclic")
        assert runnable_2.getArguments() == []
        assert runnable_2.getServerCallPoints() == []
        assert runnable_2.getSymbol() is None
        assert runnable_2.getWaitPoints() == []
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


def test_symbol_time_value_values_survive():
    runnable = _make_runnable()
    runnable.setSymbol(CIdentifier().setValue("Sym_1"))

    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, AUTOSAR.getInstance())
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        runnable_2 = document_2.getARPackages()[0].getReferrableElement("Swc").getReferrableElement("Behavior").getReferrableElement("Cyclic")
        assert runnable_2.getSymbol() is not None
        assert runnable_2.getSymbol().getValue() == "Sym_1"
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
