"""
This module contains tests for the Axis module in MSR.DataDictionary.
"""

import ast
import os
import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, Numerical, RefType
from armodel.models.M2.MSR.DataDictionary.Axis import (
    SwAxisGeneric,
    SwAxisGrouped,
    SwAxisIndividual,
    SwAxisType,
    SwGenericAxisParam,
    SwGenericAxisParamType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock


class TestSwGenericAxisParam:
    """Test class for SwGenericAxisParam class (SWCT Table 5.53, p.356, R23-11)."""

    SPEC_MEMBER_ORDER = ["swGenericAxisParamTypeRef", "vfs"]

    SPEC_CLASS_NOTE = (
        "This meta-class describes a specific parameter of a generic axis. The name of the parameter is defined through "
        "a reference to a parameter type defined on a corresponding axis type. The value of the parameter is given here "
        "in case that it is not changeable during calibration. Example is shift / offset in a fixed axis."
    )

    SPEC_NOTES = {
        "swGenericAxisParamTypeRef": (
            "Parameter type defined on a corresponding axis type. References can only be made to axis parameters types "
            "which are defined within the referenced axis type. Tags: xml.sequenceOffset=20"
        ),
        "vfs": (
            "This attribute represents the value of the generic axis parameter. Stereotypes: atpVariation "
            "Tags: vh.latestBindingTime=preCompileTime xml.roleElement=true xml.roleWrapperElement=false "
            "xml.sequenceOffset=30 xml.typeElement=false"
        ),
    }

    def _axis_class(self) -> ast.ClassDef:
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
            "Axis.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        return next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwGenericAxisParam")

    def _init_field_order(self) -> list:
        init = next(n for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_generic_axis_param_class_note_verbatim(self):
        """The class docstring carries the Table 5.53 Note verbatim."""
        assert cleandoc(SwGenericAxisParam.__doc__) == self.SPEC_CLASS_NOTE

    def test_sw_generic_axis_param_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.53 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_generic_axis_param_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; scalars getter-first, lists mutator-first (Rule 0001.11)."""
        expected = [
            "getSwGenericAxisParamTypeRef",
            "setSwGenericAxisParamTypeRef",
            "addVf",
            "getVfs",
        ]
        source_order = [n.name for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name != "__init__"]
        assert source_order == expected
        for name in expected:
            assert hasattr(SwGenericAxisParam, name), f"missing accessor {name}"

    def test_sw_generic_axis_param_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getSwGenericAxisParamTypeRef", "setSwGenericAxisParamTypeRef", "addVf", "getVfs"):
            hints = typing.get_type_hints(getattr(SwGenericAxisParam, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwGenericAxisParam.setSwGenericAxisParamTypeRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwGenericAxisParam.getSwGenericAxisParamTypeRef)["return"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwGenericAxisParam.addVf)["value"] == typing.Optional[Numerical]
        assert typing.get_type_hints(SwGenericAxisParam.getVfs)["return"] == typing.List[Numerical]

    def test_sw_generic_axis_param_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.53 Notes verbatim (Tags:/Stereotypes: tails kept, Rule 0012.2.5.3); mutators append the None-no-op sentence."""
        assert cleandoc(SwGenericAxisParam.getSwGenericAxisParamTypeRef.__doc__) == self.SPEC_NOTES["swGenericAxisParamTypeRef"]
        assert cleandoc(SwGenericAxisParam.setSwGenericAxisParamTypeRef.__doc__) == (
            self.SPEC_NOTES["swGenericAxisParamTypeRef"] + " A None value is a no-op and does not overwrite an existing swGenericAxisParamTypeRef."
        )
        assert cleandoc(SwGenericAxisParam.addVf.__doc__) == (self.SPEC_NOTES["vfs"] + " A None value is a no-op and is not appended to vfs.")
        assert cleandoc(SwGenericAxisParam.getVfs.__doc__) == self.SPEC_NOTES["vfs"]

    def test_sw_generic_axis_param_initialization(self):
        """Test that a SwGenericAxisParam object can be initialized with default values."""
        sw_generic_axis_param = SwGenericAxisParam()
        assert sw_generic_axis_param.swGenericAxisParamTypeRef is None
        assert sw_generic_axis_param.vfs == []

    def test_sw_generic_axis_param_type_ref_methods(self):
        """Test the swGenericAxisParamTypeRef getter and setter."""
        sw_generic_axis_param = SwGenericAxisParam()
        ref = RefType().setValue("/axis/types/fixed/shift")
        ref.setDest("SW-GENERIC-AXIS-PARAM-TYPE")

        result = sw_generic_axis_param.setSwGenericAxisParamTypeRef(ref)
        assert sw_generic_axis_param.getSwGenericAxisParamTypeRef() == ref
        assert result == sw_generic_axis_param

    def test_sw_generic_axis_param_type_ref_setter_none_noop(self):
        """Test that setSwGenericAxisParamTypeRef(None) does not overwrite an existing reference."""
        sw_generic_axis_param = SwGenericAxisParam()
        ref = RefType().setValue("/axis/types/fixed/shift")

        assert sw_generic_axis_param.setSwGenericAxisParamTypeRef(ref) is sw_generic_axis_param
        assert sw_generic_axis_param.setSwGenericAxisParamTypeRef(None) is sw_generic_axis_param
        assert sw_generic_axis_param.getSwGenericAxisParamTypeRef() is ref

    def test_sw_generic_axis_param_vfs_methods(self):
        """Test adding and getting numerical values."""
        sw_generic_axis_param = SwGenericAxisParam()
        first = Numerical().setValue("1.5")
        second = Numerical().setValue("2.5")

        result = sw_generic_axis_param.addVf(first)
        sw_generic_axis_param.addVf(second)
        vfs = sw_generic_axis_param.getVfs()
        assert vfs == [first, second]
        assert result == sw_generic_axis_param

    def test_sw_generic_axis_param_vfs_none_noop(self):
        """Test that addVf(None) is a no-op."""
        sw_generic_axis_param = SwGenericAxisParam()
        result = sw_generic_axis_param.addVf(None)
        assert sw_generic_axis_param.getVfs() == []
        assert result == sw_generic_axis_param


class TestSwAxisGeneric:
    """Test class for SwAxisGeneric class (SWCT Table 5.51, p.355, R23-11)."""

    SPEC_MEMBER_ORDER = ["swAxisTypeRef", "swGenericAxisParams"]

    SPEC_CLASS_NOTE = (
        "This meta-class defines a generic axis. In a generic axis the axispoints points are calculated in the ECU. "
        "The ECU is equipped with a fixed calculation algorithm. Parameters for the algorithm can be stored in the "
        "data component of the ECU. Therefore these parameters are specified in the data declaration, not in the calibration data."
    )

    SPEC_NOTES = {
        "swAxisTypeRef": "Associated axis calculation strategy.",
        "swGenericAxisParams": "Specific parameter of a generic axis.",
    }

    def _axis_class(self) -> ast.ClassDef:
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
            "Axis.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        return next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwAxisGeneric")

    def _init_field_order(self) -> list:
        init = next(n for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_axis_generic_class_note_verbatim(self):
        """The class docstring carries the Table 5.51 Note verbatim."""
        assert cleandoc(SwAxisGeneric.__doc__) == self.SPEC_CLASS_NOTE

    def test_sw_axis_generic_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.51 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_axis_generic_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; scalars getter-first, lists mutator-first (Rule 0001.11)."""
        expected = [
            "getSwAxisTypeRef",
            "setSwAxisTypeRef",
            "addSwGenericAxisParam",
            "getSwGenericAxisParams",
        ]
        source_order = [n.name for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name != "__init__"]
        assert source_order == expected
        for name in expected:
            assert hasattr(SwAxisGeneric, name), f"missing accessor {name}"

    def test_sw_axis_generic_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getSwAxisTypeRef", "setSwAxisTypeRef", "addSwGenericAxisParam", "getSwGenericAxisParams"):
            hints = typing.get_type_hints(getattr(SwAxisGeneric, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwAxisGeneric.setSwAxisTypeRef)["value"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwAxisGeneric.getSwAxisTypeRef)["return"] == typing.Optional[RefType]
        assert typing.get_type_hints(SwAxisGeneric.addSwGenericAxisParam)["value"] == typing.Optional[SwGenericAxisParam]
        assert typing.get_type_hints(SwAxisGeneric.getSwGenericAxisParams)["return"] == typing.List[SwGenericAxisParam]

    def test_sw_axis_generic_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.51 Notes verbatim; mutators append the None-no-op sentence."""
        assert cleandoc(SwAxisGeneric.getSwAxisTypeRef.__doc__) == self.SPEC_NOTES["swAxisTypeRef"]
        assert cleandoc(SwAxisGeneric.setSwAxisTypeRef.__doc__) == (self.SPEC_NOTES["swAxisTypeRef"] + " A None value is a no-op and does not overwrite an existing swAxisTypeRef.")
        assert cleandoc(SwAxisGeneric.getSwGenericAxisParams.__doc__) == self.SPEC_NOTES["swGenericAxisParams"]
        assert cleandoc(SwAxisGeneric.addSwGenericAxisParam.__doc__) == (self.SPEC_NOTES["swGenericAxisParams"] + " A None value is a no-op and is not appended to swGenericAxisParams.")

    def test_sw_axis_generic_initialization(self):
        """Test that a SwAxisGeneric object can be initialized with default values."""
        sw_axis_generic = SwAxisGeneric()
        assert sw_axis_generic.swAxisTypeRef is None
        assert sw_axis_generic.swGenericAxisParams == []

    def test_sw_axis_type_ref_methods(self):
        """Test the swAxisTypeRef getter and setter."""
        sw_axis_generic = SwAxisGeneric()
        ref = RefType()

        result = sw_axis_generic.setSwAxisTypeRef(ref)
        assert sw_axis_generic.getSwAxisTypeRef() == ref
        assert result == sw_axis_generic

    def test_sw_axis_type_ref_setter_none_noop(self):
        """Test that setSwAxisTypeRef(None) does not overwrite an existing reference."""
        sw_axis_generic = SwAxisGeneric()
        ref = RefType().setValue("/axis/types/fixed")

        assert sw_axis_generic.setSwAxisTypeRef(ref) is sw_axis_generic
        assert sw_axis_generic.setSwAxisTypeRef(None) is sw_axis_generic
        assert sw_axis_generic.getSwAxisTypeRef() is ref

    def test_sw_axis_generic_params_methods(self):
        """Test adding and getting generic axis parameters."""
        sw_axis_generic = SwAxisGeneric()
        param = SwGenericAxisParam()

        result = sw_axis_generic.addSwGenericAxisParam(param)
        params = sw_axis_generic.getSwGenericAxisParams()
        assert param in params
        assert result == sw_axis_generic

    def test_sw_axis_generic_params_are_typed_ordered_and_none_safe(self):
        """Test that parameters land in a dedicated typed list in append order and None is a no-op."""
        sw_axis_generic = SwAxisGeneric()
        first = SwGenericAxisParam()
        second = SwGenericAxisParam()

        assert sw_axis_generic.getSwGenericAxisParams() == []
        assert sw_axis_generic.addSwGenericAxisParam(first) is sw_axis_generic
        assert sw_axis_generic.addSwGenericAxisParam(None) is sw_axis_generic
        assert sw_axis_generic.addSwGenericAxisParam(second) is sw_axis_generic
        assert sw_axis_generic.getSwGenericAxisParams() == [first, second]


class TestSwAxisIndividual:
    """Test class for SwAxisIndividual class."""

    def test_sw_axis_individual_initialization(self):
        """Test that a SwAxisIndividual object can be initialized with default values."""
        sw_axis_individual = SwAxisIndividual()
        assert sw_axis_individual.compuMethodRef is None
        assert sw_axis_individual.dataConstrRef is None
        assert sw_axis_individual.inputVariableTypeRef is None
        assert sw_axis_individual.swAxisGeneric is None
        assert sw_axis_individual.swMaxAxisPoints is None
        assert sw_axis_individual.swMinAxisPoints is None
        assert sw_axis_individual.swVariableRefs == []
        assert sw_axis_individual.unitRef is None

    def test_sw_axis_individual_compu_method_ref_methods(self):
        """Test the compuMethodRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()

        result = sw_axis_individual.setCompuMethodRef(ref)
        assert sw_axis_individual.getCompuMethodRef() == ref
        assert result == sw_axis_individual

    def test_sw_axis_individual_data_constr_ref_methods(self):
        """Test the dataConstrRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()

        result = sw_axis_individual.setDataConstrRef(ref)
        assert sw_axis_individual.getDataConstrRef() == ref
        assert result == sw_axis_individual

    def test_sw_axis_individual_input_variable_type_ref_methods(self):
        """Test the inputVariableTypeRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()

        result = sw_axis_individual.setInputVariableTypeRef(ref)
        assert sw_axis_individual.getInputVariableTypeRef() == ref
        assert result == sw_axis_individual

    def test_sw_axis_individual_sw_axis_generic_methods(self):
        """Test the swAxisGeneric getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        sw_axis_gen = SwAxisGeneric()

        result = sw_axis_individual.setSwAxisGeneric(sw_axis_gen)
        assert sw_axis_individual.getSwAxisGeneric() == sw_axis_gen
        assert result == sw_axis_individual

    def test_sw_axis_individual_max_axis_points_methods(self):
        """Test the swMaxAxisPoints getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        max_points = Numerical()

        result = sw_axis_individual.setSwMaxAxisPoints(max_points)
        assert sw_axis_individual.getSwMaxAxisPoints() == max_points
        assert result == sw_axis_individual

    def test_sw_axis_individual_min_axis_points_methods(self):
        """Test the swMinAxisPoints getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        min_points = Numerical()

        result = sw_axis_individual.setSwMinAxisPoints(min_points)
        assert sw_axis_individual.getSwMinAxisPoints() == min_points
        assert result == sw_axis_individual

    def test_sw_axis_individual_variable_refs_methods(self):
        """Test the swVariableRefs getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        refs = [SwVariableRefProxy(), SwVariableRefProxy()]

        result = sw_axis_individual.addSwVariableRef(refs[0])
        sw_axis_individual.addSwVariableRef(refs[1])
        assert sw_axis_individual.getSwVariableRefs() == refs
        assert result == sw_axis_individual

    def test_sw_axis_individual_unit_ref_methods(self):
        """Test the unitRef getter and setter."""
        sw_axis_individual = SwAxisIndividual()
        ref = RefType()

        result = sw_axis_individual.setUnitRef(ref)
        assert sw_axis_individual.getUnitRef() == ref
        assert result == sw_axis_individual

    def test_sw_axis_individual_variable_refs_are_typed_ordered_and_none_safe(self):
        sw_axis_individual = SwAxisIndividual()
        first = SwVariableRefProxy()
        second = SwVariableRefProxy()

        assert sw_axis_individual.getSwVariableRefs() == []
        assert sw_axis_individual.addSwVariableRef(first) is sw_axis_individual
        assert sw_axis_individual.addSwVariableRef(None) is sw_axis_individual
        assert sw_axis_individual.addSwVariableRef(second) is sw_axis_individual
        assert sw_axis_individual.getSwVariableRefs() == [first, second]

    def test_sw_axis_individual_setters_do_not_overwrite_with_none(self):
        sw_axis_individual = SwAxisIndividual()
        integer = Integer().setValue("4")
        ref = RefType().setValue("/compu")

        sw_axis_individual.setSwMaxAxisPoints(integer)
        sw_axis_individual.setCompuMethodRef(ref)
        sw_axis_individual.setSwMaxAxisPoints(None)
        sw_axis_individual.setCompuMethodRef(None)

        assert sw_axis_individual.getSwMaxAxisPoints() is integer
        assert sw_axis_individual.getCompuMethodRef() is ref


class TestSwAxisType:
    """Test class for SwAxisType class (SWCT Table 5.52, p.356, R23-11)."""

    SPEC_MEMBER_ORDER = ["swGenericAxisDesc", "swGenericAxisParamTypes"]

    SPEC_CLASS_NOTE = (
        "This meta-class represents a specific axis calculation strategy. No formal specification is given, due to "
        "the fact that it is possible to use arbitrary algorithms for calculating axis-points. Instead, the algorithm "
        "is described verbally but the parameters are specified formally with respect to their names and constraints. "
        "As a result, SwAxisType mainly reserves appropriate keywords."
    )

    SPEC_NOTES = {
        "swGenericAxisDesc": "Associated axis description in textual form.",
        "swGenericAxisParamTypes": "Parameters for this calculation algorithm.",
    }

    def _axis_class(self) -> ast.ClassDef:
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
            "Axis.py",
        )
        tree = ast.parse(open(src, encoding="utf-8").read())
        return next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SwAxisType")

    def _init_field_order(self) -> list:
        init = next(n for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name == "__init__")
        return [t.target.attr for t in init.body if isinstance(t, ast.AnnAssign) and isinstance(t.target, ast.Attribute)]

    def test_sw_axis_type_class_note_verbatim(self):
        """The class docstring carries the Table 5.52 Note verbatim."""
        assert cleandoc(SwAxisType.__doc__) == self.SPEC_CLASS_NOTE

    def test_sw_axis_type_member_order(self):
        """Fields in __init__ follow the SWCT Table 5.52 displayed row order (Rule 0001.11)."""
        assert self._init_field_order() == self.SPEC_MEMBER_ORDER

    def test_sw_axis_type_accessors_follow_member_order(self):
        """Accessor groups per attribute, in spec row order; scalars getter-first, lists mutator-first (Rule 0001.11)."""
        expected = [
            "getSwGenericAxisDesc",
            "setSwGenericAxisDesc",
            "createSwGenericAxisParamType",
            "getSwGenericAxisParamTypes",
        ]
        source_order = [n.name for n in self._axis_class().body if isinstance(n, ast.FunctionDef) and n.name != "__init__"]
        assert source_order == expected
        for name in expected:
            assert hasattr(SwAxisType, name), f"missing accessor {name}"

    def test_sw_axis_type_type_hints_resolve(self):
        """Every accessor annotation resolves at runtime (Rule 0003 — no TYPE_CHECKING-only names)."""
        for name in ("getSwGenericAxisDesc", "setSwGenericAxisDesc", "createSwGenericAxisParamType", "getSwGenericAxisParamTypes"):
            hints = typing.get_type_hints(getattr(SwAxisType, name))
            assert hints, f"no annotations resolved for {name}"
            assert "return" in hints
        assert typing.get_type_hints(SwAxisType.setSwGenericAxisDesc)["value"] == typing.Optional[DocumentationBlock]
        assert typing.get_type_hints(SwAxisType.getSwGenericAxisDesc)["return"] == typing.Optional[DocumentationBlock]
        assert typing.get_type_hints(SwAxisType.createSwGenericAxisParamType)["return"] == SwGenericAxisParamType
        assert typing.get_type_hints(SwAxisType.getSwGenericAxisParamTypes)["return"] == typing.List[SwGenericAxisParamType]

    def test_sw_axis_type_accessor_docstrings_verbatim(self):
        """Getter docstrings carry the Table 5.52 Notes verbatim; mutators append the None-no-op sentence."""
        assert cleandoc(SwAxisType.getSwGenericAxisDesc.__doc__) == self.SPEC_NOTES["swGenericAxisDesc"]
        assert cleandoc(SwAxisType.setSwGenericAxisDesc.__doc__) == (self.SPEC_NOTES["swGenericAxisDesc"] + " A None value is a no-op and does not overwrite an existing swGenericAxisDesc.")
        assert cleandoc(SwAxisType.createSwGenericAxisParamType.__doc__) == self.SPEC_NOTES["swGenericAxisParamTypes"]
        assert cleandoc(SwAxisType.getSwGenericAxisParamTypes.__doc__) == self.SPEC_NOTES["swGenericAxisParamTypes"]

    def test_sw_axis_type_initialization(self):
        """Test that a SwAxisType object can be initialized with default values."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")

        assert isinstance(sw_axis_type, ARElement)
        assert sw_axis_type.getShortName() == "axis_type"
        assert sw_axis_type.swGenericAxisDesc is None
        assert sw_axis_type.swGenericAxisParamTypes == []

    def test_sw_axis_type_sw_generic_axis_desc_methods(self):
        """Test the swGenericAxisDesc getter and setter."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")
        desc = DocumentationBlock()

        result = sw_axis_type.setSwGenericAxisDesc(desc)
        assert sw_axis_type.getSwGenericAxisDesc() == desc
        assert result == sw_axis_type

    def test_sw_axis_type_sw_generic_axis_desc_setter_none_noop(self):
        """Test that setSwGenericAxisDesc(None) does not overwrite an existing description."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")
        desc = DocumentationBlock()

        assert sw_axis_type.setSwGenericAxisDesc(desc) is sw_axis_type
        assert sw_axis_type.setSwGenericAxisDesc(None) is sw_axis_type
        assert sw_axis_type.getSwGenericAxisDesc() is desc

    def test_sw_axis_type_param_types_create(self):
        """Test that createSwGenericAxisParamType appends to the dedicated list and returns the instance."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")

        param_type = sw_axis_type.createSwGenericAxisParamType("param_type")
        assert isinstance(param_type, SwGenericAxisParamType)
        assert param_type.getShortName() == "param_type"
        assert sw_axis_type.getSwGenericAxisParamTypes() == [param_type]

    def test_sw_axis_type_param_types_duplicate_returns_existing(self):
        """Test that createSwGenericAxisParamType returns the existing element for a duplicate short name."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")

        first = sw_axis_type.createSwGenericAxisParamType("param_type")
        second = sw_axis_type.createSwGenericAxisParamType("param_type")
        assert first is second
        assert sw_axis_type.getSwGenericAxisParamTypes() == [first]

    def test_sw_axis_type_param_types_are_typed_ordered(self):
        """Test that parameter types land in a dedicated typed list in creation order."""
        sw_axis_type = SwAxisType(parent=AUTOSAR.getInstance(), short_name="axis_type")

        assert sw_axis_type.getSwGenericAxisParamTypes() == []
        first = sw_axis_type.createSwGenericAxisParamType("first")
        second = sw_axis_type.createSwGenericAxisParamType("second")
        assert sw_axis_type.getSwGenericAxisParamTypes() == [first, second]


