import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    Compiler,
    DependencyOnArtifact,
    DependencyUsageEnum,
    Implementation,
    ImplementationProps,
    Linker,
    ProgramminglanguageEnum,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport import McSupportData
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, CIdentifier, PositiveInteger, RefType, String


class TestImplementationProps:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that ImplementationProps abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="ImplementationProps is an abstract class."):
            ImplementationProps(ar_root, "TestImplementationProps")

    def test_concrete_subclass_can_be_instantiated(self):
        """Test that a concrete subclass of ImplementationProps can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementationProps(ImplementationProps):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl_props = ConcreteImplementationProps(ar_root, "TestImplementationProps")
        assert impl_props is not None
        assert impl_props.getShortName() == "TestImplementationProps"
        assert impl_props.symbol is None

    def test_get_symbol(self):
        """Test getSymbol method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementationProps(ImplementationProps):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl_props = ConcreteImplementationProps(ar_root, "TestImplementationProps")
        assert impl_props.getSymbol() is None

    def test_set_symbol(self):
        """Test setSymbol method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementationProps(ImplementationProps):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl_props = ConcreteImplementationProps(ar_root, "TestImplementationProps")
        test_value = CIdentifier().setValue("test_symbol")
        result = impl_props.setSymbol(test_value)
        assert result is impl_props  # Method chaining
        assert impl_props.getSymbol() == test_value


class TestCode:
    def test_initialization(self):
        """Test Code initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")

        assert code is not None
        assert code.getShortName() == "TestCode"
        assert code.artifactDescriptors == []
        assert code.callbackHeaderRefs == []

    def test_add_artifact_descriptor(self):
        """Test addArtifactDescriptor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")

        desc1 = AutosarEngineeringObject()
        desc2 = AutosarEngineeringObject()

        code.addArtifactDescriptor(desc1)
        code.addArtifactDescriptor(desc2)

        descriptors = code.getArtifactDescriptors()
        assert len(descriptors) == 2
        assert descriptors[0] == desc1
        assert descriptors[1] == desc2

    def test_get_artifact_descriptors_all(self):
        """Test getArtifactDescriptors method without category filter"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")

        desc1 = AutosarEngineeringObject()
        desc2 = AutosarEngineeringObject()

        code.addArtifactDescriptor(desc1)
        code.addArtifactDescriptor(desc2)

        descriptors = code.getArtifactDescriptors()
        assert len(descriptors) == 2
        assert descriptors[0] == desc1
        assert descriptors[1] == desc2

    def test_get_artifact_descriptors_by_category(self):
        """Test getArtifactDescriptors method with category filter"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")

        desc1 = AutosarEngineeringObject()
        desc1.setCategory(ARLiteral().setValue("SWC"))
        desc2 = AutosarEngineeringObject()
        desc2.setCategory(ARLiteral().setValue("BSW"))

        code.addArtifactDescriptor(desc1)
        code.addArtifactDescriptor(desc2)

        swc_descriptors = code.getArtifactDescriptors("SWC")
        assert len(swc_descriptors) == 1
        assert swc_descriptors[0] == desc1

        bsw_descriptors = code.getArtifactDescriptors("BSW")
        assert len(bsw_descriptors) == 1
        assert bsw_descriptors[0] == desc2

    def test_get_callback_header_refs(self):
        """Test getCallbackHeaderRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")
        assert code.getCallbackHeaderRefs() == []

    def test_add_callback_header_ref(self):
        """Test addCallbackHeaderRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")

        ref1 = RefType().setValue("/Foo/Callback.h")
        ref2 = RefType().setValue("/Foo/Other.h")
        result = code.addCallbackHeaderRef(ref1).addCallbackHeaderRef(ref2)
        assert result is code  # Method chaining
        assert code.getCallbackHeaderRefs() == [ref1, ref2]

    def test_add_callback_header_ref_none(self):
        """Test addCallbackHeaderRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        code = Code(ar_root, "TestCode")
        result = code.addCallbackHeaderRef(None)
        assert result is code  # Method chaining
        assert code.getCallbackHeaderRefs() == []


