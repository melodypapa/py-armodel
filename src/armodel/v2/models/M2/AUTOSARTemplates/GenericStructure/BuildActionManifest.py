"""
AUTOSAR Package - BuildActionManifest

Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest
"""

from abc import ABC
from typing import List, Optional

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    NameToken,
    RefType,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import (
    EngineeringObject,
)
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Identifiable,
)


class BuildActionManifest(ARElement):
    """
    This meta-class represents the ability to specify a manifest for processing
    artifacts. An example use case is the processing of ECUC parameter values.
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionManifest
    
    Sources:
      - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (Page 134, Classic
      Platform R23-11)
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 365, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 173, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a build action environment.
        # atpSplitable; atpVariation.
        self._buildAction: List["BuildActionEnvironment"] = []

    @property
    def build_action(self) -> List["BuildActionEnvironment"]:
        """Get buildAction (Pythonic accessor)."""
        return self._buildAction
        # This denotes an Action which is to be executed as part of action set.
        self._dynamicAction: List["BuildAction"] = []

    @property
    def dynamic_action(self) -> List["BuildAction"]:
        """Get dynamicAction (Pythonic accessor)."""
        return self._dynamicAction
        # This specifies the list of actions to be performed at the the process.
        # 381 Document ID 89: AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate Module
                # Description Template R23-11.
        self._startAction: List["BuildAction"] = []

    @property
    def start_action(self) -> List["BuildAction"]:
        """Get startAction (Pythonic accessor)."""
        return self._startAction
        # This specifies the set of action which shall be performed other actions in
        # the manifest were performed.
        self._tearDownAction: List["BuildAction"] = []

    @property
    def tear_down_action(self) -> List["BuildAction"]:
        """Get tearDownAction (Pythonic accessor)."""
        return self._tearDownAction

    def with_build_action(self, value):
        """
        Set build_action and return self for chaining.

        Args:
            value: The build_action to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_build_action("value")
        """
        self.build_action = value  # Use property setter (gets validation)
        return self

    def with_dynamic_action(self, value):
        """
        Set dynamic_action and return self for chaining.

        Args:
            value: The dynamic_action to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_dynamic_action("value")
        """
        self.dynamic_action = value  # Use property setter (gets validation)
        return self

    def with_start_action(self, value):
        """
        Set start_action and return self for chaining.

        Args:
            value: The start_action to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_start_action("value")
        """
        self.start_action = value  # Use property setter (gets validation)
        return self

    def with_tear_down_action(self, value):
        """
        Set tear_down_action and return self for chaining.

        Args:
            value: The tear_down_action to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_tear_down_action("value")
        """
        self.tear_down_action = value  # Use property setter (gets validation)
        return self

    def with_sdg(self, value):
        """
        Set sdg and return self for chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    def with_sdg(self, value):
        """
        Set sdg and return self for chaining.

        Args:
            value: The sdg to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_sdg("value")
        """
        self.sdg = value  # Use property setter (gets validation)
        return self

    def with_delivery_artifact(self, value):
        """
        Set delivery_artifact and return self for chaining.

        Args:
            value: The delivery_artifact to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_delivery_artifact("value")
        """
        self.delivery_artifact = value  # Use property setter (gets validation)
        return self

    def with_created_data(self, value):
        """
        Set created_data and return self for chaining.

        Args:
            value: The created_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_created_data("value")
        """
        self.created_data = value  # Use property setter (gets validation)
        return self

    def with_follow_up_action(self, value):
        """
        Set follow_up_action and return self for chaining.

        Args:
            value: The follow_up_action to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_follow_up_action("value")
        """
        self.follow_up_action = value  # Use property setter (gets validation)
        return self

    def with_input_data(self, value):
        """
        Set input_data and return self for chaining.

        Args:
            value: The input_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_input_data("value")
        """
        self.input_data = value  # Use property setter (gets validation)
        return self

    def with_modified_data(self, value):
        """
        Set modified_data and return self for chaining.

        Args:
            value: The modified_data to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_modified_data("value")
        """
        self.modified_data = value  # Use property setter (gets validation)
        return self

    def with_predecessor(self, value):
        """
        Set predecessor and return self for chaining.

        Args:
            value: The predecessor to set

        Returns:
            self for method chaining

        Example:
            >>> obj.with_predecessor("value")
        """
        self.predecessor = value  # Use property setter (gets validation)
        return self

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBuildAction(self) -> List["BuildActionEnvironment"]:
        """
        AUTOSAR-compliant getter for buildAction.
        
        Returns:
            The buildAction value
        
        Note:
            Delegates to build_action property (CODING_RULE_V2_00017)
        """
        return self.build_action  # Delegates to property

    def getDynamicAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for dynamicAction.
        
        Returns:
            The dynamicAction value
        
        Note:
            Delegates to dynamic_action property (CODING_RULE_V2_00017)
        """
        return self.dynamic_action  # Delegates to property

    def getStartAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for startAction.
        
        Returns:
            The startAction value
        
        Note:
            Delegates to start_action property (CODING_RULE_V2_00017)
        """
        return self.start_action  # Delegates to property

    def getTearDownAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for tearDownAction.
        
        Returns:
            The tearDownAction value
        
        Note:
            Delegates to tear_down_action property (CODING_RULE_V2_00017)
        """
        return self.tear_down_action  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BuildActionIoElement(ARObject):
    """
    that the reference to the definition denotes the right for a build action to
    read and/or write values for the given definition and all contained
    definitions. engineering BuildEngineeringObject 0..1 aggr This represents an
    artifact applicable to the build action. Object foreignModel
    ForeignModelReference 0..1 aggr This is a reference to a foreign model
    element. Note that Reference it is not modeled as an association because it
    should also be able to refer also to non AUTOSAR models. (cid:53) 368 of 535
    Document ID 202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure
    Template AUTOSAR FO R23-11 (cid:52)
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionIoElement
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 368, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This element assigns a category to the parent element.
        # It to specialize the usage and/or the content of Such a specialization may
                # also impose constraints on the entire substructure.
        # Identifiable.
        self._category: "NameToken" = None

    @property
    def category(self) -> "NameToken":
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: "NameToken") -> None:
        """
        Set category with validation.
        
        Args:
            value: The category to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"category must be NameToken or str, got {type(value).__name__}"
            )
        self._category = value
        # This association denotes an ECUC parameter definition.
        # referenced parameters are subject of the build.
        self._ecucDefinition: Optional["EcucDefinitionElement"] = None

    @property
    def ecuc_definition(self) -> Optional["EcucDefinitionElement"]:
        """Get ecucDefinition (Pythonic accessor)."""
        return self._ecucDefinition

    @ecuc_definition.setter
    def ecuc_definition(self, value: Optional["EcucDefinitionElement"]) -> None:
        """
        Set ecucDefinition with validation.
        
        Args:
            value: The ecucDefinition to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._ecucDefinition = None
            return

        if not isinstance(value, EcucDefinitionElement):
            raise TypeError(
                f"ecucDefinition must be EcucDefinitionElement or None, got {type(value).__name__}"
            )
        self._ecucDefinition = value
        # This attribute allows to denote a particular role of the that the applicable
        # semantics shall be between the two parties.
        self._role: Optional["Identifier"] = None

    @property
    def role(self) -> Optional["Identifier"]:
        """Get role (Pythonic accessor)."""
        return self._role

    @role.setter
    def role(self, value: Optional["Identifier"]) -> None:
        """
        Set role with validation.
        
        Args:
            value: The role to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._role = None
            return

        if not isinstance(value, (Identifier, str)):
            raise TypeError(
                f"role must be Identifier or str or None, got {type(value).__name__}"
            )
        self._role = value
        # This special data group allows to denote specific data.
        # is subject of mutual agreement.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCategory(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for category.
        
        Returns:
            The category value
        
        Note:
            Delegates to category property (CODING_RULE_V2_00017)
        """
        return self.category  # Delegates to property

    def setCategory(self, value: "NameToken") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for category with method chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to category property setter (gets validation automatically)
        """
        self.category = value  # Delegates to property setter
        return self

    def getEcucDefinition(self) -> "EcucDefinitionElement":
        """
        AUTOSAR-compliant getter for ecucDefinition.
        
        Returns:
            The ecucDefinition value
        
        Note:
            Delegates to ecuc_definition property (CODING_RULE_V2_00017)
        """
        return self.ecuc_definition  # Delegates to property

    def setEcucDefinition(self, value: "EcucDefinitionElement") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for ecucDefinition with method chaining.
        
        Args:
            value: The ecucDefinition to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ecuc_definition property setter (gets validation automatically)
        """
        self.ecuc_definition = value  # Delegates to property setter
        return self

    def getRole(self) -> "Identifier":
        """
        AUTOSAR-compliant getter for role.
        
        Returns:
            The role value
        
        Note:
            Delegates to role property (CODING_RULE_V2_00017)
        """
        return self.role  # Delegates to property

    def setRole(self, value: "Identifier") -> "BuildActionIoElement":
        """
        AUTOSAR-compliant setter for role with method chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to role property setter (gets validation automatically)
        """
        self.role = value  # Delegates to property setter
        return self

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.
        
        Returns:
            The sdg value
        
        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: "NameToken") -> "BuildActionIoElement":
        """
        Set category and return self for chaining.
        
        Args:
            value: The category to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_category("value")
        """
        self.category = value  # Use property setter (gets validation)
        return self

    def with_ecuc_definition(self, value: Optional["EcucDefinitionElement"]) -> "BuildActionIoElement":
        """
        Set ecucDefinition and return self for chaining.
        
        Args:
            value: The ecucDefinition to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ecuc_definition("value")
        """
        self.ecuc_definition = value  # Use property setter (gets validation)
        return self

    def with_role(self, value: Optional["Identifier"]) -> "BuildActionIoElement":
        """
        Set role and return self for chaining.
        
        Args:
            value: The role to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_role("value")
        """
        self.role = value  # Use property setter (gets validation)
        return self



