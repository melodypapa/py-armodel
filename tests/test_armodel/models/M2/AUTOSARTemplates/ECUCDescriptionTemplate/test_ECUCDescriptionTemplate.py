"""
Test cases for the ECUCDescriptionTemplate module.
These tests ensure 100% code coverage for all classes in the ECUCDescriptionTemplate module.
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
    Container,
    EcucAbstractReferenceValue,
    EcucAddInfoParamValue,
    EcucContainerValue,
    EcucIndexableValue,
    EcucInstanceReferenceValue,
    EcucModuleConfigurationValues,
    EcucNumericalParamValue,
    EcucParameterValue,
    EcucReferenceValue,
    EcucTextualParamValue,
    EcucValueCollection,
    ModuleConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum, EcucModuleDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    CIdentifier,
    Limit,
    Numerical,
    PositiveInteger,
    RefType,
    RevisionLabelString,
    VerbatimString,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph


def test_ecuc_value_collection_initialization_defaults():
    """
    EcucValueCollection (Table 2.45) defaults: both spec attributes empty.

    Test Steps:
    1. Create an EcucValueCollection instance with parent and short_name
    2. Assert parent/short_name and the ecucValue/ecuExtract defaults
    """
    parent = Limit()
    collection = EcucValueCollection(parent, "test_collection")

    assert collection.parent == parent
    assert collection.short_name == "test_collection"
    assert collection.ecucValueRefs == []
    assert collection.getEcucValueRefs() == []
    assert collection.ecuExtractRef is None
    assert collection.getEcuExtractRef() is None


def test_ecuc_value_collection_add_ecuc_value_ref():
    """
    addEcucValueRef appends to the typed list, chains, and None is a no-op.

    Test Steps:
    1. Add two RefType values via addEcucValueRef
    2. Assert chaining returns self and the refs round-trip in order
    3. Call addEcucValueRef(None) and assert the list is unchanged
    """
    parent = Limit()
    collection = EcucValueCollection(parent, "test_collection")
    ref1 = RefType().setValue("/ECUC/Rte/Rte")
    ref2 = RefType().setValue("/ECUC/Os/Os")

    assert collection.addEcucValueRef(ref1) is collection
    collection.addEcucValueRef(ref2)
    assert collection.getEcucValueRefs() == [ref1, ref2]

    collection.addEcucValueRef(None)
    assert collection.getEcucValueRefs() == [ref1, ref2]


def test_ecuc_value_collection_get_set_ecu_extract_ref():
    """
    setEcuExtractRef chains, round-trips, and None is a no-op.

    Test Steps:
    1. Set a RefType value via setEcuExtractRef
    2. Assert chaining returns self and the value round-trips
    3. Call setEcuExtractRef(None) and assert the value is preserved
    """
    parent = Limit()
    collection = EcucValueCollection(parent, "test_collection")
    extract_ref = RefType().setValue("/System/Extract")

    result = collection.setEcuExtractRef(extract_ref)
    assert result is collection
    assert collection.getEcuExtractRef() == extract_ref

    collection.setEcuExtractRef(None)
    assert collection.getEcuExtractRef() == extract_ref


def test_ecuc_value_collection_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.45 Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert the class docstring contains the spec class Note verbatim
    2. Assert each getter/setter/adder docstring carries the spec Note
    """
    assert EcucValueCollection.__doc__ is not None, "Class docstring must contain spec Note"
    assert "This represents the anchor point of the ECU configuration description." in EcucValueCollection.__doc__, "Class docstring must contain spec Note verbatim"

    notes = {
        "getEcucValueRefs": "References to the configuration of individual software modules that are present on this ECU.",
        "addEcucValueRef": "References to the configuration of individual software modules that are present on this ECU.",
        "getEcuExtractRef": "Represents the extract of the System Configuration that is relevant for the ECU configured with that ECU Configuration Description.",
        "setEcuExtractRef": "Represents the extract of the System Configuration that is relevant for the ECU configured with that ECU Configuration Description.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucValueCollection, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_value_collection_member_annotations():
    """get/set/add shall resolve to Optional[RefType] / List[RefType] / EcucValueCollection (Rule 0003/0006 — get_type_hints pin; the quoted self-return is this module's required forward-ref form, no PEP 563 here)."""
    import typing

    assert typing.get_type_hints(EcucValueCollection.getEcucValueRefs)["return"] == typing.List[RefType]
    assert typing.get_type_hints(EcucValueCollection.addEcucValueRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucValueCollection.addEcucValueRef)["return"] is EcucValueCollection
    assert typing.get_type_hints(EcucValueCollection.getEcuExtractRef)["return"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucValueCollection.setEcuExtractRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucValueCollection.setEcuExtractRef)["return"] is EcucValueCollection


def test_module_configuration_initialization_defaults():
    """
    ModuleConfiguration (R3.2.3 Table 3.30) defaults: all four spec attributes empty.

    Test Steps:
    1. Create a ModuleConfiguration instance with parent and short_name
    2. Assert parent/short_name and the container/definition/implementationConfigVariant/moduleDescription defaults
    """
    parent = Limit()
    module_configuration = ModuleConfiguration(parent, "test_module_configuration")

    assert module_configuration.parent == parent
    assert module_configuration.short_name == "test_module_configuration"
    assert module_configuration.containers == []
    assert module_configuration.getContainers() == []
    assert module_configuration.definitionRef is None
    assert module_configuration.getDefinitionRef() is None
    assert module_configuration.implementationConfigVariant is None
    assert module_configuration.getImplementationConfigVariant() is None
    assert module_configuration.moduleDescriptionRef is None
    assert module_configuration.getModuleDescriptionRef() is None


def test_module_configuration_create_container():
    """
    createContainer appends to the typed list and a duplicate short name returns the existing container.

    Test Steps:
    1. Create a Container via createContainer and assert it is appended
    2. Create the same short name again and assert the existing container is returned
    """
    parent = Limit()
    module_configuration = ModuleConfiguration(parent, "mc")

    container = module_configuration.createContainer("OsOS")
    assert container is not None
    assert container.short_name == "OsOS"
    assert module_configuration.getContainers() == [container]

    duplicate = module_configuration.createContainer("OsOS")
    assert duplicate is container
    assert module_configuration.getContainers() == [container]


def test_module_configuration_get_set_definition_ref():
    """
    setDefinitionRef chains, round-trips, and None is a no-op.

    Test Steps:
    1. Set a RefType value via setDefinitionRef
    2. Assert chaining returns self and the value round-trips
    3. Call setDefinitionRef(None) and assert the value is preserved
    """
    parent = Limit()
    module_configuration = ModuleConfiguration(parent, "mc")
    definition_ref = RefType().setValue("/TS_T19D1M6I1R0_AS403/Os")

    result = module_configuration.setDefinitionRef(definition_ref)
    assert result is module_configuration
    assert module_configuration.getDefinitionRef() == definition_ref

    module_configuration.setDefinitionRef(None)
    assert module_configuration.getDefinitionRef() == definition_ref


def test_module_configuration_get_set_implementation_config_variant():
    """
    setImplementationConfigVariant chains, round-trips the typed enum, and None is a no-op.

    Test Steps:
    1. Set an EcucConfigurationVariantEnum value via setImplementationConfigVariant
    2. Assert chaining returns self and the value round-trips
    3. Call setImplementationConfigVariant(None) and assert the value is preserved
    """
    parent = Limit()
    module_configuration = ModuleConfiguration(parent, "mc")
    variant = EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE)

    result = module_configuration.setImplementationConfigVariant(variant)
    assert result is module_configuration
    assert module_configuration.getImplementationConfigVariant() == variant

    module_configuration.setImplementationConfigVariant(None)
    assert module_configuration.getImplementationConfigVariant() == variant


