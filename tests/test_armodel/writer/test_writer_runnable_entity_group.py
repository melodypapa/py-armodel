"""Tests for reading and writing RunnableEntityGroup elements."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import RunnableEntityGroup
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str = "RUNNABLE-ENTITY-GROUP") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _build_document(group: RunnableEntityGroup):
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
    return next(element for element in package.referrableElements if isinstance(element, RunnableEntityGroup))


class TestWriteRunnableEntityGroup:
    def test_round_trip_populated(self):
        """Test parse -> write -> re-parse of populated runnableEntityIRefs and runnableEntityGroupIRefs."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        group = RunnableEntityGroup(ar_root, "RunnableGroup")

        inner_iref = InnerRunnableEntityGroupInCompositionInstanceRef()
        inner_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        inner_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/B", "SW-COMPONENT-PROTOTYPE"))
        inner_iref.setTargetRunnableEntityGroupRef(make_ref("/Comp/A/Group"))
        group.addRunnableEntityGroupIRef(inner_iref)

        runnable_iref = RunnableEntityInCompositionInstanceRef()
        runnable_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        runnable_iref.setTargetRunnableEntityRef(make_ref("/Comp/A/Runnable", "RUNNABLE-ENTITY"))
        group.addRunnableEntityIRef(runnable_iref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(group))
            group_2 = _reload(file_path)
            assert group_2.getShortName() == "RunnableGroup"
            inner_refs = group_2.getRunnableEntityGroupIRefs()
            assert len(inner_refs) == 1
            assert [r.getValue() for r in inner_refs[0].getContextSwComponentPrototypeRefs()] == ["/Comp/A", "/Comp/B"]
            assert inner_refs[0].getTargetRunnableEntityGroupRef().getValue() == "/Comp/A/Group"
            runnable_refs = group_2.getRunnableEntityIRefs()
            assert len(runnable_refs) == 1
            assert [r.getValue() for r in runnable_refs[0].getContextSwComponentPrototypeRefs()] == ["/Comp/A"]
            assert runnable_refs[0].getTargetRunnableEntityRef().getValue() == "/Comp/A/Runnable"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_wrappers(self):
        """Test empty iref lists round-trip to no wrapper elements."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        group = RunnableEntityGroup(ar_root, "RunnableGroup")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(group))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "RUNNABLE-ENTITY-GROUP-IREFS" not in content
            assert "RUNNABLE-ENTITY-IREFS" not in content

            group_2 = _reload(file_path)
            assert group_2.getShortName() == "RunnableGroup"
            assert group_2.getRunnableEntityGroupIRefs() == []
            assert group_2.getRunnableEntityIRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestWriteRunnableEntityGroupVariationPoint:
    """VARIATION-POINT is anchored in the XSD group RUNNABLE-ENTITY-GROUP with
    xml.sequenceOffset="10000" — it serializes last, after the two iref wrapper
    lists (AUTOSAR_00052.xsd)."""

    def test_write_variation_point_last(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "RunnableGroup")
        runnable_group.addRunnableEntityGroupIRef(InnerRunnableEntityGroupInCompositionInstanceRef())
        variation_point = VariationPoint()
        vp_label = Identifier()
        vp_label.setValue("VP1")
        variation_point.setShortLabel(vp_label)
        runnable_group.setVariationPoint(variation_point)

        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeRunnableEntityGroup(parent_element, runnable_group)

        child = parent_element[0]
        assert child.tag == "RUNNABLE-ENTITY-GROUP"
        tags = [element.tag for element in child]
        assert tags.index("RUNNABLE-ENTITY-GROUP-IREFS") < tags.index("VARIATION-POINT")
        assert tags[-1] == "VARIATION-POINT"
        assert child.find("VARIATION-POINT/SHORT-LABEL").text == "VP1"

    def test_write_no_variation_point_omits_element(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "RunnableGroup")

        parent_element = ET.Element("PARENT")
        ARXMLWriter().writeRunnableEntityGroup(parent_element, runnable_group)

        child = parent_element[0]
        assert child.find("VARIATION-POINT") is None

    def test_round_trip_variation_point(self):
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        runnable_group = RunnableEntityGroup(ar_root, "RunnableGroup")
        runnable_iref = RunnableEntityInCompositionInstanceRef()
        runnable_iref.setTargetRunnableEntityRef(make_ref("/Comp/A/Runnable", "RUNNABLE-ENTITY"))
        runnable_group.addRunnableEntityIRef(runnable_iref)
        variation_point = VariationPoint()
        vp_label = Identifier()
        vp_label.setValue("VP2")
        variation_point.setShortLabel(vp_label)
        runnable_group.setVariationPoint(variation_point)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(runnable_group))
            group_2 = _reload(file_path)
            assert group_2.getVariationPoint() is not None
            assert group_2.getVariationPoint().getShortLabel().getValue() == "VP2"
            assert group_2.getRunnableEntityIRefs()[0].getTargetRunnableEntityRef().getValue() == "/Comp/A/Runnable"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
