from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject, EngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, NameToken, RefType, RegularExpression, UriString, VerbatimString
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg


class BuildActionInvocator(ARObject):
    """
    This meta-class represents the ability to specify the invocation of a task in a build action.
    """

    # BuildActionInvocator method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.6, p.372 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCommand   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCommand   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSdg       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized.
        self.command: Optional[VerbatimString] = None

        # This represents a general data structure intended to denote parameters for the BuildAction.
        self.sdgs: List[Sdg] = []

    def getCommand(self) -> Optional[VerbatimString]:
        """This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized."""
        return self.command

    def setCommand(self, value: Optional[VerbatimString]) -> "BuildActionInvocator":
        """This represents the command to invocate the processor. Note that this is a generic string which can be interpreted properly in the processor environment. Note that it is optional due to the fact that some actions are hardwired in the environment and do not need an explicit command. On the other hand the properties of an invocator can be complex and not standardized. A None value is a no-op and does not overwrite an existing command."""
        if value is not None:
            self.command = value
        return self

    def getSdgs(self) -> List[Sdg]:
        """This represents a general data structure intended to denote parameters for the BuildAction."""
        return self.sdgs

    def addSdg(self, value: Optional[Sdg]) -> "BuildActionInvocator":
        """This represents a general data structure intended to denote parameters for the BuildAction. A None value is a no-op and does not append anything."""
        if value is not None:
            self.sdgs.append(value)
        return self


class BuildActionEntity(Identifiable):
    """
    This meta-class represents the ability to describe a build action entity which might be specialized to environments as well as to individual build actions.
    """

    # BuildActionEntity method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.5, p.371 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__          [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addDeliveryArtifact [x] impl  [x] docstring  [x] test  [x] reader  [ ] writer  R23-11
    # [x] getDeliveryArtifacts [x] impl  [x] docstring  [x] test  [ ] reader  [x] writer  R23-11
    # [x] getInvocation     [x] impl  [x] docstring  [x] test  [ ] reader  [x] writer  R23-11
    # [x] setInvocation     [x] impl  [x] docstring  [x] test  [x] reader  [ ] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        if type(self) is BuildActionEntity:
            raise TypeError("BuildActionEntity is an abstract class.")

        super().__init__(parent, short_name)

        # This denotes the delivery artifacts for the entity for reference purposes.
        self.deliveryArtifacts: List[AutosarEngineeringObject] = []

        # This specifies how to invoke a build action in the given environment.
        self.invocation: Optional[BuildActionInvocator] = None

    def addDeliveryArtifact(self, value: Optional[AutosarEngineeringObject]) -> "BuildActionEntity":
        """This denotes the delivery artifacts for the entity for reference purposes. A None value is a no-op and does not append anything."""
        if value is not None:
            self.deliveryArtifacts.append(value)
        return self

    def getDeliveryArtifacts(self) -> List[AutosarEngineeringObject]:
        """This denotes the delivery artifacts for the entity for reference purposes."""
        return self.deliveryArtifacts

    def getInvocation(self) -> Optional[BuildActionInvocator]:
        """This specifies how to invoke a build action in the given environment."""
        return self.invocation

    def setInvocation(self, value: Optional[BuildActionInvocator]) -> "BuildActionEntity":
        """This specifies how to invoke a build action in the given environment. A None value is a no-op and does not overwrite an existing invocation."""
        if value is not None:
            self.invocation = value
        return self


