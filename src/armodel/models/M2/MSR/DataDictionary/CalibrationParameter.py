from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional
from abc import ABC
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, ARFloat, DisplayFormatString, MonotonyEnum

if TYPE_CHECKING:
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwCalibrationAccessEnum
    from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class CalprmAxisCategoryEnum(AREnum):
    """
    This enum specifies the possible values of the category property within SwCalprmAxis.
    """

    # CalprmAxisCategoryEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.48, p.353
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # (no methods) — enum value form serialized on SwCalprmAxis.category
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # COM_AXIS is equal to an STD_AXIS, the difference is, that a COM_AXIS is an shared axis, that means this axis can be used multiple times by different CURVEs, MAPs, CUBOIDs, CUBE_4s, and CUBE_5s. Tags: atp.EnumerationLiteralIndex=0 xml.name=COM_AXIS
    COM_AXIS = "COM_AXIS"

    # FIX_AXIS means that the input axis is not stored. The axis is calculated using parameters and so on it is also not possible to modify the axis points. Tags: atp.EnumerationLiteralIndex=4 xml.name=FIX_AXIS
    FIX_AXIS = "FIX_AXIS"

    # RES_AXIS is also an shared axis like COM_AXIS, the difference is that this kind of axis can be used for rescaling. Tags: atp.EnumerationLiteralIndex=6 xml.name=RES_AXIS
    RES_AXIS = "RES_AXIS"

    # STD_AXIS means that input and output axis definition are stored within this CURVE, MAP, CUBOID, CUBE_4, and CUBE_5. There is no shared or calculated axis. Tags: atp.EnumerationLiteralIndex=8 xml.name=STD_AXIS
    STD_AXIS = "STD_AXIS"

    def __init__(self):
        super().__init__([CalprmAxisCategoryEnum.COM_AXIS, CalprmAxisCategoryEnum.FIX_AXIS, CalprmAxisCategoryEnum.RES_AXIS, CalprmAxisCategoryEnum.STD_AXIS])


class SwCalprmAxisTypeProps(ARObject, ABC):
    """
    Base class for the type of the calibration axis. This provides the particular model of the specialization. If the specialization would be the directly from SwCalPrmAxis, the sequence of common properties and the specializes ones would be different.
    """

    # SwCalprmAxisTypeProps method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.49, p.353
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # XML: element group SW-CALPRM-AXIS-TYPE-PROPS inlined into SW-AXIS-INDIVIDUAL / SW-AXIS-GROUPED
    # [x] __init__        [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMaxGradient  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  (xml.name=MAX-GRADIENT)
    # [x] setMaxGradient  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getMonotony     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  (xml.name=MONOTONY)
    # [x] setMonotony     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        if type(self) is SwCalprmAxisTypeProps:
            raise TypeError("SwCalprmAxisTypeProps is an abstract class.")

        super().__init__()

        # This attribute defines the maximum permissible gradient for an adjustable object (curve, map or cuboid) with respect to a specific axis. MaxGrad = maximum( absolute((Value i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) )
        self.maxGradient: Optional[ARFloat] = None

        # This attribute specifies the monotony constraint for an adjustable object (curve, map or cuboid) with respect to a specific axis. This information can be used by MCD system to verify whether the monotony constraint is fulfilled and to prevent from changes violating the constraint.
        self.monotony: Optional[MonotonyEnum] = None

    def getMaxGradient(self) -> Optional[ARFloat]:
        """
        This attribute defines the maximum permissible gradient for an adjustable object (curve, map or cuboid) with respect to a specific axis. MaxGrad = maximum( absolute((Value i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) )
        """
        return self.maxGradient

    def setMaxGradient(self, value: Optional[ARFloat]) -> SwCalprmAxisTypeProps:
        """
        This attribute defines the maximum permissible gradient for an adjustable object (curve, map or cuboid) with respect to a specific axis. MaxGrad = maximum( absolute((Value i,k - Value i-1,k)/(Axis Point i - Axis Point i-1)) ) A None value is a no-op and does not overwrite an existing maxGradient.
        """
        if value is not None:
            self.maxGradient = value
        return self

    def getMonotony(self) -> Optional[MonotonyEnum]:
        """
        This attribute specifies the monotony constraint for an adjustable object (curve, map or cuboid) with respect to a specific axis. This information can be used by MCD system to verify whether the monotony constraint is fulfilled and to prevent from changes violating the constraint.
        """
        return self.monotony

    def setMonotony(self, value: Optional[MonotonyEnum]) -> SwCalprmAxisTypeProps:
        """
        This attribute specifies the monotony constraint for an adjustable object (curve, map or cuboid) with respect to a specific axis. This information can be used by MCD system to verify whether the monotony constraint is fulfilled and to prevent from changes violating the constraint. A None value is a no-op and does not overwrite an existing monotony.
        """
        if value is not None:
            self.monotony = value
        return self


