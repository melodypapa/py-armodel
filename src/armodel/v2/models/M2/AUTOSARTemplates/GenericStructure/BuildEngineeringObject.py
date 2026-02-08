from typing import Optional
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import EngineeringObject


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
        if not isinstance(value, NameToken):
            raise TypeError(
                f"fileType must be NameToken, got {type(value).__name__}"
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
