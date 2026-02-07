from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from armodel.v2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class EndToEndDescription(ARObject):
    """
    that if the receiver does not receive new Data at a consecutive read, then
    the receiver increments the tolerance by 1. maxNoNewOr PositiveInteger 0..1
    attr The maximum amount of missing or repeated Data which RepeatedData the
    receiver does not expect to exceed under normal communication conditions.
    syncCounterInit PositiveInteger 0..1 attr Number of Data required for
    validating the consistency of the counter that shall be received with a
    valid counter (i.e. counter within the allowed lock-in range) after the
    detection of an unexpected behavior of a received counter. Table 4.95:
    EndToEndDescription 206 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 [constr_1901] Existence of attribute EndToEndDescription.category
    (cid:100)For each EndToEndDescription, attribute category shall exist at the
    time when the contract phase generation is executed.(cid:99)()
    [TPS_SWCT_01090] EndToEndProtection (cid:100)EndToEndProtection is the Iden-
    tifiable class that owns specific elements for referencing the
    to-be-protected data elements and signals •
    EndToEndProtectionVariablePrototype: a specific dataElement owned by a
    specific PortPrototype • EndToEndProtectionISignalIPdu: a specific
    ISignalGroup in the con- text of an ISignalIPdu. For more details please
    refer to [10] (cid:99)(RS_SWCT_03240) [TPS_SWCT_01091] Two cases for
    end-to-end protection (cid:100)In order to protect a VariableDataPrototype
    the EndToEndProtectionVariablePrototype shall be defined. If communication
    is defined between ECUs using AUTOSAR COM the End-
    ToEndProtectionISignalIPdu shall be defined as well.(cid:99)(RS_SWCT_03240)
    The following features apply: • [constr_1000] End-to-end protection is
    limited to sender/receiver commu- nication (cid:100)A VariableDataPrototype
    referenced in the roles – EndToEndProtectionVariablePrototype.sender –
    EndToEndProtectionVariablePrototype.receiver shall be aggregated in the role
    dataElement at a SenderReceiverInter- face at the time when the contract
    phase generation is exe- cuted.(cid:99)() • The value of the dataId is
    assigned by a central authority rather than by the developer of the
    software-component. • The information about the dataId shall be available at
    both the sender and the receiver(s). • [TPS_SWCT_01508] Scope of end-to-end
    protection (cid:100)End-to-end protection applies to local (i.e. within the
    ECU) as well as remote (i.e. ECU to ECU) commu-
    nication.(cid:99)(RS_SWCT_03240) [TPS_SWCT_01092] EndToEndProtectionSet
    (cid:100)The meta-class EndToEndPro- tectionSet provides a container for
    EndToEndProtection. The aggregation is stereotyped
    (cid:28)atpSplitable(cid:29) because the information about end-to-end
    protection is added at a later step in the development
    workflow.(cid:99)(RS_SWCT_03240) It also has the stereotype
    (cid:28)atpVariation(cid:29) because this allows for implementing the
    software-component in two variants, one that uses end-to-end protection and
    one that does not use it. It also might happen that the communication ends
    themselves are variant. 207 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 EndToEndProtection maintains InstanceRefs to one dataElement in
    the role of sender and to one or many dataElements in the role of receiver.
    By this means it is possible to support a 1:n communication scenario.
    EndToEndDescription + category: NameToken [0..1] ARElement Identifiable +
    counterOffset: PositiveInteger [0..1] EndToEndProtectionSet
    EndToEndProtection + + c d r a c t O aI f d fs : e P t: o P si o ti s v it e
    iv In e t I e n g te e g r e [0 r . [ . 0 * . ] . 1 {o ] rdered} +
    dataIdMode: PositiveInteger [0..1] + dataIdNibbleOffset: PositiveInteger
    [0..1] + dataLength: PositiveInteger [0..1] + maxDeltaCounterInit:
    PositiveInteger [0..1] + maxNoNewOrRepeatedData: PositiveInteger [0..1] +
    syncCounterInit: PositiveInteger [0..1] (cid:1) (cid:16) (cid:4) (cid:2)
    (cid:17) (cid:6) (cid:3) (cid:18) (cid:20) (cid:4) (cid:2) (cid:19) (cid:25)
    (cid:5) (cid:3) (cid:8) (cid:20) (cid:2) (cid:23) (cid:14) (cid:6) (cid:7)
    (cid:3) (cid:2) (cid:21) (cid:4) (cid:3) (cid:7) (cid:7) (cid:7) (cid:9)
    (cid:19) (cid:8) (cid:20) (cid:9) (cid:22) (cid:12) (cid:7) (cid:7) (cid:10)
    (cid:9) (cid:23) (cid:13) (cid:12) (cid:20) (cid:2) (cid:12) (cid:13)
    (cid:7) (cid:23) (cid:14) (cid:15) (cid:20) (cid:24) +endToEndProfile
    +endToEndProtection «atpVariation,atpSplitable» 0..* «atpSplitable» 0..1
    «atpVariation,atpSplitable» 0..* +endToEndProtectionVariablePrototype
    +receiver AtpInstanceRef EndToEndProtectionVariablePrototype
    VariableDataPrototypeInSystemInstanceRef 0..* «atpIdentityContributor»
    +sender + shortLabel: Identifier [0..1] 0..1 0..1 +targetDataPrototype
    {redefines atpTarget} +receiver AutosarDataPrototype «instanceRef» 0..*
    VariableDataPrototype +sender «instanceRef»0..1 Figure 4.51: Details of the
    modeling of end-to-end protection [TPS_SWCT_01093] Aggregation
    EndToEndProtection.endToEndProfile is splitable (cid:100)EndToEndProtection
    aggregates EndToEndDescription using stereotype
    (cid:28)atpSplitable(cid:29). By this means it is for the integrator of an
    ECU possible to generally specify the nature of a specific end-to-end
    protection but leave the actual assignment of values (e.g. for dataId) to a
    later process step.(cid:99)(RS_SWCT_03240) According to [19] the following
    constraints apply on the attributes of EndToEndPro- tection (note that
    additional M1 constraints apply as described in [19]): [TPS_SWCT_01094]
    Standardized values of attribute EndToEndDescription category (cid:100)The
    following values for the category of EndToEndDescription are standardized
    and reserved for being used in the way the AUTOSAR standard foresees: • NONE
    • PROFILE_01 • PROFILE_02 In addition, it is positively possible to use
    other than the standardized values for the category if it is ensured that
    the proprietary values do not clash with an extension of the standardized
    values, e.g. by using a company-specific prefix.(cid:99)(RS_SWCT_03240) The
    semantics of the standardized values of attribute EndToEndDescription.cat-
    egory is explained below: NONE This value indicates that the E2E framework
    shall be enabled for the given sender/receiver respectively the given
    iSignalIPdu. The wrapper code 208 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 shall be generated but it shall not invoke E2E library protection
    routines. E2E wrapper works as pass-through. This may be used when a profile
    selection or profile options are not yet selected in a given system but it
    is required that the system can be built successfully under consideration of
    the E2E library. This would also be applicable for migrating from/to a
    system with/without E2E protection. [TPS_SWCT_01095] category set to NONE
    (cid:100)If attributes exist in the presence of the category being set to
    NONE, the attributes shall be ignored.(cid:99)(RS_SWCT_- 03240) PROFILE_01
    This value indicates that the settings of E2E profile 1 (that uses a SAE
    CRC8, implicit 16-bit data ID, and a 4 bit alive counter) apply.
    [constr_1113] Existence of attributes in PROFILE_01 (cid:100)In PROFILE_01,
    the following attributes shall exist: • dataLength • dataId at the time when
    the contract phase generation is exe- cuted.(cid:99)() Please note that the
    attribute maxDeltaCounterInit is also part of PRO- FILE_01 but it does not
    necessarily have to exist provided that ReceiverCom-
    Spec.maxDeltaCounterInit exists. [TPS_SWCT_01850] Usage of attribute
    RPortPrototype.requiredCom- Spec.maxDeltaCounterInit vs.
    EndToEndProtection.endToEndPro- file.maxDeltaCounterInit (cid:100)If • the
    value of reference EndToEndProtection.endToEndProtection-
    VariablePrototype.receiver is identical to the value of the reference
    RPortPrototype.requiredComSpec.dataElement and • attribute
    RPortPrototype.requiredComSpec.maxDeltaCounterInit exists, then the value of
    attribute RPortPrototype.requiredComSpec.maxDelta- CounterInit shall be
    preferred over the value of attribute EndToEndPro-
    tection.endToEndProfile.maxDeltaCounterInit.(cid:99)(RS_SWCT_03240)
    [constr_1170] Existence of attribute EndToEndDescription.maxDelta-
    CounterInit for PROFILE_01 (cid:100)If the value of attribute
    EndToEndDescrip- tion.category is set to PROFILE_01 and either • the
    condition described in [TPS_SWCT_01850] concerning the referenced
    VariableDataPrototype is not fulfilled or • attribute
    RPortPrototype.requiredComSpec.maxDeltaCounterInit does not exist, 209 of
    1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software
    Component Template AUTOSAR CP R23-11 then attribute
    EndToEndProtection.endToEndProfile.maxDeltaCoun- terInit shall exist at the
    time when the contract phase genera- tion is executed.(cid:99)()
    [constr_1111] Constraints of dataId in PROFILE_01 (cid:100)In PROFILE_01,
    there shall be only one element in the set and the applicable range of
    values is [0 .. 65535]. This rule shall be imposed at the time when the
    contract phase generation is executed.(cid:99)() [constr_1112] Constraints
    of dataIdMode in PROFILE_01 (cid:100)In PROFILE_01, the applicable range of
    values for dataIdMode is [0 .. 3]. This rule shall be imposed at the time
    when the contract phase generation is executed.(cid:99)() [constr_1114]
    Constraints of crcOffset in PROFILE_01 (cid:100)In PROFILE_01, the
    applicable range of values for crcOffset is [0 .. 65535]. For the value of
    this attribute the constraint value mod 4 = 0 applies. This rule shall be
    imposed at the time when the contract phase generation is
    executed.(cid:99)() [constr_1115] Constraints of counterOffset in PROFILE_01
    (cid:100)In PRO- FILE_01, the applicable range of values for counterOffset
    is [0 .. 65535]. For the value of this attribute the constraint value mod 4
    = 0 applies. This rule shall be imposed at the time when the contract phase
    generation is executed.(cid:99)() [constr_1116] Constraints of dataLength in
    PROFILE_01 (cid:100)In PROFILE_01, the applicable range of values for
    dataLength is [0 .. 240]. For the value of this attribute the constraint
    value mod 8 = 0 applies. This rule shall be imposed at the time when the
    contract phase generation is executed.(cid:99)() [constr_1117] Constraints
    of maxDeltaCounterInit in PROFILE_01 (cid:100)In PROFILE_01, the applicable
    range of values for EndToEndDescription. maxDeltaCounterInit and
    ReceiverComSpec.maxDeltaCounterInit is [0 .. 14]. This rule shall be imposed
    at the time when the contract phase generation is executed.(cid:99)()
    [constr_1211] Constraints of maxNoNewOrRepeatedData in PROFILE_- 01
    (cid:100)In PROFILE_01, the applicable range of values for EndToEndDescrip-
    tion.maxNoNewOrRepeatedData and ReceiverComSpec.maxNoNewOrRe- peatedData is
    [0 .. 14]. 210 of 1228 Document ID 62:
    AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component Template AUTOSAR
    CP R23-11 This rule shall be imposed at the time when the contract phase
    generation is executed.(cid:99)() [constr_1212] Constraints of
    syncCounterInit in PROFILE_01 (cid:100)In PRO- FILE_01, the applicable range
    of values for EndToEndDescription.sync- CounterInit and
    ReceiverComSpec.syncCounterInit is [0 .. 14]. This rule shall be imposed at
    the time when the contract phase generation is executed.(cid:99)()
    [TPS_SWCT_01851] Usage of attribute RPortPrototype.requiredCom-
    Spec.maxNoNewOrRepeatedData vs. EndToEndProtection.endToEnd-
    Profile.maxNoNewOrRepeatedData (cid:100)If • the value of reference
    EndToEndProtection.endToEndProtection- VariablePrototype.receiver is
    identical to the value of the reference
    RPortPrototype.requiredComSpec.dataElement and • attribute
    RPortPrototype.requiredComSpec.maxNoNewOrRepeated- Data exists, then the
    value of RPortPrototype.requiredComSpec.maxNoNewOrRe- peatedData shall be
    preferred over the value of EndToEndProtection.
    endToEndProfile.maxNoNewOrRepeatedData.(cid:99)(RS_SWCT_03240) [constr_1215]
    Existence of attribute EndToEndDescription.maxNoNewOr- RepeatedData for
    PROFILE_01 (cid:100)If the value of attribute EndToEndDescrip- tion.category
    is set to PROFILE_01 and either • the condition described in
    [TPS_SWCT_01851] concerning the referenced VariableDataPrototype is not
    fulfilled or • attribute RPortPrototype.requiredComSpec.maxNoNewOrRepeated-
    Data does not exist, then attribute
    EndToEndProtection.endToEndProfile.maxNoNewOrRe- peatedData shall exist at
    the time when the contract phase gen- eration is executed.(cid:99)()
    [TPS_SWCT_01852] Usage of attribute RPortPrototype.requiredCom-
    Spec.syncCounterInit vs. attribute EndToEndProtection.endToEnd-
    Profile.syncCounterInit (cid:100)If • the value of reference
    EndToEndProtection.endToEndProtection- VariablePrototype.receiver is
    identical to the value of the reference
    RPortPrototype.requiredComSpec.dataElement and • attribute
    RPortPrototype.requiredComSpec.syncCounterInit ex- ists, 211 of 1228
    Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component
    Template AUTOSAR CP R23-11 then the value of
    RPortPrototype.requiredComSpec.syncCounterInit shall be preferred over the
    value of EndToEndProtection.endToEndPro-
    file.syncCounterInit.(cid:99)(RS_SWCT_03240) [constr_1216] Existence of
    attribute EndToEndDescription.syncCoun- terInit for PROFILE_01 (cid:100)If
    the value of attribute EndToEndDescription. category is set to PROFILE_01
    and either • the condition described in [TPS_SWCT_01852] concerning the
    referenced VariableDataPrototype is not fulfilled or • attribute
    RPortPrototype.requiredComSpec.syncCounterInit does not exist, then the
    attribute EndToEndProtection.endToEndProfile.syncCoun- terInit shall exist
    at the time when the contract phase genera- tion is executed.(cid:99)()
    [constr_1261] Applicability for EndToEndDescription.dataIdNibble- Offset
    (cid:100)EndToEndDescription.dataIdNibbleOffset shall be used only if
    EndToEndDescription.dataIdMode is set to the value 3 and at the same time
    EndToEndDescription.category is set to PROFILE_01. This rule shall be
    imposed at the time when the contract phase generation is
    executed.(cid:99)() [TPS_SWCT_01529] Default value for
    EndToEndDescription.dataIdNib- bleOffset (cid:100)If
    EndToEndDescription.dataIdMode is set to the value 3 and at the same time
    EndToEndDescription.category is set to the value PRO- FILE_01 and
    EndToEndDescription.dataIdNibbleOffset is not speci- fied, then the default
    value of 12 (bits) shall be assumed for the attribute End-
    ToEndDescription.dataIdNibbleOffset.(cid:99)(RS_SWCT_03240) PROFILE_02 This
    value indicates that the settings of E2E profile 2 apply. [constr_1118]
    Existence of attributes in PROFILE_02 (cid:100)In PROFILE_02, only the
    following attributes shall exist: • dataLength • dataId at the time when the
    contract phase generation is executed(cid:99) () Please note that the
    attribute maxDeltaCounterInit is also part of PRO- FILE_01 but it does not
    necessarily have to exist provided that ReceiverCom-
    Spec.maxDeltaCounterInit exists. [constr_1171] Existence of attribute
    EndToEndDescription.maxDelta- CounterInit for PROFILE_02 (cid:100)If the
    value of EndToEndDescription.cat- egory is set to PROFILE_02 and either 212
    of 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software
    Component Template AUTOSAR CP R23-11 • the condition described in
    [TPS_SWCT_01850] concerning the referenced VariableDataPrototype is not
    fulfilled or • attribute RPortPrototype.requiredComSpec.maxDeltaCounterInit
    does not exist, then attribute
    EndToEndProtection.endToEndProfile.maxDeltaCoun- terInit shall exist at the
    time when the contract phase genera- tion is executed.(cid:99)()
    [constr_1119] Constraints of dataLength in PROFILE_02 (cid:100)In
    PROFILE_02, the applicable range of values for dataLength is [0 .. 65535].
    For the value of this attribute the constraint value mod 8 = 0 applies. This
    rule shall be imposed at the time when the contract phase generation is
    executed.(cid:99)() [constr_1120] Constraints of dataId in PROFILE_02
    (cid:100)In PROFILE_02, there shall be exactly ordered 16 elements in the
    set and the applicable range of values is [0 .. 255]. This rule shall be
    imposed at the time when the contract phase generation is
    executed.(cid:99)() [constr_1121] Constraints of maxDeltaCounterInit in
    PROFILE_02 (cid:100)In PROFILE_02, the applicable range of values for
    EndToEndDescription. maxDeltaCounterInit and
    ReceiverComSpec.maxDeltaCounterInit is [0 .. 15]. This rule shall be imposed
    at the time when the contract phase generation is executed.(cid:99)()
    [constr_1213] Constraints of maxNoNewOrRepeatedData in PROFILE_- 02
    (cid:100)In PROFILE_02, the applicable range of values for EndToEndDescrip-
    tion.maxNoNewOrRepeatedData and ReceiverComSpec.maxNoNewOrRe- peatedData is
    [0 .. 15]. This rule shall be imposed at the time when the contract phase
    generation is executed.(cid:99)() [constr_1214] Constraints of
    syncCounterInit in PROFILE_02 (cid:100)In PRO- FILE_02, the applicable range
    of values for EndToEndDescription.sync- CounterInit and
    ReceiverComSpec.syncCounterInit is [0 .. 15]. This rule shall be imposed at
    the time when the contract phase generation is executed.(cid:99)()
    [constr_1217] Existence of attribute EndToEndDescription.maxNoNewOr-
    RepeatedData for PROFILE_02 (cid:100)If the value of attribute
    EndToEndDescrip- tion.category is set to PROFILE_02 and either 213 of 1228
    Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Software Component
    Template AUTOSAR CP R23-11 • the condition described in [TPS_SWCT_01851]
    concerning the referenced VariableDataPrototype is not fulfilled or •
    attribute RPortPrototype.requiredComSpec.maxNoNewOrRepeated- Data does not
    exist, then attribute EndToEndProtection.endToEndProfile.maxNoNewOrRe-
    peatedData shall exist at the time when the contract phase gen- eration is
    executed.(cid:99)() [constr_1218] Existence of attribute
    EndToEndDescription.syncCoun- terInit for PROFILE_02 (cid:100)If the value
    of attribute EndToEndDescription. category is set to PROFILE_01 and either •
    the condition described in [TPS_SWCT_01852] concerning the referenced
    VariableDataPrototype is not fulfilled or • attribute
    RPortPrototype.requiredComSpec.syncCounterInit does not exist, then the
    attribute EndToEndProtection.endToEndProfile.syncCoun- terInit shall exist
    at the time when the contract phase genera- tion is executed.(cid:99)()
    
    Package: M2::AUTOSARTemplates::SWComponentTemplate::EndToEndProtection::EndToEndDescription
    
    Sources:
      - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (Page 205, Classic Platform
      R23-11)
      - AUTOSAR_CP_TPS_SystemTemplate.pdf (Page 385, Classic Platform R23-11)
    """
    def __init__(self):
        super().__init__()

    # ===== Pythonic properties (CODING_RULE_V2_00016) =====
        # The category represents the identification of the concrete The applicable
        # values are specified in a and determine the applicable EndToEndDescription.
        self._category: Optional["NameToken"] = None

    @property
    def category(self) -> Optional["NameToken"]:
        """Get category (Pythonic accessor)."""
        return self._category

    @category.setter
    def category(self, value: Optional["NameToken"]) -> None:
        """
        Set category with validation.
        
        Args:
            value: The category to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._category = None
            return

        if not isinstance(value, NameToken):
            raise TypeError(
                f"category must be NameToken or None, got {type(value).__name__}"
            )
        self._category = value
        # Bit offset of Counter from the beginning of the Array the Signal
                # Group/VariableDataPrototype bit numbering: bit 0 is the least important).
        # shall be a multiplicity of 4 and it should be 8 For example, offset 8 means
                # that the take the low nibble of the byte 1, i.
        # e.
        # bits 8.
        # counterOffset is not present the value is defined by profile.
        self._counterOffset: Optional["PositiveInteger"] = None

    @property
    def counter_offset(self) -> Optional["PositiveInteger"]:
        """Get counterOffset (Pythonic accessor)."""
        return self._counterOffset

    @counter_offset.setter
    def counter_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set counterOffset with validation.
        
        Args:
            value: The counterOffset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._counterOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"counterOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._counterOffset = value
        # Bit offset of CRC from the beginning of the Array the Signal
                # Group/VariableDataPrototype bit numbering: bit 0 is the least important).
        # shall be a multiplicity of 8 and it should be 0 For example, offset 8 means
                # that the take the byte 1, i.
        # e.
        # bits 8.
        # 15.
        # If crcOffset is not value is defined by the selected profile.
        # 1228 Document ID 62: AUTOSAR_CP_TPS_SoftwareComponentTemplate Template R23-11
                # PositiveInteger * attr This represents a unique numerical identifier.
        # is used for protection against masquerading.
        # concerning the maximum number of values is specific for each E2E profile)
                # this attribute are controlled by a semantic depends on the category of the
                # EndToEnd.
        self._crcOffset: Optional["PositiveInteger"] = None

    @property
    def crc_offset(self) -> Optional["PositiveInteger"]:
        """Get crcOffset (Pythonic accessor)."""
        return self._crcOffset

    @crc_offset.setter
    def crc_offset(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set crcOffset with validation.
        
        Args:
            value: The crcOffset to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._crcOffset = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"crcOffset must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._crcOffset = value
        # There are three inclusion modes how the implicit two-byte is included in the
                # one-byte CRC: = 0: Two bytes are included in the CRC configuration) This is
                # used in variant 1A.
        # = 1: One of the two bytes byte is included, and low byte, depending on parity
                # of (alternating ID configuration).
        # For even byte is included; For odd counters the high included.
        # This is used in variant 1B.
        # = 2: Only low byte is included, high byte is This is applicable if the IDs in
                # a particular 8 bits.
        # = 3: The low byte is included in the implicit the low nibble of the high byte
                # is with the data (i.
        # e.
        # it is explicitly high nibble of the high byte is not used.
        # applicable for the IDs up to 12 bits.
        self._dataIdMode: Optional["PositiveInteger"] = None

    @property
    def data_id_mode(self) -> Optional["PositiveInteger"]:
        """Get dataIdMode (Pythonic accessor)."""
        return self._dataIdMode

    @data_id_mode.setter
    def data_id_mode(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataIdMode with validation.
        
        Args:
            value: The dataIdMode to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdMode = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataIdMode must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataIdMode = value
        # Bit offset of the low nibble of the high byte of Data ID.
        # The of this attribute is controlled by [constr_1261].
        self._dataIdNibble: Optional["PositiveInteger"] = None

    @property
    def data_id_nibble(self) -> Optional["PositiveInteger"]:
        """Get dataIdNibble (Pythonic accessor)."""
        return self._dataIdNibble

    @data_id_nibble.setter
    def data_id_nibble(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataIdNibble with validation.
        
        Args:
            value: The dataIdNibble to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataIdNibble = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataIdNibble must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataIdNibble = value
        # This attribute represents the length of the Array the Signal
        # Group/VariableDataPrototype and Counter in bits.
        self._dataLength: Optional["PositiveInteger"] = None

    @property
    def data_length(self) -> Optional["PositiveInteger"]:
        """Get dataLength (Pythonic accessor)."""
        return self._dataLength

    @data_length.setter
    def data_length(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set dataLength with validation.
        
        Args:
            value: The dataLength to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._dataLength = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"dataLength must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._dataLength = value
        # Initial maximum allowed gap between two counter values two consecutively
                # received valid Data, i.
        # e.
        # how many data is accepted.
        # For example, if the Data with counter 1 and MaxDeltaCounter 1, then at the
                # next reception the receiver can accept values 2 and 3, but not 4.
        self._maxDelta: Optional["PositiveInteger"] = None

    @property
    def max_delta(self) -> Optional["PositiveInteger"]:
        """Get maxDelta (Pythonic accessor)."""
        return self._maxDelta

    @max_delta.setter
    def max_delta(self, value: Optional["PositiveInteger"]) -> None:
        """
        Set maxDelta with validation.
        
        Args:
            value: The maxDelta to set
        
        Raises:
            TypeError: If value type is incorrect
        """
        if value is None:
            self._maxDelta = None
            return

        if not isinstance(value, PositiveInteger):
            raise TypeError(
                f"maxDelta must be PositiveInteger or None, got {type(value).__name__}"
            )
        self._maxDelta = value

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

    def setCategory(self, value: "NameToken") -> "EndToEndDescription":
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

    def getCounterOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for counterOffset.
        
        Returns:
            The counterOffset value
        
        Note:
            Delegates to counter_offset property (CODING_RULE_V2_00017)
        """
        return self.counter_offset  # Delegates to property

    def setCounterOffset(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for counterOffset with method chaining.
        
        Args:
            value: The counterOffset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to counter_offset property setter (gets validation automatically)
        """
        self.counter_offset = value  # Delegates to property setter
        return self

    def getCrcOffset(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for crcOffset.
        
        Returns:
            The crcOffset value
        
        Note:
            Delegates to crc_offset property (CODING_RULE_V2_00017)
        """
        return self.crc_offset  # Delegates to property

    def setCrcOffset(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for crcOffset with method chaining.
        
        Args:
            value: The crcOffset to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to crc_offset property setter (gets validation automatically)
        """
        self.crc_offset = value  # Delegates to property setter
        return self

    def getDataIdMode(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataIdMode.
        
        Returns:
            The dataIdMode value
        
        Note:
            Delegates to data_id_mode property (CODING_RULE_V2_00017)
        """
        return self.data_id_mode  # Delegates to property

    def setDataIdMode(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for dataIdMode with method chaining.
        
        Args:
            value: The dataIdMode to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id_mode property setter (gets validation automatically)
        """
        self.data_id_mode = value  # Delegates to property setter
        return self

    def getDataIdNibble(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataIdNibble.
        
        Returns:
            The dataIdNibble value
        
        Note:
            Delegates to data_id_nibble property (CODING_RULE_V2_00017)
        """
        return self.data_id_nibble  # Delegates to property

    def setDataIdNibble(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for dataIdNibble with method chaining.
        
        Args:
            value: The dataIdNibble to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_id_nibble property setter (gets validation automatically)
        """
        self.data_id_nibble = value  # Delegates to property setter
        return self

    def getDataLength(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for dataLength.
        
        Returns:
            The dataLength value
        
        Note:
            Delegates to data_length property (CODING_RULE_V2_00017)
        """
        return self.data_length  # Delegates to property

    def setDataLength(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for dataLength with method chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to data_length property setter (gets validation automatically)
        """
        self.data_length = value  # Delegates to property setter
        return self

    def getMaxDelta(self) -> "PositiveInteger":
        """
        AUTOSAR-compliant getter for maxDelta.
        
        Returns:
            The maxDelta value
        
        Note:
            Delegates to max_delta property (CODING_RULE_V2_00017)
        """
        return self.max_delta  # Delegates to property

    def setMaxDelta(self, value: "PositiveInteger") -> "EndToEndDescription":
        """
        AUTOSAR-compliant setter for maxDelta with method chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Note:
            Delegates to max_delta property setter (gets validation automatically)
        """
        self.max_delta = value  # Delegates to property setter
        return self

    # ===== Fluent with_ methods (CODING_RULE_V2_00019) =====

    def with_category(self, value: Optional["NameToken"]) -> "EndToEndDescription":
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

    def with_counter_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set counterOffset and return self for chaining.
        
        Args:
            value: The counterOffset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_counter_offset("value")
        """
        self.counter_offset = value  # Use property setter (gets validation)
        return self

    def with_crc_offset(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set crcOffset and return self for chaining.
        
        Args:
            value: The crcOffset to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_crc_offset("value")
        """
        self.crc_offset = value  # Use property setter (gets validation)
        return self

    def with_data_id_mode(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set dataIdMode and return self for chaining.
        
        Args:
            value: The dataIdMode to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id_mode("value")
        """
        self.data_id_mode = value  # Use property setter (gets validation)
        return self

    def with_data_id_nibble(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set dataIdNibble and return self for chaining.
        
        Args:
            value: The dataIdNibble to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_id_nibble("value")
        """
        self.data_id_nibble = value  # Use property setter (gets validation)
        return self

    def with_data_length(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set dataLength and return self for chaining.
        
        Args:
            value: The dataLength to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_data_length("value")
        """
        self.data_length = value  # Use property setter (gets validation)
        return self

    def with_max_delta(self, value: Optional["PositiveInteger"]) -> "EndToEndDescription":
        """
        Set maxDelta and return self for chaining.
        
        Args:
            value: The maxDelta to set
        
        Returns:
            self for method chaining
        
        Example:
            >>> obj.with_max_delta("value")
        """
        self.max_delta = value  # Use property setter (gets validation)
        return self