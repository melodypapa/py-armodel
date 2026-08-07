from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McDataAccessDetails, McSupportData, RteEventInEcuInstanceRef, VariableAccessInEcuInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter
import os
import tempfile


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestMcDataAccessDetailsInitialization:
    def test_initialization(self):
        """Test McDataAccessDetails __init__ defaults"""
        details = McDataAccessDetails()
        assert details is not None
        assert details.rteEventIRefs == []
        assert details.variableAccessIRefs == []


class TestMcDataAccessDetailsRteEvent:
    def test_add_get_rte_event_iref(self):
        """Test addRteEventIRef appends and returns self"""
        details = McDataAccessDetails()
        iref = RteEventInEcuInstanceRef()
        result = details.addRteEventIRef(iref)
        assert result is details
        assert details.getRteEventIRefs() == [iref]

    def test_add_rte_event_iref_none_is_noop(self):
        """Test adding a None rteEvent iref is a no-op"""
        details = McDataAccessDetails()
        details.addRteEventIRef(None)
        assert details.getRteEventIRefs() == []


class TestMcDataAccessDetailsVariableAccess:
    def test_add_get_variable_access_iref(self):
        """Test addVariableAccessIRef appends and returns self"""
        details = McDataAccessDetails()
        iref = VariableAccessInEcuInstanceRef()
        result = details.addVariableAccessIRef(iref)
        assert result is details
        assert details.getVariableAccessIRefs() == [iref]

    def test_add_variable_access_iref_none_is_noop(self):
        """Test adding a None variableAccess iref is a no-op"""
        details = McDataAccessDetails()
        details.addVariableAccessIRef(None)
        assert details.getVariableAccessIRefs() == []


class TestMcDataAccessDetailsRoundTrip:
    def _build_document(self, details: McDataAccessDetails):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        mc_support = McSupportData()
        impl.setMcSupport(mc_support)
        instance = mc_support.createMcParameterInstance("CalPrm1")
        instance.setMcDataAccessDetails(details)
        return document

    def _reload(self, file_path):
        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        return document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport().getMcParameterInstances()[0]

    def test_round_trip_populated(self):
        """Test parse -> write -> re-parse of populated rteEventIRefs and variableAccessIRefs."""
        details = McDataAccessDetails()
        rte_iref = RteEventInEcuInstanceRef()
        rte_iref.setContextRootCompositionRef(make_ref("/Root"))
        rte_iref.setContextAtomicComponentRef(make_ref("/Root/Comp"))
        rte_iref.setTargetRteEventRef(make_ref("/Root/Comp/Evt"))
        details.addRteEventIRef(rte_iref)
        var_iref = VariableAccessInEcuInstanceRef()
        var_iref.setContextRootCompositionRef(make_ref("/Root"))
        var_iref.setContextAtomicComponentRef(make_ref("/Root/Comp"))
        var_iref.setTargetVariableAccessRef(make_ref("/Root/Comp/Var"))
        details.addVariableAccessIRef(var_iref)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, self._build_document(details))
            instance_2 = self._reload(file_path)
            details_2 = instance_2.getMcDataAccessDetails()
            assert details_2 is not None
            assert details_2.getRteEventIRefs()[0].getContextRootCompositionRef().getValue() == "/Root"
            assert details_2.getRteEventIRefs()[0].getContextAtomicComponentRef().getValue() == "/Root/Comp"
            assert details_2.getRteEventIRefs()[0].getTargetRteEventRef().getValue() == "/Root/Comp/Evt"
            assert details_2.getVariableAccessIRefs()[0].getTargetVariableAccessRef().getValue() == "/Root/Comp/Var"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_wrappers(self):
        """Test empty rteEventIRefs/variableAccessIRefs round-trip to no wrapper elements."""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, self._build_document(McDataAccessDetails()))
            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "RTE-EVENT-IREFS" not in content
            assert "VARIABLE-ACCESS-IREFS" not in content

            instance_2 = self._reload(file_path)
            details_2 = instance_2.getMcDataAccessDetails()
            assert details_2 is not None
            assert details_2.getRteEventIRefs() == []
            assert details_2.getVariableAccessIRefs() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