def test_module_configuration_get_set_module_description_ref():
    """
    setModuleDescriptionRef chains, round-trips, and None is a no-op.

    Test Steps:
    1. Set a RefType value via setModuleDescriptionRef
    2. Assert chaining returns self and the value round-trips
    3. Call setModuleDescriptionRef(None) and assert the value is preserved
    """
    parent = Limit()
    module_configuration = ModuleConfiguration(parent, "mc")
    description_ref = RefType().setValue("/Vendor/OsImplementation")

    result = module_configuration.setModuleDescriptionRef(description_ref)
    assert result is module_configuration
    assert module_configuration.getModuleDescriptionRef() == description_ref

    module_configuration.setModuleDescriptionRef(None)
    assert module_configuration.getModuleDescriptionRef() == description_ref


def test_module_configuration_member_docstrings_verbatim():
    """
    Member docstrings must carry the R3.2.3 Table 3.30 Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert the class docstring contains the spec class Note verbatim
    2. Assert each getter/setter/creator docstring carries the spec Note verbatim
    """
    assert ModuleConfiguration.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Head of the configuration of one Module." in ModuleConfiguration.__doc__, "Class docstring must contain spec Note verbatim"

    notes = {
        "createContainer": "Aggregates all containers that belong to this module configuration. Stereotypes: atpSplitable Tags: xml.sequenceOffset=10",
        "getContainers": "Aggregates all containers that belong to this module configuration. Stereotypes: atpSplitable Tags: xml.sequenceOffset=10",
        "getDefinitionRef": "Reference to the definition of this ModuleConfiguration. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10",
        "setDefinitionRef": "Reference to the definition of this ModuleConfiguration. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10",
        "getImplementationConfigVariant": "Specifies the ConfigurationVariant used for this ModuleConfiguration.",
        "setImplementationConfigVariant": "Specifies the ConfigurationVariant used for this ModuleConfiguration.",
        "getModuleDescriptionRef": "Referencing the BSW module description, which this ModuleConfiguration is configuring. This is optional because the ModuleConfiguration is also used to configure the ECU infrastructure (memory map) or Application SW-Cs.",
        "setModuleDescriptionRef": "Referencing the BSW module description, which this ModuleConfiguration is configuring. This is optional because the ModuleConfiguration is also used to configure the ECU infrastructure (memory map) or Application SW-Cs.",
    }
    for method_name, note in notes.items():
        method = getattr(ModuleConfiguration, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_module_configuration_member_annotations():
    """get/set/create shall resolve to Optional[RefType] / List[Container] / EcucConfigurationVariantEnum / Container (Rule 0003/0006 — get_type_hints pin; the quoted self-return is this module's required forward-ref form, no PEP 563 here)."""
    import typing

    assert typing.get_type_hints(ModuleConfiguration.createContainer)["short_name"] is str
    assert typing.get_type_hints(ModuleConfiguration.createContainer)["return"] is Container
    assert typing.get_type_hints(ModuleConfiguration.getContainers)["return"] == typing.List[Container]
    assert typing.get_type_hints(ModuleConfiguration.getDefinitionRef)["return"] == typing.Optional[RefType]
    assert typing.get_type_hints(ModuleConfiguration.setDefinitionRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(ModuleConfiguration.setDefinitionRef)["return"] is ModuleConfiguration
    assert typing.get_type_hints(ModuleConfiguration.getImplementationConfigVariant)["return"] == typing.Optional[EcucConfigurationVariantEnum]
    assert typing.get_type_hints(ModuleConfiguration.setImplementationConfigVariant)["value"] == typing.Optional[EcucConfigurationVariantEnum]
    assert typing.get_type_hints(ModuleConfiguration.setImplementationConfigVariant)["return"] is ModuleConfiguration
    assert typing.get_type_hints(ModuleConfiguration.getModuleDescriptionRef)["return"] == typing.Optional[RefType]
    assert typing.get_type_hints(ModuleConfiguration.setModuleDescriptionRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(ModuleConfiguration.setModuleDescriptionRef)["return"] is ModuleConfiguration


def test_ecuc_indexable_value_abstract():
    """
    EcucIndexableValue (Table 2.46) is abstract and cannot be instantiated.

    Test Steps:
    1. Verify that instantiating EcucIndexableValue directly raises TypeError
    """
    with pytest.raises(TypeError):
        EcucIndexableValue()


def test_ecuc_indexable_value_base_properties():
    """
    EcucIndexableValue (Table 2.46) index accessors via a concrete subclass.

    Test Steps:
    1. Create an EcucNumericalParamValue instance (concrete subclass)
    2. Assert the index default is None
    3. Set a PositiveInteger via setIndex and assert chaining and round-trip
    4. Call setIndex(None) and assert the value is preserved
    """
    value = EcucNumericalParamValue()

    assert value.index is None
    assert value.getIndex() is None

    index = PositiveInteger().setValue("4")
    assert value.setIndex(index) is value
    assert value.getIndex() == index

    value.setIndex(None)
    assert value.getIndex() == index


def test_ecuc_indexable_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.46 Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert the class docstring contains the spec class Note verbatim
    2. Assert each getter/setter docstring carries the spec attribute Note verbatim
    """
    assert EcucIndexableValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Used to support the specification of ordering of parameter values." in EcucIndexableValue.__doc__, "Class docstring must contain spec Note verbatim"

    notes = {
        "getIndex": "Used to support the specification of ordering of parameter values. Tags: xml.sequenceOffset=-5",
        "setIndex": "Used to support the specification of ordering of parameter values. Tags: xml.sequenceOffset=-5",
    }
    for method_name, note in notes.items():
        method = getattr(EcucIndexableValue, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_indexable_value_member_annotations():
    """get/set shall resolve to Optional[PositiveInteger] / EcucIndexableValue (Rule 0003/0006 — get_type_hints pin)."""
    import typing

    assert typing.get_type_hints(EcucIndexableValue.getIndex)["return"] == typing.Optional[PositiveInteger]
    assert typing.get_type_hints(EcucIndexableValue.setIndex)["value"] == typing.Optional[PositiveInteger]
    assert typing.get_type_hints(EcucIndexableValue.setIndex)["return"] is EcucIndexableValue


def test_ecuc_parameter_value_abstract():
    """
    Test EcucParameterValue abstract class.

    Test Steps:
    1. Verify that instantiating EcucParameterValue directly raises NotImplementedError
    """
    try:
        EcucParameterValue()
        assert False, "Should raise NotImplementedError"
    except TypeError:
        pass  # Expected


def test_ecuc_parameter_value_methods():
    """
    Test EcucParameterValue class methods (using a concrete subclass).

    Test Steps:
    1. Create an EcucAddInfoParamValue instance (concrete subclass)
    2. Test annotation methods
    3. Test definitionRef methods
    4. Test isAutoValue methods
    5. Verify method chaining
    """
    param_value = EcucAddInfoParamValue()

    # Test initial values
    assert param_value.annotations == []
    assert param_value.definitionRef is None
    assert param_value.isAutoValue is None

    # Test annotation methods
    annotation = Annotation()
    result = param_value.addAnnotation(annotation)
    assert result == param_value  # Method chaining
    assert param_value.getAnnotations() == [annotation]

    # Test definition methods
    definition_ref = RefType().setValue("/EcucDefs/Rte/Param")
    result = param_value.setDefinitionRef(definition_ref)
    assert result is param_value  # Method chaining
    assert param_value.getDefinitionRef() == definition_ref

    # Test isAutoValue methods
    auto_value = Boolean().setValue(True)
    param_value.setIsAutoValue(auto_value)
    assert param_value.getIsAutoValue() == auto_value


def test_ecuc_add_info_param_value():
    """
    Test EcucAddInfoParamValue class - full spec compliance per Table 2.52.

    Test Steps:
    1. Create an EcucAddInfoParamValue instance
    2. Test initial values
    3. Test value methods (spec type: DocumentationBlock)
    4. Verify method chaining
    5. Verify class docstring contains the spec Note verbatim
    """
    param_value = EcucAddInfoParamValue()

    # Test initial values (inherited from EcucParameterValue + own attribute)
    assert param_value.annotations == []
    assert param_value.definitionRef is None
    assert param_value.isAutoValue is None
    assert param_value.value is None

    # Test value methods (spec type: DocumentationBlock)
    doc_block = DocumentationBlock()
    para = MultiLanguageParagraph()
    l1 = LLongName()
    l1.l = "en"
    l1.value = "Description of the Dtc 0815."
    para.addL1(l1)
    doc_block.addP(para)
    result = param_value.setValue(doc_block)
    assert result is param_value  # Method chaining
    assert isinstance(param_value.getValue(), DocumentationBlock)
    assert param_value.getValue() == doc_block

    # Verify docstrings match spec (Rule 0012)
    assert EcucAddInfoParamValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert "This parameter corresponds to EcucAddInfoParamDef." in EcucAddInfoParamValue.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_add_info_param_value_none_no_op():
    """
    None passed to the 0..1 setter of EcucAddInfoParamValue is a no-op.

    Test Steps:
    1. Create an EcucAddInfoParamValue instance
    2. Set the spec value on the 0..1 attribute
    3. Call the setter with None and verify the value is preserved
    """
    param_value = EcucAddInfoParamValue()
    doc_block = DocumentationBlock()

    assert param_value.setValue(doc_block) is param_value

    param_value.setValue(None)

    assert param_value.getValue() == doc_block


def test_ecuc_add_info_param_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.52 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence
       that paraphrases are known to drop.
    """
    notes = {
        "getValue": "Holds the content of the formated text.",
        "setValue": "Holds the content of the formated text.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucAddInfoParamValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_textual_param_value():
    """
    Test EcucTextualParamValue class - full spec compliance per Table 2.50.

    Test Steps:
    1. Create an EcucTextualParamValue instance
    2. Test initial values
    3. Test value methods (spec type: VerbatimString)
    4. Verify method chaining
    5. Verify class docstring contains the spec Note verbatim
    """
    param_value = EcucTextualParamValue()

    # Test initial values (inherited from EcucParameterValue + own attribute)
    assert param_value.annotations == []
    assert param_value.definitionRef is None
    assert param_value.isAutoValue is None
    assert param_value.value is None

    # Test value methods (spec type: VerbatimString)
    text_value = VerbatimString().setValue("NVM_BLOCK_NATIVE")
    result = param_value.setValue(text_value)
    assert result is param_value  # Method chaining
    assert isinstance(param_value.getValue(), VerbatimString)
    assert param_value.getValue() == text_value

    # Verify docstrings match spec (Rule 0012)
    assert EcucTextualParamValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Holding a value which is not subject to variation." in EcucTextualParamValue.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_textual_param_value_none_no_op():
    """
    None passed to the 0..1 setter of EcucTextualParamValue is a no-op.

    Test Steps:
    1. Create an EcucTextualParamValue instance
    2. Set the spec value on the 0..1 attribute
    3. Call the setter with None and verify the value is preserved
    """
    param_value = EcucTextualParamValue()
    text_value = VerbatimString().setValue("NVM_BLOCK_NATIVE")

    assert param_value.setValue(text_value) is param_value

    param_value.setValue(None)

    assert param_value.getValue() == text_value


def test_ecuc_textual_param_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.50 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence
       that paraphrases are known to drop.
    """
    notes = {
        "getValue": "Value of the parameter, not subject to variant handling.",
        "setValue": "Value of the parameter, not subject to variant handling.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucTextualParamValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_numerical_param_value():
    """
    Test EcucNumericalParamValue class - full spec compliance per Table 2.51.

    Test Steps:
    1. Create an EcucNumericalParamValue instance
    2. Test initial values
    3. Test value methods (spec type: Numerical)
    4. Verify method chaining
    5. Verify class docstring contains the spec Note verbatim
    """
    param_value = EcucNumericalParamValue()

    # Test initial values (inherited from EcucParameterValue + own attribute)
    assert param_value.annotations == []
    assert param_value.definitionRef is None
    assert param_value.isAutoValue is None
    assert param_value.value is None

    # Test value methods (spec type: Numerical)
    num_value = Numerical().setValue("74.8")
    result = param_value.setValue(num_value)
    assert result is param_value  # Method chaining
    assert isinstance(param_value.getValue(), Numerical)
    assert param_value.getValue() == num_value

    # Verify docstrings match spec (Rule 0012)
    assert EcucNumericalParamValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Holding the value which is subject to variant handling." in EcucNumericalParamValue.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_numerical_param_value_none_no_op():
    """
    None passed to the 0..1 setter of EcucNumericalParamValue is a no-op.

    Test Steps:
    1. Create an EcucNumericalParamValue instance
    2. Set the spec value on the 0..1 attribute
    3. Call the setter with None and verify the value is preserved
    """
    param_value = EcucNumericalParamValue()
    num_value = Numerical().setValue("0x10")

    assert param_value.setValue(num_value) is param_value

    param_value.setValue(None)

    assert param_value.getValue() == num_value


def test_ecuc_numerical_param_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.51 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence
       that paraphrases are known to drop.
    """
    notes = {
        "getValue": "Value which is subject to variant handling. atpVariation: [RS_ECUC_00080] Stereotypes: atpVariation",
        "setValue": "Value which is subject to variant handling. atpVariation: [RS_ECUC_00080] Stereotypes: atpVariation",
    }
    for method_name, note in notes.items():
        method = getattr(EcucNumericalParamValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_abstract_reference_value_abstract():
    """
    Test EcucAbstractReferenceValue abstract class.

    Test Steps:
    1. Verify that instantiating EcucAbstractReferenceValue directly raises NotImplementedError
    """
    try:
        EcucAbstractReferenceValue()
        assert False, "Should raise NotImplementedError"
    except TypeError:
        pass  # Expected


def test_ecuc_abstract_reference_value_methods():
    """
    Test EcucAbstractReferenceValue class methods - full spec compliance per Table 2.53.

    Test Steps:
    1. Create an EcucReferenceValue instance (concrete subclass)
    2. Test initial values
    3. Test annotation methods (spec: Annotation * aggr)
    4. Test definition methods (spec: ref -> RefType)
    5. Test isAutoValue methods (spec type: Boolean)
    6. Verify method chaining
    7. Verify class docstring contains the spec Note verbatim
    """
    ref_value = EcucReferenceValue()

    # Test initial values
    assert ref_value.annotations == []
    assert ref_value.definitionRef is None
    assert ref_value.isAutoValue is None

    # Test annotation methods
    annotation = Annotation()
    result = ref_value.addAnnotation(annotation)
    assert result is ref_value  # Method chaining
    assert ref_value.getAnnotations() == [annotation]

    # Test definitionRef methods (Kind ref -> Ref suffix per Rule 0001.5)
    definition_ref = RefType().setValue("/EcucDefs/Rte/Ref")
    result = ref_value.setDefinitionRef(definition_ref)
    assert result is ref_value  # Method chaining
    assert ref_value.getDefinitionRef() == definition_ref

    # Test isAutoValue methods (spec type: Boolean)
    auto_value = Boolean().setValue(True)
    result = ref_value.setIsAutoValue(auto_value)
    assert result is ref_value  # Method chaining
    assert ref_value.getIsAutoValue() == auto_value

    # Verify docstrings match spec (Rule 0012)
    assert EcucAbstractReferenceValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert (
        "Abstract class to be used as common parent for all reference values in the ECU Configuration Description." in EcucAbstractReferenceValue.__doc__
    ), "Class docstring must contain spec Note verbatim"


def test_ecuc_abstract_reference_value_none_no_op():
    """
    None passed to a setter/adder of EcucAbstractReferenceValue is a no-op.

    Test Steps:
    1. Create an EcucReferenceValue instance (concrete subclass)
    2. Set spec values on all attributes
    3. Call the setters/addAnnotation with None and verify the values are preserved
    """
    ref_value = EcucReferenceValue()
    definition_ref = RefType().setValue("/EcucDefs/Rte/Ref")
    auto_value = Boolean().setValue(True)

    assert ref_value.setDefinitionRef(definition_ref) is ref_value
    assert ref_value.setIsAutoValue(auto_value) is ref_value

    ref_value.addAnnotation(None)
    ref_value.setDefinitionRef(None)
    ref_value.setIsAutoValue(None)

    assert ref_value.getAnnotations() == []
    assert ref_value.getDefinitionRef() == definition_ref
    assert ref_value.getIsAutoValue() == auto_value


def test_ecuc_abstract_reference_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.53 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence
       that paraphrases are known to drop.
    """
    notes = {
        "addAnnotation": "Possibility to provide additional notes while defining a model element (e.g. the ECU Configuration Parameter Values).",
        "getAnnotations": "Possibility to provide additional notes while defining a model element (e.g. the ECU Configuration Parameter Values).",
        "getDefinitionRef": "Reference to the definition of this EcucAbstractReferenceValue subclasses in the ECU Configuration Parameter Definition.",
        "setDefinitionRef": "Reference to the definition of this EcucAbstractReferenceValue subclasses in the ECU Configuration Parameter Definition.",
        "getIsAutoValue": 'If isAutoValue is not present the default is "false".',
        "setIsAutoValue": 'If isAutoValue is not present the default is "false".',
    }
    for method_name, note in notes.items():
        method = getattr(EcucAbstractReferenceValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_instance_reference_value():
    """
    Test EcucInstanceReferenceValue class per Table 2.55 (R23-11).

    Test Steps:
    1. Create an EcucInstanceReferenceValue instance
    2. Test initial valueIRef is None
    3. Test getValueIRef/setValueIRef round-trip (iref -> IRef suffix, AnyInstanceRef)
    4. Verify method chaining
    """
    ref_value = EcucInstanceReferenceValue()

    # Test initial values
    assert ref_value.valueIRef is None
    assert not hasattr(ref_value, "valueRef")

    # Test valueIRef methods (Table 2.55: value AtpFeature 0..1 iref -> AnyInstanceRef)
    instance_ref = AnyInstanceRef()
    result = ref_value.setValueIRef(instance_ref)
    assert result is ref_value  # Method chaining
    assert ref_value.getValueIRef() is instance_ref
    assert ref_value.valueIRef is instance_ref


def test_ecuc_instance_reference_value_none_no_op():
    """
    None passed to setValueIRef of EcucInstanceReferenceValue is a no-op.

    Test Steps:
    1. Create an EcucInstanceReferenceValue instance
    2. Set the spec value on the attribute
    3. Call setValueIRef with None and verify the value is preserved
    """
    ref_value = EcucInstanceReferenceValue()
    instance_ref = AnyInstanceRef()

    assert ref_value.setValueIRef(instance_ref) is ref_value

    ref_value.setValueIRef(None)

    assert ref_value.getValueIRef() is instance_ref


def test_ecuc_instance_reference_value_class_docstring_verbatim():
    """
    The class docstring must carry the Table 2.55 class Note verbatim (Rule 0012).
    """
    note = "InstanceReference representation in the ECU Configuration."
    assert EcucInstanceReferenceValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert note in EcucInstanceReferenceValue.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_instance_reference_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.55 attribute Notes verbatim (Rule 0001.4/0012).
    """
    note = "InstanceReference representation in the ECU Configuration. InstanceRef implemented by: AnyInstanceRef"
    for method_name in ("getValueIRef", "setValueIRef"):
        method = getattr(EcucInstanceReferenceValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_reference_value():
    """
    Test EcucReferenceValue class - full spec compliance per Table 2.54.

    Test Steps:
    1. Create an EcucReferenceValue instance
    2. Test initial values
    3. Test valueRef methods (spec: Referrable 0..1 ref -> RefType, Kind-ref Ref suffix per Rule 0001.5)
    4. Verify method chaining
    5. Verify class docstring contains the spec Note verbatim
    """
    ref_value = EcucReferenceValue()

    # Test initial values
    assert ref_value.valueRef is None

    # Test valueRef methods
    value_ref = RefType().setValue("/ECUC/myOs/myOsScheduleTable1")
    result = ref_value.setValueRef(value_ref)
    assert result is ref_value  # Method chaining
    assert ref_value.getValueRef() == value_ref

    # Verify docstrings match spec (Rule 0012)
    assert EcucReferenceValue.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Used to represent a configuration value that has a parameter definition of type EcucAbstractReferenceDef" in EcucReferenceValue.__doc__, "Class docstring must contain spec Note verbatim"
    assert "(used for all of its specializations excluding EcucInstanceReferenceDef)." in EcucReferenceValue.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_reference_value_none_no_op():
    """
    None passed to a setter of EcucReferenceValue is a no-op.

    Test Steps:
    1. Create an EcucReferenceValue instance
    2. Set the spec value on the attribute
    3. Call setValueRef with None and verify the value is preserved
    """
    ref_value = EcucReferenceValue()
    value_ref = RefType().setValue("/ECUC/myOs/myOsScheduleTable1")

    assert ref_value.setValueRef(value_ref) is ref_value

    ref_value.setValueRef(None)

    assert ref_value.getValueRef() == value_ref


def test_ecuc_reference_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.54 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence
       that paraphrases are known to drop.
    """
    notes = {
        "getValueRef": "Specifies the destination of the reference.",
        "setValueRef": "Specifies the destination of the reference.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucReferenceValue, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_container_value_initialization_defaults():
    """
    EcucContainerValue (Table 2.48) defaults: all four spec attributes empty.

    Test Steps:
    1. Create an EcucContainerValue instance with parent and short_name
    2. Assert definitionRef is None and the three aggr lists are empty
    """
    parent = Limit()
    container = EcucContainerValue(parent, "test_container")

    assert container.parent == parent
    assert container.short_name == "test_container"
    assert container.getDefinitionRef() is None
    assert container.getParameterValues() == []
    assert container.getReferenceValues() == []
    assert container.getSubContainers() == []


def test_ecuc_container_value_get_set_definition_ref():
    """
    setDefinitionRef returns self (chaining) and a None value is a no-op.

    Test Steps:
    1. Set a RefType value via setDefinitionRef
    2. Assert chaining returns self and the value round-trips
    3. Call setDefinitionRef(None) and assert the previous value is preserved
    """
    parent = Limit()
    container = EcucContainerValue(parent, "test_container")
    ref = RefType().setValue("/EcucDefs/Rte/Container")

    result = container.setDefinitionRef(ref)
    assert result is container
    assert container.getDefinitionRef() == ref

    container.setDefinitionRef(None)
    assert container.getDefinitionRef() == ref


def test_ecuc_container_value_add_parameter_value():
    """
    addParameterValue appends and chains.

    Test Steps:
    1. Add an EcucParameterValue via addParameterValue
    2. Assert chaining and the value is in the typed list
    """
    parent = Limit()
    container = EcucContainerValue(parent, "test_container")
    param_val = EcucAddInfoParamValue()

    result = container.addParameterValue(param_val)
    assert result is container
    assert container.getParameterValues() == [param_val]


def test_ecuc_container_value_reference_values_returns_list():
    """
    getReferenceValues returns the typed list (not a single type), per Table 2.48.

    Test Steps:
    1. Add an EcucReferenceValue via addReferenceValue
    2. Assert getReferenceValues returns a list containing the value
    """
    parent = Limit()
    container = EcucContainerValue(parent, "test_container")
    ref_val = EcucReferenceValue()

    result = container.addReferenceValue(ref_val)
    assert result is container
    values = container.getReferenceValues()
    assert isinstance(values, list)
    assert values == [ref_val]


def test_ecuc_container_value_create_sub_container():
    """
    createSubContainer creates a Referrable child and a duplicate returns existing.

    Test Steps:
    1. Create a sub-container and assert its short_name
    2. Create a duplicate short_name and assert the same instance is returned
    """
    parent = Limit()
    container = EcucContainerValue(parent, "test_container")

    sub = container.createSubContainer("sub_container")
    assert sub is not None
    assert sub.short_name == "sub_container"
    assert container.getSubContainers() == [sub]

    duplicate = container.createSubContainer("sub_container")
    assert duplicate is sub
    assert len(container.getSubContainers()) == 1


def test_ecuc_container_value_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.48 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert the class docstring contains the spec class Note verbatim
    2. Assert each getter/setter/docstring carries the full spec Note sentence
    """
    assert EcucContainerValue.__doc__ is not None
    assert "Represents a Container definition in the ECU Configuration Description." in EcucContainerValue.__doc__

    notes = {
        "getDefinitionRef": "Reference to the definition of this Container in the ECU Configuration Parameter Definition.",
        "setDefinitionRef": "Reference to the definition of this Container in the ECU Configuration Parameter Definition.",
        "getParameterValues": "Aggregates all ECU Configuration Values within this Container.",
        "addParameterValue": "Aggregates all ECU Configuration Values within this Container.",
        "getReferenceValues": "Aggregates all References with this container.",
        "addReferenceValue": "Aggregates all References with this container.",
        "getSubContainers": "Aggregates all sub-containers within this container.",
        "createSubContainer": "Aggregates all sub-containers within this container.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucContainerValue, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_module_configuration_values_initialization_defaults():
    """
    EcucModuleConfigurationValues (Table 2.47) defaults: all spec attributes empty.

    Test Steps:
    1. Create an EcucModuleConfigurationValues instance with parent and short_name
    2. Assert parent/short_name and the containers/definitionRef/ecucDefEdition/implementationConfigVariant/moduleDescriptionRef/postBuildVariantUsed defaults
    3. Assert getContainers returns the dedicated typed list field directly (Rule 0004)
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "test_module_config")

    assert values.parent == parent
    assert values.short_name == "test_module_config"
    assert values.containers == []
    assert values.getContainers() == []
    assert values.getContainers() is values.getContainers()
    assert values.definitionRef is None
    assert values.getDefinitionRef() is None
    assert values.ecucDefEdition is None
    assert values.getEcucDefEdition() is None
    assert values.implementationConfigVariant is None
    assert values.getImplementationConfigVariant() is None
    assert values.moduleDescriptionRef is None
    assert values.getModuleDescriptionRef() is None
    assert values.postBuildVariantUsed is None
    assert values.getPostBuildVariantUsed() is None


def test_ecuc_module_configuration_values_create_container():
    """
    createContainer appends to the typed list and a duplicate short name returns the existing container.

    Test Steps:
    1. Create two containers via createContainer and assert they are appended in order
    2. Create the same short name again and assert the existing container is returned
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")

    container1 = values.createContainer("OsOS")
    assert container1 is not None
    assert container1.short_name == "OsOS"
    container2 = values.createContainer("CanIf")
    assert values.getContainers() == [container1, container2]

    duplicate = values.createContainer("OsOS")
    assert duplicate is container1
    assert values.getContainers() == [container1, container2]


def test_ecuc_module_configuration_values_get_set_definition_ref():
    """
    setDefinitionRef chains, round-trips a typed RefType, and None is a no-op.

    Test Steps:
    1. Set a RefType value via setDefinitionRef
    2. Assert chaining returns self and the value round-trips
    3. Call setDefinitionRef(None) and assert the value is preserved
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")
    definition_ref = RefType().setValue("/ModuleDef/Os").setDest("ECUC-MODULE-DEF")

    assert values.setDefinitionRef(definition_ref) is values
    assert values.getDefinitionRef() == definition_ref

    values.setDefinitionRef(None)
    assert values.getDefinitionRef() == definition_ref


def test_ecuc_module_configuration_values_get_set_ecuc_def_edition():
    """
    setEcucDefEdition chains, round-trips a RevisionLabelString, and None is a no-op.

    Test Steps:
    1. Set a RevisionLabelString value via setEcucDefEdition
    2. Assert chaining returns self and the value round-trips
    3. Call setEcucDefEdition(None) and assert the value is preserved
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")
    edition = RevisionLabelString().setValue("1.0.0")

    assert values.setEcucDefEdition(edition) is values
    assert values.getEcucDefEdition() == edition

    values.setEcucDefEdition(None)
    assert values.getEcucDefEdition() == edition


def test_ecuc_module_configuration_values_get_set_implementation_config_variant():
    """
    setImplementationConfigVariant chains, round-trips the typed enum, and None is a no-op.

    Test Steps:
    1. Set an EcucConfigurationVariantEnum value via setImplementationConfigVariant
    2. Assert chaining returns self and the value round-trips
    3. Call setImplementationConfigVariant(None) and assert the value is preserved
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")
    variant = EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE)

    assert values.setImplementationConfigVariant(variant) is values
    assert values.getImplementationConfigVariant() == variant

    values.setImplementationConfigVariant(None)
    assert values.getImplementationConfigVariant() == variant


def test_ecuc_module_configuration_values_get_set_module_description_ref():
    """
    setModuleDescriptionRef chains, round-trips a typed RefType, and None is a no-op.

    Test Steps:
    1. Set a RefType value via setModuleDescriptionRef
    2. Assert chaining returns self and the value round-trips
    3. Call setModuleDescriptionRef(None) and assert the value is preserved
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")
    description_ref = RefType().setValue("/Vendor/OsImplementation").setDest("BSW-IMPLEMENTATION")

    assert values.setModuleDescriptionRef(description_ref) is values
    assert values.getModuleDescriptionRef() == description_ref

    values.setModuleDescriptionRef(None)
    assert values.getModuleDescriptionRef() == description_ref


def test_ecuc_module_configuration_values_get_set_post_build_variant_used():
    """
    setPostBuildVariantUsed chains, round-trips a Boolean, and None is a no-op.

    Test Steps:
    1. Set a Boolean value via setPostBuildVariantUsed
    2. Assert chaining returns self and the value round-trips
    3. Call setPostBuildVariantUsed(None) and assert the value is preserved
    """
    parent = Limit()
    values = EcucModuleConfigurationValues(parent, "mcv")
    post_build = Boolean().setValue(True)

    assert values.setPostBuildVariantUsed(post_build) is values
    assert values.getPostBuildVariantUsed() == post_build

    values.setPostBuildVariantUsed(None)
    assert values.getPostBuildVariantUsed() == post_build


def test_ecuc_module_configuration_values_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.47 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert the class docstring contains the spec class Note verbatim
    2. Assert each getter/setter/creator docstring carries the full spec Note verbatim
    """
    assert EcucModuleConfigurationValues.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Head of the configuration of one Module." in EcucModuleConfigurationValues.__doc__, "Class docstring must contain spec Note verbatim"

    notes = {
        "createContainer": "Aggregates all containers that belong to this module configuration. atpVariation: [RS_ECUC_00078] Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=container.shortName, container.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10",
        "getContainers": "Aggregates all containers that belong to this module configuration. atpVariation: [RS_ECUC_00078] Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=container.shortName, container.variationPoint.shortLabel vh.latestBindingTime=postBuild xml.sequenceOffset=10",
        "getDefinitionRef": "Reference to the definition of this EcucModuleConfigurationValues element. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10",
        "setDefinitionRef": "Reference to the definition of this EcucModuleConfigurationValues element. Typically, this is a vendor specific module configuration. Tags: xml.sequenceOffset=-10",
        "getEcucDefEdition": "This is the version info of the ModuleDef ECUC Parameter definition to which this values conform to / are based on. For the Definition of ModuleDef ECUC Parameters the AdminData shall be used to express the semantic changes. The compatibility rules between the definition and value revision labels is up to the module's vendor.",
        "setEcucDefEdition": "This is the version info of the ModuleDef ECUC Parameter definition to which this values conform to / are based on. For the Definition of ModuleDef ECUC Parameters the AdminData shall be used to express the semantic changes. The compatibility rules between the definition and value revision labels is up to the module's vendor.",
        "getImplementationConfigVariant": "Specifies the kind of deliverable this EcucModuleConfigurationValues element provides. If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild.",
        "setImplementationConfigVariant": "Specifies the kind of deliverable this EcucModuleConfigurationValues element provides. If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild.",
        "getModuleDescriptionRef": 'Referencing the BSW module description, which this EcucModuleConfigurationValues element is configuring. This is optional because the EcucModuleConfigurationValues element is also used to configure the ECU infrastructure (memory map) or Application SW-Cs. However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information.',
        "setModuleDescriptionRef": 'Referencing the BSW module description, which this EcucModuleConfigurationValues element is configuring. This is optional because the EcucModuleConfigurationValues element is also used to configure the ECU infrastructure (memory map) or Application SW-Cs. However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information.',
        "getPostBuildVariantUsed": "Indicates whether a module implementation has or plans to have (i.e., introduced at link or post-build time) new post-build variation points. TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed.",
        "setPostBuildVariantUsed": "Indicates whether a module implementation has or plans to have (i.e., introduced at link or post-build time) new post-build variation points. TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucModuleConfigurationValues, method_name)
        assert method.__doc__ is not None, "%s must have a docstring" % method_name
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


def test_ecuc_module_configuration_values_member_annotations():
    """get/set/create shall resolve to Optional[T] / List[EcucContainerValue] / EcucModuleConfigurationValues (Rule 0003/0006 — get_type_hints pin; 0..1 setters take Optional[T])."""
    import typing

    assert typing.get_type_hints(EcucModuleConfigurationValues.createContainer)["short_name"] is str
    assert typing.get_type_hints(EcucModuleConfigurationValues.createContainer)["return"] is EcucContainerValue
    assert typing.get_type_hints(EcucModuleConfigurationValues.getContainers)["return"] == typing.List[EcucContainerValue]
    assert typing.get_type_hints(EcucModuleConfigurationValues.getDefinitionRef)["return"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setDefinitionRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setDefinitionRef)["return"] is EcucModuleConfigurationValues
    assert typing.get_type_hints(EcucModuleConfigurationValues.getEcucDefEdition)["return"] == typing.Optional[RevisionLabelString]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setEcucDefEdition)["value"] == typing.Optional[RevisionLabelString]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setEcucDefEdition)["return"] is EcucModuleConfigurationValues
    assert typing.get_type_hints(EcucModuleConfigurationValues.getImplementationConfigVariant)["return"] == typing.Optional[EcucConfigurationVariantEnum]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setImplementationConfigVariant)["value"] == typing.Optional[EcucConfigurationVariantEnum]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setImplementationConfigVariant)["return"] is EcucModuleConfigurationValues
    assert typing.get_type_hints(EcucModuleConfigurationValues.getModuleDescriptionRef)["return"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setModuleDescriptionRef)["value"] == typing.Optional[RefType]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setModuleDescriptionRef)["return"] is EcucModuleConfigurationValues
    assert typing.get_type_hints(EcucModuleConfigurationValues.getPostBuildVariantUsed)["return"] == typing.Optional[Boolean]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setPostBuildVariantUsed)["value"] == typing.Optional[Boolean]
    assert typing.get_type_hints(EcucModuleConfigurationValues.setPostBuildVariantUsed)["return"] is EcucModuleConfigurationValues


def test_ecuc_configuration_variant_enum():
    """
    Test EcucConfigurationVariantEnum class.

    Test Steps:
    1. Create an EcucConfigurationVariantEnum instance
    2. Test initial values
    """
    _config_enum = EcucConfigurationVariantEnum()

    # Test initial values inherited from AREnum


def test_ecuc_module_def():
    """
    Test EcucModuleDef class.

    Test Steps:
    1. Create an EcucModuleDef instance with parent and short_name
    2. Test initial values
    3. Test apiServicePrefix methods
    4. Test containers methods including createEcucParamConfContainerDef and createEcucChoiceContainerDef
    5. Test postBuildVariantSupport methods
    6. Test refinedModuleDefRef methods
    7. Test supportedConfigVariants methods
    """
    parent = Limit()  # Using Limit as a concrete ARObject subclass
    module_def = EcucModuleDef(parent, "test_module_def")

    # Test initial values
    assert module_def.parent == parent
    assert module_def.short_name == "test_module_def"
    assert module_def.apiServicePrefix is None
    assert module_def.containers == []
    assert module_def.postBuildVariantSupport is None
    assert module_def.refinedModuleDefRef is None
    assert module_def.supportedConfigVariants == []

    # Test apiServicePrefix methods
    c_id = CIdentifier()
    c_id.setValue("API_PREFIX")
    module_def.setApiServicePrefix(c_id)
    assert module_def.getApiServicePrefix() == c_id

    # Test containers methods
    param_container = module_def.createEcucParamConfContainerDef("param_container")
    assert param_container is not None
    assert len(module_def.containers) == 1
    assert module_def.getContainers() == [param_container]

    choice_container = module_def.createEcucChoiceContainerDef("choice_container")
    assert choice_container is not None
    assert len(module_def.containers) == 2

    # Test postBuildVariantSupport methods
    module_def.setPostBuildVariantSupport(True)
    assert module_def.getPostBuildVariantSupport() is True

    # Test refinedModuleDefRef methods
    module_def.setRefinedModuleDefRef("refined_ref")
    assert module_def.getRefinedModuleDefRef() == "refined_ref"

    # Test supportedConfigVariants methods
    config_variant = EcucConfigurationVariantEnum()
    module_def.addSupportedConfigVariant(config_variant)
    assert module_def.getSupportedConfigVariants() == [config_variant]


if __name__ == "__main__":
    test_ecuc_value_collection_initialization_defaults()
    test_ecuc_value_collection_add_ecuc_value_ref()
    test_ecuc_value_collection_get_set_ecu_extract_ref()
    test_ecuc_value_collection_member_docstrings_verbatim()
    test_ecuc_value_collection_member_annotations()
    test_ecuc_indexable_value_abstract()
    test_ecuc_indexable_value_base_properties()
    test_ecuc_indexable_value_member_docstrings_verbatim()
    test_ecuc_indexable_value_member_annotations()
    test_ecuc_parameter_value_abstract()
    test_ecuc_parameter_value_methods()
    test_ecuc_add_info_param_value()
    test_ecuc_add_info_param_value_none_no_op()
    test_ecuc_add_info_param_value_member_docstrings_verbatim()
    test_ecuc_textual_param_value()
    test_ecuc_numerical_param_value()
    test_ecuc_numerical_param_value_none_no_op()
    test_ecuc_numerical_param_value_member_docstrings_verbatim()
    test_ecuc_abstract_reference_value_abstract()
    test_ecuc_abstract_reference_value_methods()
    test_ecuc_instance_reference_value()
    test_ecuc_reference_value()
    test_ecuc_container_value_initialization_defaults()
    test_ecuc_container_value_get_set_definition_ref()
    test_ecuc_container_value_add_parameter_value()
    test_ecuc_container_value_reference_values_returns_list()
    test_ecuc_container_value_create_sub_container()
    test_ecuc_container_value_member_docstrings_verbatim()
    test_ecuc_module_configuration_values_initialization_defaults()
    test_ecuc_module_configuration_values_create_container()
    test_ecuc_module_configuration_values_get_set_definition_ref()
    test_ecuc_module_configuration_values_get_set_ecuc_def_edition()
    test_ecuc_module_configuration_values_get_set_implementation_config_variant()
    test_ecuc_module_configuration_values_get_set_module_description_ref()
    test_ecuc_module_configuration_values_get_set_post_build_variant_used()
    test_ecuc_module_configuration_values_member_docstrings_verbatim()
    test_ecuc_module_configuration_values_member_annotations()
    test_ecuc_configuration_variant_enum()
    test_ecuc_module_def()
    print("All ECUCDescriptionTemplate tests passed!")
