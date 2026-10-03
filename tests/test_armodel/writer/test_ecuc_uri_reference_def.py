"""Writer/reader round-trip tests for EcucUriReferenceDef (ECUC-URI-REFERENCE-DEF)."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import (
    EcucDestinationUriPolicy,
    EcucParamConfContainerDef,
    EcucUriReferenceDef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
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


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _uri_ref(parent, short_name):
    ref_def = EcucUriReferenceDef(parent, short_name)
    ref_def.setDestinationUriRef(_ref("/Mod/TargetContainer", "ECUC-DESTINATION-URI-DEF"))
    return ref_def


class TestEcucUriReferenceDefRoundTrip:
    def test_container_references_round_trip(self, writer, parser):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        module = pkg.createEcucModuleDef("Mod")
        container = module.createEcucParamConfContainerDef("Ct")
        container.createEcucUriReferenceDef("UriRef1").setDestinationUriRef(_ref("/Mod/TargetContainer", "ECUC-DESTINATION-URI-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucContainerDefReferences(parent, container)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-URI-REFERENCE-DEF>" in inner
        assert "<DESTINATION-URI-REF" in inner
        assert 'DEST="ECUC-DESTINATION-URI-DEF"' in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded_container = EcucParamConfContainerDef(None, "Ct")
        parser.readEcucContainerDefReferences(root[0], reloaded_container)
        references = reloaded_container.getReferences()
        assert len(references) == 1
        ref_def = references[0]
        assert isinstance(ref_def, EcucUriReferenceDef)
        assert ref_def.getShortName() == "UriRef1"
        destination_uri_ref = ref_def.getDestinationUriRef()
        assert destination_uri_ref is not None
        assert destination_uri_ref.getValue() == "/Mod/TargetContainer"
        assert destination_uri_ref.getDest() == "ECUC-DESTINATION-URI-DEF"

    def test_destination_uri_policy_references_round_trip(self, writer, parser):
        policy = EcucDestinationUriPolicy()
        policy.createEcucUriReferenceDef("UriRef2").setDestinationUriRef(_ref("/Mod/TargetContainer", "ECUC-DESTINATION-URI-DEF"))

        parent = ET.Element("PARENT")
        writer.writeEcucDestinationUriPolicyReferences(parent, policy)
        inner = ET.tostring(parent).decode("utf-8")
        assert "<ECUC-URI-REFERENCE-DEF>" in inner

        root = ET.fromstring("<AUTOSAR xmlns='%s'>%s</AUTOSAR>" % (NS, inner))
        reloaded_policy = EcucDestinationUriPolicy()
        parser.readEcucDestinationUriPolicyReferences(root[0], reloaded_policy)
        references = reloaded_policy.getReferences()
        assert len(references) == 1
        ref_def = references[0]
        assert isinstance(ref_def, EcucUriReferenceDef)
        assert ref_def.getShortName() == "UriRef2"
        assert ref_def.getDestinationUriRef().getValue() == "/Mod/TargetContainer"
        assert ref_def.getDestinationUriRef().getDest() == "ECUC-DESTINATION-URI-DEF"

    def test_no_references_no_element(self, writer):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        module = pkg.createEcucModuleDef("Mod")
        container = module.createEcucParamConfContainerDef("Ct")
        parent = ET.Element("PARENT")
        writer.writeEcucContainerDefReferences(parent, container)
        assert len(parent) == 0
