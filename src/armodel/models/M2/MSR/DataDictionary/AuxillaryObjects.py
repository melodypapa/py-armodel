from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, Identifier, SectionInitializationPolicyType


class MemoryAllocationKeywordPolicyType(AREnum):
    """
    Enumeration to specify the name pattern of the Memory Allocation Keyword.
    """

    # MemoryAllocationKeywordPolicyType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.95, p.418
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # The MemorySection shortNames of referring MemorySections and therefore the belonging Memory Allocation Keywords in the code are build with the shortName of the SwAddrMethod. This is the default value if the attribute does not exist. Tags: atp.EnumerationLiteralIndex=0
    ADDR_METHOD_SHORT_NAME = "addrMethodShortName"

    # The MemorySection shortNames of referring MemorySections and therefore the belonging Memory Allocation Keywords in the code are build with the shortName of the SwAddrMethod and a variable alignment postfix. Thereby the alignment postfix needs to be consistent with the alignment attribute of the related MemorySection. Tags: atp.EnumerationLiteralIndex=1
    ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT = "addrMethodShortNameAndAlignment"

    def __init__(self):
        super().__init__(
            [
                MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME,
                MemoryAllocationKeywordPolicyType.ADDR_METHOD_SHORT_NAME_AND_ALIGNMENT,
            ]
        )


class MemorySectionType(AREnum):
    """
    Enumeration to specify the essential nature of the data which can be allocated in a common memory class by the means of the AUTOSAR Memory Mapping.
    """

    # MemorySectionType method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.94, p.418
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer

    # This memory section is reserved for "virtual variables" that are computed by an MCD system during a measurement session but do not exist in the ECU memory. Tags: atp.EnumerationLiteralIndex=2
    CALIBRATION_VARIABLES = "calibrationVariables"

    # To be used for calibratable constants of ECU-functions. Tags: atp.EnumerationLiteralIndex=3
    CALPRM = "calprm"

    # To be used for mapping code to application block, boot block, external flash etc. Tags: atp.EnumerationLiteralIndex=4
    CODE = "code"

    # Constants with attributes that show that they reside in one segment for module configuration. Tags: atp.EnumerationLiteralIndex=5
    CONFIG_DATA = "configData"

    # To be used for global or static constants. Tags: atp.EnumerationLiteralIndex=6
    CONST = "const"

    # This memory section is reserved for "virtual parameters" that are taken for computing the values of so-called dependent parameter of an MCD system. Dependent Parameters that are not at the same time "virtual parameters" are allocated in the ECU memory. Virtual parameters, on the other hand, are not allocated in the ECU memory. Virtual parameters exist in the ECU Hex file for the purpose of being considered (for computing the values of dependent parameters) during an offline-calibration session. Tags: atp.EnumerationLiteralIndex=7
    EXCLUDE_FROM_FLASH = "excludeFromFlash"

    # To be used for global or static variables. The expected initialization is specified with the attribute sectionInitializationPolicy. Tags: atp.EnumerationLiteralIndex=9
    VAR = "var"

    def __init__(self):
        super().__init__(
            (
                MemorySectionType.CALIBRATION_VARIABLES,
                MemorySectionType.CALPRM,
                MemorySectionType.CODE,
                MemorySectionType.CONFIG_DATA,
                MemorySectionType.CONST,
                MemorySectionType.EXCLUDE_FROM_FLASH,
                MemorySectionType.VAR,
            )
        )


