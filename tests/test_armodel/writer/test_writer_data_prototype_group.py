"""Tests for reading and writing DataPrototypeGroup elements."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import DataPrototypeGroup
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str = "DATA-PROTOTYPE-GROUP") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _build_document(group: DataPrototypeGroup):
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    ar_root = document.createARPackage("AUTOSAR")
    ar_root.addReferrableElement(group)
    return document


def _reload(file_path):
    document_2 = AUTOSAR.getInstance()
    document_2.clear()
    ARXMLParser().load(file_path, document_2)
    package = document_2.getARPackages()[0]
    return next(element for element in package.referrableElements if isinstance(element, DataPrototypeGroup))


class TestWriteDataPrototypeGroup:
    def test_round_trip_populated(self):
        """Test parse -> write -> re-parse of populated dataPrototypeGroupIRefs and implicitDataAccessIRefs."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        group = DataPrototypeGroup(ar_root, "ImplicitDataGroup")

        inner_iref = InnerDataPrototypeGroupInCompositionInstanceRef()
        inner_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        inner_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/B", "SW-COMPONENT-PROTOTYPE"))
        inner_iref.setTargetDataPrototypeGroupRef(make_ref("/Comp/A/Group"))
        group.addDataPrototypeGroupIRef(inner_iref)

        implicit_iref = VariableDataPrototypeInCompositionInstanceRef()
        implicit_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        implicit_iref.setContextPortPrototypeRef(make_ref("/Comp/A/PPort", "P-PORT-PROTOTYPE"))
        implicit_iref.setTargetVariableDataPrototypeRef(make_ref("/Comp/A/PPort/Data", "VARIABLE-DATA-PROTOTYPE"))
        group.addImplicitDataAccessIRef(implicit_iref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(group))
            group_2 = _reload(file_path)
            assert group_2.getShortName() == "ImplicitDataGroup"
            inner_refs = group_2.getDataPrototypeGroupIRefs()
            assert len(inner_refs) == 1
            assert [r.getValue() for r in inner_refs[0].getContextSwComponentPrototypeRefs()] == ["/Comp/A", "/Comp/B"]
            assert inner_refs[0].getTargetDataPrototypeGroupRef().getValue() == "/Comp/A/Group"
            implicit_refs = group_2.getImplicitDataAccessIRefs()
            assert len(implicit_refs) == 1
            assert [r.getValue() for r in implicit_refs[0].getContextSwComponentPrototypeRefs()] == ["/Comp/A"]
            assert implicit_refs[0].getContextPortPrototypeRef().getValue() == "/Comp/A/PPort"
            assert implicit_refs[0].getTargetVariableDataPrototypeRef().getValue() == "/Comp/A/PPort/Data"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_wrappers(self):
        """Test empty iref lists round-trip to no wrapper elements."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        group = DataPrototypeGroup(ar_root, "ImplicitDataGroup")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(group))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "DATA-PROTOTYPE-GROUP-IREFS" not in content
            assert "IMPLICIT-DATA-ACCESS-IREFS" not in content

            group_2 = _reload(file_path)
            assert group_2.getShortName() == "ImplicitDataGroup"
            assert group_2.getDataPrototypeGroupIRefs() == []
            assert group_2.getImplicitDataAccessIRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestWriteDataPrototypeGroupVariationPoint:
    """VARIATION-POINT is anchored in the XSD group DATA-PROTOTYPE-GROUP with
    xml.sequenceOffset="10000" — it serializes last, after the two iref wrapper
    lists (AUTOSAR_00052.xsd)."""

    def test_write_variation_point_last(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "ImplicitDataGroup")
        data_group.addDataPrototypeGroupIRef(InnerDataPrototypeGroupInCompositionInstanceRef())
        implicit_iref = VariableDataPrototypeInCompositionInstanceRef()
        implicit_iref.setTargetVariableDataPrototypeRef(make_ref("/Comp/A/PPort/Data", "VARIABLE-DATA-PROTOTYPE"))
        data_group.addImplicitDataAccessIRef(implicit_iref)
        variation_point = VariationPoint()
        vp_label = Identifier()
        vp_label.setValue("VP1")
        variation_point.setShortLabel(vp_label)
        data_group.setVariationPoint(variation_point)

        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeDataPrototypeGroup(parent_element, data_group)

        child = parent_element[0]
        assert child.tag == "DATA-PROTOTYPE-GROUP"
        tags = [element.tag for element in child]
        assert tags.index("DATA-PROTOTYPE-GROUP-IREFS") < tags.index("VARIATION-POINT")
        assert tags.index("IMPLICIT-DATA-ACCESS-IREFS") < tags.index("VARIATION-POINT")
        assert tags[-1] == "VARIATION-POINT"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_no_variation_point_omits_element(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "ImplicitDataGroup")

        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeDataPrototypeGroup(parent_element, data_group)

        child = parent_element[0]
        assert child.find("VARIATION-POINT") is None

    def test_round_trip_variation_point(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        data_group = DataPrototypeGroup(ar_root, "ImplicitDataGroup")
        implicit_iref = VariableDataPrototypeInCompositionInstanceRef()
        implicit_iref.setTargetVariableDataPrototypeRef(make_ref("/Comp/A/PPort/Data", "VARIABLE-DATA-PROTOTYPE"))
        data_group.addImplicitDataAccessIRef(implicit_iref)
        variation_point = VariationPoint()
        vp_label = Identifier()
        vp_label.setValue("VP2")
        variation_point.setShortLabel(vp_label)
        data_group.setVariationPoint(variation_point)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(data_group))
            group_2 = _reload(file_path)
            assert group_2.getVariationPoint() is not None
            assert group_2.getVariationPoint().getShortLabel().getValue() == "VP2"
            assert group_2.getImplicitDataAccessIRefs()[0].getTargetVariableDataPrototypeRef().getValue() == "/Comp/A/PPort/Data"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
