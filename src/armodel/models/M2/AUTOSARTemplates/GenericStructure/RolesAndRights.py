"""
RolesAndRights module for AUTOSAR M2 models.
"""

from abc import ABC

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Referrable

__all__ = ["AtpDefinition"]


class AtpDefinition(Referrable, ABC):
    """This abstract meta class represents "definition"-elements which identify the respective values. For example the value of a particular system constant is identified by the definition of this system constant."""

    # AtpDefinition method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 11.3, p.383 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name: str):
        if type(self) is AtpDefinition:
            raise TypeError("AtpDefinition is an abstract class.")
        super().__init__(parent, short_name)