class BuildEngineeringObject(EngineeringObject):
    """
    This meta-class represents the ability to denote an artifact which is processed within a particular build action.
    """

    # BuildEngineeringObject method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.7, p.373 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__              [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getFileType           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFileType           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFileTypePattern    [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setFileTypePattern    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getIntendedFilename   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setIntendedFilename   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParentCategory     [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParentCategory     [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getParentShortLabel   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setParentShortLabel   [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getShortLabelPattern  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setShortLabelPattern  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This attribute indicates the file type which shall used for the engineering object. Note that an engineering object may deliver multiple representations of the same artifact. This attribute can select one of the provided representations.
        self.fileType: Optional[NameToken] = None

        # This attribute allows to define a set of engineering objects as pattern based search applied to the filetype of the individual Engineering objects.
        self.fileTypePattern: Optional[RegularExpression] = None

        # This attribute represents the name of the file if it is created newly. Note that engineering object resolves category + ShortLabel indicate mainly to refer to an existing file. If the file is created newly, the filename can either be determined by built in policy or predefined here. Note that extensions shall part of file name even if it could be derived from fileType.
        self.intendedFilename: Optional[UriString] = None

        # This represents the category of the parent object.
        self.parentCategory: Optional[NameToken] = None

        # This represents the shortLabel of the parent object. This allows to specify the output position in a hierarchically organized system.
        self.parentShortLabel: Optional[NameToken] = None

        # This attribute allows to define a set of engineering objects as pattern based search applied to the shortLabel of the individual Engineering objects.
        self.shortLabelPattern: Optional[RegularExpression] = None

    def getFileType(self) -> Optional[NameToken]:
        """This attribute indicates the file type which shall used for the engineering object. Note that an engineering object may deliver multiple representations of the same artifact. This attribute can select one of the provided representations."""
        return self.fileType

    def setFileType(self, value: Optional[NameToken]) -> "BuildEngineeringObject":
        """This attribute indicates the file type which shall used for the engineering object. Note that an engineering object may deliver multiple representations of the same artifact. This attribute can select one of the provided representations. A None value is a no-op and does not overwrite an existing fileType."""
        if value is not None:
            self.fileType = value
        return self

    def getFileTypePattern(self) -> Optional[RegularExpression]:
        """This attribute allows to define a set of engineering objects as pattern based search applied to the filetype of the individual Engineering objects."""
        return self.fileTypePattern

    def setFileTypePattern(self, value: Optional[RegularExpression]) -> "BuildEngineeringObject":
        """This attribute allows to define a set of engineering objects as pattern based search applied to the filetype of the individual Engineering objects. A None value is a no-op and does not overwrite an existing fileTypePattern."""
        if value is not None:
            self.fileTypePattern = value
        return self

    def getIntendedFilename(self) -> Optional[UriString]:
        """This attribute represents the name of the file if it is created newly. Note that engineering object resolves category + ShortLabel indicate mainly to refer to an existing file. If the file is created newly, the filename can either be determined by built in policy or predefined here. Note that extensions shall part of file name even if it could be derived from fileType."""
        return self.intendedFilename

    def setIntendedFilename(self, value: Optional[UriString]) -> "BuildEngineeringObject":
        """This attribute represents the name of the file if it is created newly. Note that engineering object resolves category + ShortLabel indicate mainly to refer to an existing file. If the file is created newly, the filename can either be determined by built in policy or predefined here. Note that extensions shall part of file name even if it could be derived from fileType. A None value is a no-op and does not overwrite an existing intendedFilename."""
        if value is not None:
            self.intendedFilename = value
        return self

    def getParentCategory(self) -> Optional[NameToken]:
        """This represents the category of the parent object."""
        return self.parentCategory

    def setParentCategory(self, value: Optional[NameToken]) -> "BuildEngineeringObject":
        """This represents the category of the parent object. A None value is a no-op and does not overwrite an existing parentCategory."""
        if value is not None:
            self.parentCategory = value
        return self

    def getParentShortLabel(self) -> Optional[NameToken]:
        """This represents the shortLabel of the parent object. This allows to specify the output position in a hierarchically organized system."""
        return self.parentShortLabel

    def setParentShortLabel(self, value: Optional[NameToken]) -> "BuildEngineeringObject":
        """This represents the shortLabel of the parent object. This allows to specify the output position in a hierarchically organized system. A None value is a no-op and does not overwrite an existing parentShortLabel."""
        if value is not None:
            self.parentShortLabel = value
        return self

    def getShortLabelPattern(self) -> Optional[RegularExpression]:
        """This attribute allows to define a set of engineering objects as pattern based search applied to the shortLabel of the individual Engineering objects."""
        return self.shortLabelPattern

    def setShortLabelPattern(self, value: Optional[RegularExpression]) -> "BuildEngineeringObject":
        """This attribute allows to define a set of engineering objects as pattern based search applied to the shortLabel of the individual Engineering objects. A None value is a no-op and does not overwrite an existing shortLabelPattern."""
        if value is not None:
            self.shortLabelPattern = value
        return self


