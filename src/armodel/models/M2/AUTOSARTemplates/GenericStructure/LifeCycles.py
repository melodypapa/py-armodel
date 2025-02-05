from typing import List
from xmlrpc.client import DateTime

from ....M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, RevisionLabelString
from ....M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement


class LifeCyclePeriod(ARObject):
    '''
        This meta class represents the ability to specify a point of time within a specified period, e.g. the starting
        or end point, in which a specific life cycle state is valid/applies to.
    '''
    def __init__(self):
        super().__init__()

        self.arReleaseVersion = None                            # type: RevisionLabelString
        self.date = None                                        # type: DateTime
        self.productRelease = None                              # type: RevisionLabelString

    def getArReleaseVersion(self):
        return self.arReleaseVersion

    def setArReleaseVersion(self, value):
        if value is not None:
            self.arReleaseVersion = value
        return self

    def getDate(self):
        return self.date

    def setDate(self, value):
        if value is not None:
            self.date = value
        return self

    def getProductRelease(self):
        return self.productRelease

    def setProductRelease(self, value):
        if value is not None:
            self.productRelease = value
        return self


class LifeCycleInfo(ARObject):
    def __init__(self):
        super().__init__()

        self.lcObjectRef = None                                 # type: RefType
        self.lcStateRef = None                                  # type: RefType
        self.periodBegin = None                                 # type: LifeCyclePeriod
        self.periodEnd = None                                   # type: LifeCyclePeriod
        self.remark = None                                      # type: DocumentationBlock
        self.useInsteadRefs = []                                # type: List[RefType]

    def getLcObjectRef(self):
        return self.lcObjectRef

    def setLcObjectRef(self, value):
        if value is not None:
            self.lcObjectRef = value
        return self

    def getLcStateRef(self):
        return self.lcStateRef

    def setLcStateRef(self, value):
        if value is not None:
            self.lcStateRef = value
        return self

    def getPeriodBegin(self):
        return self.periodBegin

    def setPeriodBegin(self, value):
        if value is not None:
            self.periodBegin = value
        return self

    def getPeriodEnd(self):
        return self.periodEnd

    def setPeriodEnd(self, value):
        if value is not None:
            self.periodEnd = value
        return self

    def getRemark(self):
        return self.remark

    def setRemark(self, value):
        if value is not None:
            self.remark = value
        return self

    def getUseInsteadRefs(self):
        return self.useInsteadRefs

    def addUseInsteadRef(self, value):
        if value is not None:
            self.useInsteadRefs.append(value)
        return self


class LifeCycleInfoSet(ARElement):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)

        self.defaultLcStateRef = None                           # type: RefType
        self.defaultPeriodBegin = None                          # type: LifeCyclePeriod
        self.defaultPeriodEnd = None                            # type: LifeCyclePeriod
        self.lifeCycleInfos = []                                # type: List[LifeCycleInfo]
        self.usedLifeCycleStateDefinitionGroupRef = None        # type: RefType

    def getDefaultLcStateRef(self):
        return self.defaultLcStateRef

    def setDefaultLcStateRef(self, value):
        if value is not None:
            self.defaultLcStateRef = value
        return self

    def getDefaultPeriodBegin(self):
        return self.defaultPeriodBegin

    def setDefaultPeriodBegin(self, value):
        if value is not None:
            self.defaultPeriodBegin = value
        return self

    def getDefaultPeriodEnd(self):
        return self.defaultPeriodEnd

    def setDefaultPeriodEnd(self, value):
        if value is not None:
            self.defaultPeriodEnd = value
        return self

    def getLifeCycleInfos(self):
        return self.lifeCycleInfos

    def addLifeCycleInfo(self, value):
        if value is not None:
            self.lifeCycleInfos.append(value)
        return self

    def getUsedLifeCycleStateDefinitionGroupRef(self):
        return self.usedLifeCycleStateDefinitionGroupRef

    def setUsedLifeCycleStateDefinitionGroupRef(self, value):
        if value is not None:
            self.usedLifeCycleStateDefinitionGroupRef = value
        return self
