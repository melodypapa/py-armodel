import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    Compiler,
    DependencyOnArtifact,
    Implementation,
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveInteger,
    RefType,
    String,
)


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
        test_value = ARLiteral().setValue("test_symbol")
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
        assert dependency.usage is None

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

    def test_get_usage(self):
        """Test getUsage method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")
        assert dependency.getUsage() is None

    def test_set_usage(self):
        """Test setUsage method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        dependency = DependencyOnArtifact(ar_root, "TestDependency")
        # Create a mock usage enum for testing
        class MockUsageEnum:
            pass
        test_value = MockUsageEnum()
        result = dependency.setUsage(test_value)
        assert result is dependency  # Method chaining
        assert dependency.getUsage() == test_value


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
        assert impl.swVersion == []
        assert impl.usedCodeGenerator is None
        assert impl.vendorId == 0

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

    def test_set_compilers(self):
        """Test setCompilers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        compiler1 = Compiler(ar_root, "Compiler1")
        compiler2 = Compiler(ar_root, "Compiler2")
        test_value = [compiler1, compiler2]
        result = impl.setCompilers(test_value)
        assert result is impl  # Method chaining
        assert impl.getCompilers() == test_value

    def test_set_compilers_none(self):
        """Test setCompilers with None value"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        result = impl.setCompilers(None)
        assert result is impl  # Method chaining
        assert impl.getCompilers() is None

    def test_get_generated_artifacts(self):
        """Test getGeneratedArtifacts method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getGeneratedArtifacts() == []

    def test_set_generated_artifacts(self):
        """Test setGeneratedArtifacts method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact1 = DependencyOnArtifact(ar_root, "Artifact1")
        artifact2 = DependencyOnArtifact(ar_root, "Artifact2")
        test_value = [artifact1, artifact2]
        result = impl.setGeneratedArtifacts(test_value)
        assert result is impl  # Method chaining
        assert impl.getGeneratedArtifacts() == test_value

    def test_get_hw_element_refs(self):
        """Test getHwElementRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getHwElementRefs() == []

    def test_set_hw_element_refs(self):
        """Test setHwElementRefs method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        ref1 = RefType().setValue("HwElement1")
        ref2 = RefType().setValue("HwElement2")
        test_value = [ref1, ref2]
        result = impl.setHwElementRefs(test_value)
        assert result is impl  # Method chaining
        assert impl.getHwElementRefs() == test_value

    def test_get_linkers(self):
        """Test getLinkers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getLinkers() == []

    def test_set_linkers(self):
        """Test setLinkers method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        # Create a mock linker for testing (since Linker class is not defined in the file)
        class MockLinker:
            def __init__(self, parent, short_name):
                self.parent = parent
                self.short_name = short_name
        linker1 = MockLinker(ar_root, "Linker1")
        linker2 = MockLinker(ar_root, "Linker2")
        test_value = [linker1, linker2]
        result = impl.setLinkers(test_value)
        assert result is impl  # Method chaining
        assert impl.getLinkers() == test_value

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
        test_value = "Microcontroller Support Info"
        result = impl.setMcSupport(test_value)
        assert result is impl  # Method chaining
        assert impl.getMcSupport() == test_value

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
        # Create a mock programming language enum for testing
        class MockProgrammingLanguageEnum:
            pass
        test_value = MockProgrammingLanguageEnum()
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

    def test_set_required_artifacts(self):
        """Test setRequiredArtifacts method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact1 = DependencyOnArtifact(ar_root, "Artifact1")
        artifact2 = DependencyOnArtifact(ar_root, "Artifact2")
        test_value = [artifact1, artifact2]
        result = impl.setRequiredArtifacts(test_value)
        assert result is impl  # Method chaining
        assert impl.getRequiredArtifacts() == test_value

    def test_get_required_generator_tools(self):
        """Test getRequiredGeneratorTools method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        assert impl.getRequiredGeneratorTools() == []

    def test_set_required_generator_tools(self):
        """Test setRequiredGeneratorTools method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        artifact1 = DependencyOnArtifact(ar_root, "Tool1")
        artifact2 = DependencyOnArtifact(ar_root, "Tool2")
        test_value = [artifact1, artifact2]
        result = impl.setRequiredGeneratorTools(test_value)
        assert result is impl  # Method chaining
        assert impl.getRequiredGeneratorTools() == test_value

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
        assert impl.getSwVersion() == []

    def test_set_sw_version(self):
        """Test setSwVersion method"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")

        class ConcreteImplementation(Implementation):
            def __init__(self, parent, short_name):
                super().__init__(parent, short_name)

        impl = ConcreteImplementation(ar_root, "TestImplementation")
        # Create a mock version string for testing
        test_value = ["1.0.0", "1.0.1"]
        result = impl.setSwVersion(test_value)
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
        assert impl.getVendorId() == 0

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
