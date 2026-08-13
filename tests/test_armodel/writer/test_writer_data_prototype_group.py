"""Tests for reading and writing DataPrototypeGroup elements."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import DataPrototypeGroup
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRefs import (
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
    ar_root.addElement(group)
    return document


def _reload(file_path):
    document_2 = AUTOSAR.getInstance()
    document_2.clear()
    ARXMLParser().load(file_path, document_2)
    package = document_2.getARPackages()[0]
    return next(element for element in package.elements if isinstance(element, DataPrototypeGroup))


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
