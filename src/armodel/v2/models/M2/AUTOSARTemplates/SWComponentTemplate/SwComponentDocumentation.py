from typing import List, Optional

from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)


class SwComponentDocumentation(ARObject):
    """
    that this is subject to variation because Chapter aggregations in the role
    chapter are variant within the documentation in general. Stereotypes:
    atpSplitable; atpVariation , chapter.variation Point.shortLabel
    vh.latestBindingTime=postBuild (cid:53) 337 of 381 Document ID 89:
    AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Basic Software Module
    Description Template AUTOSAR CP R23-11 (cid:52)

    Package: M2::AUTOSARTemplates::SWComponentTemplate::SoftwareComponentDocumentation::SwComponentDocumentation

    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 337, Classic
      Platform R23-11)
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 697, Classic Platform
      R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 465, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # These chapters provide additional information about the that do not fit in
        # the other chapters.
        self._chapter: List["Chapter"] = []

    @property
    def chapter(self) -> List["Chapter"]:
        """Get chapter (Pythonic accessor)."""
        return self._chapter
        # This element contains calibration instructions and hints a calibration
        # engineer.
        self._swCalibration: Optional["Chapter"] = None

    @property
    def sw_calibration(self) -> Optional["Chapter"]:
        """Get swCalibration (Pythonic accessor)."""
        return self._swCalibration

    @sw_calibration.setter
    def sw_calibration(self, value: Optional["Chapter"]) -> None:
        """
        Set swCalibration with validation.

        Args:
            value: The swCalibration to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCalibration = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swCalibration must be Chapter or None, got {type(value).__name__}"
            )
        self._swCalibration = value
        # This element records the documentation requested by.
        self._swCarbDoc: Optional["Chapter"] = None

    @property
    def sw_carb_doc(self) -> Optional["Chapter"]:
        """Get swCarbDoc (Pythonic accessor)."""
        return self._swCarbDoc

    @sw_carb_doc.setter
    def sw_carb_doc(self, value: Optional["Chapter"]) -> None:
        """
        Set swCarbDoc with validation.

        Args:
            value: The swCarbDoc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swCarbDoc = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swCarbDoc must be Chapter or None, got {type(value).__name__}"
            )
        self._swCarbDoc = value
        # This element contains general information about issues within the component.
        self._swDiagnostics: Optional["Chapter"] = None

    @property
    def sw_diagnostics(self) -> Optional["Chapter"]:
        """Get swDiagnostics (Pythonic accessor)."""
        return self._swDiagnostics

    @sw_diagnostics.setter
    def sw_diagnostics(self, value: Optional["Chapter"]) -> None:
        """
        Set swDiagnostics with validation.

        Args:
            value: The swDiagnostics to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swDiagnostics = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swDiagnostics must be Chapter or None, got {type(value).__name__}"
            )
        self._swDiagnostics = value
        # This element contains the definition of the physical this software component.
        # This definition is less formal and is intended to be delivered from.
        self._swFeatureDef: Optional["Chapter"] = None

    @property
    def sw_feature_def(self) -> Optional["Chapter"]:
        """Get swFeatureDef (Pythonic accessor)."""
        return self._swFeatureDef

    @sw_feature_def.setter
    def sw_feature_def(self, value: Optional["Chapter"]) -> None:
        """
        Set swFeatureDef with validation.

        Args:
            value: The swFeatureDef to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swFeatureDef = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swFeatureDef must be Chapter or None, got {type(value).__name__}"
            )
        self._swFeatureDef = value
        # This element contains the textual description of the of this software
                # component.
        # Expert this description.
        self._swFeatureDesc: Optional["Chapter"] = None

    @property
    def sw_feature_desc(self) -> Optional["Chapter"]:
        """Get swFeatureDesc (Pythonic accessor)."""
        return self._swFeatureDesc

    @sw_feature_desc.setter
    def sw_feature_desc(self, value: Optional["Chapter"]) -> None:
        """
        Set swFeatureDesc with validation.

        Args:
            value: The swFeatureDesc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swFeatureDesc = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swFeatureDesc must be Chapter or None, got {type(value).__name__}"
            )
        self._swFeatureDesc = value
        # This element contains information regarding the software of the component.
        self._swMaintenance: Optional["Chapter"] = None

    @property
    def sw_maintenance(self) -> Optional["Chapter"]:
        """Get swMaintenance (Pythonic accessor)."""
        return self._swMaintenance

    @sw_maintenance.setter
    def sw_maintenance(self, value: Optional["Chapter"]) -> None:
        """
        Set swMaintenance with validation.

        Args:
            value: The swMaintenance to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swMaintenance = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swMaintenance must be Chapter or None, got {type(value).__name__}"
            )
        self._swMaintenance = value
        # This element contains suggestions and hints for the test software
        # functionality of this software component.
        self._swTestDesc: Optional["Chapter"] = None

    @property
    def sw_test_desc(self) -> Optional["Chapter"]:
        """Get swTestDesc (Pythonic accessor)."""
        return self._swTestDesc

    @sw_test_desc.setter
    def sw_test_desc(self, value: Optional["Chapter"]) -> None:
        """
        Set swTestDesc with validation.

        Args:
            value: The swTestDesc to set

        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._swTestDesc = None
            return

        if not isinstance(value, Chapter):
            raise TypeError(
                f"swTestDesc must be Chapter or None, got {type(value).__name__}"
            )
        self._swTestDesc = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getChapter(self) -> List["Chapter"]:
        """
        AUTOSAR-compliant getter for chapter.

        Returns:
            The chapter value

        Note:
            Delegates to chapter property (CODING_RULE_V2_00017)
        """
        return self.chapter  # Delegates to property

    def getSwCalibration(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swCalibration.

        Returns:
            The swCalibration value

        Note:
            Delegates to sw_calibration property (CODING_RULE_V2_00017)
        """
        return self.sw_calibration  # Delegates to property

    def setSwCalibration(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swCalibration with method chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_calibration property setter (gets validation automatically)
        """
        self.sw_calibration = value  # Delegates to property setter
        return self

    def getSwCarbDoc(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swCarbDoc.

        Returns:
            The swCarbDoc value

        Note:
            Delegates to sw_carb_doc property (CODING_RULE_V2_00017)
        """
        return self.sw_carb_doc  # Delegates to property

    def setSwCarbDoc(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swCarbDoc with method chaining.

        Args:
            value: The swCarbDoc to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_carb_doc property setter (gets validation automatically)
        """
        self.sw_carb_doc = value  # Delegates to property setter
        return self

    def getSwDiagnostics(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swDiagnostics.

        Returns:
            The swDiagnostics value

        Note:
            Delegates to sw_diagnostics property (CODING_RULE_V2_00017)
        """
        return self.sw_diagnostics  # Delegates to property

    def setSwDiagnostics(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swDiagnostics with method chaining.

        Args:
            value: The swDiagnostics to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_diagnostics property setter (gets validation automatically)
        """
        self.sw_diagnostics = value  # Delegates to property setter
        return self

    def getSwFeatureDef(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swFeatureDef.

        Returns:
            The swFeatureDef value

        Note:
            Delegates to sw_feature_def property (CODING_RULE_V2_00017)
        """
        return self.sw_feature_def  # Delegates to property

    def setSwFeatureDef(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swFeatureDef with method chaining.

        Args:
            value: The swFeatureDef to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_feature_def property setter (gets validation automatically)
        """
        self.sw_feature_def = value  # Delegates to property setter
        return self

    def getSwFeatureDesc(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swFeatureDesc.

        Returns:
            The swFeatureDesc value

        Note:
            Delegates to sw_feature_desc property (CODING_RULE_V2_00017)
        """
        return self.sw_feature_desc  # Delegates to property

    def setSwFeatureDesc(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swFeatureDesc with method chaining.

        Args:
            value: The swFeatureDesc to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_feature_desc property setter (gets validation automatically)
        """
        self.sw_feature_desc = value  # Delegates to property setter
        return self

    def getSwMaintenance(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swMaintenance.

        Returns:
            The swMaintenance value

        Note:
            Delegates to sw_maintenance property (CODING_RULE_V2_00017)
        """
        return self.sw_maintenance  # Delegates to property

    def setSwMaintenance(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swMaintenance with method chaining.

        Args:
            value: The swMaintenance to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_maintenance property setter (gets validation automatically)
        """
        self.sw_maintenance = value  # Delegates to property setter
        return self

    def getSwTestDesc(self) -> "Chapter":
        """
        AUTOSAR-compliant getter for swTestDesc.

        Returns:
            The swTestDesc value

        Note:
            Delegates to sw_test_desc property (CODING_RULE_V2_00017)
        """
        return self.sw_test_desc  # Delegates to property

    def setSwTestDesc(self, value: "Chapter") -> "SwComponentDocumentation":
        """
        AUTOSAR-compliant setter for swTestDesc with method chaining.

        Args:
            value: The swTestDesc to set

        Returns:
            self for method chaining

        Note:
            Delegates to sw_test_desc property setter (gets validation automatically)
        """
        self.sw_test_desc = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_sw_calibration(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swCalibration and return self for chaining.

        Args:
            value: The swCalibration to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_calibration("value")
        """
        self.sw_calibration = value  # Use property setter (gets validation)
        return self

    def with_sw_carb_doc(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swCarbDoc and return self for chaining.

        Args:
            value: The swCarbDoc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_carb_doc("value")
        """
        self.sw_carb_doc = value  # Use property setter (gets validation)
        return self

    def with_sw_diagnostics(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swDiagnostics and return self for chaining.

        Args:
            value: The swDiagnostics to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_diagnostics("value")
        """
        self.sw_diagnostics = value  # Use property setter (gets validation)
        return self

    def with_sw_feature_def(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swFeatureDef and return self for chaining.

        Args:
            value: The swFeatureDef to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_feature_def("value")
        """
        self.sw_feature_def = value  # Use property setter (gets validation)
        return self

    def with_sw_feature_desc(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swFeatureDesc and return self for chaining.

        Args:
            value: The swFeatureDesc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_feature_desc("value")
        """
        self.sw_feature_desc = value  # Use property setter (gets validation)
        return self

    def with_sw_maintenance(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swMaintenance and return self for chaining.

        Args:
            value: The swMaintenance to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_maintenance("value")
        """
        self.sw_maintenance = value  # Use property setter (gets validation)
        return self

    def with_sw_test_desc(self, value: Optional["Chapter"]) -> "SwComponentDocumentation":
        """
        Set swTestDesc and return self for chaining.

        Args:
            value: The swTestDesc to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sw_test_desc("value")
        """
        self.sw_test_desc = value  # Use property setter (gets validation)
        return self
