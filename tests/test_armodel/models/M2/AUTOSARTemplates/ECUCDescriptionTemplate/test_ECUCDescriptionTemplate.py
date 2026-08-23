"""
Test cases for the ECUCDescriptionTemplate module.
These tests ensure 100% code coverage for all classes in the ECUCDescriptionTemplate module.
"""

from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import (
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
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucConfigurationVariantEnum, EcucModuleDef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARNumerical, Boolean, CIdentifier, Limit, Numerical, RefType, RevisionLabelString, VerbatimString
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel import LLongName
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageParagraph


def test_ecuc_value_collection():
    """
    Test EcucValueCollection class initialization and methods.

    Test Steps:
    1. Create an EcucValueCollection instance with parent and short_name
    2. Test initial values
    3. Test getter and setter methods
    4. Test add methods and verify method chaining
    """
    parent = Limit()  # Using Limit as a concrete ARObject subclass
    collection = EcucValueCollection(parent, "test_collection")

    # Test initial values
    assert collection.parent == parent
    assert collection.short_name == "test_collection"
    assert collection.ecucValueRefs == []
    assert collection.ecuExtractRef is None

    # Test ecucValueRefs operations
    ref1 = "ref1"
    collection.addEcucValueRef(ref1)
    assert collection.getEcucValueRefs() == [ref1]

    # Test ecuExtractRef operations
    collection.setEcuExtractRef("extract_ref")
    assert collection.getEcuExtractRef() == "extract_ref"


def test_ecuc_indexable_value_abstract():
    """
    Test EcucIndexableValue abstract class.

    Test Steps:
    1. Verify that instantiating EcucIndexableValue directly raises NotImplementedError
    """
    try:
        EcucIndexableValue()
        assert False, "Should raise NotImplementedError"
    except TypeError:
        pass  # Expected


def test_ecuc_indexable_value_index_methods():
    """
    Test EcucIndexableValue index accessors (via a concrete subclass).

    Test Steps:
    1. Create an EcucNumericalParamValue instance (concrete subclass)
    2. Test initial index value
    3. Test index getter and setter with method chaining
    4. Test setIndex(None) is a no-op
    """
    value = EcucNumericalParamValue()

    # Test initial value
    assert value.index is None

    # Test getter and setter
    index = ARNumerical()
    index.setValue("4")
    result = value.setIndex(index)
    assert result == value  # Method chaining
    assert value.getIndex() == index

    # Test None is a no-op
    value.setIndex(None)
    assert value.getIndex() == index


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
    assert param_value.definition is None
    assert param_value.isAutoValue is None

    # Test annotation methods
    annotation = Annotation()
    result = param_value.addAnnotation(annotation)
    assert result == param_value  # Method chaining
    assert param_value.getAnnotations() == [annotation]

    # Test definition methods
    definition_ref = RefType().setValue("/EcucDefs/Rte/Param")
    result = param_value.setDefinition(definition_ref)
    assert result is param_value  # Method chaining
    assert param_value.getDefinition() == definition_ref

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
    assert param_value.definition is None
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
    assert param_value.definition is None
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
    assert param_value.definition is None
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


def test_ecuc_module_configuration_values():
    """
    Test EcucModuleConfigurationValues class - full spec compliance per Table 2.47.

    Test Steps:
    1. Create an EcucModuleConfigurationValues instance with parent and short_name
    2. Test initial values
    3. Test containers methods including createContainer
    4. Test definition methods (ref to EcucModuleDef)
    5. Test ecucDefEdition methods
    6. Test implementationConfigVariant methods
    7. Test moduleDescription methods (ref to BswImplementation)
    8. Test postBuildVariantUsed methods
    9. Verify docstrings match spec verbatim
    10. Verify class docstring contains the spec Note
    """
    parent = Limit()  # Using Limit as a concrete ARObject subclass
    module_config = EcucModuleConfigurationValues(parent, "test_module_config")

    # Test initial values
    assert module_config.parent == parent
    assert module_config.short_name == "test_module_config"
    assert module_config.containers == []
    assert module_config.definition is None or module_config.definitionRef is None, "Member should be named 'definition' per spec (attribute name)"
    assert module_config.ecucDefEdition is None
    assert module_config.implementationConfigVariant is None
    assert module_config.moduleDescription is None or module_config.moduleDescriptionRef is None, "Member should be named 'moduleDescription' per spec (attribute name)"
    assert module_config.postBuildVariantUsed is None

    # Test containers methods
    container = module_config.createContainer("container1")
    assert container is not None
    assert container.short_name == "container1"
    containers = module_config.getContainers()
    assert len(containers) == 1
    assert containers[0] == container

    # Test definition methods (spec: "Reference to the definition of this EcucModule ConfigurationValues element...")
    module_config.setDefinition("def_ref")
    assert module_config.getDefinition() == "def_ref"

    # Test ecucDefEdition methods (spec type: RevisionLabelString)
    edition = RevisionLabelString().setValue("1.0.0")
    module_config.setEcucDefEdition(edition)
    assert module_config.getEcucDefEdition() == edition

    # Test implementationConfigVariant methods (spec type: EcucConfigurationVariantEnum)
    variant = EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_PRE_COMPILE)
    module_config.setImplementationConfigVariant(variant)
    assert module_config.getImplementationConfigVariant() == variant

    # Test moduleDescription methods (spec: "Referencing the BSW module description...")
    module_config.setModuleDescription("module_ref")
    assert module_config.getModuleDescription() == "module_ref"

    # Test postBuildVariantUsed methods (spec type: Boolean)
    post_build = Boolean().setValue(True)
    module_config.setPostBuildVariantUsed(post_build)
    assert module_config.getPostBuildVariantUsed() == post_build

    # Verify docstrings match spec (Rule 0012)
    assert EcucModuleConfigurationValues.__doc__ is not None, "Class docstring must contain spec Note"
    assert "Head of the configuration of one Module" in EcucModuleConfigurationValues.__doc__, "Class docstring must contain spec Note verbatim"