class TestSwAxisGrouped:
    """Test class for SwAxisGrouped class."""

    def test_sw_axis_grouped_initialization(self):
        """Test that a SwAxisGrouped object can be initialized with default values."""
        sw_axis_grouped = SwAxisGrouped()
        assert sw_axis_grouped.sharedAxisTypeRef is None
        assert sw_axis_grouped.swAxisIndex is None
        assert sw_axis_grouped.swCalprmRef is None

    def test_sw_axis_grouped_shared_axis_type_ref_methods(self):
        """Test the sharedAxisTypeRef getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        ref = RefType()

        result = sw_axis_grouped.setSharedAxisTypeRef(ref)
        assert sw_axis_grouped.getSharedAxisTypeRef() == ref
        assert result == sw_axis_grouped

    def test_sw_axis_grouped_sw_axis_index_methods(self):
        """Test the swAxisIndex getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        index = AxisIndexType()

        result = sw_axis_grouped.setSwAxisIndex(index)
        assert sw_axis_grouped.getSwAxisIndex() == index
        assert result == sw_axis_grouped

    def test_sw_axis_grouped_sw_calprm_ref_methods(self):
        """Test the swCalprmRef getter and setter."""
        sw_axis_grouped = SwAxisGrouped()
        ref = SwCalprmRefProxy()

        result = sw_axis_grouped.setSwCalprmRef(ref)
        assert sw_axis_grouped.getSwCalprmRef() == ref
        assert result == sw_axis_grouped

    def test_sw_axis_grouped_setters_are_typed_and_none_safe(self):
        sw_axis_grouped = SwAxisGrouped()
        shared_ref = RefType().setValue("/types/shared")
        axis_index = AxisIndexType().setValue("1")
        calprm_ref = SwCalprmRefProxy()

        sw_axis_grouped.setSharedAxisTypeRef(shared_ref)
        sw_axis_grouped.setSwAxisIndex(axis_index)
        sw_axis_grouped.setSwCalprmRef(calprm_ref)
        sw_axis_grouped.setSharedAxisTypeRef(None)
        sw_axis_grouped.setSwAxisIndex(None)
        sw_axis_grouped.setSwCalprmRef(None)

        assert sw_axis_grouped.getSharedAxisTypeRef() is shared_ref
        assert sw_axis_grouped.getSwAxisIndex() is axis_index
        assert sw_axis_grouped.getSwCalprmRef() is calprm_ref


class TestSwGenericAxisParamType:
    def test_sw_generic_axis_param_type_initialization(self):
        param_type = SwGenericAxisParamType(parent=AUTOSAR.getInstance(), short_name="param")

        assert param_type.getDataConstrRef() is None

    def test_sw_generic_axis_param_type_data_constr_ref_is_none_safe(self):
        param_type = SwGenericAxisParamType(parent=AUTOSAR.getInstance(), short_name="param")
        ref = RefType().setValue("/constraints/axis")

        assert param_type.setDataConstrRef(ref) is param_type
        assert param_type.setDataConstrRef(None) is param_type
        assert param_type.getDataConstrRef() is ref