class TestCompiler:
    def test_initialization(self):
        """Test Compiler initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")

        assert compiler is not None
        assert compiler.getShortName() == "TestCompiler"
        assert compiler.name is None
        assert compiler.options is None
        assert compiler.vendor is None
        assert compiler.version is None

    def test_get_name(self):
        """Test getName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        assert compiler.getName() is None

    def test_set_name(self):
        """Test setName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        test_value = String().setValue("GCC")
        result = compiler.setName(test_value)
        assert result is compiler  # Method chaining
        assert compiler.getName() == test_value

    def test_get_options(self):
        """Test getOptions method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        assert compiler.getOptions() is None

    def test_set_options(self):
        """Test setOptions method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        test_value = String().setValue("-O2 -Wall")
        result = compiler.setOptions(test_value)
        assert result is compiler  # Method chaining
        assert compiler.getOptions() == test_value

    def test_get_vendor(self):
        """Test getVendor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        assert compiler.getVendor() is None

    def test_set_vendor(self):
        """Test setVendor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        test_value = String().setValue("GNU")
        result = compiler.setVendor(test_value)
        assert result is compiler  # Method chaining
        assert compiler.getVendor() == test_value

    def test_get_version(self):
        """Test getVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        assert compiler.getVersion() is None

    def test_set_version(self):
        """Test setVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")
        test_value = String().setValue("11.2.0")
        result = compiler.setVersion(test_value)
        assert result is compiler  # Method chaining
        assert compiler.getVersion() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        compiler = Compiler(ar_root, "TestCompiler")

        name = String().setValue("GCC")
        options = String().setValue("-O2 -Wall")
        vendor = String().setValue("GNU")
        version = String().setValue("11.2.0")

        compiler.setName(name)
        compiler.setOptions(options)
        compiler.setVendor(vendor)
        compiler.setVersion(version)

        assert compiler.getName() == name
        assert compiler.getOptions() == options
        assert compiler.getVendor() == vendor
        assert compiler.getVersion() == version


class TestDependencyOnArtifact:
    def test_initialization(self):
        """Test DependencyOnArtifact initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")

        assert dependency is not None
        assert dependency.getShortName() == "TestDependency"
        assert dependency.artifactDescriptor is None
        assert dependency.usages == []

    def test_get_artifact_descriptor(self):
        """Test getArtifactDescriptor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")
        assert dependency.getArtifactDescriptor() is None

    def test_set_artifact_descriptor(self):
        """Test setArtifactDescriptor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")
        test_value = AutosarEngineeringObject()
        result = dependency.setArtifactDescriptor(test_value)
        assert result is dependency  # Method chaining
        assert dependency.getArtifactDescriptor() == test_value

    def test_get_usages(self):
        """Test getUsages method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")
        assert dependency.getUsages() == []

    def test_add_usage(self):
        """Test addUsage method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")

        test_value = DependencyUsageEnum().setValue(DependencyUsageEnum.BUILD)
        result = dependency.addUsage(test_value)
        assert result is dependency  # Method chaining
        assert dependency.getUsages() == [test_value]

    def test_add_usage_none(self):
        """Test addUsage with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")

        result = dependency.addUsage(None)
        assert result is dependency  # Method chaining
        assert dependency.getUsages() == []


class TestImplementation:
    def test_abstract_class_cannot_be_instantiated(self):
        """Test that Implementation abstract class cannot be instantiated directly"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        with pytest.raises(TypeError, match="Implementation is an abstract class."):
            Implementation(ar_root, "TestImplementation")

    def test_concrete_subclass_initialization(self):
        """Test that a concrete subclass of Implementation can be instantiated"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl is not None
        assert impl.getShortName() == "TestImplementation"
        assert impl.buildActionManifestRef is None
        assert impl.codeDescriptors == []
        assert impl.compilers == []
        assert impl.generatedArtifacts == []
        assert impl.hwElementRefs == []
        assert impl.linkers == []
        assert impl.mcSupport is None
        assert impl.programmingLanguage is None
        assert impl.requiredArtifacts == []
        assert impl.requiredGeneratorTools == []
        assert impl.resourceConsumption is None
        assert impl.swcBswMappingRef is None
        assert impl.swVersion is None
        assert impl.usedCodeGenerator is None
        assert impl.vendorId is None

    def test_get_build_action_manifest_ref(self):
        """Test getBuildActionManifestRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getBuildActionManifestRef() is None

    def test_set_build_action_manifest_ref(self):
        """Test setBuildActionManifestRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = RefType().setValue("BuildManifest")
        result = impl.setBuildActionManifestRef(test_value)
        assert result is impl  # Method chaining
        assert impl.getBuildActionManifestRef() == test_value

    def test_get_code_descriptors_empty(self):
        """Test getCodeDescriptors method with empty list"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        code_descs = impl.getCodeDescriptors()
        assert code_descs == []

    def test_create_code_descriptor(self):
        """Test createCodeDescriptor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        code_desc = impl.createCodeDescriptor("TestCode")

        assert code_desc is not None
        assert code_desc.getShortName() == "TestCode"
        assert len(impl.codeDescriptors) == 1
        assert impl.codeDescriptors[0] == code_desc
        assert code_desc in impl.getCodeDescriptors()

    def test_get_compilers(self):
        """Test getCompilers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getCompilers() == []

    def test_create_compiler(self):
        """Test createCompiler method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        compiler = impl.createCompiler("Compiler1")

        assert compiler is not None
        assert compiler.getShortName() == "Compiler1"
        assert len(impl.compilers) == 1
        assert impl.compilers[0] == compiler

    def test_get_generated_artifacts(self):
        """Test getGeneratedArtifacts method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getGeneratedArtifacts() == []

    def test_create_generated_artifact(self):
        """Test createGeneratedArtifact method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact = impl.createGeneratedArtifact("Artifact1")

        assert artifact is not None
        assert artifact.getShortName() == "Artifact1"
        assert len(impl.generatedArtifacts) == 1
        assert impl.generatedArtifacts[0] == artifact

    def test_get_hw_element_refs(self):
        """Test getHwElementRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getHwElementRefs() == []

    def test_add_hw_element_ref(self):
        """Test addHwElementRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        ref1 = RefType().setValue("HwElement1")
        ref2 = RefType().setValue("HwElement2")
        result = impl.addHwElementRef(ref1).addHwElementRef(ref2)
        assert result is impl  # Method chaining
        assert impl.getHwElementRefs() == [ref1, ref2]

    def test_add_hw_element_ref_none(self):
        """Test addHwElementRef with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        result = impl.addHwElementRef(None)
        assert result is impl  # Method chaining
        assert impl.getHwElementRefs() == []

    def test_get_linkers(self):
        """Test getLinkers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getLinkers() == []

    def test_create_linker(self):
        """Test createLinker method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        linker = impl.createLinker("Linker1")

        assert linker is not None
        assert linker.getShortName() == "Linker1"
        assert len(impl.linkers) == 1
        assert impl.linkers[0] == linker

    def test_get_mc_support(self):
        """Test getMcSupport method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getMcSupport() is None

    def test_set_mc_support(self):
        """Test setMcSupport method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = McSupportData()
        result = impl.setMcSupport(test_value)
        assert result is impl  # Method chaining
        assert impl.getMcSupport() == test_value

    def test_set_mc_support_none(self):
        """Test setMcSupport with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        result = impl.setMcSupport(None)
        assert result is impl  # Method chaining
        assert impl.getMcSupport() is None

    def test_get_programming_language(self):
        """Test getProgrammingLanguage method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getProgrammingLanguage() is None

    def test_set_programming_language(self):
        """Test setProgrammingLanguage method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")

        test_value = ProgramminglanguageEnum().setValue(ProgramminglanguageEnum.C)
        result = impl.setProgrammingLanguage(test_value)
        assert result is impl  # Method chaining
        assert impl.getProgrammingLanguage() == test_value

    def test_set_programming_language_none(self):
        """Test setProgrammingLanguage with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        result = impl.setProgrammingLanguage(None)
        assert result is impl  # Method chaining
        assert impl.getProgrammingLanguage() is None

    def test_get_required_artifacts(self):
        """Test getRequiredArtifacts method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getRequiredArtifacts() == []

    def test_create_required_artifact(self):
        """Test createRequiredArtifact method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact = impl.createRequiredArtifact("Artifact1")

        assert artifact is not None
        assert artifact.getShortName() == "Artifact1"
        assert len(impl.requiredArtifacts) == 1
        assert impl.requiredArtifacts[0] == artifact

    def test_get_required_generator_tools(self):
        """Test getRequiredGeneratorTools method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getRequiredGeneratorTools() == []

    def test_create_required_generator_tool(self):
        """Test createRequiredGeneratorTool method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact = impl.createRequiredGeneratorTool("Tool1")

        assert artifact is not None
        assert artifact.getShortName() == "Tool1"
        assert len(impl.requiredGeneratorTools) == 1
        assert impl.requiredGeneratorTools[0] == artifact

    def test_get_resource_consumption(self):
        """Test getResourceConsumption method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getResourceConsumption() is None

    def test_create_resource_consumption(self):
        """Test createResourceConsumption method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        resource = impl.createResourceConsumption("TestResource")

        assert resource is not None
        assert resource.getShortName() == "TestResource"
        assert impl.resourceConsumption == resource

    def test_get_swc_bsw_mapping_ref(self):
        """Test getSwcBswMappingRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getSwcBswMappingRef() is None

    def test_set_swc_bsw_mapping_ref(self):
        """Test setSwcBswMappingRef method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = RefType().setValue("SwcBswMapping")
        result = impl.setSwcBswMappingRef(test_value)
        assert result is impl  # Method chaining
        assert impl.getSwcBswMappingRef() == test_value

    def test_get_sw_version(self):
        """Test getSwVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getSwVersion() is None

    def test_set_sw_version(self):
        """Test setSwVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = ARLiteral().setValue("1.0.0")
        result = impl.setSwVersion(test_value)
        assert result is impl  # Method chaining
        assert impl.getSwVersion() == test_value

    def test_set_sw_version_none(self):
        """Test setSwVersion with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = ARLiteral().setValue("1.0.0")
        impl.setSwVersion(test_value)
        result = impl.setSwVersion(None)
        assert result is impl  # Method chaining
        assert impl.getSwVersion() == test_value

    def test_get_used_code_generator(self):
        """Test getUsedCodeGenerator method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getUsedCodeGenerator() is None

    def test_set_used_code_generator(self):
        """Test setUsedCodeGenerator method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = String().setValue("CodeGenerator")
        result = impl.setUsedCodeGenerator(test_value)
        assert result is impl  # Method chaining
        assert impl.getUsedCodeGenerator() == test_value

    def test_get_vendor_id(self):
        """Test getVendorId method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getVendorId() is None

    def test_set_vendor_id(self):
        """Test setVendorId method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = PositiveInteger().setValue(12345)
        result = impl.setVendorId(test_value)
        assert result is impl  # Method chaining
        assert impl.getVendorId() == test_value

    def test_set_vendor_id_none(self):
        """Test setVendorId with None value (no-op)"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        test_value = PositiveInteger().setValue(12345)
        impl.setVendorId(test_value)
        result = impl.setVendorId(None)
        assert result is impl  # Method chaining
        assert impl.getVendorId() == test_value