class SwAddrMethod(AtpBlueprintable):
    """
    Used to assign a common addressing method, e.g. common memory section, to data or code objects. These objects could actually live in different modules or components. Tags: atp.recommendedPackage=SwAddrMethods
    """

    # SwAddrMethod method parity checklist:
    # Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table 5.92, p.414
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer
    # [x] getMemoryAllocationKeywordPolicy [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setMemoryAllocationKeywordPolicy [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getOptions                   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] addOption                    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSectionInitializationPolicy [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSectionInitializationPolicy [x] impl  [x] docstring  [x] test  [x] reader  [—] writer
    # [x] getSectionType               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer
    # [x] setSectionType               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # Enumeration to specify the name pattern of the Memory Allocation Keyword.
        self.memoryAllocationKeywordPolicy: Optional[MemoryAllocationKeywordPolicyType] = None

        # This attribute introduces the ability to specify further intended properties of the MemorySection in with the related objects shall be placed. These properties are handled as to be selected. The intended options are mentioned in the list. In the Memory Mapping configuration, this option list is used to determine an appropriate MemMapAddressingModeSet.
        self.options: List[Identifier] = []

        # Specifies the expected initialization of the variables (inclusive those which are implementing VariableDataPrototypes). Therefore this is an implementation constraint for initialization code of BSW modules (especially RTE) as well as the start-up code which initializes the memory segment to which the AutosarDataPrototypes referring to the SwAddrMethod's are later on mapped. If the attribute is not defined it has the identical semantic as the attribute value "INIT".
        self.sectionInitializationPolicy: Optional[SectionInitializationPolicyType] = None

        # Defines the type of memory sections which can be associated with this addressing method.
        self.sectionType: Optional[MemorySectionType] = None

    def getMemoryAllocationKeywordPolicy(self) -> Optional[MemoryAllocationKeywordPolicyType]:
        """
        Enumeration to specify the name pattern of the Memory Allocation Keyword.
        """
        return self.memoryAllocationKeywordPolicy

    def setMemoryAllocationKeywordPolicy(self, value: Optional[MemoryAllocationKeywordPolicyType]) -> "SwAddrMethod":
        """
        Enumeration to specify the name pattern of the Memory Allocation Keyword. A None value is a no-op and does not overwrite an existing memoryAllocationKeywordPolicy.
        """
        if value is not None:
            self.memoryAllocationKeywordPolicy = value
        return self

    def getOptions(self) -> List[Identifier]:
        """
        This attribute introduces the ability to specify further intended properties of the MemorySection in with the related objects shall be placed. These properties are handled as to be selected. The intended options are mentioned in the list. In the Memory Mapping configuration, this option list is used to determine an appropriate MemMapAddressingModeSet.
        """
        return self.options

    def addOption(self, value: Identifier) -> "SwAddrMethod":
        """
        This attribute introduces the ability to specify further intended properties of the MemorySection in with the related objects shall be placed. These properties are handled as to be selected. The intended options are mentioned in the list. In the Memory Mapping configuration, this option list is used to determine an appropriate MemMapAddressingModeSet.
        """
        self.options.append(value)
        return self

    def getSectionInitializationPolicy(self) -> Optional[SectionInitializationPolicyType]:
        """
        Specifies the expected initialization of the variables (inclusive those which are implementing VariableDataPrototypes). Therefore this is an implementation constraint for initialization code of BSW modules (especially RTE) as well as the start-up code which initializes the memory segment to which the AutosarDataPrototypes referring to the SwAddrMethod's are later on mapped. If the attribute is not defined it has the identical semantic as the attribute value "INIT".
        """
        return self.sectionInitializationPolicy

    def setSectionInitializationPolicy(self, value: Optional[SectionInitializationPolicyType]) -> "SwAddrMethod":
        """
        Specifies the expected initialization of the variables (inclusive those which are implementing VariableDataPrototypes). Therefore this is an implementation constraint for initialization code of BSW modules (especially RTE) as well as the start-up code which initializes the memory segment to which the AutosarDataPrototypes referring to the SwAddrMethod's are later on mapped. If the attribute is not defined it has the identical semantic as the attribute value "INIT". A None value is a no-op and does not overwrite an existing sectionInitializationPolicy.
        """
        if value is not None:
            self.sectionInitializationPolicy = value
        return self

    def getSectionType(self) -> Optional[MemorySectionType]:
        """
        Defines the type of memory sections which can be associated with this addressing method.
        """
        return self.sectionType

    def setSectionType(self, value: Optional[MemorySectionType]) -> "SwAddrMethod":
        """
        Defines the type of memory sections which can be associated with this addressing method. A None value is a no-op and does not overwrite an existing sectionType.
        """
        if value is not None:
            self.sectionType = value
        return self
