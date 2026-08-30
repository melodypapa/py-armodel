from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy


class TestSwVariableRefProxy:
    """Test class for SwVariableRefProxy class."""

    def test_sw_variable_ref_proxy_initialization(self):
        proxy = SwVariableRefProxy()
        assert proxy.getAutosarVariable() is None
        assert proxy.getMcDataInstanceVarRef() is None

    def test_sw_variable_ref_proxy_methods(self):
        proxy = SwVariableRefProxy()
        autosar_variable = AutosarVariableRef().setLocalVariableRef(RefType().setDest("AUTOSAR/Variables/var"))
        mc_data_instance_var = RefType().setDest("AUTOSAR/McDataInstances/inst")

        assert proxy.setAutosarVariable(autosar_variable) == proxy
        assert proxy.getAutosarVariable() == autosar_variable
        assert proxy.setMcDataInstanceVarRef(mc_data_instance_var) == proxy
        assert proxy.getMcDataInstanceVarRef() == mc_data_instance_var

    def test_sw_variable_ref_proxy_none_noop(self):
        proxy = SwVariableRefProxy()
        autosar_variable = AutosarVariableRef().setLocalVariableRef(RefType().setDest("AUTOSAR/Variables/var"))
        proxy.setAutosarVariable(autosar_variable)
        proxy.setAutosarVariable(None)
        assert proxy.getAutosarVariable() == autosar_variable


class TestSwCalprmRefProxy:
    """Test class for SwCalprmRefProxy class."""

    def test_sw_calprm_ref_proxy_initialization(self):
        proxy = SwCalprmRefProxy()
        assert proxy.getArParameter() is None
        assert proxy.getMcDataInstanceRef() is None

    def test_sw_calprm_ref_proxy_methods(self):
        proxy = SwCalprmRefProxy()
        ar_parameter = AutosarParameterRef().setLocalParameterRef(RefType().setDest("AUTOSAR/Parameters/param"))
        mc_data_instance = RefType().setDest("AUTOSAR/McDataInstances/inst")

        assert proxy.setArParameter(ar_parameter) == proxy
        assert proxy.getArParameter() == ar_parameter
        assert proxy.setMcDataInstanceRef(mc_data_instance) == proxy
        assert proxy.getMcDataInstanceRef() == mc_data_instance

    def test_sw_calprm_ref_proxy_none_noop(self):
        proxy = SwCalprmRefProxy()
        ar_parameter = AutosarParameterRef().setLocalParameterRef(RefType().setDest("AUTOSAR/Parameters/param"))
        proxy.setArParameter(ar_parameter)
        proxy.setArParameter(None)
        assert proxy.getArParameter() == ar_parameter