class BuildActionEnvironment(Identifiable):
    """
    This meta-class represents the ability to specify a build action
    environment.
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionEnvironment
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 370, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 173, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents a general data structure intended to for the
        # BuildActionEnvironment.
        self._sdg: List["Sdg"] = []

    @property
    def sdg(self) -> List["Sdg"]:
        """Get sdg (Pythonic accessor)."""
        return self._sdg

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getSdg(self) -> List["Sdg"]:
        """
        AUTOSAR-compliant getter for sdg.
        
        Returns:
            The sdg value
        
        Note:
            Delegates to sdg property (CODING_RULE_V2_00017)
        """
        return self.sdg  # Delegates to property

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====



class BuildActionEntity(Identifiable, ABC):
    """
    This meta-class represents the ability to describe a build action entity
    which might be specialized to environments as well as to individual build
    actions.
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionEntity
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 370, Foundation
      R23-11)
    """
    def __init__(self):
        if type(self) is BuildActionEntity:
            raise TypeError("BuildActionEntity is an abstract class.")
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This denotes the delivery artifacts for the entity for purposes.
        self._deliveryArtifact: List["AutosarEngineering"] = []

    @property
    def delivery_artifact(self) -> List["AutosarEngineering"]:
        """Get deliveryArtifact (Pythonic accessor)."""
        return self._deliveryArtifact
        # This specifies how to invoke a build action in the given.
        self._invocation: Optional["BuildActionInvocator"] = None

    @property
    def invocation(self) -> Optional["BuildActionInvocator"]:
        """Get invocation (Pythonic accessor)."""
        return self._invocation

    @invocation.setter
    def invocation(self, value: Optional["BuildActionInvocator"]) -> None:
        """
        Set invocation with validation.
        
        Args:
            value: The invocation to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._invocation = None
            return

        if not isinstance(value, BuildActionInvocator):
            raise TypeError(
                f"invocation must be BuildActionInvocator or None, got {type(value).__name__}"
            )
        self._invocation = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getDeliveryArtifact(self) -> List["AutosarEngineering"]:
        """
        AUTOSAR-compliant getter for deliveryArtifact.
        
        Returns:
            The deliveryArtifact value
        
        Note:
            Delegates to delivery_artifact property (CODING_RULE_V2_00017)
        """
        return self.delivery_artifact  # Delegates to property

    def getInvocation(self) -> "BuildActionInvocator":
        """
        AUTOSAR-compliant getter for invocation.
        
        Returns:
            The invocation value
        
        Note:
            Delegates to invocation property (CODING_RULE_V2_00017)
        """
        return self.invocation  # Delegates to property

    def setInvocation(self, value: "BuildActionInvocator") -> "BuildActionEntity":
        """
        AUTOSAR-compliant setter for invocation with method chaining.
        
        Args:
            value: The invocation to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to invocation property setter (gets validation automatically)
        """
        self.invocation = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_invocation(self, value: Optional["BuildActionInvocator"]) -> "BuildActionEntity":
        """
        Set invocation and return self for chaining.
        
        Args:
            value: The invocation to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_invocation("value")
        """
        self.invocation = value  # Use property setter (gets validation)
        return self



