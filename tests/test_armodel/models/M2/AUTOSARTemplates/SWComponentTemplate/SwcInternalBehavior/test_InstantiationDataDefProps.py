"""Tests for the InstantiationDataDefProps class (R23-11 AUTOSAR_CP_TPS_SoftwareComponentTemplate, Table 7.41, p.588)."""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps

CLASS_NOTE = (
    "This is a general class allowing to apply additional SwDataDefProps to particular instantiations of a DataPrototype. "
    "Typically the accessibility and further information like alias names for a particular data is modeled on the level of DataPrototypes (especially VariableDataPrototypes, ParameterDataPrototypes). "  # noqa E501
    "But due to the recursive structure of the meta-model concerning data types (a composite (data) type consists out of data prototypes) "
    "a part of the MCD information is described in the data type (in case of ApplicationCompositeDataType). "  # noqa E501
    "This is a strong restriction in the reuse of data typed because the data type should be re-used for different VariableDataPrototypes and ParameterDataPrototypes "  # noqa E501
    "to guarantee type compatibility on C-implementation level (e.g. data of a Port is stored in PIM or a ParameterDataPrototype used as ROM Block and shall be typed by the same data type as NVRAM Block). "  # noqa E501
    "This class overcomes such a restriction if applied properly."  # noqa E501
)

CONSTRAINT_1959 = (
    "[constr_1959] Existence of attribute InstantiationDataDefProps.swDataDefProps: "
    "For each InstantiationDataDefProps, attribute swDataDefProps shall exist at the time when the contract phase generation is executed."
)

PARAMETER_INSTANCE_NOTE = (
    "This reference identifies the particular DataPrototype (defined in the context of a composite ParameterDataPrototype) on which the swDataDefProps shall be applied."  # noqa E501
)
SW_DATA_DEF_PROPS_NOTE = "These are the particular data definition properties which shall be applied"
VARIABLE_INSTANCE_NOTE = (
    "This reference identifies the particular DataPrototype (defined in the context of a composite VariableDataPrototype) on which the swDataDefProps shall be applied."  # noqa E501
)


class TestInstantiationDataDefProps:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 7.41)"""
        assert inspect.cleandoc(InstantiationDataDefProps.__doc__) == (CLASS_NOTE + "\n\n" + CONSTRAINT_1959)
        assert InstantiationDataDefProps.getParameterInstance.__doc__.strip() == PARAMETER_INSTANCE_NOTE
        assert InstantiationDataDefProps.setParameterInstance.__doc__.strip() == (PARAMETER_INSTANCE_NOTE + " A None value is a no-op and does not overwrite an existing parameterInstance.")
        assert InstantiationDataDefProps.getSwDataDefProps.__doc__.strip() == SW_DATA_DEF_PROPS_NOTE
        assert InstantiationDataDefProps.setSwDataDefProps.__doc__.strip() == (SW_DATA_DEF_PROPS_NOTE + " A None value is a no-op and does not overwrite an existing swDataDefProps.")
        assert InstantiationDataDefProps.getVariableInstance.__doc__.strip() == VARIABLE_INSTANCE_NOTE
        assert InstantiationDataDefProps.setVariableInstance.__doc__.strip() == (VARIABLE_INSTANCE_NOTE + " A None value is a no-op and does not overwrite an existing variableInstance.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        assert issubclass(InstantiationDataDefProps, ARObject)
        assert issubclass(InstantiationDataDefProps, VariationPointCapable)
        props = InstantiationDataDefProps()
        assert props.parameterInstance is None
        assert props.swDataDefProps is None
        assert props.variableInstance is None

        hints = typing.get_type_hints(InstantiationDataDefProps.getParameterInstance)
        assert hints["return"] == typing.Optional[AutosarParameterRef]
        hints = typing.get_type_hints(InstantiationDataDefProps.setParameterInstance)
        assert hints["value"] == typing.Optional[AutosarParameterRef]
        assert hints["return"] is InstantiationDataDefProps
        hints = typing.get_type_hints(InstantiationDataDefProps.getSwDataDefProps)
        assert hints["return"] == typing.Optional[SwDataDefProps]
        hints = typing.get_type_hints(InstantiationDataDefProps.setSwDataDefProps)
        assert hints["value"] == typing.Optional[SwDataDefProps]
        assert hints["return"] is InstantiationDataDefProps
        hints = typing.get_type_hints(InstantiationDataDefProps.getVariableInstance)
        assert hints["return"] == typing.Optional[AutosarVariableRef]
        hints = typing.get_type_hints(InstantiationDataDefProps.setVariableInstance)
        assert hints["value"] == typing.Optional[AutosarVariableRef]
        assert hints["return"] is InstantiationDataDefProps

    def test_initialization(self):
        """Test InstantiationDataDefProps initialization"""
        props = InstantiationDataDefProps()

        assert props is not None
        assert props.parameterInstance is None
        assert props.swDataDefProps is None
        assert props.variableInstance is None

    def test_get_set_parameter_instance(self):
        """Test getParameterInstance and setParameterInstance methods"""
        props = InstantiationDataDefProps()

        assert props.getParameterInstance() is None
        param_ref = AutosarParameterRef()
        assert props.setParameterInstance(param_ref) is props
        assert props.getParameterInstance() is param_ref

        # None is a no-op
        props.setParameterInstance(None)
        assert props.getParameterInstance() is param_ref

    def test_get_set_sw_data_def_props(self):
        """Test getSwDataDefProps and setSwDataDefProps methods"""
        props = InstantiationDataDefProps()

        assert props.getSwDataDefProps() is None
        def_props = SwDataDefProps()
        assert props.setSwDataDefProps(def_props) is props
        assert props.getSwDataDefProps() is def_props

        # None is a no-op
        props.setSwDataDefProps(None)
        assert props.getSwDataDefProps() is def_props

    def test_get_set_variable_instance(self):
        """Test getVariableInstance and setVariableInstance methods"""
        props = InstantiationDataDefProps()

        assert props.getVariableInstance() is None
        var_ref = AutosarVariableRef()
        assert props.setVariableInstance(var_ref) is props
        assert props.getVariableInstance() is var_ref

        # None is a no-op
        props.setVariableInstance(None)
        assert props.getVariableInstance() is var_ref
