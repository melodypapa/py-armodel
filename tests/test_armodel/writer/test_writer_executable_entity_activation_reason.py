"""Writer/reader round-trip tests for ExecutableEntityActivationReason (Table 7.7, p.539, R23-11).

EEAR aggregates under RunnableEntity via the ACTIVATION-REASONS wrapper
(one EXECUTABLE-ENTITY-ACTIVATION-REASON per entry). Element order per the XSD
complexType: AR-OBJECT, REFERRABLE, IMPLEMENTATION-PROPS (SYMBOL), EEAR (BIT-POSITION).

Round-trip counterpart: tests/test_armodel/parser/test_runnable_entity.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import ExecutableEntityActivationReason
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity
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


def test_write_activation_reason_field_values():
    runnable = _make_runnable()
    reason = runnable.createActivationReason("ReasonA")
    reason.setBitPosition(PositiveInteger().setValue("7"))

    element = ET.Element("RUNNABLE-ENTITY")
    ARXMLWriter().writeActivationReasons(element, runnable)

    wrapper = element.find("ACTIVATION-REASONS")
    assert wrapper is not None
    reason_tag = wrapper.find("EXECUTABLE-ENTITY-ACTIVATION-REASON")
    assert reason_tag is not None
    bit_position = reason_tag.find("BIT-POSITION")
    assert bit_position is not None
    assert bit_position.text == "7"


def test_write_activation_reasons_empty_wrapper():
    runnable = _make_runnable()
    element = ET.Element("RUNNABLE-ENTITY")
    ARXMLWriter().writeActivationReasons(element, runnable)
    assert element.find("ACTIVATION-REASONS") is None


def test_round_trip_preserves_field_values():
    runnable = _make_runnable()
    reason = runnable.createActivationReason("ReasonA")
    reason.setBitPosition(PositiveInteger().setValue("7"))

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
        reasons = runnable_2.getActivationReasons()
        assert len(reasons) == 1
        reason_2 = reasons[0]
        assert isinstance(reason_2, ExecutableEntityActivationReason)
        assert reason_2.getShortName() == "ReasonA"
        assert reason_2.getBitPosition() is not None
        assert reason_2.getBitPosition().getValue() == 7
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
