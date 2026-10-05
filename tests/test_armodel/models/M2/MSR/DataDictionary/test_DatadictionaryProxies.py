import ast
import os
import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarParameterRef, AutosarVariableRef
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy


class TestSwVariableRefProxy:
    """Test class for SwVariableRefProxy class (SWCT Table 5.57, p.370, R23-11)."""

    SPEC_MEMBER_ORDER = ["autosarVariable", "mcDataInstanceVarRef"]

    SPEC_CLASS_NOTE = "Proxy class for several kinds of references to a variable."

    SPEC_NOTES = {
        "autosarVariable": "This represents the reference to a Variable in an Autosar system. Note that the target of the reference within AutosarVariableRef shall be typed by a primitive data type",
        "mcDataInstanceVarRef": "This reference is used in the McSupport file to express the final instance of input values etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a VariableDataPrototype.",
    }

    def _proxy_class(self) -> ast.ClassDef:
        src = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "..",
            "..",
            "src",
            "armodel",
            "models",
            "M2",
            "MSR",
            "DataDictionary",
            "DatadictionaryProxies.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        return next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwVariableRefProxy")

    def _init_field_order(self) -> list:
        init = next(n for n in self._proxy_class().body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_variable_ref_proxy_class_note_verbatim(self):
        """The class docstring carries the Table 5.57 Note verbatim."""
        assert cleandoc(SwVariableRefProxy.__doc__) == self.SPEC_CLASS_NOTE

    def test_sw_variable_ref_proxy_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.57 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_variable_ref_proxy_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; 0..1 scalars getter-first (Rule 0001.11)."""
        expected = [
            "getAutosarVariable",
            "setAutosarVariable",
            "getMcDataInstanceVarRef",
            "setMcDataInstanceVarRef",
        ]
        source_order = [n.name for n in self._proxy_class().body if isinstance(n, ast.FunctionDef) and n.name != "__init__"]
        assert source_order == expected
        for name in expected:
            assert hasattr(SwVariableRefProxy, name), f"missing accessor {name}"

    def test_sw_variable_ref_proxy_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getAutosarVariable", "setAutosarVariable", "getMcDataInstanceVarRef", "setMcDataInstanceVarRef"):
            hints = typing.get_type_hints(getattr(SwVariableRefProxy, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwVariableRefProxy.setAutosarVariable)["value"] == typing.Optional[AutosarVariableRef]
        assert typing.get_type_hints(SwVariableRefProxy.getAutosarVariable)["return"] == typing.Optional[AutosarVariableRef]
        assert typing.get_type_hints(SwVariableRefProxy.setMcDataInstanceVarRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwVariableRefProxy.getMcDataInstanceVarRef)["return"] == typing.Optional[RefType]

    def test_sw_variable_ref_proxy_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.57 Notes verbatim (no trailing period on the autosarVariable Note — verbatim from the markdown); setters append the None-no-op sentence."""
        assert cleandoc(SwVariableRefProxy.getAutosarVariable.__doc__) == self.SPEC_NOTES["autosarVariable"]
        assert cleandoc(SwVariableRefProxy.setAutosarVariable.__doc__) == (self.SPEC_NOTES["autosarVariable"] + " A None value is a no-op and does not overwrite an existing autosarVariable.")
        assert cleandoc(SwVariableRefProxy.getMcDataInstanceVarRef.__doc__) == self.SPEC_NOTES["mcDataInstanceVarRef"]
        assert cleandoc(SwVariableRefProxy.setMcDataInstanceVarRef.__doc__) == (
            self.SPEC_NOTES["mcDataInstanceVarRef"] + " A None value is a no-op and does not overwrite an existing mcDataInstanceVarRef."
        )

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
        mc_data_instance_var = RefType().setDest("AUTOSAR/McDataInstances/inst")
        proxy.setAutosarVariable(autosar_variable)
        proxy.setMcDataInstanceVarRef(mc_data_instance_var)

        assert proxy.setAutosarVariable(None) is proxy
        assert proxy.setMcDataInstanceVarRef(None) is proxy
        assert proxy.getAutosarVariable() is autosar_variable
        assert proxy.getMcDataInstanceVarRef() is mc_data_instance_var


class TestSwCalprmRefProxy:
    """Test class for SwCalprmRefProxy class (SWCT Table 5.56, p.370, R23-11)."""

    SPEC_MEMBER_ORDER = ["arParameter", "mcDataInstanceRef"]

    SPEC_CLASS_NOTE = "Wrapper class for different kinds of references to a calibration parameter."

    SPEC_NOTES = {
        "arParameter": "This represents a Parameter within AUTOSAR. Note that the Datatype of the referenced ParameterDataPrototype shall be an ApplicationDataType of category VALUE.",
        "mcDataInstanceRef": "This reference is used in the McSupport file to express the final instance of group axis etc. It is not allowed to use this outside of an McDataInstance. The referenced mcDataInstance shall be originated from a ParameterDataPrototype.",
    }

    def _proxy_class(self) -> ast.ClassDef:
        src = os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "..",
            "..",
            "src",
            "armodel",
            "models",
            "M2",
            "MSR",
            "DataDictionary",
            "DatadictionaryProxies.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        return next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwCalprmRefProxy")

    def _init_field_order(self) -> list:
        init = next(n for n in self._proxy_class().body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_calprm_ref_proxy_class_note_verbatim(self):
        """The class docstring carries the Table 5.56 Note verbatim."""
        assert cleandoc(SwCalprmRefProxy.__doc__) == self.SPEC_CLASS_NOTE

    def test_sw_calprm_ref_proxy_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.56 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_calprm_ref_proxy_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; 0..1 scalars getter-first (Rule 0001.11)."""
        expected = [
            "getArParameter",
            "setArParameter",
            "getMcDataInstanceRef",
            "setMcDataInstanceRef",
        ]
        source_order = [n.name for n in self._proxy_class().body if isinstance(n, ast.FunctionDef) and n.name != "__init__"]
        assert source_order == expected
        for name in expected:
            assert hasattr(SwCalprmRefProxy, name), f"missing accessor {name}"

    def test_sw_calprm_ref_proxy_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getArParameter", "setArParameter", "getMcDataInstanceRef", "setMcDataInstanceRef"):
            hints = typing.get_type_hints(getattr(SwCalprmRefProxy, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwCalprmRefProxy.setArParameter)["value"] == typing.Optional[AutosarParameterRef]
        assert typing.get_type_hints(SwCalprmRefProxy.getArParameter)["return"] == typing.Optional[AutosarParameterRef]
        assert typing.get_type_hints(SwCalprmRefProxy.setMcDataInstanceRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwCalprmRefProxy.getMcDataInstanceRef)["return"] == typing.Optional[RefType]

    def test_sw_calprm_ref_proxy_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.56 Notes verbatim; setters append the None-no-op sentence."""
        assert cleandoc(SwCalprmRefProxy.getArParameter.__doc__) == self.SPEC_NOTES["arParameter"]
        assert cleandoc(SwCalprmRefProxy.setArParameter.__doc__) == (self.SPEC_NOTES["arParameter"] + " A None value is a no-op and does not overwrite an existing arParameter.")
        assert cleandoc(SwCalprmRefProxy.getMcDataInstanceRef.__doc__) == self.SPEC_NOTES["mcDataInstanceRef"]
        assert cleandoc(SwCalprmRefProxy.setMcDataInstanceRef.__doc__) == (self.SPEC_NOTES["mcDataInstanceRef"] + " A None value is a no-op and does not overwrite an existing mcDataInstanceRef.")

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
        mc_data_instance = RefType().setDest("AUTOSAR/McDataInstances/inst")
        proxy.setArParameter(ar_parameter)
        proxy.setMcDataInstanceRef(mc_data_instance)

        assert proxy.setArParameter(None) is proxy
        assert proxy.setMcDataInstanceRef(None) is proxy
        assert proxy.getArParameter() is ar_parameter
        assert proxy.getMcDataInstanceRef() is mc_data_instance