class TestLinker:
    def test_initialization(self):
        """Test Linker initialization"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")

        assert linker is not None
        assert linker.getShortName() == "TestLinker"
        assert linker.name is None
        assert linker.options is None
        assert linker.vendor is None
        assert linker.version is None

    def test_get_name(self):
        """Test getName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        assert linker.getName() is None

    def test_set_name(self):
        """Test setName method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        test_value = String().setValue("GCC")
        result = linker.setName(test_value)
        assert result is linker  # Method chaining
        assert linker.getName() == test_value

    def test_get_options(self):
        """Test getOptions method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        assert linker.getOptions() is None

    def test_set_options(self):
        """Test setOptions method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        test_value = String().setValue("-Wl,--gc-sections")
        result = linker.setOptions(test_value)
        assert result is linker  # Method chaining
        assert linker.getOptions() == test_value

    def test_get_vendor(self):
        """Test getVendor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        assert linker.getVendor() is None

    def test_set_vendor(self):
        """Test setVendor method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        test_value = String().setValue("GNU")
        result = linker.setVendor(test_value)
        assert result is linker  # Method chaining
        assert linker.getVendor() == test_value

    def test_get_version(self):
        """Test getVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        assert linker.getVersion() is None

    def test_set_version(self):
        """Test setVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")
        test_value = String().setValue("11.2.0")
        result = linker.setVersion(test_value)
        assert result is linker  # Method chaining
        assert linker.getVersion() == test_value

    def test_all_properties(self):
        """Test setting all properties"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        linker = Linker(ar_root, "TestLinker")

        name = String().setValue("GCC")
        options = String().setValue("-Wl,--gc-sections")
        vendor = String().setValue("GNU")
        version = String().setValue("11.2.0")

        linker.setName(name)
        linker.setOptions(options)
        linker.setVendor(vendor)
        linker.setVersion(version)

        assert linker.getName() == name
        assert linker.getOptions() == options
        assert linker.getVendor() == vendor
        assert linker.getVersion() == version


