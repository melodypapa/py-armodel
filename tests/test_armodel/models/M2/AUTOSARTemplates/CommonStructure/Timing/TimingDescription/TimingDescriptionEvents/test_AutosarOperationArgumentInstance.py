"""
This module contains tests for the AutosarOperationArgumentInstance class in the
AUTOSAR CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression module.
"""

import inspect
import re
import typing

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents.TDEventOccurrenceExpression import (
    AutosarOperationArgumentInstance,
    OperationArgumentInComponentInstanceRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable


class TestAutosarOperationArgumentInstance:
    """
    Test class for AutosarOperationArgumentInstance functionality.
    """

    def _parent(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        return document.createARPackage("AUTOSAR")

    def test_initialization(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        assert isinstance(obj, AutosarOperationArgumentInstance)
        assert obj.getShortName() == "Arg1"
        assert obj.getOperationArgumentInstanceIRef() is None

    def test_set_operation_argument_instance_iref(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        iref = OperationArgumentInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        assert obj.setOperationArgumentInstanceIRef(iref) is obj
        assert obj.getOperationArgumentInstanceIRef() is iref
        assert isinstance(obj.getOperationArgumentInstanceIRef(), OperationArgumentInComponentInstanceRef)

    def test_set_operation_argument_instance_iref_none_noop(self):
        parent = self._parent()
        obj = AutosarOperationArgumentInstance(parent, "Arg1")
        iref = OperationArgumentInComponentInstanceRef()
        iref.setTargetDataPrototypeRef(RefType().setValue("/Pkg/DP").setDest("DATA-PROTOTYPE"))
        obj.setOperationArgumentInstanceIRef(iref)
        assert obj.setOperationArgumentInstanceIRef(None) is obj
        assert obj.getOperationArgumentInstanceIRef() is iref


class TestAutosarOperationArgumentInstanceSpecContract:
    """Table 3.53 (AUTOSAR_CP_TPS_TimingExtensions, p.85) spec contract
    for AutosarOperationArgumentInstance."""

    def test_class_docstring_verbatim(self):
        """
        Test that the class docstring is the Table 3.53 Note verbatim (the
        markdown's second-bullet wrap artifact "ClientServer Interface" — space
        inside the class name, absent from the first bullet — normalized by
        dropping the artifact space; the XSD group documentation
        (AUTOSAR-OPERATION-ARGUMENT-INSTANCE, AUTOSAR_00052.xsd) canonicalizes
        both bullets as "ClientServerInterface").
        """
        assert AutosarOperationArgumentInstance.__doc__.strip() == (
            "This class represents a reference to an argument instance. This way it is possible to reference an argument instance in the occurrence expression formula. "
            "The argument instance can target to one of the following arguments: "
            "• a whole argument used in an operation of a PortPrototype with ClientServerInterface "
            "• an element inside of a composite argument used in an operation of a PortPrototype with ClientServerInterface"
        )

    def test_init_has_no_docstring(self):
        """
        Test that __init__ has no docstring (spec Notes live in inline member comments).
        """
        assert AutosarOperationArgumentInstance.__init__.__doc__ is None

    def test_base_is_identifiable(self):
        """
        Test that the Base per Table 3.53 is Identifiable (most-derived —
        ARObject , Identifiable , MultilanguageReferrable , Referrable; the XSD
        complexType AUTOSAR-OPERATION-ARGUMENT-INSTANCE composes AR-OBJECT →
        REFERRABLE → MULTILANGUAGE-REFERRABLE → IDENTIFIABLE → own group). The
        VariationPointCapable mixin models the XSD own group's optional
        VARIATION-POINT element (atpVariation, applicable only for
        TimingExtensionResource.timingArgument) — the stamped sibling
        AutosarVariableInstance (Table 3.52) carries the same shape.
        """
        assert issubclass(AutosarOperationArgumentInstance, Identifiable)
        assert issubclass(AutosarOperationArgumentInstance, VariationPointCapable)

    def test_operation_argument_instance_iref_typed_optional_iref(self):
        """
        Test that operationArgumentInstance (DataPrototype, 0..1, iref) maps to
        an Optional[OperationArgumentInComponentInstanceRef] accessor pair
        (Kind-suffix IRef per Rule 0001.5; the XSD declares the element
        OPERATION-ARGUMENT-INSTANCE-IREF of type
        OPERATION-ARGUMENT-IN-COMPONENT-INSTANCE-REF).
        """
        getter_hints = typing.get_type_hints(AutosarOperationArgumentInstance.getOperationArgumentInstanceIRef)
        assert getter_hints.get("return") == typing.Optional[OperationArgumentInComponentInstanceRef]

        setter_hints = typing.get_type_hints(AutosarOperationArgumentInstance.setOperationArgumentInstanceIRef)
        assert setter_hints.get("value") == typing.Optional[OperationArgumentInComponentInstanceRef]
        assert setter_hints.get("return") is AutosarOperationArgumentInstance

    def test_member_order_matches_markdown_displayed_order(self):
        """
        Test that the __init__ declares exactly the single Table 3.53 attribute
        field (operationArgumentInstance → operationArgumentInstanceIRef), in
        the markdown displayed row order — no extra fields (Rule 0001.11).
        """
        init_source = inspect.getsource(AutosarOperationArgumentInstance.__init__)
        assert re.findall(r"self\.(\w+):", init_source) == ["operationArgumentInstanceIRef"]

    def test_accessor_order_matches_markdown_displayed_order(self):
        """
        Test that the accessor definition order follows the Table 3.53 markdown
        displayed row order (get/set per attribute).
        """
        class_source = inspect.getsource(AutosarOperationArgumentInstance)
        accessors = (
            "getOperationArgumentInstanceIRef",
            "setOperationArgumentInstanceIRef",
        )
        assert re.findall(r"def (get\w+|set\w+)\(", class_source) == list(accessors)

    def test_getter_docstring_is_note_verbatim(self):
        """
        Test that the getter docstring is the Table 3.53 attribute Note verbatim
        (the markdown's wrap artifact "OperationArgumentIn
        ComponentInstanceRef" — space inside the class name — normalized by
        dropping the artifact space).
        """
        assert (
            AutosarOperationArgumentInstance.getOperationArgumentInstanceIRef.__doc__.strip()
            == "This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef"
        )

    def test_setter_docstring_is_note_with_none_noop(self):
        """
        Test that the setter docstring is the Table 3.53 attribute Note verbatim
        (no terminal punctuation added — the SynchronizationTimingConstraint
        addScopeEvent family form) plus the appended None-no-op sentence.
        """
        assert (
            AutosarOperationArgumentInstance.setOperationArgumentInstanceIRef.__doc__.strip()
            == "This is the reference to the instanceRef definition. InstanceRef implemented by: OperationArgumentInComponentInstanceRef A None value is a no-op and does not overwrite an existing operationArgumentInstanceIRef."
        )