class BuildActionIoElement(ARObject):
    """
    This meta-class represents the ability to specify the input/output entities of a BuildAction.
    """

    # BuildActionIoElement method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.3, p.369 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__            [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getCategory         [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setCategory         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEcucDefinitionRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEcucDefinitionRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getEngineeringObject [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setEngineeringObject [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getRole             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRole             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getSdgs             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSdg              [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self):
        super().__init__()

        # This element assigns a category to the parent element. It is intended to specialize the usage and/or the content of the object. Such a specialization may also impose particular semantic constraints on the entire substructure. See also Identifiable.
        self.category: Optional[NameToken] = None

        # This association denotes an ECUC parameter definition. The such referenced parameters are subject of the build action input/output. Note that the reference to the definition denotes the right for a build action to read and/or write values for the given definition and all contained definitions.
        self.ecucDefinitionRef: Optional[RefType] = None

        # This represents an artifact applicable to the build action.
        self.engineeringObject: Optional[BuildEngineeringObject] = None

        # foreignModelReference (ForeignModelReference, 0..1, aggr) is intentionally unmodeled: the member class has no Class table in the R23-11 or R4.3.1 corpus (XSD-only, AUTOSAR_00052.xsd) and is not in the confirmed sync closure — tracked as a deviation in method_deviation_by_class.md.

        # This allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties.
        self.role: Optional[Identifier] = None

        # This special data group allows to denote specific data. The structure is subject of mutual agreement.
        self.sdgs: List[Sdg] = []

    def getCategory(self) -> Optional[NameToken]:
        """This element assigns a category to the parent element. It is intended to specialize the usage and/or the content of the object. Such a specialization may also impose particular semantic constraints on the entire substructure. See also Identifiable."""
        return self.category

    def setCategory(self, value: Optional[NameToken]) -> "BuildActionIoElement":
        """This element assigns a category to the parent element. It is intended to specialize the usage and/or the content of the object. Such a specialization may also impose particular semantic constraints on the entire substructure. See also Identifiable. A None value is a no-op and does not overwrite an existing category."""
        if value is not None:
            self.category = value
        return self

    def getEcucDefinitionRef(self) -> Optional[RefType]:
        """This association denotes an ECUC parameter definition. The such referenced parameters are subject of the build action input/output. Note that the reference to the definition denotes the right for a build action to read and/or write values for the given definition and all contained definitions."""
        return self.ecucDefinitionRef

    def setEcucDefinitionRef(self, value: Optional[RefType]) -> "BuildActionIoElement":
        """This association denotes an ECUC parameter definition. The such referenced parameters are subject of the build action input/output. Note that the reference to the definition denotes the right for a build action to read and/or write values for the given definition and all contained definitions. A None value is a no-op and does not overwrite an existing ecucDefinitionRef."""
        if value is not None:
            self.ecucDefinitionRef = value
        return self

    def getEngineeringObject(self) -> Optional[BuildEngineeringObject]:
        """This represents an artifact applicable to the build action."""
        return self.engineeringObject

    def setEngineeringObject(self, value: Optional[BuildEngineeringObject]) -> "BuildActionIoElement":
        """This represents an artifact applicable to the build action. A None value is a no-op and does not overwrite an existing engineeringObject."""
        if value is not None:
            self.engineeringObject = value
        return self

    def getRole(self) -> Optional[Identifier]:
        """This allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties."""
        return self.role

    def setRole(self, value: Optional[Identifier]) -> "BuildActionIoElement":
        """This allows to denote a particular role of the collection. Note that the applicable semantics shall be mutually agreed between the two parties. A None value is a no-op and does not overwrite an existing role."""
        if value is not None:
            self.role = value
        return self

    def getSdgs(self) -> List[Sdg]:
        """This special data group allows to denote specific data. The structure is subject of mutual agreement."""
        return self.sdgs

    def addSdg(self, value: Optional[Sdg]) -> "BuildActionIoElement":
        """This special data group allows to denote specific data. The structure is subject of mutual agreement. A None value is a no-op and does not append anything."""
        if value is not None:
            self.sdgs.append(value)
        return self


