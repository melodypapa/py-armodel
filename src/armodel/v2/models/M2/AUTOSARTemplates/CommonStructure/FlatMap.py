from typing import List


class FlatMap(ARElement):
    """
    Contains a flat list of references to software objects. This list is used to
    identify instances and to resolve name conflicts. The scope is given by the
    RootSwCompositionPrototype for which it is used, i.e. it can be applied to a
    system, system extract or ECU-extract. An instance of FlatMap may also be
    used in a preliminary context, e.g. in the scope of a software component
    before integration into a system. In this case it is not referred by a
    RootSwComposition Prototype.

    Package: M2::AUTOSARTemplates::CommonStructure::FlatMap::FlatMap

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 317, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 965, Classic Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 445, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 190, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # A descriptor instance aggregated in the flat map.
        # point accounts for the fact, that the system can be subject to variability,
                # and thus the some instances is variable.
        # has been made splitable because the be contributed by different stakeholders
                # at in the workflow.
        # Plus, the overall size might big that eventually it becomes more manageable
                # if distributed over several files.
        # atpVariation.
        self._instance: List["FlatInstanceDescriptor"] = []

    @property
    def instance(self) -> List["FlatInstanceDescriptor"]:
        """Get instance (Pythonic accessor)."""
        return self._instance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getInstance(self) -> List["FlatInstanceDescriptor"]:
        """
        AUTOSAR-compliant getter for instance.

        Returns:
            The instance value

        Note:
            Delegates to instance property (CODING_RULE_V2_00017)
        """
        return self.instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
