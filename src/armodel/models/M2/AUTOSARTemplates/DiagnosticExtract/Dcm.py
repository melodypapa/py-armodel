from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import AREnum, PositiveInteger, RefType, TimeValue


class DiagnosticAuthRoleProxy(ARObject):
    """This meta-class indicates that an authentication is generally foreseen. The question whether the authentication is done in general or whether it is done role-specific depends on the existence of references to DiagAuthRole."""

    # DiagnosticAuthRoleProxy method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.33, p.76
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11  (writer emits the DIAGNOSTIC-AUTH-ROLE-PROXY tag; reader construction via DiagnosticAccessPermission)
    # [x] getAuthenticationRoleRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addAuthenticationRoleRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.
        self.authenticationRoleRefs: List[RefType] = []

    def getAuthenticationRoleRefs(self) -> List[RefType]:
        """
        This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.
        """
        return self.authenticationRoleRefs

    def addAuthenticationRoleRef(self, ref: Optional[RefType]):
        """
        This reference identifies the authenticationRole applicable for the enclosing DiagnosticAccessPermission.

        A None value is a no-op and does not extend the authenticationRoleRefs list.
        """
        if ref is not None:
            self.authenticationRoleRefs.append(ref)
        return self


class DiagnosticJumpToBootLoaderEnum(AREnum):
    """This enumeration contains the options for jumping to a boot loader."""

    # DiagnosticJumpToBootLoaderEnum method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.31, p.75
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # (no methods) — enum value form serialized on DiagnosticSession.jumpToBootLoader
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11

    # This diagnostic session doesn't allow to jump to Bootloader. Tags: atp.EnumerationLiteralIndex=0
    NO_BOOT = "NO-BOOT"

    # This diagnostic session allows to jump to OEM Bootloader. In this case the bootloader send the final response. Tags: atp.EnumerationLiteralIndex=1
    OEM_BOOT = "OEM-BOOT"

    # This diagnostic session allows to jump to OEM Bootloader and application sends final response. Tags: atp.EnumerationLiteralIndex=3
    OEM_BOOT_RESP_APP = "OEM-BOOT-RESP-APP"

    # This diagnostic session allows to jump to System Supplier Bootloader.  In this case the bootloader send the final response. Tags: atp.EnumerationLiteralIndex=2
    SYSTEM_SUPPLIER_BOOT = "SYSTEM-SUPPLIER-BOOT"

    # This diagnostic session allows to jump to System Supplier Bootloader and application sends final response. Tags: atp.EnumerationLiteralIndex=4
    SYSTEM_SUPPLIER_BOOT_RESP_APP = "SYSTEM-SUPPLIER-BOOT-RESP-APP"

    def __init__(self):
        super().__init__(
            (
                DiagnosticJumpToBootLoaderEnum.NO_BOOT,
                DiagnosticJumpToBootLoaderEnum.OEM_BOOT,
                DiagnosticJumpToBootLoaderEnum.OEM_BOOT_RESP_APP,
                DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT,
                DiagnosticJumpToBootLoaderEnum.SYSTEM_SUPPLIER_BOOT_RESP_APP,
            )
        )


class DiagnosticSession(DiagnosticCommonElement):
    """This meta-class represents the ability to define a diagnostic session. Tags: atp.recommendedPackage=DiagnosticSessions"""

    # DiagnosticSession method parity checklist:
    # Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.30, p.74
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getId                        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setId                        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getJumpToBootLoader          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setJumpToBootLoader          [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getP2ServerMax               [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setP2ServerMax               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getP2StarServerMax           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setP2StarServerMax           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This is the numerical identifier used to identify the DiagnosticSession in the scope of diagnostic workflow
        self.id: Optional[PositiveInteger] = None

        # This attribute represents the ability to define whether this diagnostic session allows to jump to Bootloader (OEM Bootloader or System Supplier Bootloader). If this diagnostic session doesn't allow to jump to Bootloader the value JumpToBootLoaderEnum.noBoot shall be chosen.
        self.jumpToBootLoader: Optional[DiagnosticJumpToBootLoaderEnum] = None

        # This is the session value for P2ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.
        self.p2ServerMax: Optional[TimeValue] = None

        # This is the session value for P2*ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.
        self.p2StarServerMax: Optional[TimeValue] = None

    def getId(self) -> Optional[PositiveInteger]:
        """
        This is the numerical identifier used to identify the DiagnosticSession in the scope of diagnostic workflow
        """
        return self.id

    def setId(self, value: Optional[PositiveInteger]):
        """
        This is the numerical identifier used to identify the DiagnosticSession in the scope of diagnostic workflow

        A None value is a no-op and does not overwrite an existing id.
        """
        if value is not None:
            self.id = value
        return self

    def getJumpToBootLoader(self) -> Optional[DiagnosticJumpToBootLoaderEnum]:
        """
        This attribute represents the ability to define whether this diagnostic session allows to jump to Bootloader (OEM Bootloader or System Supplier Bootloader). If this diagnostic session doesn't allow to jump to Bootloader the value JumpToBootLoaderEnum.noBoot shall be chosen.
        """
        return self.jumpToBootLoader

    def setJumpToBootLoader(self, value: Optional[DiagnosticJumpToBootLoaderEnum]):
        """
        This attribute represents the ability to define whether this diagnostic session allows to jump to Bootloader (OEM Bootloader or System Supplier Bootloader). If this diagnostic session doesn't allow to jump to Bootloader the value JumpToBootLoaderEnum.noBoot shall be chosen.

        A None value is a no-op and does not overwrite an existing jumpToBootLoader.
        """
        if value is not None:
            self.jumpToBootLoader = value
        return self

    def getP2ServerMax(self) -> Optional[TimeValue]:
        """
        This is the session value for P2ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.
        """
        return self.p2ServerMax

    def setP2ServerMax(self, value: Optional[TimeValue]):
        """
        This is the session value for P2ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.

        A None value is a no-op and does not overwrite an existing p2ServerMax.
        """
        if value is not None:
            self.p2ServerMax = value
        return self

    def getP2StarServerMax(self) -> Optional[TimeValue]:
        """
        This is the session value for P2*ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.
        """
        return self.p2StarServerMax

    def setP2StarServerMax(self, value: Optional[TimeValue]):
        """
        This is the session value for P2*ServerMax in seconds (per Session Control). The AUTOSAR configuration standard is to use SI units, so this parameter is defined as a float value in seconds.

        A None value is a no-op and does not overwrite an existing p2StarServerMax.
        """
        if value is not None:
            self.p2StarServerMax = value
        return self