class BuildActionEnvironment(Identifiable):
    """
    This meta-class represents the ability to specify a build action environment.
    """

    # BuildActionEnvironment method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.4, p.370 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__     [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] getSdgs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addSdg       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a general data structure intended to denote parameters for the BuildActionEnvironment.
        self.sdgs: List[Sdg] = []

    def getSdgs(self) -> List[Sdg]:
        """This represents a general data structure intended to denote parameters for the BuildActionEnvironment."""
        return self.sdgs

    def addSdg(self, value: Optional[Sdg]) -> "BuildActionEnvironment":
        """This represents a general data structure intended to denote parameters for the BuildActionEnvironment. A None value is a no-op and does not append anything."""
        if value is not None:
            self.sdgs.append(value)
        return self


class BuildAction(BuildActionEntity):
    """
    This meta-class represents the ability to specify a build action.
    """

    # BuildAction method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.2, p.366 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                   [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] addCreatedData             [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getCreatedDatas            [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addFollowUpActionRef       [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getFollowUpActionRefs      [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addInputData               [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getInputDatas              [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addModifiedData            [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getModifiedDatas           [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addPredecessorActionRef    [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getPredecessorActionRefs   [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] getRequiredEnvironmentRef  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] setRequiredEnvironmentRef  [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents the artifacts which are created by the processor.
        self.createdDatas: List[BuildActionIoElement] = []

        # This association specifies a set of follow up actions.
        self.followUpActionRefs: List[RefType] = []

        # This represents the artifacts which are read by the processor.
        self.inputDatas: List[BuildActionIoElement] = []

        # This denotes the data which are modified by the action.
        self.modifiedDatas: List[BuildActionIoElement] = []

        # This association specifies a set of predecessors. These actions shall be finished before but necessarily immediately after the given action.. These actions need to be performed in the specified order.
        self.predecessorActionRefs: List[RefType] = []

        # This represents the environment which is required to use the specified Processor.
        self.requiredEnvironmentRef: Optional[RefType] = None

    def addCreatedData(self, value: Optional[BuildActionIoElement]) -> "BuildAction":
        """This represents the artifacts which are created by the processor. A None value is a no-op and does not append anything."""
        if value is not None:
            self.createdDatas.append(value)
        return self

    def getCreatedDatas(self) -> List[BuildActionIoElement]:
        """This represents the artifacts which are created by the processor."""
        return self.createdDatas

    def addFollowUpActionRef(self, value: Optional[RefType]) -> "BuildAction":
        """This association specifies a set of follow up actions. A None value is a no-op and does not append anything."""
        if value is not None:
            self.followUpActionRefs.append(value)
        return self

    def getFollowUpActionRefs(self) -> List[RefType]:
        """This association specifies a set of follow up actions."""
        return self.followUpActionRefs

    def addInputData(self, value: Optional[BuildActionIoElement]) -> "BuildAction":
        """This represents the artifacts which are read by the processor. A None value is a no-op and does not append anything."""
        if value is not None:
            self.inputDatas.append(value)
        return self

    def getInputDatas(self) -> List[BuildActionIoElement]:
        """This represents the artifacts which are read by the processor."""
        return self.inputDatas

    def addModifiedData(self, value: Optional[BuildActionIoElement]) -> "BuildAction":
        """This denotes the data which are modified by the action. A None value is a no-op and does not append anything."""
        if value is not None:
            self.modifiedDatas.append(value)
        return self

    def getModifiedDatas(self) -> List[BuildActionIoElement]:
        """This denotes the data which are modified by the action."""
        return self.modifiedDatas

    def addPredecessorActionRef(self, value: Optional[RefType]) -> "BuildAction":
        """This association specifies a set of predecessors. These actions shall be finished before but necessarily immediately after the given action.. These actions need to be performed in the specified order. A None value is a no-op and does not append anything."""
        if value is not None:
            self.predecessorActionRefs.append(value)
        return self

    def getPredecessorActionRefs(self) -> List[RefType]:
        """This association specifies a set of predecessors. These actions shall be finished before but necessarily immediately after the given action.. These actions need to be performed in the specified order."""
        return self.predecessorActionRefs

    def getRequiredEnvironmentRef(self) -> Optional[RefType]:
        """This represents the environment which is required to use the specified Processor."""
        return self.requiredEnvironmentRef

    def setRequiredEnvironmentRef(self, value: Optional[RefType]) -> "BuildAction":
        """This represents the environment which is required to use the specified Processor. A None value is a no-op and does not overwrite an existing requiredEnvironmentRef."""
        if value is not None:
            self.requiredEnvironmentRef = value
        return self