class BuildActionInvocator(ARObject):
    """
    that it is optional due to the fact that some actions are hardwired in the
    environment and do not need an explicit command. On the other hand the
    properties of an invocator can be complex and not standardized. sdg Sdg *
    aggr This represents a general data structure intended to denote parameters
    for the BuildAction. Table 10.6: BuildActionInvocator
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildActionInvocator
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 372, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the command to invocate the processor.
        self._command: Optional["VerbatimString"] = None

    @property
    def command(self) -> Optional["VerbatimString"]:
        """Get command (Pythonic accessor)."""
        return self._command

    @command.setter
    def command(self, value: Optional["VerbatimString"]) -> None:
        """
        Set command with validation.
        
        Args:
            value: The command to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._command = None
            return

        if not isinstance(value, VerbatimString):
            raise TypeError(
                f"command must be VerbatimString or None, got {type(value).__name__}"
            )
        self._command = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCommand(self) -> "VerbatimString":
        """
        AUTOSAR-compliant getter for command.
        
        Returns:
            The command value
        
        Note:
            Delegates to command property (CODING_RULE_V2_00017)
        """
        return self.command  # Delegates to property

    def setCommand(self, value: "VerbatimString") -> "BuildActionInvocator":
        """
        AUTOSAR-compliant setter for command with method chaining.
        
        Args:
            value: The command to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to command property setter (gets validation automatically)
        """
        self.command = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_command(self, value: Optional["VerbatimString"]) -> "BuildActionInvocator":
        """
        Set command and return self for chaining.
        
        Args:
            value: The command to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_command("value")
        """
        self.command = value  # Use property setter (gets validation)
        return self



