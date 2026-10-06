"""
This module contains classes for representing AUTOSAR Run-Time Protection (RPT) scenarios
and access point identification elements in software component templates.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum, RptExecutionControlEnum, RptPreparationEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, CIdentifier, NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg
from abc import ABC
from typing import List, Optional, cast


class IdentCaption(AtpStructureElement, ABC):
    """
    This meta-class represents the caption. This allows having some meta-classes optionally identifiable.
    """

    # IdentCaption method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.4, p.851 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdentCaption:
            raise TypeError("IdentCaption is an abstract class.")

        super().__init__(parent, short_name)


class ModeAccessPointIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become referenced into the meta-class Mode AccessPoint without breaking backwards compatibility.
    """

    # ModeAccessPointIdent method parity checklist:
    # Spec: R23-11/AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.5, p.852 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # reader/writer: dedicated helpers readModeAccessPointIdent/writeModeAccessPointIdent
    # (readIdentifiable/writeIdentifiable; element <IDENT> of type MODE-ACCESS-POINT-IDENT
    # inside <MODE-ACCESS-POINT>, XSD AUTOSAR_00052.xsd l.81733/l.81788, sequenceOffset -100)

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)


class RptServicePointEnum(AREnum):
    """
    Specifies whether the invocation of ExecutableEntitys due to activation of specific RteEvents/Bsw Events requires the insertion of Service Points.
    """

    # RptServicePointEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.15, p.860
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # (no methods) — serialized as an attribute value on the consuming class

    # Enables generation of service points by the RTE generator. Tags: atp.EnumerationLiteralIndex=0
    ENABLED = "ENABLED"

    # No Service Points are requested. Tags: atp.EnumerationLiteralIndex=1
    NONE = "NONE"

    def __init__(self):
        super().__init__(
            (
                RptServicePointEnum.ENABLED,
                RptServicePointEnum.NONE,
            )
        )