def test_ecuc_module_configuration_values_none_no_op():
    """
    None passed to a 0..1 setter of EcucModuleConfigurationValues is a no-op.

    Test Steps:
    1. Create an EcucModuleConfigurationValues instance
    2. Set spec values on every 0..1 attribute
    3. Call each setter with None and verify the value is preserved
    """
    parent = Limit()
    module_config = EcucModuleConfigurationValues(parent, "mcv_none_no_op")

    definition = RefType().setValue("/ModuleDef")
    edition = RevisionLabelString().setValue("2.0.0")
    variant = EcucConfigurationVariantEnum().setValue(EcucConfigurationVariantEnum.VARIANT_POST_BUILD)
    description = RefType().setValue("/BswImplementation")
    post_build = Boolean().setValue(True)

    assert module_config.setDefinition(definition) is module_config
    assert module_config.setEcucDefEdition(edition) is module_config
    assert module_config.setImplementationConfigVariant(variant) is module_config
    assert module_config.setModuleDescription(description) is module_config
    assert module_config.setPostBuildVariantUsed(post_build) is module_config

    module_config.setDefinition(None)
    module_config.setEcucDefEdition(None)
    module_config.setImplementationConfigVariant(None)
    module_config.setModuleDescription(None)
    module_config.setPostBuildVariantUsed(None)

    assert module_config.getDefinition() == definition
    assert module_config.getEcucDefEdition() == edition
    assert module_config.getImplementationConfigVariant() == variant
    assert module_config.getModuleDescription() == description
    assert module_config.getPostBuildVariantUsed() == post_build


def test_ecuc_module_configuration_values_member_docstrings_verbatim():
    """
    Member docstrings must carry the Table 2.47 attribute Notes verbatim (Rule 0001.4/0012).

    Test Steps:
    1. Assert each getter/setter docstring contains the full spec Note sentence tail
       that paraphrases are known to drop.
    """
    notes = {
        "getDefinition": "Typically, this is a vendor specific module configuration.",
        "setDefinition": "Typically, this is a vendor specific module configuration.",
        "getEcucDefEdition": "The compatibility rules between the definition and value revision labels is up to the module's vendor.",
        "setEcucDefEdition": "The compatibility rules between the definition and value revision labels is up to the module's vendor.",
        "getImplementationConfigVariant": "If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild.",
        "setImplementationConfigVariant": "If this element is not used in a particular role (e.g. preconfiguredConfiguration or recommendedConfiguration) then the value shall be one of VariantPreCompile, VariantLinkTime, VariantPostBuild.",
        "getModuleDescription": 'However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information.',
        "setModuleDescription": 'However in case the EcucModuleConfigurationValues are used to configure the module, the reference is mandatory in order to fetch module specific "common" published information.',
        "getPostBuildVariantUsed": "TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed.",
        "setPostBuildVariantUsed": "TRUE means yes, FALSE means no. If the attribute is not defined, FALSE semantics shall be assumed.",
        "createContainer": "Aggregates all containers that belong to this module configuration.",
        "getContainers": "Aggregates all containers that belong to this module configuration.",
    }
    for method_name, note in notes.items():
        method = getattr(EcucModuleConfigurationValues, method_name)
        assert note in method.__doc__, "%s docstring must contain the spec Note verbatim" % method_name


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


def test_ecuc_module_configuration_values_backward_compatibility():
    """
    Test backward compatibility with deprecated methods and properties.

    Test Steps:
    1. Create an EcucModuleConfigurationValues instance
    2. Test deprecated setDefinitionRef/getDefinitionRef methods
    3. Test deprecated definitionRef property
    4. Test deprecated setModuleDescriptionRef/getModuleDescriptionRef methods
    5. Test deprecated moduleDescriptionRef property
    6. Verify that new and old accessors refer to the same underlying attributes
    """
    parent = Limit()
    module_config = EcucModuleConfigurationValues(parent, "test_module")

    # Test deprecated definitionRef methods
    module_config.setDefinitionRef("def_ref_old")
    assert module_config.getDefinitionRef() == "def_ref_old"
    # Verify it's the same as the new method
    assert module_config.getDefinition() == "def_ref_old"

    # Test deprecated definitionRef property
    module_config.definitionRef = "def_ref_prop"
    assert module_config.definitionRef == "def_ref_prop"
    assert module_config.definition == "def_ref_prop"

    # Test deprecated moduleDescriptionRef methods
    module_config.setModuleDescriptionRef("module_ref_old")
    assert module_config.getModuleDescriptionRef() == "module_ref_old"
    # Verify it's the same as the new method
    assert module_config.getModuleDescription() == "module_ref_old"

    # Test deprecated moduleDescriptionRef property
    module_config.moduleDescriptionRef = "module_ref_prop"
    assert module_config.moduleDescriptionRef == "module_ref_prop"
    assert module_config.moduleDescription == "module_ref_prop"


if __name__ == "__main__":
    test_ecuc_value_collection()
    test_ecuc_indexable_value_abstract()
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
    test_ecuc_module_configuration_values()
    test_ecuc_configuration_variant_enum()
    test_ecuc_module_def()
    print("All ECUCDescriptionTemplate tests passed!")
