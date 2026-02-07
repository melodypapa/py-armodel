from typing import List

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class McFunctionDataRefSet(ARObject):
    """
    Refers to a set of data assigned to an McFunction in a particular role. The
    data are given • either by entries in a FlatMap • or by data instances that
    are part of MC support data. These two possibilities are exclusive within a
    given McFunctionDataRefSet. Which one to use depends on the process and tool
    environment. The set is subject to variability because the same functional
    model may be used with various representation of the data. Tags:
    vh.latestBindingTime=preCompileTime

    Package: M2::AUTOSARTemplates::CommonStructure::MeasurementCalibrationSupport::RptSupport::McFunctionDataRefSet

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 187, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 455, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # Refers to an entry in a FlatMap that is part of the set, for calibration
                # parameter or measured variable.
        # atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._flatMapEntry: List["FlatInstanceDescriptor"] = []

    @property
    def flat_map_entry(self) -> List["FlatInstanceDescriptor"]:
        """Get flatMapEntry (Pythonic accessor)."""
        return self._flatMapEntry
        # Refers to a data instance within MC support data that is the set, i.
        # e.
        # a calibration parameter or measured atpSplitable property has no atp.
        # Splitkey due (PropertySetPattern).
        self._mcDataInstance: List["McDataInstance"] = []

    @property
    def mc_data_instance(self) -> List["McDataInstance"]:
        """Get mcDataInstance (Pythonic accessor)."""
        return self._mcDataInstance

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFlatMapEntry(self) -> List["FlatInstanceDescriptor"]:
        """
        AUTOSAR-compliant getter for flatMapEntry.

        Returns:
            The flatMapEntry value

        Note:
            Delegates to flat_map_entry property (CODING_RULE_V2_00017)
        """
        return self.flat_map_entry  # Delegates to property

    def getMcDataInstance(self) -> List["McDataInstance"]:
        """
        AUTOSAR-compliant getter for mcDataInstance.

        Returns:
            The mcDataInstance value

        Note:
            Delegates to mc_data_instance property (CODING_RULE_V2_00017)
        """
        return self.mc_data_instance  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====