class RptImplPolicy(ARObject):
    """
    Describes the code preparation for rapid prototyping at data accesses.
    """

    # RptImplPolicy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.8, p.854
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getRptEnablerImplType       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptEnablerImplType       [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRptPreparationLevel      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptPreparationLevel      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # For Level 2 or Level3 this property determines how the RTE implements the additional "RP enabler" flag.
        self.rptEnablerImplType: Optional[RptEnablerImplTypeEnum] = None

        # Mandates RP preparation level for access to VariableData Prototype within generated RTE implementation.
        self.rptPreparationLevel: Optional[RptPreparationEnum] = None

    def getRptEnablerImplType(self) -> Optional[RptEnablerImplTypeEnum]:
        """
        For Level 2 or Level3 this property determines how the RTE implements the additional "RP enabler" flag.
        """
        return self.rptEnablerImplType

    def setRptEnablerImplType(self, value: Optional[RptEnablerImplTypeEnum]) -> "RptImplPolicy":
        """
        For Level 2 or Level3 this property determines how the RTE implements the additional "RP enabler" flag.
        A None value is a no-op and does not overwrite an existing rptEnablerImplType.
        """
        if value is not None:
            self.rptEnablerImplType = value
        return self

    def getRptPreparationLevel(self) -> Optional[RptPreparationEnum]:
        """
        Mandates RP preparation level for access to VariableData Prototype within generated RTE implementation.
        """
        return self.rptPreparationLevel

    def setRptPreparationLevel(self, value: Optional[RptPreparationEnum]) -> "RptImplPolicy":
        """
        Mandates RP preparation level for access to VariableData Prototype within generated RTE implementation.
        A None value is a no-op and does not overwrite an existing rptPreparationLevel.
        """
        if value is not None:
            self.rptPreparationLevel = value
        return self


class RptExecutableEntityProperties(ARObject):
    """
    Describes the code preparation for rapid prototyping at ExecutableEntity invocation.
    """

    # RptExecutableEntityProperties method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.13, p.859
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getMaxRptEventId            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMaxRptEventId            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getMinRptEventId            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setMinRptEventId            [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRptExecutionControl      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptExecutionControl      [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] getRptServicePoint          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11
    # [x] setRptServicePoint          [x] impl  [x] docstring  [x] test  [x] reader  [x] writer  R23-11

    def __init__(self):
        super().__init__()

        # Highest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        self.maxRptEventId: Optional[PositiveInteger] = None

        # Lowest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        self.minRptEventId: Optional[PositiveInteger] = None

        # This attribute specifies the rapid prototyping control of the executable
        self.rptExecutionControl: Optional[RptExecutionControlEnum] = None

        # Enables generation of service points by the RTE generator.
        self.rptServicePoint: Optional[RptServicePointEnum] = None

    def getMaxRptEventId(self) -> Optional[PositiveInteger]:
        """
        Highest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        """
        return self.maxRptEventId

    def setMaxRptEventId(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityProperties":
        """
        Highest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        A None value is a no-op and does not overwrite an existing maxRptEventId.
        """
        if value is not None:
            self.maxRptEventId = value
        return self

    def getMinRptEventId(self) -> Optional[PositiveInteger]:
        """
        Lowest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        """
        return self.minRptEventId

    def setMinRptEventId(self, value: Optional[PositiveInteger]) -> "RptExecutableEntityProperties":
        """
        Lowest RPT event id usable for RTE generated service points. This attribute is relevant, if dedicated id range shall be applied to the ExecutableEntitys of a software component or specific ExecutableEntitys.
        A None value is a no-op and does not overwrite an existing minRptEventId.
        """
        if value is not None:
            self.minRptEventId = value
        return self

    def getRptExecutionControl(self) -> Optional[RptExecutionControlEnum]:
        """
        This attribute specifies the rapid prototyping control of the executable
        """
        return self.rptExecutionControl

    def setRptExecutionControl(self, value: Optional[RptExecutionControlEnum]) -> "RptExecutableEntityProperties":
        """
        This attribute specifies the rapid prototyping control of the executable
        A None value is a no-op and does not overwrite an existing rptExecutionControl.
        """
        if value is not None:
            self.rptExecutionControl = value
        return self

    def getRptServicePoint(self) -> Optional[RptServicePointEnum]:
        """
        Enables generation of service points by the RTE generator.
        """
        return self.rptServicePoint

    def setRptServicePoint(self, value: Optional[RptServicePointEnum]) -> "RptExecutableEntityProperties":
        """
        Enables generation of service points by the RTE generator.
        A None value is a no-op and does not overwrite an existing rptServicePoint.
        """
        if value is not None:
            self.rptServicePoint = value
        return self


class RptHook(ARObject, VariationPointCapable):
    """
    This meta-class provide the ability to describe a rapid prototyping hook. This can either be described by an other AUTOSAR system with the category RPT_SYSTEM or as a non AUTOSAR software.
    """

    # RptHook method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.3, p.848
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCodeLabel        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCodeLabel        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getMcdIdentifier    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setMcdIdentifier    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRptArHookIRef    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRptArHookIRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] addSdg              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # reader/writer: dedicated helpers readRptHook/writeRptHook (readARObject/writeARObject
    # once each, Rule 0025; element <RPT-HOOK>, group RPT-HOOK XSD AUTOSAR_00052.xsd
    # l.100040, sequenceOffset order CODE-LABEL, MCD-IDENTIFIER, RPT-AR-HOOK-IREF, SDGS,
    # VARIATION-POINT). Aggregated by RptContainer.rptHook (RPT-HOOKS wrapper) — the
    # RptContainer dispatch is that class's own queued sync.
    # get/setVariationPoint provided by the VariationPointCapable base (mixin) — no spec
    # rows (Rule 0020: RptContainer.rptHook atpVariation; XSD VARIATION-POINT
    # xml.sequenceOffset 10000)

    def __init__(self):
        super().__init__()

        # This attribute provides a code label which is used in the implementation of the hook. For example this can be an C function name or the name of data definition.
        self.codeLabel: Optional[CIdentifier] = None

        # This attribute provides an identifier which shall be used in a MCD System to display the Rpt Hook.
        self.mcdIdentifier: Optional[NameToken] = None

        # This describes the hook with the means of another AUTOSAR system. InstanceRef implemented by: AnyInstanceRef
        self.rptArHookIRef: Optional[AnyInstanceRef] = None

        # This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data.
        self.sdgs: List[Sdg] = []

    def getCodeLabel(self) -> Optional[CIdentifier]:
        """
        This attribute provides a code label which is used in the implementation of the hook. For example this can be an C function name or the name of data definition.
        """
        return self.codeLabel

    def setCodeLabel(self, value: Optional[CIdentifier]) -> "RptHook":
        """
        This attribute provides a code label which is used in the implementation of the hook. For example this can be an C function name or the name of data definition.
        A None value is a no-op and does not overwrite an existing codeLabel.
        """
        if value is not None:
            self.codeLabel = value
        return self

    def getMcdIdentifier(self) -> Optional[NameToken]:
        """
        This attribute provides an identifier which shall be used in a MCD System to display the Rpt Hook.
        """
        return self.mcdIdentifier

    def setMcdIdentifier(self, value: Optional[NameToken]) -> "RptHook":
        """
        This attribute provides an identifier which shall be used in a MCD System to display the Rpt Hook.
        A None value is a no-op and does not overwrite an existing mcdIdentifier.
        """
        if value is not None:
            self.mcdIdentifier = value
        return self

    def getRptArHookIRef(self) -> Optional[AnyInstanceRef]:
        """
        This describes the hook with the means of another AUTOSAR system. InstanceRef implemented by: AnyInstanceRef
        """
        return self.rptArHookIRef

    def setRptArHookIRef(self, value: Optional[AnyInstanceRef]) -> "RptHook":
        """
        This describes the hook with the means of another AUTOSAR system. InstanceRef implemented by: AnyInstanceRef
        A None value is a no-op and does not overwrite an existing rptArHookIRef.
        """
        if value is not None:
            self.rptArHookIRef = value
        return self

    def addSdg(self, sdg: Optional[Sdg]) -> "RptHook":
        """
        This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data.
        A None value is a no-op and is not appended.
        """
        if sdg is not None:
            self.sdgs.append(sdg)
        return self

    def getSdgs(self) -> List[Sdg]:
        """
        This property allows to keep special data which is not represented by the standard model. It can be utilized to keep e.g. tool specific data.
        """
        return self.sdgs


class ExternalTriggeringPointIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become referenced into the meta-class ExternalTriggeringPoint without breaking backwards compatibility.
    """

    # ExternalTriggeringPointIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 14.6, p.852 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__  [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class DiagnosticParameterIdent(IdentCaption):
    """
    This meta-class has been created to introduce the ability to become referenced into the meta-class AbstractDiagnosticParameter without breaking backwards compatibility.
    """

    # DiagnosticParameterIdent method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.7, p.37
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createSubElement  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSubElements    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    #
    # XSD complexType DIAGNOSTIC-PARAMETER-IDENT (AUTOSAR_00052.xsd l.40756): the
    # ATP-CLASSIFIER / ATP-FEATURE / ATP-STRUCTURE-ELEMENT / IDENT-CAPTION /
    # DIAGNOSTIC-SERVICE-MAPPING-DIAG-TARGET groups are empty sequences — only the
    # Identifiable identity groups and SUB-ELEMENTS are serialized.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This collection represents the subElements on the top level.
        self.subElements: List[DiagnosticParameterElement] = []

    def createSubElement(self, short_name: str) -> DiagnosticParameterElement:
        """
        This collection represents the subElements on the top level.
        The existing sub element is returned when the short name already exists (no duplicate creation).
        """
        if not self.IsReferrableElementExists(short_name, DiagnosticParameterElement):
            sub_element = DiagnosticParameterElement(self, short_name)
            self.addReferrableElement(sub_element)
            self.subElements.append(sub_element)
        return cast(DiagnosticParameterElement, self.getReferrableElement(short_name, DiagnosticParameterElement))

    def getSubElements(self) -> List[DiagnosticParameterElement]:
        """
        This collection represents the subElements on the top level.
        """
        return self.subElements
