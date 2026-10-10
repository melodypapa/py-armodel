"""
Repo-wide invariant: the cooperative MRO chain must remain constructible.

`Referrable.__init__` dispatches via `super().__init__()`. Any class whose MRO
places a base with an argument-requiring `__init__` immediately after
`Referrable` would raise `TypeError` the moment it is constructed. This test
fails at collection-time-cheap cost rather than at some future construction
site nobody tests.
"""

import importlib
import inspect
import pkgutil

import pytest

import armodel
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable


def _model_classes():
    loaded = {}
    for module_info in pkgutil.walk_packages(armodel.__path__, "armodel."):
        try:
            loaded[module_info.name] = importlib.import_module(module_info.name)
        except Exception:  # pragma: no cover - optional modules
            continue
    classes = {}
    for module in loaded.values():
        for name, obj in vars(module).items():
            if inspect.isclass(obj) and obj.__module__.startswith("armodel"):
                classes[name] = obj
    return classes


def _required_positional(init_func):
    try:
        signature = inspect.signature(init_func)
    except (ValueError, TypeError):  # pragma: no cover - builtins
        return []
    return [
        parameter
        for parameter_name, parameter in list(signature.parameters.items())[1:]
        if parameter.default is inspect.Parameter.empty and parameter.kind in (parameter.POSITIONAL_ONLY, parameter.POSITIONAL_OR_KEYWORD)
    ]


# Computed once at import time — the decorator and the test body both read
# this instead of re-running the pkgutil/importlib sweep per parametrized
# case (2,042 cases; re-running it per case would redo the whole-package
# import-and-scan 2,042 times for no benefit, since nothing it returns
# changes between calls).
_CLASSES = _model_classes()


@pytest.mark.parametrize("class_name", sorted(_CLASSES))
def test_no_incompatible_init_after_referrable(class_name):
    cls = _CLASSES[class_name]
    mro = cls.__mro__
    if Referrable not in mro:
        pytest.skip(f"{class_name} does not inherit Referrable")
    for candidate in mro[mro.index(Referrable) + 1 :]:
        init_func = candidate.__dict__.get("__init__")
        if init_func is None or init_func is object.__init__:
            continue
        required = _required_positional(init_func)
        assert not required, f"{class_name}: cooperative super() from Referrable lands on " f"{candidate.__name__}.__init__ which requires {required}"
