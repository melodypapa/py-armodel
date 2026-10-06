"""
Spec-contract tests for the atomic-SWC instance-ref family (SWC TPS appendix D tables).
"""

from typing import Optional, get_type_hints

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.InstanceRefs import (
    ModeGroupInAtomicSwcInstanceRef,
    OperationInAtomicSwcInstanceRef,
    PModeGroupInAtomicSwcInstanceRef,
    POperationInAtomicSwcInstanceRef,
    PTriggerInAtomicSwcTypeInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
    RTriggerInAtomicSwcInstanceRef,
    RVariableInAtomicSwcInstanceRef,
    TriggerInAtomicSwcInstanceRef,
)

ABSTRACT = [ModeGroupInAtomicSwcInstanceRef, OperationInAtomicSwcInstanceRef, TriggerInAtomicSwcInstanceRef]
CONCRETE = [
    PModeGroupInAtomicSwcInstanceRef,
    RModeGroupInAtomicSWCInstanceRef,
    RModeInAtomicSwcInstanceRef,
    PTriggerInAtomicSwcTypeInstanceRef,
    RVariableInAtomicSwcInstanceRef,
    POperationInAtomicSwcInstanceRef,
    ROperationInAtomicSwcInstanceRef,
    RTriggerInAtomicSwcInstanceRef,
]


def test_abstract_guards():
    for cls in ABSTRACT:
        with pytest.raises(TypeError):
            cls()


def test_base_anchoring():
    """All family members derive from AtpInstanceRef (appendix D Base rows)."""
    for cls in ABSTRACT + CONCRETE:
        assert issubclass(cls, AtpInstanceRef), cls.__name__


@pytest.mark.parametrize("cls", CONCRETE)
def test_defaults_and_ref_types(cls):
    probe = type("_Probe", (AtpInstanceRef,), {})
    inherited = set(vars(probe()).keys())
    instance = cls()
    for name, value in vars(instance).items():
        if name in inherited:
            continue
        assert value is None, "%s.%s" % (cls.__name__, name)


@pytest.mark.parametrize("cls", CONCRETE)
def test_accessors_optional_reftype_and_none_noop(cls):
    inherited = set(vars(AtpInstanceRef.__new__(AtpInstanceRef)).keys())
    for name in vars(cls.__new__(cls)):
        if name in inherited:
            continue
        getter = getattr(cls, "get" + name[0].upper() + name[1:])
        setter = getattr(cls, "set" + name[0].upper() + name[1:])
        hints = get_type_hints(getter)
        assert hints["return"] == Optional[RefType], "%s.%s" % (cls.__name__, name)
        instance = cls()
        ref = RefType().setValue("/x")
        assert setter(instance, ref) is instance
        assert getattr(instance, name) is ref
        setter(instance, None)
        assert getattr(instance, name) is ref


@pytest.mark.parametrize("cls", ABSTRACT + CONCRETE)
def test_no_class_docstring(cls):
    """All appendix D instance-ref tables carry an empty Note — no class docstring."""
    assert not cls.__doc__ or not cls.__doc__.strip(), cls.__name__
