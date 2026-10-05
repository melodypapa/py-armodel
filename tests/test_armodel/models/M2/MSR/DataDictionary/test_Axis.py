"""
This module contains tests for the Axis module in MSR.DataDictionary.
"""

import ast
import os
import typing
from inspect import cleandoc

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, Numerical, RefType
from armodel.models.M2.MSR.DataDictionary.Axis import (
    SwAxisGeneric,
    SwAxisGrouped,
    SwAxisIndividual,
    SwGenericAxisParam,
    SwGenericAxisParamType,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies import SwCalprmRefProxy, SwVariableRefProxy
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class TestSwGenericAxisParam:
    """Test class for SwGenericAxisParam class."""

    def test_sw_generic_axis_param_initialization(self):
        """Test that a SwGenericAxisParam object can be initialized with default values."""
        sw_generic_axis_param = SwGenericAxisParam()
        assert sw_generic_axis_param.swGenericAxisParamTypeRef is None
        assert sw_generic_axis_param.vfs == []

    def test_sw_generic_axis_param_type_ref_methods(self):
        """Test the swGenericAxisParamTypeRef getter and setter."""
        sw_generic_axis_param = SwGenericAxisParam()
        ref = RefType()

        result = sw_generic_axis_param.setSwGenericAxisParamTypeRef(ref)
        assert sw_generic_axis_param.getSwGenericAxisParamTypeRef() == ref
        assert result == sw_generic_axis_param

    def test_sw_generic_axis_param_vfs_methods(self):
        """Test adding and getting numerical values."""
        sw_generic_axis_param = SwGenericAxisParam()
        value = Numerical()
        value.setValue("1.5")

        result = sw_generic_axis_param.addVf(value)
        vfs = sw_generic_axis_param.getVfs()
        assert value in vfs
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
