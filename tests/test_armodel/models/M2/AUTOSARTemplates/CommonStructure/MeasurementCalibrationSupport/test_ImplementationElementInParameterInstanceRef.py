import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import ImplementationElementInParameterInstanceRef, McSupportData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def make_ref(value: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    return ref


class TestImplementationElementInParameterInstanceRefInitialization:
    def test_initialization(self):
        """Test ImplementationElementInParameterInstanceRef __init__ defaults"""
        instance_ref = ImplementationElementInParameterInstanceRef()
        assert instance_ref is not None
        assert instance_ref.contextRef is None
        assert instance_ref.targetRef is None


class TestImplementationElementInParameterInstanceRefContext:
    def test_get_set_context_ref(self):
        """Test setContextRef returns self and getContextRef round-trips"""
        instance_ref = ImplementationElementInParameterInstanceRef()
        ref = make_ref("/Context/Prototype")
        result = instance_ref.setContextRef(ref)
        assert result is instance_ref
        assert instance_ref.getContextRef() is ref

    def test_set_context_ref_none_is_noop(self):
        """Test setting a None context ref is a no-op"""
        instance_ref = ImplementationElementInParameterInstanceRef()
        ref = make_ref("/Context/Prototype")
        instance_ref.setContextRef(ref)
        instance_ref.setContextRef(None)
        assert instance_ref.getContextRef() is ref


class TestImplementationElementInParameterInstanceRefTarget:
    def test_get_set_target_ref(self):
        """Test setTargetRef returns self and getTargetRef round-trips"""
        instance_ref = ImplementationElementInParameterInstanceRef()
        ref = make_ref("/Context/Prototype/Element")
        result = instance_ref.setTargetRef(ref)
        assert result is instance_ref
        assert instance_ref.getTargetRef() is ref

    def test_set_target_ref_none_is_noop(self):
        """Test setting a None target ref is a no-op"""
        instance_ref = ImplementationElementInParameterInstanceRef()
        ref = make_ref("/Context/Prototype/Element")
        instance_ref.setTargetRef(ref)
        instance_ref.setTargetRef(None)
        assert instance_ref.getTargetRef() is ref


class TestImplementationElementInParameterInstanceRefRoundTrip:
    def test_round_trip_via_mc_support_data(self):
        """Test parse -> write -> re-parse round trip of the typed iref nested under MC-DATA-INSTANCE/INSTANCE-IN-MEMORY."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        mc_support = McSupportData()
        impl.setMcSupport(mc_support)

        instance = mc_support.createMcParameterInstance("CalPrm1")
        instance_in_memory = ImplementationElementInParameterInstanceRef()
        instance_in_memory.setContextRef(make_ref("/Context/Prototype"))
        instance_in_memory.setTargetRef(make_ref("/Context/Prototype/Element"))
        instance.setInstanceInMemory(instance_in_memory)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            mc_support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()
            instance_2 = mc_support_2.getMcParameterInstances()[0]
            instance_in_memory_2 = instance_2.getInstanceInMemory()
            assert instance_in_memory_2 is not None
            assert instance_in_memory_2.getContextRef().getValue() == "/Context/Prototype"
            assert instance_in_memory_2.getTargetRef().getValue() == "/Context/Prototype/Element"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_unset_emits_no_iref_element(self):
        """Test an unset instanceInMemory round-trips to no INSTANCE-IN-MEMORY element."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        impl = ar_root.createBswImplementation("test_impl")
        mc_support = McSupportData()
        impl.setMcSupport(mc_support)
        mc_support.createMcParameterInstance("CalPrm1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            with open(file_path, "r", encoding="utf-8") as file_handle:
                content = file_handle.read()
            assert "INSTANCE-IN-MEMORY" not in content

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)
            mc_support_2 = document_2.getARPackages()[0].getBswImplementations()[0].getMcSupport()
            assert mc_support_2.getMcParameterInstances()[0].getInstanceInMemory() is None
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