class BuildEngineeringObject(EngineeringObject):
    """
    that instanceRefs are not supported, since there was no use case. It could
    be supported using a FlatMap.(cid:99)() • [TPS_GST_00237] engineeringObject
    (cid:100)This indicates an engineering ob- ject. The specified permissions
    apply to all objects in the partial model which is stored in the denoted
    AutosarEngineeringObject.(cid:99)() 379 of 535 Document ID 202:
    AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR
    FO R23-11 ARElement +derivedFromBlueprint Identifiable AtpBlueprintable
    «atpUriDef» 0..* AtpBlueprint AclObjectSet + aclObjectClass:
    ReferrableSubtypesEnum [0..*] + aclScope: AclScopeEnum ARElement +collection
    Collection 0..1 + autoCollect: AutoCollectEnum [0..1] + collectionSemantics:
    NameToken [0..1] + elementRole: Identifier [0..1] EngineeringObject
    +engineeringObject AutosarEngineeringObject 0..* Referrable +object
    «atpIdentityContributor» 0..* + shortName: Identifier AtpDefinition
    +objectDefinition «atpUriDef» 0..* ARElement ARElement HwCategory
    PostBuildVariantCriterion Identifiable ARElement EcucDefinitionElement
    SwSystemconst + scope: EcucScopeEnum [0..1] «atpVariation» +
    lowerMultiplicity: PositiveInteger [0..1] + upperMultiplicity:
    PositiveInteger [0..1] + upperMultiplicityInfinite: Boolean [0..1] Figure
    11.2: Roles and Rights Object Set Listing 11.1 illustrates how the roles and
    rights approach can be applied to control the access on objects in an
    AUTOSAR description. It defines • a set of permissions named "Integrator"
    representing the Relation in [TPS_GST_00226] based on the definitions below
    • a role named "ECU_Integrator" • an object set named
    "MemoryStackConfiguration" • two operations <AR-PACKAGE>
    <SHORT-NAME>GenericStructureTemplate</SHORT-NAME> 380 of 535 Document ID
    202: AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template
    AUTOSAR FO R23-11 <CATEGORY>EXAMPLE</CATEGORY> <AR-PACKAGES> <AR-PACKAGE>
    <SHORT-NAME>AclPermissions</SHORT-NAME> <ELEMENTS> <ACL-PERMISSION>
    <SHORT-NAME>Integrator</SHORT-NAME> <ACL-OBJECT-REFS> <ACL-OBJECT-REF
    DEST="ACL-OBJECT-SET">/AUTOSAR/ GenericStructureTemplate/AccessObjectSets/
    MemoryStackConfiguration</ACL-OBJECT-REF> </ACL-OBJECT-REFS>
    <ACL-OPERATION-REFS> <ACL-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/
    GenericStructureTemplate/AclOperations/AssignValue</ACL- OPERATION-REF>
    <ACL-OPERATION-REF DEST="ACL-OPERATION">/AUTOSAR/
    GenericStructureTemplate/AclOperations/ReassignValue</ACL- OPERATION-REF>
    </ACL-OPERATION-REFS> <ACL-ROLE-REFS> <ACL-ROLE-REF
    DEST="ACL-ROLE">/AUTOSAR/
    GenericStructureTemplate/AclRoles/ECU_Integrator</ACL-ROLE- REF>
    </ACL-ROLE-REFS> </ACL-PERMISSION> </ELEMENTS> </AR-PACKAGE> <AR-PACKAGE>
    <SHORT-NAME>AccessObjectSets</SHORT-NAME> <ELEMENTS> <ACL-OBJECT-SET>
    <SHORT-NAME>MemoryStackConfiguration</SHORT-NAME>
    <ACL-SCOPE>DESCENDANT</ACL-SCOPE> <OBJECT-DEFINITION-REFS>
    <OBJECT-DEFINITION-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/
    EcucDefs/MemIf</OBJECT-DEFINITION-REF> <OBJECT-DEFINITION-REF
    DEST="ECUC-MODULE-DEF">/AUTOSAR/ EcucDefs/MemMap</OBJECT-DEFINITION-REF>
    <OBJECT-DEFINITION-REF DEST="ECUC-MODULE-DEF">/AUTOSAR/
    EcucDefs/NvM</OBJECT-DEFINITION-REF> </OBJECT-DEFINITION-REFS>
    </ACL-OBJECT-SET> </ELEMENTS> </AR-PACKAGE> <AR-PACKAGE>
    <SHORT-NAME>AclOperations</SHORT-NAME> <REFERENCE-BASES> <REFERENCE-BASE>
    <SHORT-LABEL>op</SHORT-LABEL>
    <BASE-IS-THIS-PACKAGE>true</BASE-IS-THIS-PACKAGE> </REFERENCE-BASE>
    </REFERENCE-BASES> <ELEMENTS> <ACL-OPERATION>
    <SHORT-NAME>AssignValue</SHORT-NAME> 381 of 535 Document ID 202:
    AUTOSAR_FO_TPS_GenericStructureTemplate Generic Structure Template AUTOSAR
    FO R23-11 </ACL-OPERATION> <ACL-OPERATION>
    <SHORT-NAME>ReassignValue</SHORT-NAME> <IMPLIED-OPERATION-REFS>
    <IMPLIED-OPERATION-REF DEST="ACL-OPERATION" BASE="op">
    AssignValue</IMPLIED-OPERATION-REF> </IMPLIED-OPERATION-REFS>
    </ACL-OPERATION> </ELEMENTS> </AR-PACKAGE> <AR-PACKAGE>
    <SHORT-NAME>AclRoles</SHORT-NAME> <ELEMENTS> <ACL-ROLE>
    <SHORT-NAME>ECU_Integrator</SHORT-NAME> <LONG-NAME> <L-4 L="EN">See <TT>ECU
    Integrator</TT></L-4> </LONG-NAME> </ACL-ROLE> </ELEMENTS> </AR-PACKAGE>
    </AR-PACKAGES> </AR-PACKAGE> Listing 11.1: Example for Access Control
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildEngineeringObject
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 372, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This attribute indicates the file type which shall used for object.
        # Note that an engineering object multiple representations of the same
                # artifact.
        # can select one of the provided.
        self._fileType: "NameToken" = None

    @property
    def file_type(self) -> "NameToken":
        """Get fileType (Pythonic accessor)."""
        return self._fileType

    @file_type.setter
    def file_type(self, value: "NameToken") -> None:
        """
        Set fileType with validation.
        
        Args:
            value: The fileType to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"fileType must be NameToken or str, got {type(value).__name__}"
            )
        self._fileType = value
        # This attribute allows to define a set of engineering objects based search
        # applied to the filetype of the objects.
        self._fileTypePattern: "RegularExpression" = None

    @property
    def file_type_pattern(self) -> "RegularExpression":
        """Get fileTypePattern (Pythonic accessor)."""
        return self._fileTypePattern

    @file_type_pattern.setter
    def file_type_pattern(self, value: "RegularExpression") -> None:
        """
        Set fileTypePattern with validation.
        
        Args:
            value: The fileTypePattern to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, RegularExpression):
            raise TypeError(
                f"fileTypePattern must be RegularExpression, got {type(value).__name__}"
            )
        self._fileTypePattern = value
        # This attribute represents the name of the file if it is newly.
        # Note that engineering object resolves ShortLabel indicate mainly to refer to
                # an If the file is created newly, the filename can determined by built in
                # policy or predefined here.
        self._intended: Optional["UriString"] = None

    @property
    def intended(self) -> Optional["UriString"]:
        """Get intended (Pythonic accessor)."""
        return self._intended

    @intended.setter
    def intended(self, value: Optional["UriString"]) -> None:
        """
        Set intended with validation.
        
        Args:
            value: The intended to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._intended = None
            return

        if not isinstance(value, UriString):
            raise TypeError(
                f"intended must be UriString or None, got {type(value).__name__}"
            )
        self._intended = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getFileType(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for fileType.
        
        Returns:
            The fileType value
        
        Note:
            Delegates to file_type property (CODING_RULE_V2_00017)
        """
        return self.file_type  # Delegates to property

    def setFileType(self, value: "NameToken") -> "BuildEngineeringObject":
        """
        AUTOSAR-compliant setter for fileType with method chaining.
        
        Args:
            value: The fileType to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to file_type property setter (gets validation automatically)
        """
        self.file_type = value  # Delegates to property setter
        return self

    def getFileTypePattern(self) -> "RegularExpression":
        """
        AUTOSAR-compliant getter for fileTypePattern.
        
        Returns:
            The fileTypePattern value
        
        Note:
            Delegates to file_type_pattern property (CODING_RULE_V2_00017)
        """
        return self.file_type_pattern  # Delegates to property

    def setFileTypePattern(self, value: "RegularExpression") -> "BuildEngineeringObject":
        """
        AUTOSAR-compliant setter for fileTypePattern with method chaining.
        
        Args:
            value: The fileTypePattern to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to file_type_pattern property setter (gets validation automatically)
        """
        self.file_type_pattern = value  # Delegates to property setter
        return self

    def getIntended(self) -> "UriString":
        """
        AUTOSAR-compliant getter for intended.
        
        Returns:
            The intended value
        
        Note:
            Delegates to intended property (CODING_RULE_V2_00017)
        """
        return self.intended  # Delegates to property

    def setIntended(self, value: "UriString") -> "BuildEngineeringObject":
        """
        AUTOSAR-compliant setter for intended with method chaining.
        
        Args:
            value: The intended to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to intended property setter (gets validation automatically)
        """
        self.intended = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_file_type(self, value: "NameToken") -> "BuildEngineeringObject":
        """
        Set fileType and return self for chaining.
        
        Args:
            value: The fileType to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_file_type("value")
        """
        self.file_type = value  # Use property setter (gets validation)
        return self

    def with_file_type_pattern(self, value: "RegularExpression") -> "BuildEngineeringObject":
        """
        Set fileTypePattern and return self for chaining.
        
        Args:
            value: The fileTypePattern to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_file_type_pattern("value")
        """
        self.file_type_pattern = value  # Use property setter (gets validation)
        return self

    def with_intended(self, value: Optional["UriString"]) -> "BuildEngineeringObject":
        """
        Set intended and return self for chaining.
        
        Args:
            value: The intended to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_intended("value")
        """
        self.intended = value  # Use property setter (gets validation)
        return self



class GenericModelReference(ARObject):
    """
    This meta-class represents the ability to express a late binding reference
    to a model element. The model element can be from every model. Even if it is
    modeled according to the association representation, it is not limited to
    refer to AUTOSAR model elements.
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::GenericModelReference
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 449, Foundation
      R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This establishes the reference base.
        self._base: "NameToken" = None

    @property
    def base(self) -> "NameToken":
        """Get base (Pythonic accessor)."""
        return self._base

    @base.setter
    def base(self, value: "NameToken") -> None:
        """
        Set base with validation.
        
        Args:
            value: The base to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"base must be NameToken or str, got {type(value).__name__}"
            )
        self._base = value
        # This attribute represents the class of the referenced It is a String, since
                # the model element in any model.
        # Therefore we cannot have any.
        self._dest: "NameToken" = None

    @property
    def dest(self) -> "NameToken":
        """Get dest (Pythonic accessor)."""
        return self._dest

    @dest.setter
    def dest(self, value: "NameToken") -> None:
        """
        Set dest with validation.
        
        Args:
            value: The dest to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, (NameToken, str)):
            raise TypeError(
                f"dest must be NameToken or str, got {type(value).__name__}"
            )
        self._dest = value
        # This is the full qualified name of the model element.
        self._ref: "RefType" = None

    @property
    def ref(self) -> "RefType":
        """Get ref (Pythonic accessor)."""
        return self._ref

    @ref.setter
    def ref(self, value: "RefType") -> None:
        """
        Set ref with validation.
        
        Args:
            value: The ref to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        self._ref = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getBase(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for base.
        
        Returns:
            The base value
        
        Note:
            Delegates to base property (CODING_RULE_V2_00017)
        """
        return self.base  # Delegates to property

    def setBase(self, value: "NameToken") -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for base with method chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to base property setter (gets validation automatically)
        """
        self.base = value  # Delegates to property setter
        return self

    def getDest(self) -> "NameToken":
        """
        AUTOSAR-compliant getter for dest.
        
        Returns:
            The dest value
        
        Note:
            Delegates to dest property (CODING_RULE_V2_00017)
        """
        return self.dest  # Delegates to property

    def setDest(self, value: "NameToken") -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for dest with method chaining.
        
        Args:
            value: The dest to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to dest property setter (gets validation automatically)
        """
        self.dest = value  # Delegates to property setter
        return self

    def getRef(self) -> "RefType":
        """
        AUTOSAR-compliant getter for ref.
        
        Returns:
            The ref value
        
        Note:
            Delegates to ref property (CODING_RULE_V2_00017)
        """
        return self.ref  # Delegates to property

    def setRef(self, value: "RefType") -> "GenericModelReference":
        """
        AUTOSAR-compliant setter for ref with method chaining.
        
        Args:
            value: The ref to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to ref property setter (gets validation automatically)
        """
        self.ref = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_base(self, value: "NameToken") -> "GenericModelReference":
        """
        Set base and return self for chaining.
        
        Args:
            value: The base to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_base("value")
        """
        self.base = value  # Use property setter (gets validation)
        return self

    def with_dest(self, value: "NameToken") -> "GenericModelReference":
        """
        Set dest and return self for chaining.
        
        Args:
            value: The dest to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_dest("value")
        """
        self.dest = value  # Use property setter (gets validation)
        return self

    def with_ref(self, value: RefType) -> "GenericModelReference":
        """
        Set ref and return self for chaining.
        
        Args:
            value: The ref to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_ref("value")
        """
        self.ref = value  # Use property setter (gets validation)
        return self



