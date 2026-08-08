"""Tests for the InstantiationDataDefProps class."""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstantiationDataDefProps import InstantiationDataDefProps
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestInstantiationDataDefProps:
    """Tests for InstantiationDataDefProps."""

    def test_initialization(self):
        props = InstantiationDataDefProps()
        assert props.parameterInstance is None
        assert props.swDataDefProps is None
        assert props.variableInstance is None

    def test_get_set_parameter_instance(self):
        props = InstantiationDataDefProps()
        value = AutosarParameterRef()
        assert props.setParameterInstance(value) is props
        assert props.getParameterInstance() is value
        props.setParameterInstance(None)
        assert props.getParameterInstance() is value

    def test_get_set_sw_data_def_props(self):
        props = InstantiationDataDefProps()
        value = SwDataDefProps()
        assert props.setSwDataDefProps(value) is props
        assert props.getSwDataDefProps() is value
        props.setSwDataDefProps(None)
        assert props.getSwDataDefProps() is value

    def test_get_set_variable_instance(self):
        props = InstantiationDataDefProps()
        value = AutosarVariableRef()
        assert props.setVariableInstance(value) is props
        assert props.getVariableInstance() is value
        props.setVariableInstance(None)
        assert props.getVariableInstance() is value
