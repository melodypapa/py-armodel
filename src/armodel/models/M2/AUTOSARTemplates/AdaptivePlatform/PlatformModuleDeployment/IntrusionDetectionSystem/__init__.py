from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

__all__ = ["IdsPlatformInstantiation", "IdsmModuleInstantiation"]


class IdsPlatformInstantiation(AtpStructureElement, ABC):
    """
    This meta-class acts as an abstract base class for platform modules that implement the intrusion detection system. Tags: atp.Status=candidate
    """

    # IdsPlatformInstantiation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf, Table B.13, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addNetworkInterfaceRef     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getNetworkInterfaceRefs    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setTimeBaseRef             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTimeBaseRef             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is IdsPlatformInstantiation:
            raise TypeError("IdsPlatformInstantiation is an abstract class.")
        super().__init__(parent, short_name)

        # This association contains the network configuration that shall be applied to an instance of an IDS entity. Tags: atp.Status=candidate
        self.networkInterfaceRefs: List[RefType] = []

        # This reference identifies the applicable time base resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timeBase.timeBaseResource, timeBase.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        self.timeBaseRef: Optional[RefType] = None

    def addNetworkInterfaceRef(self, value: Optional[RefType]) -> "IdsPlatformInstantiation":
        """
        This association contains the network configuration that shall be applied to an instance of an IDS entity. Tags: atp.Status=candidate

        A None value is a no-op and does not extend the networkInterfaceRefs list.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.networkInterfaceRefs.append(value)
        return self

    def getNetworkInterfaceRefs(self) -> List[RefType]:
        """
        This association contains the network configuration that shall be applied to an instance of an IDS entity. Tags: atp.Status=candidate
        """
        return self.networkInterfaceRefs

    def setTimeBaseRef(self, value: Optional[RefType]) -> "IdsPlatformInstantiation":
        """
        This reference identifies the applicable time base resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timeBase.timeBaseResource, timeBase.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime

        A None value is a no-op and does not overwrite an existing timeBaseRef.

        Returns:
            self for method chaining
        """
        if value is not None:
            self.timeBaseRef = value
        return self

    def getTimeBaseRef(self) -> Optional[RefType]:
        """
        This reference identifies the applicable time base resource. Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=timeBase.timeBaseResource, timeBase.variationPoint.shortLabel atp.Status=candidate vh.latestBindingTime=systemDesignTime
        """
        return self.timeBaseRef


class IdsmModuleInstantiation(IdsPlatformInstantiation):
    """
    This meta-class defines the attributes for the IdsM configuration on a specific machine. Tags: atp.Status=candidate
    """

    # IdsmModuleInstantiation method parity checklist:
    # Spec: AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf, Table B.14, p.63
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    #
    # Table B.14 lists no Attribute rows; the readIdsmModuleInstantiation /
    # writeIdsmModuleInstantiation helpers forward to the inherited
    # IdsPlatformInstantiation coverage.

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)
