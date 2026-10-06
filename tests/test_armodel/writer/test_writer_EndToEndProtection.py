"""Writer/reader round-trip tests for EndToEndProtection (Swc TPS Table 4.97, p.215).

The expected XML uses the XSD-valid element spellings and order from the group
END-TO-END-PROTECTION in ``autosar/R23-11/xsd/AUTOSAR_00052.xsd``: after the
IDENTIFIABLE group content, END-TO-END-PROFILE, then the two wrapper lists,
then VARIATION-POINT (sequenceOffset 10000). The class is aggregated by
EndToEndProtectionSet.endToEndProtection, so the save/load round-trip goes
through the ARPackage dispatch on both sides.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription, EndToEndProtectionSet, EndToEndProtectionVariablePrototype
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLParser()


def _populate(protection):
    profile = EndToEndDescription()
    category = Identifier()
    category.setValue("CATEGORY1")
    profile.setCategory(category)
    protection.setEndToEndProfile(profile)

    ipdu = EndToEndProtectionISignalIPdu()
    offset = PositiveInteger()
    offset.setValue("8")
    ipdu.setDataOffset(offset)
    group_ref = RefType()
    group_ref.setValue("/isg/Group1")
    group_ref.setDest("I-SIGNAL-GROUP")
    ipdu.setISignalGroupRef(group_ref)
    protection.addEndToEndProtectionISignalIPdu(ipdu)

    prototype = EndToEndProtectionVariablePrototype()
    label = Identifier()
    label.setValue("SegA")
    prototype.setShortLabel(label)
    sender = VariableDataPrototypeInSystemInstanceRef()
    target_ref = RefType()
    target_ref.setValue("/vdp/Var")
    target_ref.setDest("VARIABLE-DATA-PROTOTYPE")
    sender.setTargetDataPrototypeRef(target_ref)
    prototype.setSenderIref(sender)
    protection.addEndToEndProtectionVariablePrototype(prototype)

    variation_point = VariationPoint()
    vp_label = Identifier()
    vp_label.setValue("VP1")
    variation_point.setShortLabel(vp_label)
    protection.setVariationPoint(variation_point)


class TestEndToEndProtectionWriter:
    def test_write_full_element_order_and_values(self, writer):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        protection_set = package.createEndToEndProtectionSet("E2eSet")
        protection = protection_set.createEndToEndProtection("Protection")
        _populate(protection)

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtection(parent, protection)

        assert len(parent) == 1
        child = parent[0]
        assert child.tag == "END-TO-END-PROTECTION"
        tags = [element.tag for element in child]
        assert tags.index("END-TO-END-PROFILE") < tags.index("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS")
        assert tags.index("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS") < tags.index("END-TO-END-PROTECTION-VARIABLE-PROTOTYPES")
        assert tags[-1] == "VARIATION-POINT"
        assert child.find("END-TO-END-PROFILE/CATEGORY").text == "CATEGORY1"
        assert child.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS/END-TO-END-PROTECTION-I-SIGNAL-I-PDU/DATA-OFFSET").text == "8"
        assert child.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS/END-TO-END-PROTECTION-I-SIGNAL-I-PDU/I-SIGNAL-GROUP-REF").text == "/isg/Group1"
        assert child.find("END-TO-END-PROTECTION-VARIABLE-PROTOTYPES/END-TO-END-PROTECTION-VARIABLE-PROTOTYPE/SHORT-LABEL").text == "SegA"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_empty_wrappers_omitted(self, writer):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        protection_set = package.createEndToEndProtectionSet("E2eSet")
        protection = protection_set.createEndToEndProtection("BareProtection")

        parent = ET.Element("PARENT")
        writer.writeEndToEndProtection(parent, protection)

        child = parent[0]
        assert child.find("END-TO-END-PROFILE") is None
        assert child.find("END-TO-END-PROTECTION-I-SIGNAL-I-PDUS") is None
        assert child.find("END-TO-END-PROTECTION-VARIABLE-PROTOTYPES") is None
        assert child.find("VARIATION-POINT") is None

    def test_write_none(self, writer):
        parent = ET.Element("PARENT")
        writer.writeEndToEndProtection(parent, None)
        assert len(parent) == 0


class TestEndToEndProtectionRoundTrip:
    def _round_trip(self, writer, parser, tmp_path, populate):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        package = document.createARPackage("Pkg")
        protection_set = package.createEndToEndProtectionSet("E2eSet")
        protection = protection_set.createEndToEndProtection("Protection")
        if populate:
            _populate(protection)

        out_file = str(tmp_path / "end_to_end_protection.arxml")
        writer.save(out_file, document)

        recovered = AUTOSAR.getInstance()
        recovered.clear()
        recovered.setARRelease("R23-11")
        parser.load(out_file, recovered)
        return recovered

    def test_round_trip_preserves_field_values(self, writer, parser, tmp_path):
        recovered = self._round_trip(writer, parser, tmp_path, True)

        reloaded_pkg = recovered.getARPackages()[0]
        protection_set = reloaded_pkg.getReferrableElement("E2eSet", EndToEndProtectionSet)
        assert protection_set is not None
        protections = protection_set.getEndToEndProtections()
        assert len(protections) == 1
        protection = protections[0]
        assert protection.getShortName() == "Protection"
        assert protection.getEndToEndProfile() is not None
        assert protection.getEndToEndProfile().getCategory().getValue() == "CATEGORY1"
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 1
        assert ipdus[0].getDataOffset().getValue() == 8
        assert ipdus[0].getISignalGroupRef().getValue() == "/isg/Group1"
        prototypes = protection.getEndToEndProtectionVariablePrototypes()
        assert len(prototypes) == 1
        assert prototypes[0].getShortLabel().getValue() == "SegA"
        assert prototypes[0].getSenderIref().getTargetDataPrototypeRef().getValue() == "/vdp/Var"
        assert protection.getVariationPoint() is not None
        assert protection.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_round_trip_empty(self, writer, parser, tmp_path):
        recovered = self._round_trip(writer, parser, tmp_path, False)

        reloaded_pkg = recovered.getARPackages()[0]
        protection_set = reloaded_pkg.getReferrableElement("E2eSet", EndToEndProtectionSet)
        protection = protection_set.getEndToEndProtections()[0]
        assert protection.getShortName() == "Protection"
        assert protection.getEndToEndProfile() is None
        assert protection.getEndToEndProtectionISignalIPdus() == []
        assert protection.getEndToEndProtectionVariablePrototypes() == []
        assert protection.getVariationPoint() is None
