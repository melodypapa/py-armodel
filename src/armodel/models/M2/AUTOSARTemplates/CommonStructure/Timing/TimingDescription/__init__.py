"""
This module contains timing description classes for AUTOSAR models.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescriptionEvents import (  # noqa: F401
    AutosarOperationArgumentInstance,
    AutosarVariableInstance,
    OperationArgumentInComponentInstanceRef,
    VariableInComponentInstanceRef,
)


class TimingDescription(Identifiable, ABC):
    """
    The abstract parent class of the model elements that are used to define the scope of a timing constraint.
    """

    # TimingDescription method parity checklist:
    # Spec: AUTOSAR_CP_TPS_TimingExtensions.pdf, Table D.62, p.253
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    def __init__(self, parent, short_name: str):
        if type(self) is TimingDescription:
            raise TypeError("TimingDescription is an abstract class.")

        super().__init__(parent, short_name)


__all__ = [
    "AutosarOperationArgumentInstance",
    "AutosarVariableInstance",
    "OperationArgumentInComponentInstanceRef",
    "VariableInComponentInstanceRef",
    "TimingDescription",
]