class BuildAction(BuildActionEntity):
    """
    This meta-class represents the ability to specify a build action.
    
    Package: M2::AUTOSARTemplates::GenericStructure::BuildActionManifest::BuildAction
    
    Sources:
      - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (Page 366, Foundation
      R23-11)
      - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (Page 172, Foundation R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # This represents the artifacts which are created by the.
        self._createdData: List["BuildActionIoElement"] = []

    @property
    def created_data(self) -> List["BuildActionIoElement"]:
        """Get createdData (Pythonic accessor)."""
        return self._createdData
        # This association specifies a set of follow up actions.
        self._followUpAction: List["BuildAction"] = []

    @property
    def follow_up_action(self) -> List["BuildAction"]:
        """Get followUpAction (Pythonic accessor)."""
        return self._followUpAction
        # This represents the artifacts which are read by the.
        self._inputData: List["BuildActionIoElement"] = []

    @property
    def input_data(self) -> List["BuildActionIoElement"]:
        """Get inputData (Pythonic accessor)."""
        return self._inputData
        # This denotes the data which are modified by the action.
        self._modifiedData: List["BuildActionIoElement"] = []

    @property
    def modified_data(self) -> List["BuildActionIoElement"]:
        """Get modifiedData (Pythonic accessor)."""
        return self._modifiedData
        # This association specifies a set of predecessors.
        # These shall be finished before but necessarily the given action.
        # need to be performed in the specified.
        self._predecessor: List["BuildAction"] = []

    @property
    def predecessor(self) -> List["BuildAction"]:
        """Get predecessor (Pythonic accessor)."""
        return self._predecessor
        # This represents the environment which is required to use specified Processor.
        self._required: "BuildActionEnvironment" = None

    @property
    def required(self) -> "BuildActionEnvironment":
        """Get required (Pythonic accessor)."""
        return self._required

    @required.setter
    def required(self, value: "BuildActionEnvironment") -> None:
        """
        Set required with validation.
        
        Args:
            value: The required to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if not isinstance(value, BuildActionEnvironment):
            raise TypeError(
                f"required must be BuildActionEnvironment, got {type(value).__name__}"
            )
        self._required = value

    # ===== AUTOSAR-compatible methods (delegate to properties) =====

    def getCreatedData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for createdData.
        
        Returns:
            The createdData value
        
        Note:
            Delegates to created_data property (CODING_RULE_V2_00017)
        """
        return self.created_data  # Delegates to property

    def getFollowUpAction(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for followUpAction.
        
        Returns:
            The followUpAction value
        
        Note:
            Delegates to follow_up_action property (CODING_RULE_V2_00017)
        """
        return self.follow_up_action  # Delegates to property

    def getInputData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for inputData.
        
        Returns:
            The inputData value
        
        Note:
            Delegates to input_data property (CODING_RULE_V2_00017)
        """
        return self.input_data  # Delegates to property

    def getModifiedData(self) -> List["BuildActionIoElement"]:
        """
        AUTOSAR-compliant getter for modifiedData.
        
        Returns:
            The modifiedData value
        
        Note:
            Delegates to modified_data property (CODING_RULE_V2_00017)
        """
        return self.modified_data  # Delegates to property

    def getPredecessor(self) -> List["BuildAction"]:
        """
        AUTOSAR-compliant getter for predecessor.
        
        Returns:
            The predecessor value
        
        Note:
            Delegates to predecessor property (CODING_RULE_V2_00017)
        """
        return self.predecessor  # Delegates to property

    def getRequired(self) -> "BuildActionEnvironment":
        """
        AUTOSAR-compliant getter for required.
        
        Returns:
            The required value
        
        Note:
            Delegates to required property (CODING_RULE_V2_00017)
        """
        return self.required  # Delegates to property

    def setRequired(self, value: "BuildActionEnvironment") -> "BuildAction":
        """
        AUTOSAR-compliant setter for required with method chaining.
        
        Args:
            value: The required to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to required property setter (gets validation automatically)
        """
        self.required = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_required(self, value: "BuildActionEnvironment") -> "BuildAction":
        """
        Set required and return self for chaining.
        
        Args:
            value: The required to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_required("value")
        """
        self.required = value  # Use property setter (gets validation)
        return self