class BuildActionManifest(Identifiable):
    """
    This meta-class represents the ability to specify a manifest for processing artifacts. An example use case is the processing of ECUC parameter values.
    """

    # BuildActionManifest method parity checklist:
    # Spec: R23-11/AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 10.1, p.365 (R23-11)
    # Spec verified: R23-11
    # Columns: impl / docstring / test / reader / writer / release   ([—] = no XML element)
    # [x] __init__                    [x] impl  [x] docstring  [x] test  [—] reader  [—] writer  R23-11
    # [x] createBuildAction           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBuildActions             [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] createBuildActionEnvironment [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getBuildActionEnvironments  [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addDynamicActionRef         [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getDynamicActionRefs        [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addStartActionRef           [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getStartActionRefs          [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11
    # [x] addTearDownActionRef        [x] impl  [x] docstring  [x] test  [x] reader  [—] writer  R23-11
    # [x] getTearDownActionRefs       [x] impl  [x] docstring  [x] test  [—] reader  [x] writer  R23-11

    def __init__(self, parent: ARObject, short_name: str):
        super().__init__(parent, short_name)

        # This represents a particular action in the build chain.
        self.buildActions: List[BuildAction] = []

        # This represents a build action environment.
        self.buildActionEnvironments: List[BuildActionEnvironment] = []

        # This denotes an Action which is to be executed as part of the dynamic action set.
        self.dynamicActionRefs: List[RefType] = []

        # This specifies the list of actions to be performed at the beginning of the process.
        self.startActionRefs: List[RefType] = []

        # This specifies the set of action which shall be performed after all other actions in the manifest were performed.
        self.tearDownActionRefs: List[RefType] = []

    def createBuildAction(self, short_name: str) -> BuildAction:
        """This represents a particular action in the build chain."""
        for action in self.buildActions:
            if action.getShortName() == short_name:
                return action
        action = BuildAction(self, short_name)
        self.buildActions.append(action)
        return action

    def getBuildActions(self) -> List[BuildAction]:
        """This represents a particular action in the build chain."""
        return self.buildActions

    def createBuildActionEnvironment(self, short_name: str) -> BuildActionEnvironment:
        """This represents a build action environment."""
        for environment in self.buildActionEnvironments:
            if environment.getShortName() == short_name:
                return environment
        environment = BuildActionEnvironment(self, short_name)
        self.buildActionEnvironments.append(environment)
        return environment

    def getBuildActionEnvironments(self) -> List[BuildActionEnvironment]:
        """This represents a build action environment."""
        return self.buildActionEnvironments

    def addDynamicActionRef(self, value: Optional[RefType]) -> "BuildActionManifest":
        """This denotes an Action which is to be executed as part of the dynamic action set. A None value is a no-op and does not append anything."""
        if value is not None:
            self.dynamicActionRefs.append(value)
        return self

    def getDynamicActionRefs(self) -> List[RefType]:
        """This denotes an Action which is to be executed as part of the dynamic action set."""
        return self.dynamicActionRefs

    def addStartActionRef(self, value: Optional[RefType]) -> "BuildActionManifest":
        """This specifies the list of actions to be performed at the beginning of the process. A None value is a no-op and does not append anything."""
        if value is not None:
            self.startActionRefs.append(value)
        return self

    def getStartActionRefs(self) -> List[RefType]:
        """This specifies the list of actions to be performed at the beginning of the process."""
        return self.startActionRefs

    def addTearDownActionRef(self, value: Optional[RefType]) -> "BuildActionManifest":
        """This specifies the set of action which shall be performed after all other actions in the manifest were performed. A None value is a no-op and does not append anything."""
        if value is not None:
            self.tearDownActionRefs.append(value)
        return self

    def getTearDownActionRefs(self) -> List[RefType]:
        """This specifies the set of action which shall be performed after all other actions in the manifest were performed."""
        return self.tearDownActionRefs
