"""Tests for reading and writing ConsistencyNeeds elements."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str, dest: str = "DATA-PROTOTYPE-GROUP") -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _build_document(consistency_needs: ConsistencyNeeds):
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    ar_root = document.createARPackage("AUTOSAR")
    ar_root.addElement(consistency_needs)
    return document


def _reload(file_path):
    document_2 = AUTOSAR.getInstance()
    document_2.clear()
    ARXMLParser().load(file_path, document_2)
    package = document_2.getARPackages()[0]
    return next(element for element in package.elements if isinstance(element, ConsistencyNeeds))


class TestWriteConsistencyNeeds:
    def test_round_trip_populated(self):
        """Test parse -> write -> re-parse of populated aggregation lists."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "ConsistencyNeeds")

        dpg_not_coherent = consistency_needs.createDpgDoesNotRequireCoherency("DpgNotCoherent")
        implicit_iref = VariableDataPrototypeInCompositionInstanceRef()
        implicit_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        implicit_iref.setContextPortPrototypeRef(make_ref("/Comp/A/PPort", "P-PORT-PROTOTYPE"))
        implicit_iref.setTargetVariableDataPrototypeRef(make_ref("/Comp/A/PPort/Data", "VARIABLE-DATA-PROTOTYPE"))
        dpg_not_coherent.addImplicitDataAccessIRef(implicit_iref)

        consistency_needs.createDpgRequiresCoherency("DpgCoherent")

        reg_not_stable = consistency_needs.createRegDoesNotRequireStability("RegNotStable")
        runnable_iref = RunnableEntityInCompositionInstanceRef()
        runnable_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        runnable_iref.setTargetRunnableEntityRef(make_ref("/Comp/A/Runnable", "RUNNABLE-ENTITY"))
        reg_not_stable.addRunnableEntityIRef(runnable_iref)

        reg_stable = consistency_needs.createRegRequiresStability("RegStable")
        inner_iref = InnerRunnableEntityGroupInCompositionInstanceRef()
        inner_iref.addContextSwComponentPrototypeRef(make_ref("/Comp/A", "SW-COMPONENT-PROTOTYPE"))
        inner_iref.setTargetRunnableEntityGroupRef(make_ref("/Comp/A/Group"))
        reg_stable.addRunnableEntityGroupIRef(inner_iref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(consistency_needs))
            consistency_needs_2 = _reload(file_path)
            assert consistency_needs_2.getShortName() == "ConsistencyNeeds"

            dpg_not_coherent_2 = consistency_needs_2.getDpgDoesNotRequireCoherencys()
            assert len(dpg_not_coherent_2) == 1
            assert isinstance(dpg_not_coherent_2[0], DataPrototypeGroup)
            assert dpg_not_coherent_2[0].getShortName() == "DpgNotCoherent"
            implicit_refs = dpg_not_coherent_2[0].getImplicitDataAccessIRefs()
            assert len(implicit_refs) == 1
            assert implicit_refs[0].getTargetVariableDataPrototypeRef().getValue() == "/Comp/A/PPort/Data"

            dpg_coherent_2 = consistency_needs_2.getDpgRequiresCoherencys()
            assert len(dpg_coherent_2) == 1
            assert isinstance(dpg_coherent_2[0], DataPrototypeGroup)
            assert dpg_coherent_2[0].getShortName() == "DpgCoherent"

            reg_not_stable_2 = consistency_needs_2.getRegDoesNotRequireStabilitys()
            assert len(reg_not_stable_2) == 1
            assert isinstance(reg_not_stable_2[0], RunnableEntityGroup)
            assert reg_not_stable_2[0].getShortName() == "RegNotStable"
            runnable_refs = reg_not_stable_2[0].getRunnableEntityIRefs()
            assert len(runnable_refs) == 1
            assert runnable_refs[0].getTargetRunnableEntityRef().getValue() == "/Comp/A/Runnable"

            reg_stable_2 = consistency_needs_2.getRegRequiresStabilitys()
            assert len(reg_stable_2) == 1
            assert isinstance(reg_stable_2[0], RunnableEntityGroup)
            assert reg_stable_2[0].getShortName() == "RegStable"
            inner_refs = reg_stable_2[0].getRunnableEntityGroupIRefs()
            assert len(inner_refs) == 1
            assert inner_refs[0].getTargetRunnableEntityGroupRef().getValue() == "/Comp/A/Group"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_wrappers(self):
        """Test empty aggregation lists round-trip to no wrapper elements."""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "ConsistencyNeeds")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, _build_document(consistency_needs))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "DPG-DOES-NOT-REQUIRE-COHERENCYS" not in content
            assert "DPG-REQUIRES-COHERENCYS" not in content
            assert "REG-DOES-NOT-REQUIRE-STABILITYS" not in content
            assert "REG-REQUIRES-STABILITYS" not in content

            consistency_needs_2 = _reload(file_path)
            assert consistency_needs_2.getShortName() == "ConsistencyNeeds"
            assert consistency_needs_2.getDpgDoesNotRequireCoherencys() == []
            assert consistency_needs_2.getDpgRequiresCoherencys() == []
            assert consistency_needs_2.getRegDoesNotRequireStabilitys() == []
            assert consistency_needs_2.getRegRequiresStabilitys() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