class SwCalprmAxis(ARObject):
    """
    This element specifies an individual input parameter axis (abscissa).
    """

    # SwCalprmAxis method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.47, p.352
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # XML: element group SW-CALPRM-AXIS; BASE-TYPE-REF (baseType) has atp.Status="removed" — not mapped
    # [x] __init__                 [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getCategory              [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  (xml.name=CATEGORY, xml.sequenceOffset=30)
    # [x] setCategory              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getDisplayFormat         [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  (xml.name=DISPLAY-FORMAT, xml.sequenceOffset=100)
    # [x] setDisplayFormat         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwAxisIndex           [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  (xml.name=SW-AXIS-INDEX, xml.sequenceOffset=20)
    # [x] setSwAxisIndex           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCalibrationAccess   [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  (xml.name=SW-CALIBRATION-ACCESS, xml.sequenceOffset=90)
    # [x] setSwCalibrationAccess   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSwCalprmAxisTypeProps  [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  (xml.name=SW-AXIS-GROUPED|SW-AXIS-INDIVIDUAL, xml.sequenceOffset=40)
    # [x] setSwCalprmAxisTypeProps  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self):
        super().__init__()

        # This property specifies the category of a particular axis.
        self.category: Optional[CalprmAxisCategoryEnum] = None

        # This property specifies how the axis values shall be displayed e.g. in documents or in measurement and calibration tools.
        self.displayFormat: Optional[DisplayFormatString] = None

        # This attribute specifies which axis is specified by the containing SwCalprmAxis. For example in a curve this is usually "1". In a map this is "1" or "2".
        self.swAxisIndex: Optional[AxisIndexType] = None

        # Describes the applicability of parameters and variables.
        self.swCalibrationAccess: Optional[SwCalibrationAccessEnum] = None

        # specific properties depending on the type of the axis.
        self.swCalprmAxisTypeProps: Optional[SwCalprmAxisTypeProps] = None

    def getCategory(self) -> Optional[CalprmAxisCategoryEnum]:
        """
        This property specifies the category of a particular axis.
        """
        return self.category

    def setCategory(self, value: Optional[CalprmAxisCategoryEnum]) -> SwCalprmAxis:
        """
        This property specifies the category of a particular axis. A None value is a no-op and does not overwrite an existing category.
        """
        if value is not None:
            self.category = value
        return self

    def getDisplayFormat(self) -> Optional[DisplayFormatString]:
        """
        This property specifies how the axis values shall be displayed e.g. in documents or in measurement and calibration tools.
        """
        return self.displayFormat

    def setDisplayFormat(self, value: Optional[DisplayFormatString]) -> SwCalprmAxis:
        """
        This property specifies how the axis values shall be displayed e.g. in documents or in measurement and calibration tools. A None value is a no-op and does not overwrite an existing displayFormat.
        """
        if value is not None:
            self.displayFormat = value
        return self

    def getSwAxisIndex(self) -> Optional[AxisIndexType]:
        """
        This attribute specifies which axis is specified by the containing SwCalprmAxis. For example in a curve this is usually "1". In a map this is "1" or "2".
        """
        return self.swAxisIndex

    def setSwAxisIndex(self, value: Optional[AxisIndexType]) -> SwCalprmAxis:
        """
        This attribute specifies which axis is specified by the containing SwCalprmAxis. For example in a curve this is usually "1". In a map this is "1" or "2". A None value is a no-op and does not overwrite an existing swAxisIndex.
        """
        if value is not None:
            self.swAxisIndex = value
        return self

    def getSwCalibrationAccess(self) -> Optional[SwCalibrationAccessEnum]:
        """
        Describes the applicability of parameters and variables.
        """
        return self.swCalibrationAccess

    def setSwCalibrationAccess(self, value: Optional[SwCalibrationAccessEnum]) -> SwCalprmAxis:
        """
        Describes the applicability of parameters and variables. A None value is a no-op and does not overwrite an existing swCalibrationAccess.
        """
        if value is not None:
            self.swCalibrationAccess = value
        return self

    def getSwCalprmAxisTypeProps(self) -> Optional[SwCalprmAxisTypeProps]:
        """
        specific properties depending on the type of the axis.
        """
        return self.swCalprmAxisTypeProps

    def setSwCalprmAxisTypeProps(self, value: Optional[SwCalprmAxisTypeProps]) -> SwCalprmAxis:
        """
        specific properties depending on the type of the axis. A None value is a no-op and does not overwrite an existing swCalprmAxisTypeProps.
        """
        if value is not None:
            self.swCalprmAxisTypeProps = value
        return self


class SwCalprmAxisSet(ARObject):
    """
    Collection of SwCalprmAxis elements.
    """

    # SwCalprmAxisSet method parity checklist:
    # [ ] __init__                     [x] impl  [ ] docstring  [ ] test
    # [ ] addSwCalprmAxis              [x] impl  [ ] docstring  [ ] test
    # [ ] getSwCalprmAxises            [x] impl  [ ] docstring  [ ] test

    def __init__(self):
        super().__init__()

        self._swCalprmAxis = []  # type: List[SwCalprmAxis]

    def addSwCalprmAxis(self, axis: SwCalprmAxis):
        self._swCalprmAxis.append(axis)

    def getSwCalprmAxises(self) -> List[SwCalprmAxis]:
        return self._swCalprmAxis
