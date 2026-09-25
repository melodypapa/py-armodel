"""
This module contains comprehensive tests for the DataElements module in SWComponentTemplate.SwcInternalBehavior.
Tests cover all classes and methods in the DataElements.py file to achieve 100% test coverage.
"""

import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    ArVariableInImplementationDataInstanceRef,
    AutosarParameterRef,
    AutosarVariableRef,
    ParameterAccess,
    VariableAccess,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import (
    ParameterInAtomicSWCTypeInstanceRef,
    VariableInAtomicSWCTypeInstanceRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestParameterAccess:
    """Test class for ParameterAccess class."""

    def test_initialization(self):
        """Test ParameterAccess initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        assert param_access.parent == ar_root
        assert param_access.short_name == "TestParameterAccess"
        assert param_access.returnValueProvision is None
        assert param_access.accessedParameter is None
        assert param_access.swDataDefProps is None

    def test_get_set_accessedParameter(self):
        """Test accessedParameter round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import ParameterInAtomicSWCTypeInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        param_ref = AutosarParameterRef()
        iref = ParameterInAtomicSWCTypeInstanceRef()
        target_ref = RefType()
        target_ref.setValue("/Prm")
        iref.setTargetDataPrototypeRef(target_ref)
        param_ref.setAutosarParameterIRef(iref)

        assert param_access.setAccessedParameter(param_ref) is param_access
        assert param_access.getAccessedParameter() is param_ref
        assert param_access.getAccessedParameter().getAutosarParameterIRef().getTargetDataPrototypeRef().getValue() == "/Prm"

        assert param_access.setAccessedParameter(None) is param_access
        assert param_access.getAccessedParameter() is param_ref

        hints = typing.get_type_hints(ParameterAccess.setAccessedParameter)
        assert hints.get("value") == typing.Optional[AutosarParameterRef]
        assert hints.get("return") is ParameterAccess
        assert typing.get_type_hints(ParameterAccess.getAccessedParameter).get("return") == typing.Optional[AutosarParameterRef]

    def test_get_set_swDataDefProps(self):
        """Test swDataDefProps round-trip, None no-op and type hints."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        param_access = ParameterAccess(ar_root, "TestParameterAccess")

        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        props = SwDataDefProps()
        access_literal = ARLiteral()
        access_literal.setValue("notAccessible")
        props.setSwCalibrationAccess(access_literal)

        assert param_access.setSwDataDefProps(props) is param_access
        assert param_access.getSwDataDefProps() is props
        assert param_access.getSwDataDefProps().getSwCalibrationAccess().getValue() == "notAccessible"

        assert param_access.setSwDataDefProps(None) is param_access
        assert param_access.getSwDataDefProps() is props

        hints = typing.get_type_hints(ParameterAccess.setSwDataDefProps)
        assert hints.get("value") == typing.Optional[SwDataDefProps]
        assert hints.get("return") is ParameterAccess
        assert typing.get_type_hints(ParameterAccess.getSwDataDefProps).get("return") == typing.Optional[SwDataDefProps]


class TestVariableAccess:
    """Test class for VariableAccess class."""

    def test_initialization(self):
        """Test VariableAccess initialization defaults."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        assert var_access.parent == ar_root
        assert var_access.short_name == "TestVariableAccess"
        assert var_access.returnValueProvision is None
        assert var_access.accessedVariable is None
        assert var_access.scope is None

    def test_get_set_accessedVariable(self):
        """Test accessedVariable round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.InstanceRefsUsage import VariableInAtomicSWCTypeInstanceRef

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        var_ref = AutosarVariableRef()
        iref = VariableInAtomicSWCTypeInstanceRef()
        target_ref = RefType()
        target_ref.setValue("/Var")
        iref.setTargetDataPrototypeRef(target_ref)
        var_ref.setAutosarVariableIRef(iref)

        assert var_access.setAccessedVariable(var_ref) is var_access
        assert var_access.getAccessedVariable() is var_ref
        assert var_access.getAccessedVariable().getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/Var"

        assert var_access.setAccessedVariable(None) is var_access
        assert var_access.getAccessedVariable() is var_ref

        hints = typing.get_type_hints(VariableAccess.setAccessedVariable)
        assert hints.get("value") == typing.Optional[AutosarVariableRef]
        assert hints.get("return") is VariableAccess
        assert typing.get_type_hints(VariableAccess.getAccessedVariable).get("return") == typing.Optional[AutosarVariableRef]

    def test_get_set_scope(self):
        """Test scope round-trip, None no-op and type hints."""
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral

        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        var_access = VariableAccess(ar_root, "TestVariableAccess")

        scope = ARLiteral()
        scope.setValue("communicationIntraPartition")

        assert var_access.setScope(scope) is var_access
        assert var_access.getScope() is scope
        assert var_access.getScope().getValue() == "communicationIntraPartition"

        assert var_access.setScope(None) is var_access
        assert var_access.getScope() is scope

        hints = typing.get_type_hints(VariableAccess.setScope)
        assert hints.get("value") == typing.Optional[ARLiteral]
        assert hints.get("return") is VariableAccess
        assert typing.get_type_hints(VariableAccess.getScope).get("return") == typing.Optional[ARLiteral]


PARAMETER_CLASS_NOTE = (
    "This class represents a reference to a parameter within AUTOSAR which can be one of the following use cases: "
    "localParameter: • localParameter which is used as whole (e.g. sharedAxis for curve) "
    "autosarVariable: • a parameter provided via PortPrototype which is used as whole (e.g. parameterAccess) "
    "• an element inside of a composite local parameter typed by ApplicationDatatype (e.g. sharedAxis for a curve) "
    "• an element inside of a composite parameter provided via Port and typed by ApplicationDatatype (e.g. sharedAxis for a curve) "  # noqa E501
    "autosarParameterInImplDatatype: "
    "• an element inside of a composite local parameter typed by ImplementationDatatype "
    "• an element inside of a composite parameter provided via PortPrototype and typed by ImplementationDatatype"  # noqa E501
)

AUTOSAR_PARAMETER_NOTE = (
    "This instance reference is used if the calibration parameter is either imported via a port or is part of a composite data structure. "
    "InstanceRef implemented by: ParameterInAtomicSWCTypeInstanceRef"
)

LOCAL_PARAMETER_NOTE = (
    "In the majority of cases this reference goes to ParameterDataPrototypes rather than VariableDataPrototypes. "  # noqa E501
    "Pointing the reference to a VariableDataPrototype is limited to special use cases, e.g. if the AutosarParameterRef is used in the context of an SwAxisGrouped. "  # noqa E501
    "This reference is used if the arParameter is local to the current component. "
    "Of course, it would technically also be feasible to use an InstanceRef for this case. However, the InstanceRef would not have a contextElement (because the current instance is the context). "  # noqa E501
    "Hence, the local instance is a special case which may provide further optimization. Therefore an explicit reference is provided for this case."  # noqa E501
)


class TestAutosarParameterRef:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 5.34)"""
        assert AutosarParameterRef.__doc__.strip() == PARAMETER_CLASS_NOTE
        assert AutosarParameterRef.getAutosarParameterIRef.__doc__.strip() == AUTOSAR_PARAMETER_NOTE
        assert AutosarParameterRef.setAutosarParameterIRef.__doc__.strip() == (AUTOSAR_PARAMETER_NOTE + ". A None value is a no-op and does not overwrite an existing autosarParameterIRef.")
        assert AutosarParameterRef.getLocalParameterRef.__doc__.strip() == LOCAL_PARAMETER_NOTE
        assert AutosarParameterRef.setLocalParameterRef.__doc__.strip() == (LOCAL_PARAMETER_NOTE + " A None value is a no-op and does not overwrite an existing localParameterRef.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        assert issubclass(AutosarParameterRef, ARObject)
        ref = AutosarParameterRef()
        assert ref.autosarParameterIRef is None
        assert ref.localParameterRef is None

        hints = typing.get_type_hints(AutosarParameterRef.getAutosarParameterIRef)
        assert hints["return"] == typing.Optional[ParameterInAtomicSWCTypeInstanceRef]
        hints = typing.get_type_hints(AutosarParameterRef.setAutosarParameterIRef)
        assert hints["value"] == typing.Optional[ParameterInAtomicSWCTypeInstanceRef]
        assert hints["return"] is AutosarParameterRef
        hints = typing.get_type_hints(AutosarParameterRef.getLocalParameterRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(AutosarParameterRef.setLocalParameterRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is AutosarParameterRef

    def test_initialization(self):
        """Test AutosarParameterRef initialization"""
        ref = AutosarParameterRef()

        assert ref is not None
        assert ref.autosarParameterIRef is None
        assert ref.localParameterRef is None

    def test_get_set_autosar_parameter_iref(self):
        """Test getAutosarParameterIRef and setAutosarParameterIRef methods"""
        ref = AutosarParameterRef()

        assert ref.getAutosarParameterIRef() is None
        iref = ParameterInAtomicSWCTypeInstanceRef()
        target = RefType()
        target.setValue("/SwcInternalBehavior/ParameterDataPrototype")
        iref.setTargetDataPrototypeRef(target)
        assert ref.setAutosarParameterIRef(iref) is ref
        assert ref.getAutosarParameterIRef() is iref
        assert isinstance(ref.getAutosarParameterIRef(), ParameterInAtomicSWCTypeInstanceRef)
        assert ref.getAutosarParameterIRef().getTargetDataPrototypeRef() is target
        ref.setAutosarParameterIRef(None)
        assert ref.getAutosarParameterIRef() is iref

    def test_get_set_local_parameter_ref(self):
        """Test getLocalParameterRef and setLocalParameterRef methods"""
        ref = AutosarParameterRef()

        assert ref.getLocalParameterRef() is None
        local_ref = RefType()
        local_ref.setValue("/SwcInternalBehavior/LocalParameterDataPrototype")
        assert ref.setLocalParameterRef(local_ref) is ref
        assert ref.getLocalParameterRef() is local_ref
        assert isinstance(ref.getLocalParameterRef(), RefType)
        assert ref.getLocalParameterRef().getValue() == "/SwcInternalBehavior/LocalParameterDataPrototype"
        ref.setLocalParameterRef(None)
        assert ref.getLocalParameterRef() is local_ref


CLASS_NOTE = (
    "This class represents a reference to a variable within AUTOSAR which can be one of the following use cases: "
    "localVariable: • localVariable which is used as whole (e.g. InterRunnableVariable, inputValue for curve) "
    "autosarVariable: • a variable provided via Port which is used as whole (e.g. dataAccesspoints) "
    "• an element inside of a composite local variable typed by ApplicationDatatype (e.g. inputValue for a curve) "
    "• an element inside of a composite variable provided via Port and typed by ApplicationDatatype (e.g. inputValue for a curve) "  # noqa E501
    "autosarVariableInImplDatatype: "
    "• an element inside of a composite local variable typed by ImplementationDatatype (e.g. nvramData mapping) "
    "• an element inside of a composite variable provided via Port and typed by ImplementationDatatype (e.g. inputValue for a curve)"  # noqa E501
)

AUTOSAR_VARIABLE_NOTE = "This references a variable which is provided by a port and/or which is part of a CompositeDataType. " "InstanceRef implemented by: VariableInAtomicSWCTypeInstanceRef"

IMPL_DATATYPE_NOTE = "This is used if the target variable is inside of variableDataPrototype typed by an ImplementationDataType."

LOCAL_VARIABLE_NOTE = (
    "This reference is used if the variable is local to the current component. It would also be possible to use the instance refence here. "  # noqa E501
    "Such an instance ref would not have a contextElement, since the current instance is the context. "
    "But the local instance is a special case which may provide further optimization. Therefore an explicit reference is provided for this case."  # noqa E501
)


class TestAutosarVariableRef:
    def test_spec_notes_are_verbatim(self):
        """Test that the class docstring and every accessor docstring is the spec Note verbatim (Table 5.33)"""
        assert AutosarVariableRef.__doc__.strip() == CLASS_NOTE
        assert AutosarVariableRef.getAutosarVariableIRef.__doc__.strip() == AUTOSAR_VARIABLE_NOTE
        assert AutosarVariableRef.setAutosarVariableIRef.__doc__.strip() == (AUTOSAR_VARIABLE_NOTE + ". A None value is a no-op and does not overwrite an existing autosarVariableIRef.")
        assert AutosarVariableRef.getAutosarVariableInImplDatatype.__doc__.strip() == IMPL_DATATYPE_NOTE
        assert AutosarVariableRef.setAutosarVariableInImplDatatype.__doc__.strip() == (
            IMPL_DATATYPE_NOTE + " A None value is a no-op and does not overwrite an existing autosarVariableInImplDatatype."
        )
        assert AutosarVariableRef.getLocalVariableRef.__doc__.strip() == LOCAL_VARIABLE_NOTE
        assert AutosarVariableRef.setLocalVariableRef.__doc__.strip() == (LOCAL_VARIABLE_NOTE + " A None value is a no-op and does not overwrite an existing localVariableRef.")

    def test_base_shape(self):
        """Test the base chain, no-arg __init__ and typed accessor signatures"""
        assert issubclass(AutosarVariableRef, ARObject)
        ref = AutosarVariableRef()
        assert ref.autosarVariableIRef is None
        assert ref.autosarVariableInImplDatatype is None
        assert ref.localVariableRef is None

        hints = typing.get_type_hints(AutosarVariableRef.getAutosarVariableIRef)
        assert hints["return"] == typing.Optional[VariableInAtomicSWCTypeInstanceRef]
        hints = typing.get_type_hints(AutosarVariableRef.setAutosarVariableIRef)
        assert hints["value"] == typing.Optional[VariableInAtomicSWCTypeInstanceRef]
        assert hints["return"] is AutosarVariableRef
        hints = typing.get_type_hints(AutosarVariableRef.getAutosarVariableInImplDatatype)
        assert hints["return"] == typing.Optional[ArVariableInImplementationDataInstanceRef]
        hints = typing.get_type_hints(AutosarVariableRef.setAutosarVariableInImplDatatype)
        assert hints["value"] == typing.Optional[ArVariableInImplementationDataInstanceRef]
        assert hints["return"] is AutosarVariableRef
        hints = typing.get_type_hints(AutosarVariableRef.getLocalVariableRef)
        assert hints["return"] == typing.Optional[RefType]
        hints = typing.get_type_hints(AutosarVariableRef.setLocalVariableRef)
        assert hints["value"] == typing.Optional[RefType]
        assert hints["return"] is AutosarVariableRef

    def test_initialization(self):
        """Test AutosarVariableRef initialization"""
        ref = AutosarVariableRef()

        assert ref is not None
        assert ref.autosarVariableIRef is None
        assert ref.autosarVariableInImplDatatype is None
        assert ref.localVariableRef is None

    def test_get_set_autosar_variable_iref(self):
        """Test getAutosarVariableIRef and setAutosarVariableIRef methods"""
        ref = AutosarVariableRef()

        assert ref.getAutosarVariableIRef() is None
        iref = VariableInAtomicSWCTypeInstanceRef()
        target = RefType()
        target.setValue("/SwcInternalBehavior/VariableDataPrototype")
        iref.setTargetDataPrototypeRef(target)
        assert ref.setAutosarVariableIRef(iref) is ref
        assert ref.getAutosarVariableIRef() is iref
        assert isinstance(ref.getAutosarVariableIRef(), VariableInAtomicSWCTypeInstanceRef)
        assert ref.getAutosarVariableIRef().getTargetDataPrototypeRef() is target
        ref.setAutosarVariableIRef(None)
        assert ref.getAutosarVariableIRef() is iref

    def test_get_set_autosar_variable_in_impl_datatype(self):
        """Test getAutosarVariableInImplDatatype and setAutosarVariableInImplDatatype methods"""
        ref = AutosarVariableRef()

        assert ref.getAutosarVariableInImplDatatype() is None
        impl_ref = ArVariableInImplementationDataInstanceRef()
        root = RefType()
        root.setValue("/SwcInternalBehavior/RootVariableDataPrototype")
        impl_ref.setRootVariableDataPrototypeRef(root)
        assert ref.setAutosarVariableInImplDatatype(impl_ref) is ref
        assert ref.getAutosarVariableInImplDatatype() is impl_ref
        assert isinstance(ref.getAutosarVariableInImplDatatype(), ArVariableInImplementationDataInstanceRef)
        assert ref.getAutosarVariableInImplDatatype().getRootVariableDataPrototypeRef() is root
        ref.setAutosarVariableInImplDatatype(None)
        assert ref.getAutosarVariableInImplDatatype() is impl_ref

    def test_get_set_local_variable_ref(self):
        """Test getLocalVariableRef and setLocalVariableRef methods"""
        ref = AutosarVariableRef()

        assert ref.getLocalVariableRef() is None
        local_ref = RefType()
        local_ref.setValue("/SwcInternalBehavior/LocalVariableDataPrototype")
        assert ref.setLocalVariableRef(local_ref) is ref
        assert ref.getLocalVariableRef() is local_ref
        assert isinstance(ref.getLocalVariableRef(), RefType)
        assert ref.getLocalVariableRef().getValue() == "/SwcInternalBehavior/LocalVariableDataPrototype"
        ref.setLocalVariableRef(None)
        assert ref.getLocalVariableRef() is local_ref