class TestDependencyUsageEnum:
    def test_literals(self):
        """Test DependencyUsageEnum literal values per AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Table 7.4"""
        assert DependencyUsageEnum.BUILD == "build"
        assert DependencyUsageEnum.CODEGENERATION == "codegeneration"
        assert DependencyUsageEnum.COMPILE == "compile"
        assert DependencyUsageEnum.EXECUTE == "execute"
        assert DependencyUsageEnum.LINK == "link"

    def test_enum_values(self):
        """Test the valid enum value set"""
        enum = DependencyUsageEnum()
        assert set(enum.getEnumValues()) == {"build", "codegeneration", "compile", "execute", "link"}


class TestProgramminglanguageEnum:
    def test_literals(self):
        """Test ProgramminglanguageEnum literal values per AUTOSAR_CP_TPS_SoftwareComponentTemplate Table 8.2"""
        assert ProgramminglanguageEnum.C == "c"
        assert ProgramminglanguageEnum.CPP == "cpp"
        assert ProgramminglanguageEnum.JAVA == "java"

    def test_enum_values(self):
        """Test the valid enum value set in spec literal order (Table 8.2)"""
        enum = ProgramminglanguageEnum()
        assert enum.getEnumValues() == (
            ProgramminglanguageEnum.C,
            ProgramminglanguageEnum.CPP,
            ProgramminglanguageEnum.JAVA,
        )

    def test_instantiation_set_value(self):
        """Test enum instantiability and setValue/getValue round-trip per Rule 0011"""
        enum = ProgramminglanguageEnum()
        result = enum.setValue(ProgramminglanguageEnum.CPP)
        assert result is enum  # Method chaining
        assert enum.getValue() == "cpp"

    def test_spec_note(self):
        """Test the Table 8.2 class note."""
        assert ProgramminglanguageEnum.__doc__.strip() == "Programming language the implementation was created in."
