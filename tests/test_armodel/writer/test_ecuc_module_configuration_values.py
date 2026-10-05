"""Reader/writer round-trip tests for EcucModuleConfigurationValues (Table 2.47).

The class is dispatched from the ARPackage.element switch (reader
readEcucModuleConfigurationValues branch, writer writeARPackageElement branch) and is
exercised here through its named read/write helpers directly.
"""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    EcucModuleConfigurationValues,
    EcucTextualParamValue,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Limit, RefType, RevisionLabelString, VerbatimString
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLParser()


def _ns_wrap(parent):
    return ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, ET.tostring(parent[0]).decode("utf-8")))


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _make_values(short_name):
    values = EcucModuleConfigurationValues(Limit(), short_name)
    values.setDefinitionRef(_ref("/EcucDefs/Os", "ECUC-MODULE-DEF"))
    values.setEcucDefEdition(RevisionLabelString().setValue("1.0.0"))
    values.setImplementationConfigVariant(EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE))
    values.setModuleDescriptionRef(_ref("/Vendor/OsImplementation", "BSW-IMPLEMENTATION"))
    values.setPostBuildVariantUsed(Boolean().setValue(True))
    return values


class TestEcucModuleConfigurationValuesReadWrite:
    def test_full_round_trip(self, writer, parser):
        """All six Table 2.47 XML elements round-trip in XSD order with field values asserted."""
        values = _make_values("mcv")
        container = values.createContainer("OsOS")
        container.setDefinitionRef(_ref("/EcucDefs/Os/OsOS", "ECUC-PARAM-CONF-CONTAINER-DEF"))
        param_value = EcucTextualParamValue()
        param_value.setDefinitionRef(_ref("/EcucDefs/Os/OsOS/OsParam", "ECUC-TEXTUAL-PARAM-VALUE"))
        param_value.setValue(VerbatimString().setValue("STD"))
        container.addParameterValue(param_value)

        parent = ET.Element("PARENT")
        writer.writeEcucModuleConfigurationValues(parent, values)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-MODULE-CONFIGURATION-VALUES>" in inner
        assert '<DEFINITION-REF DEST="ECUC-MODULE-DEF">/EcucDefs/Os</DEFINITION-REF>' in inner
        assert "<ECUC-DEF-EDITION>1.0.0</ECUC-DEF-EDITION>" in inner
        assert "<IMPLEMENTATION-CONFIG-VARIANT>VARIANT-PRE-COMPILE</IMPLEMENTATION-CONFIG-VARIANT>" in inner
        assert '<MODULE-DESCRIPTION-REF DEST="BSW-IMPLEMENTATION">/Vendor/OsImplementation</MODULE-DESCRIPTION-REF>' in inner
        assert "<POST-BUILD-VARIANT-USED>true</POST-BUILD-VARIANT-USED>" in inner
        assert "<CONTAINERS>" in inner
        assert (
            inner.index("<DEFINITION-REF")
            < inner.index("<ECUC-DEF-EDITION>")
            < inner.index("<IMPLEMENTATION-CONFIG-VARIANT>")
            < inner.index("<MODULE-DESCRIPTION-REF")
            < inner.index("<POST-BUILD-VARIANT-USED>")
            < inner.index("<CONTAINERS>")
        )

        reloaded = EcucModuleConfigurationValues(Limit(), "mcv")
        parser.readEcucModuleConfigurationValues(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getDefinitionRef() is not None
        assert reloaded.getDefinitionRef().getValue() == "/EcucDefs/Os"
        assert reloaded.getDefinitionRef().getDest() == "ECUC-MODULE-DEF"
        assert reloaded.getEcucDefEdition() is not None
        assert reloaded.getEcucDefEdition().getValue() == "1.0.0"
        assert reloaded.getImplementationConfigVariant() is not None
        assert reloaded.getImplementationConfigVariant().getValue() == "VARIANT-PRE-COMPILE"
        assert reloaded.getModuleDescriptionRef() is not None
        assert reloaded.getModuleDescriptionRef().getValue() == "/Vendor/OsImplementation"
        assert reloaded.getPostBuildVariantUsed() is not None
        assert reloaded.getPostBuildVariantUsed().getValue() is True

        containers = reloaded.getContainers()
        assert len(containers) == 1
        assert containers[0].getShortName() == "OsOS"
        assert containers[0].getDefinitionRef() is not None
        assert containers[0].getDefinitionRef().getValue() == "/EcucDefs/Os/OsOS"
        param_values = containers[0].getParameterValues()
        assert len(param_values) == 1
        assert param_values[0].getDefinitionRef() is not None
        assert param_values[0].getDefinitionRef().getValue() == "/EcucDefs/Os/OsOS/OsParam"
        assert param_values[0].getValue() is not None
        assert param_values[0].getValue().getValue() == "STD"

    def test_empty_containers_wrapper_not_emitted(self, writer, parser):
        """A module configuration without containers emits no CONTAINERS wrapper and reloads empty (TPS_ECUC_02152)."""
        values = _make_values("mcv_empty")

        parent = ET.Element("PARENT")
        writer.writeEcucModuleConfigurationValues(parent, values)
        values_element = parent.find("ECUC-MODULE-CONFIGURATION-VALUES")
        assert values_element is not None
        assert values_element.find("CONTAINERS") is None

        reloaded = EcucModuleConfigurationValues(Limit(), "mcv_empty")
        parser.readEcucModuleConfigurationValues(_ns_wrap(parent)[0], reloaded)
        assert reloaded.getContainers() == []

    def test_ecuc_def_edition_uses_revision_label_string_helper(self, writer, monkeypatch):
        """ECUC-DEF-EDITION is written through the spec-typed RevisionLabelString helper (Rule 0013.2 pair of getChildElementOptionalRevisionLabelString)."""
        calls = []
        original = ARXMLWriter.setChildElementOptionalRevisionLabelString

        def recorded(w, element, key, literal):
            calls.append(key)
            return original(w, element, key, literal)

        monkeypatch.setattr(ARXMLWriter, "setChildElementOptionalRevisionLabelString", recorded)

        values = EcucModuleConfigurationValues(Limit(), "mcv")
        values.setEcucDefEdition(RevisionLabelString().setValue("2.0.0"))

        parent = ET.Element("PARENT")
        writer.writeEcucModuleConfigurationValues(parent, values)
        assert "ECUC-DEF-EDITION" in calls
        values_element = parent.find("ECUC-MODULE-CONFIGURATION-VALUES")
        assert values_element is not None
        assert values_element.find("ECUC-DEF-EDITION") is not None
        assert values_element.find("ECUC-DEF-EDITION").text == "2.0.0"
