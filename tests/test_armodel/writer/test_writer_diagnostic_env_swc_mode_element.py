"""
Tests for writing DIAGNOSTIC-ENV-SWC-MODE-ELEMENT elements —
DiagnosticEnvSwcModeElement, Table 4.45 (p.89, R23-11).

DiagnosticEnvSwcModeElement (Base most-derived DiagnosticEnvModeElement, a
Referrable) carries its own 0..1 MODE-IREF of type P-MODE-IN-SYSTEM-INSTANCE-REF
— XSD group DIAGNOSTIC-ENV-SWC-MODE-ELEMENT, AUTOSAR_00052.xsd l.36081. The
MODE-IREF write is deferred until the PModeInSystemInstanceRef model class exists
(Rule 0001.10); the Referrable identity (SHORT-NAME, AR-OBJECT attributes) is
written now. The writer reads the model via the get* getters; the dispatch
entries are writeDiagnosticEnvironmentalCondition (MODE-ELEMENTS wrapper, emitted
only when non-empty) → writeDiagnosticEnvSwcModeElement.

Round-trip counterpart: tests/test_armodel/parser/test_diagnostic_env_swc_mode_element.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.EnvironmentalCondition import (
    DiagnosticEnvConditionFormula,
    DiagnosticEnvironmentalCondition,
    DiagnosticEnvSwcModeElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(dest: str, value: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _positive_integer(value: str) -> PositiveInteger:
    nrc_value = PositiveInteger()
    nrc_value.setValue(value)
    return nrc_value


class TestWriteDiagnosticEnvSwcModeElement:
    """Tests for writeDiagnosticEnvSwcModeElement — own element field values (Table 4.45)."""

    def test_write_referrable_identity(self):
        """Test that the Referrable identity (SHORT-NAME) is emitted under DIAGNOSTIC-ENV-SWC-MODE-ELEMENT."""
        mode_element = DiagnosticEnvSwcModeElement(AUTOSAR.getInstance(), "SwcMode1")
        mode_element.setModeIRef(_ref("MODE-DECLARATION", "/AUTOSAR/ModeDcls/MDG1/Normal"))

        parent = ET.Element("MODE-ELEMENTS")
        ARXMLWriter().writeDiagnosticEnvSwcModeElement(parent, mode_element)

        child = parent.find("DIAGNOSTIC-ENV-SWC-MODE-ELEMENT")
        assert child is not None
        assert child.find("SHORT-NAME").text == "SwcMode1"
        assert child.find("MODE-IREF") is None

    def test_mode_elements_dispatch_writes_element(self):
        """Test that writeDiagnosticEnvironmentalCondition emits the MODE-ELEMENTS wrapper with the DIAGNOSTIC-ENV-SWC-MODE-ELEMENT item."""
        env_condition = DiagnosticEnvironmentalCondition(AUTOSAR.getInstance(), "Env1")
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        env_condition.addModeElement(mode_element)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvironmentalCondition(parent, env_condition)

        child = parent.find("DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        assert child is not None
        mode_elements = child.find("MODE-ELEMENTS")
        assert mode_elements is not None
        swc_element = mode_elements.find("DIAGNOSTIC-ENV-SWC-MODE-ELEMENT")
        assert swc_element is not None
        assert swc_element.find("SHORT-NAME").text == "SwcMode1"

    def test_empty_mode_elements_omits_wrapper(self):
        """Test that an empty modeElements list emits no MODE-ELEMENTS wrapper."""
        env_condition = DiagnosticEnvironmentalCondition(AUTOSAR.getInstance(), "Env1")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeDiagnosticEnvironmentalCondition(parent, env_condition)

        child = parent.find("DIAGNOSTIC-ENVIRONMENTAL-CONDITION")
        assert child is not None
        assert child.find("MODE-ELEMENTS") is None

    def test_round_trip(self):
        """Test the full build → save → reload → assert cycle over a DiagnosticEnvironmentalCondition with a DiagnosticEnvSwcModeElement."""
        document = AUTOSAR.getInstance()
        package = document.createARPackage("EnvConds")
        env_condition = package.createDiagnosticEnvironmentalCondition("Env1")
        formula = DiagnosticEnvConditionFormula()
        formula.setNrcValue(_positive_integer("49"))
        env_condition.setFormula(formula)
        mode_element = DiagnosticEnvSwcModeElement(env_condition, "SwcMode1")
        mode_element.setModeIRef(_ref("MODE-DECLARATION", "/AUTOSAR/ModeDcls/MDG1/Normal"))
        env_condition.addModeElement(mode_element)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)
            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            package_2 = document_2.getARPackages()[0]
            env_condition_2 = package_2.getElement("Env1", type(env_condition))
            assert env_condition_2 is not None
            mode_elements = env_condition_2.getModeElements()
            assert len(mode_elements) == 1
            mode_element_2 = mode_elements[0]
            assert type(mode_element_2).__name__ == "DiagnosticEnvSwcModeElement"
            assert mode_element_2.getShortName() == "SwcMode1"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
