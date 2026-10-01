"""Model tests for DiagnosticExtract CommonService classes.

DiagnosticServiceInstance (Table 4.26, p.70) and the in-pass created ref
target DiagnosticServiceClass (Table 4.25, p.69).
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import (
    DiagnosticAuthenticationClass,
    DiagnosticComControlClass,
    DiagnosticControlDTCSettingClass,
    DiagnosticCustomServiceClass,
    DiagnosticEcuResetClass,
    DiagnosticReadDataByIdentifierClass,
    DiagnosticReadScalingDataByIdentifierClass,
    DiagnosticSecurityAccessClass,
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
    DiagnosticSessionControlClass,
    DiagnosticWriteDataByIdentifierClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DiagnosticComControlSpecificChannel,
    DiagnosticComControlSubNodeChannel,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    DiagnosticResponseToEcuResetEnum,
    PositiveInteger,
    RefType,
    TimeValue,
)

DSI_NOTE = "This represents a concrete instance of a diagnostic service."
DSC_NOTE = "This meta-class provides the ability to define common properties that are shared among all instances of sub-classes of DiagnosticServiceInstance."
ACCESS_PERMISSION_NOTE = "This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance.."
CUSTOM_SERVICE_ID_NOTE = "This attribute may only be used for the definition of custom services. The values shall not overlap with existing standardized service IDs."
DCSC_CLASS_DOCSTRING = (
    "This represents the ability to define a custom diagnostic service class and assign an ID to it. "
    "Further configuration is not foreseen from the point of view of the diagnostic extract and consequently needs to be done on the level of ECUC.\n"
    "\n"
    "[constr_1330] Custom service identifier shall not overlap with standardized service identifiers: "
    "The value of the attribute customServiceId shall not be set to any of the values reserved for standardized "
    "service identifiers as defined by the ISO 14229-1, see [17]. This rule shall be imposed at the time when the DEXT is complete."
)
SERVICE_CLASS_NOTE = (
    'This represents the corresponding "class", i.e. this meta-class provides properties that are shared among all instances of applicable sub-classes of '
    'DiagnosticServiceInstance. The subclasses that affected by this pattern implement references to the applicable "class"-role that substantiate this abstract reference. Stereotypes: atpAbstract'
)


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _pkg():
    return AUTOSAR.getInstance().createARPackage("DiagPkg")


def _respond_to_reset(value):
    """Build a DiagnosticResponseToEcuResetEnum holding the given literal value."""
    return DiagnosticResponseToEcuResetEnum().setValue(value)


class _ConcreteServiceInstance(DiagnosticServiceInstance):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class _ConcreteServiceClass(DiagnosticServiceClass):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class Test_DiagnosticServiceInstance:
    """Test cases for DiagnosticServiceInstance class (Table 4.26, p.70)."""

    def test_is_abstract(self):
        with pytest.raises(TypeError):
            DiagnosticServiceInstance(_pkg(), "Dsi")

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticServiceInstance, DiagnosticCommonElement)
        assert issubclass(DiagnosticServiceInstance, ARObject)
        assert issubclass(DiagnosticServiceInstance, Identifiable)

    def test_concrete_subclass_initialization(self):
        instance = _ConcreteServiceInstance(_pkg(), "MyDsi")
        assert instance.getShortName() == "MyDsi"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticServiceInstance.__doc__ == DSI_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticServiceInstance.__init__.__doc__ is None

    def test_defaults(self):
        instance = _ConcreteServiceInstance(_pkg(), "MyDsi")
        assert instance.getAccessPermissionRef() is None
        assert instance.getServiceClassRef() is None

    def test_access_permission_ref_round_trip(self):
        instance = _ConcreteServiceInstance(_pkg(), "MyDsi")
        ref = _ref("DIAGNOSTIC-ACCESS-PERMISSION", "/Diag/AccessPerms/Ap1")
        assert instance.setAccessPermissionRef(ref) is instance
        assert instance.getAccessPermissionRef() is ref

    def test_service_class_ref_round_trip(self):
        instance = _ConcreteServiceInstance(_pkg(), "MyDsi")
        ref = _ref("DIAGNOSTIC-SERVICE-CLASS", "/Diag/ServiceClasses/Sc1")
        assert instance.setServiceClassRef(ref) is instance
        assert instance.getServiceClassRef() is ref

    def test_setter_none_is_no_op(self):
        instance = _ConcreteServiceInstance(_pkg(), "MyDsi")
        access_ref = _ref("DIAGNOSTIC-ACCESS-PERMISSION", "/Diag/AccessPerms/Ap1")
        class_ref = _ref("DIAGNOSTIC-SERVICE-CLASS", "/Diag/ServiceClasses/Sc1")
        instance.setAccessPermissionRef(access_ref)
        instance.setServiceClassRef(class_ref)
        assert instance.setAccessPermissionRef(None) is instance
        assert instance.setServiceClassRef(None) is instance
        assert instance.getAccessPermissionRef() is access_ref
        assert instance.getServiceClassRef() is class_ref

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticServiceInstance.getAccessPermissionRef.__doc__) == ACCESS_PERMISSION_NOTE
        assert inspect.cleandoc(DiagnosticServiceInstance.setAccessPermissionRef.__doc__) == (
            ACCESS_PERMISSION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing accessPermissionRef."
        )
        assert inspect.cleandoc(DiagnosticServiceInstance.getServiceClassRef.__doc__) == SERVICE_CLASS_NOTE
        assert inspect.cleandoc(DiagnosticServiceInstance.setServiceClassRef.__doc__) == (SERVICE_CLASS_NOTE + "\n\nA None value is a no-op and does not overwrite an existing serviceClassRef.")


class Test_DiagnosticServiceClass:
    """Test cases for DiagnosticServiceClass class (Table 4.25, p.69)."""

    def test_is_abstract(self):
        with pytest.raises(TypeError):
            DiagnosticServiceClass(_pkg(), "Dsc")

    def test_is_diagnostic_common_element_subclass(self):
        assert issubclass(DiagnosticServiceClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticServiceClass, ARObject)
        assert issubclass(DiagnosticServiceClass, Identifiable)

    def test_concrete_subclass_initialization(self):
        service_class = _ConcreteServiceClass(_pkg(), "MyDsc")
        assert service_class.getShortName() == "MyDsc"

    def test_class_docstring_is_spec_note_verbatim(self):
        assert DiagnosticServiceClass.__doc__ == DSC_NOTE

    def test_init_has_no_docstring(self):
        assert DiagnosticServiceClass.__init__.__doc__ is None

    def test_has_no_spec_attributes(self):
        service_class = _ConcreteServiceClass(_pkg(), "MyDsc")
        assert not hasattr(service_class, "getServiceClasses")
        assert not hasattr(service_class, "addServiceClass")
        assert isinstance(service_class, ARObject)


class Test_DiagnosticCustomServiceClass:
    """Test cases for DiagnosticCustomServiceClass class (Table 4.28, p.71)."""

    def test_is_concrete(self):
        service_class = DiagnosticCustomServiceClass(_pkg(), "MyDcsc")
        assert service_class.getShortName() == "MyDcsc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticCustomServiceClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticCustomServiceClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticCustomServiceClass, ARObject)
        assert issubclass(DiagnosticCustomServiceClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticCustomServiceClass.__doc__) == DCSC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticCustomServiceClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = DiagnosticCustomServiceClass(_pkg(), "MyDcsc")
        assert service_class.getCustomServiceId() is None

    def test_get_set_custom_service_id(self):
        service_class = DiagnosticCustomServiceClass(_pkg(), "MyDcsc")
        value = PositiveInteger()
        value.setValue("5")
        assert service_class.setCustomServiceId(value) is service_class
        assert service_class.getCustomServiceId() is value
        assert service_class.getCustomServiceId().getValue() == 5
        service_class.setCustomServiceId(None)
        assert service_class.getCustomServiceId() is value

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticCustomServiceClass.getCustomServiceId.__doc__) == CUSTOM_SERVICE_ID_NOTE
        assert inspect.cleandoc(DiagnosticCustomServiceClass.setCustomServiceId.__doc__) == (CUSTOM_SERVICE_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing customServiceId.")

    def test_create_diagnostic_custom_service_class(self):
        package = _pkg()
        service_class = package.createDiagnosticCustomServiceClass("Svc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticCustomServiceClass)
        assert service_class.getShortName() == "Svc1"
        assert package.getElement("Svc1", DiagnosticCustomServiceClass) is service_class

        duplicate = package.createDiagnosticCustomServiceClass("Svc1")
        assert duplicate is service_class


class Test_DiagnosticSessionControlClass:
    """Test cases for DiagnosticSessionControlClass class (Table 4.48, p.93)."""

    DSCL_CLASS_DOCSTRING = (
        'This meta-class contains attributes shared by all instances of the "Session Control" diagnostic service.\n'
        "\n"
        "[constr_10440] Restriction for the minimum value of attribute DiagnosticSessionControlClass.s3ServerTimeout: "
        "The value of attribute DiagnosticSessionControlClass.s3ServerTimeout shall be greater than or equal to 5.0 "
        "at the time when the DEXT is complete."
    )
    S3_SERVER_TIMEOUT_NOTE = "Time for the server to keep a diagnostic session other than the default session active while not receiving any diagnostic request message."

    def test_is_concrete(self):
        service_class = DiagnosticSessionControlClass(_pkg(), "MyDscl")
        assert service_class.getShortName() == "MyDscl"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticSessionControlClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticSessionControlClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticSessionControlClass, ARObject)
        assert issubclass(DiagnosticSessionControlClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticSessionControlClass.__doc__) == self.DSCL_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticSessionControlClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = DiagnosticSessionControlClass(_pkg(), "MyDscl")
        assert service_class.getS3ServerTimeout() is None

    def test_get_set_s3_server_timeout(self):
        service_class = DiagnosticSessionControlClass(_pkg(), "MyDscl")
        value = TimeValue()
        value.setValue("10.0")
        assert service_class.setS3ServerTimeout(value) is service_class
        assert service_class.getS3ServerTimeout() is value
        assert service_class.getS3ServerTimeout().getValue() == 10.0
        service_class.setS3ServerTimeout(None)
        assert service_class.getS3ServerTimeout() is value

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticSessionControlClass.getS3ServerTimeout.__doc__) == self.S3_SERVER_TIMEOUT_NOTE
        assert inspect.cleandoc(DiagnosticSessionControlClass.setS3ServerTimeout.__doc__) == (
            self.S3_SERVER_TIMEOUT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing s3ServerTimeout."
        )

    def test_create_diagnostic_session_control_class(self):
        package = _pkg()
        service_class = package.createDiagnosticSessionControlClass("Sscl1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticSessionControlClass)
        assert service_class.getShortName() == "Sscl1"
        assert package.getElement("Sscl1", DiagnosticSessionControlClass) is service_class

        duplicate = package.createDiagnosticSessionControlClass("Sscl1")
        assert duplicate is service_class


class Test_DiagnosticSecurityAccessClass:
    """Test cases for DiagnosticSecurityAccessClass class (Table 4.50, p.96)."""

    DSAC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Security Access" diagnostic service.'

    def test_is_concrete(self):
        service_class = DiagnosticSecurityAccessClass(_pkg(), "MyDsac")
        assert service_class.getShortName() == "MyDsac"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticSecurityAccessClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticSecurityAccessClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticSecurityAccessClass, ARObject)
        assert issubclass(DiagnosticSecurityAccessClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticSecurityAccessClass.__doc__) == self.DSAC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticSecurityAccessClass.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        own_public = {name for name, member in vars(DiagnosticSecurityAccessClass).items() if not name.startswith("_")}
        assert own_public == set()  # Table 4.50 defines no attributes

    def test_create_diagnostic_security_access_class(self):
        package = _pkg()
        service_class = package.createDiagnosticSecurityAccessClass("Ssac1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticSecurityAccessClass)
        assert service_class.getShortName() == "Ssac1"
        assert package.getElement("Ssac1", DiagnosticSecurityAccessClass) is service_class

        duplicate = package.createDiagnosticSecurityAccessClass("Ssac1")
        assert duplicate is service_class


class Test_DiagnosticAuthenticationClass:
    """Test cases for DiagnosticAuthenticationClass class (Table 4.52, p.99)."""

    DAC_CLASS_DOCSTRING = "This meta-class contains configuration shared by all instances of the Authentication diagnostic service."

    def test_is_concrete(self):
        service_class = DiagnosticAuthenticationClass(_pkg(), "MyDac")
        assert service_class.getShortName() == "MyDac"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticAuthenticationClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticAuthenticationClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticAuthenticationClass, ARObject)
        assert issubclass(DiagnosticAuthenticationClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticAuthenticationClass.__doc__) == self.DAC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticAuthenticationClass.__init__.__doc__ is None

    def test_defines_no_new_public_members(self):
        own_public = {name for name, member in vars(DiagnosticAuthenticationClass).items() if not name.startswith("_")}
        assert own_public == set()  # Table 4.52 defines no attributes

    def test_create_diagnostic_authentication_class(self):
        package = _pkg()
        service_class = package.createDiagnosticAuthenticationClass("Dac1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticAuthenticationClass)
        assert service_class.getShortName() == "Dac1"
        assert package.getElement("Dac1", DiagnosticAuthenticationClass) is service_class

        duplicate = package.createDiagnosticAuthenticationClass("Dac1")
        assert duplicate is service_class


class Test_DiagnosticEcuResetClass:
    """Test cases for DiagnosticEcuResetClass class (Table 4.61, p.102)."""

    DERSC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Ecu Reset" diagnostic service.'
    RESPOND_TO_RESET_NOTE = "This attribute defines whether the response to the EcuReset service shall be transmitted before or after the actual reset."

    def test_is_concrete(self):
        service_class = DiagnosticEcuResetClass(_pkg(), "MyDersc")
        assert service_class.getShortName() == "MyDersc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticEcuResetClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticEcuResetClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticEcuResetClass, ARObject)
        assert issubclass(DiagnosticEcuResetClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticEcuResetClass.__doc__) == self.DERSC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticEcuResetClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = DiagnosticEcuResetClass(_pkg(), "MyDersc")
        assert service_class.getRespondToReset() is None

    def test_get_set_respond_to_reset(self):
        service_class = DiagnosticEcuResetClass(_pkg(), "MyDersc")
        value = _respond_to_reset("respondAfterReset")
        assert service_class.setRespondToReset(value) is service_class
        assert service_class.getRespondToReset() is value
        assert service_class.getRespondToReset().getValue() == "respondAfterReset"
        service_class.setRespondToReset(None)
        assert service_class.getRespondToReset() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticEcuResetClass.getRespondToReset.__doc__) == self.RESPOND_TO_RESET_NOTE
        assert inspect.cleandoc(DiagnosticEcuResetClass.setRespondToReset.__doc__) == (self.RESPOND_TO_RESET_NOTE + "\n\nA None value is a no-op and does not overwrite an existing respondToReset.")

    def test_create_diagnostic_ecu_reset_class(self):
        package = _pkg()
        service_class = package.createDiagnosticEcuResetClass("Dersc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticEcuResetClass)
        assert service_class.getShortName() == "Dersc1"
        assert package.getElement("Dersc1", DiagnosticEcuResetClass) is service_class

        duplicate = package.createDiagnosticEcuResetClass("Dersc1")
        assert duplicate is service_class


class TestDiagnosticComControlClass:
    """Test cases for DiagnosticComControlClass class (Table 4.66, p.109)."""

    DCCC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Communication Control" diagnostic service.'
    ALL_CHANNELS_NOTE = (
        "This reference represents the semantics that all available channels shall be affected. "
        'It is still necessary to refer to individual CommunicatuionClusters because there could be private CommunicationClusters in the System Extract that are not subject to the service "communication control". '
        "By referring to the applicable CommunicationClusters it can be made sure that only the affected CommunicationClusters are accessed."
    )
    ALL_PHYSICAL_CHANNELS_NOTE = (
        "This reference represents the semantics that all available channels shall be affected. "
        'It is still necessary to refer to individual EthernetPhysicalChannels because there could be private VLANs (and thus private EthernetPhysicalChannels) in the System Extract that are not subject to the service "communication control". '
        "By referring to the applicable EthernetPhysicalChannels it can be made sure that only the affected EthernetPhysicalChannels are accessed."
    )
    SPECIFIC_CHANNEL_NOTE = "This represents the ability to add additional attributes to the case that only specific channels are supposed to be considered,"
    SUB_NODE_CHANNEL_NOTE = (
        'This attribute represents the ability to add further attributes to the definition of a specific sub-node channel that is subject to the diagnostic service "communication control".'
    )

    def _make_obj(self) -> DiagnosticComControlClass:
        return DiagnosticComControlClass(_pkg(), "MyDccc")

    def test_is_concrete(self):
        service_class = self._make_obj()
        assert service_class.getShortName() == "MyDccc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticComControlClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticComControlClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticComControlClass, ARObject)
        assert issubclass(DiagnosticComControlClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticComControlClass.__doc__) == self.DCCC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticComControlClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = self._make_obj()
        assert service_class.getAllChannels() == []
        assert service_class.getAllPhysicalChannels() == []
        assert service_class.getSpecificChannels() == []
        assert service_class.getSubNodeChannels() == []

    def test_add_get_all_channels(self):
        service_class = self._make_obj()
        ref = _ref("COMMUNICATION-CLUSTER", "/System/Clusters/Cluster1")
        assert service_class.addAllChannel(ref) is service_class
        assert service_class.getAllChannels() == [ref]

        service_class.addAllChannel(None)
        assert service_class.getAllChannels() == [ref]  # None is a no-op

    def test_add_get_all_physical_channels(self):
        service_class = self._make_obj()
        ref = _ref("ETHERNET-PHYSICAL-CHANNEL", "/System/EthernetClusters/Cluster1/Vlan1")
        assert service_class.addAllPhysicalChannel(ref) is service_class
        assert service_class.getAllPhysicalChannels() == [ref]
        assert service_class.getAllPhysicalChannels()[0].getValue() == "/System/EthernetClusters/Cluster1/Vlan1"

        service_class.addAllPhysicalChannel(None)
        assert service_class.getAllPhysicalChannels() == [ref]  # None is a no-op

    def test_add_get_specific_channels(self):
        service_class = self._make_obj()
        channel = DiagnosticComControlSpecificChannel()
        channel.setSubnetNumber(PositiveInteger().setValue("3"))
        assert service_class.addSpecificChannel(channel) is service_class
        assert service_class.getSpecificChannels() == [channel]
        assert service_class.getSpecificChannels()[0].getSubnetNumber().getValue() == 3

        service_class.addSpecificChannel(None)
        assert service_class.getSpecificChannels() == [channel]  # None is a no-op

    def test_add_get_sub_node_channels(self):
        service_class = self._make_obj()
        channel = DiagnosticComControlSubNodeChannel()
        channel.setSubNodeNumber(PositiveInteger().setValue("7"))
        assert service_class.addSubNodeChannel(channel) is service_class
        assert service_class.getSubNodeChannels() == [channel]
        assert service_class.getSubNodeChannels()[0].getSubNodeNumber().getValue() == 7

        service_class.addSubNodeChannel(None)
        assert service_class.getSubNodeChannels() == [channel]  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticComControlClass.addAllChannel.__doc__) == (self.ALL_CHANNELS_NOTE + "\n\nA None value is a no-op and does not append an allChannel.")
        assert inspect.cleandoc(DiagnosticComControlClass.getAllChannels.__doc__) == self.ALL_CHANNELS_NOTE
        assert inspect.cleandoc(DiagnosticComControlClass.addAllPhysicalChannel.__doc__) == (self.ALL_PHYSICAL_CHANNELS_NOTE + "\n\nA None value is a no-op and does not append an allPhysicalChannel.")
        assert inspect.cleandoc(DiagnosticComControlClass.getAllPhysicalChannels.__doc__) == self.ALL_PHYSICAL_CHANNELS_NOTE
        assert inspect.cleandoc(DiagnosticComControlClass.addSpecificChannel.__doc__) == (self.SPECIFIC_CHANNEL_NOTE + "\n\nA None value is a no-op and does not append a specificChannel.")
        assert inspect.cleandoc(DiagnosticComControlClass.getSpecificChannels.__doc__) == self.SPECIFIC_CHANNEL_NOTE
        assert inspect.cleandoc(DiagnosticComControlClass.addSubNodeChannel.__doc__) == (self.SUB_NODE_CHANNEL_NOTE + "\n\nA None value is a no-op and does not append a subNodeChannel.")
        assert inspect.cleandoc(DiagnosticComControlClass.getSubNodeChannels.__doc__) == self.SUB_NODE_CHANNEL_NOTE

    def test_create_diagnostic_com_control_class(self):
        package = _pkg()
        service_class = package.createDiagnosticComControlClass("Dccc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticComControlClass)
        assert service_class.getShortName() == "Dccc1"
        assert package.getElement("Dccc1", DiagnosticComControlClass) is service_class

        duplicate = package.createDiagnosticComControlClass("Dccc1")
        assert duplicate is service_class


class TestDiagnosticControlDTCSettingClass:
    """Test cases for DiagnosticControlDTCSettingClass class (Table 4.69, p.111)."""

    DCDTSC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Control DTC Setting" diagnostic service.'
    CONTROL_OPTION_RECORD_PRESENT_NOTE = "This represents the decision whether the DTCSettingControlOptionRecord (see ISO 14229-1) is in general supported in the request message."

    def _make_obj(self) -> DiagnosticControlDTCSettingClass:
        return DiagnosticControlDTCSettingClass(_pkg(), "MyDcdtsc")

    def test_is_concrete(self):
        service_class = self._make_obj()
        assert service_class.getShortName() == "MyDcdtsc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticControlDTCSettingClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticControlDTCSettingClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticControlDTCSettingClass, ARObject)
        assert issubclass(DiagnosticControlDTCSettingClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticControlDTCSettingClass.__doc__) == self.DCDTSC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticControlDTCSettingClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = self._make_obj()
        assert service_class.getControlOptionRecordPresent() is None

    def test_get_set_control_option_record_present(self):
        service_class = self._make_obj()
        value = Boolean()
        value.setValue(True)
        assert service_class.setControlOptionRecordPresent(value) is service_class
        assert service_class.getControlOptionRecordPresent() is value
        assert service_class.getControlOptionRecordPresent().getValue() is True

        service_class.setControlOptionRecordPresent(None)
        assert service_class.getControlOptionRecordPresent() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticControlDTCSettingClass.getControlOptionRecordPresent.__doc__) == self.CONTROL_OPTION_RECORD_PRESENT_NOTE
        assert inspect.cleandoc(DiagnosticControlDTCSettingClass.setControlOptionRecordPresent.__doc__) == (
            self.CONTROL_OPTION_RECORD_PRESENT_NOTE + "\n\nA None value is a no-op and does not overwrite an existing controlOptionRecordPresent."
        )

    def test_create_diagnostic_control_dtc_setting_class(self):
        package = _pkg()
        service_class = package.createDiagnosticControlDTCSettingClass("Dcdtsc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticControlDTCSettingClass)
        assert service_class.getShortName() == "Dcdtsc1"
        assert package.getElement("Dcdtsc1", DiagnosticControlDTCSettingClass) is service_class

        duplicate = package.createDiagnosticControlDTCSettingClass("Dcdtsc1")
        assert duplicate is service_class


class Test_DiagnosticReadDataByIdentifierClass:
    """Test cases for DiagnosticReadDataByIdentifierClass class (Table 4.74, p.114)."""

    DRDIBC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Read Data by Identifier" diagnostic service.'
    MAX_DID_TO_READ_NOTE = "This attribute represents the maximum number of allowed DIDs in a single instance of DiagnosticReadDataByIdentifier."

    def test_is_concrete(self):
        service_class = DiagnosticReadDataByIdentifierClass(_pkg(), "MyRdibc")
        assert service_class.getShortName() == "MyRdibc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticReadDataByIdentifierClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticReadDataByIdentifierClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticReadDataByIdentifierClass, ARObject)
        assert issubclass(DiagnosticReadDataByIdentifierClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticReadDataByIdentifierClass.__doc__) == self.DRDIBC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticReadDataByIdentifierClass.__init__.__doc__ is None

    def test_defaults(self):
        service_class = DiagnosticReadDataByIdentifierClass(_pkg(), "MyRdibc")
        assert service_class.getMaxDidToRead() is None

    def test_get_set_max_did_to_read(self):
        service_class = DiagnosticReadDataByIdentifierClass(_pkg(), "MyRdibc")
        value = PositiveInteger()
        value.setValue("10")
        assert service_class.setMaxDidToRead(value) is service_class
        assert service_class.getMaxDidToRead() is value
        assert service_class.getMaxDidToRead().getValue() == 10
        service_class.setMaxDidToRead(None)
        assert service_class.getMaxDidToRead() is value  # None is a no-op

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        assert inspect.cleandoc(DiagnosticReadDataByIdentifierClass.getMaxDidToRead.__doc__) == self.MAX_DID_TO_READ_NOTE
        assert inspect.cleandoc(DiagnosticReadDataByIdentifierClass.setMaxDidToRead.__doc__) == (
            self.MAX_DID_TO_READ_NOTE + "\n\nA None value is a no-op and does not overwrite an existing maxDidToRead."
        )

    def test_create_diagnostic_read_data_by_identifier_class(self):
        package = _pkg()
        service_class = package.createDiagnosticReadDataByIdentifierClass("Rdibc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticReadDataByIdentifierClass)
        assert service_class.getShortName() == "Rdibc1"
        assert package.getElement("Rdibc1", DiagnosticReadDataByIdentifierClass) is service_class

        duplicate = package.createDiagnosticReadDataByIdentifierClass("Rdibc1")
        assert duplicate is service_class


class Test_DiagnosticWriteDataByIdentifierClass:
    """Test cases for DiagnosticWriteDataByIdentifierClass class (Table 4.72, p.113)."""

    DWDIBC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Write Data by Identifier" diagnostic service.'

    def test_is_concrete(self):
        service_class = DiagnosticWriteDataByIdentifierClass(_pkg(), "MyWdibc")
        assert service_class.getShortName() == "MyWdibc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticWriteDataByIdentifierClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticWriteDataByIdentifierClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticWriteDataByIdentifierClass, ARObject)
        assert issubclass(DiagnosticWriteDataByIdentifierClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticWriteDataByIdentifierClass.__doc__) == self.DWDIBC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticWriteDataByIdentifierClass.__init__.__doc__ is None

    def test_has_no_own_attributes(self):
        """Table 4.72 defines no attribute rows beyond the inherited ones."""
        service_class = DiagnosticWriteDataByIdentifierClass(_pkg(), "MyWdibc")
        assert not any(attr.startswith("set") or attr.startswith("get") for attr in vars(service_class))

    def test_create_diagnostic_write_data_by_identifier_class(self):
        package = _pkg()
        service_class = package.createDiagnosticWriteDataByIdentifierClass("Wdibc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticWriteDataByIdentifierClass)
        assert service_class.getShortName() == "Wdibc1"
        assert package.getElement("Wdibc1", DiagnosticWriteDataByIdentifierClass) is service_class

        duplicate = package.createDiagnosticWriteDataByIdentifierClass("Wdibc1")
        assert duplicate is service_class


class Test_DiagnosticReadScalingDataByIdentifierClass:
    """Test cases for DiagnosticReadScalingDataByIdentifierClass class (Table 4.79, p.116)."""

    DRSDIBC_CLASS_DOCSTRING = 'This meta-class contains attributes shared by all instances of the "Read Scaling Data by Identifier" diagnostic service.'

    def test_is_concrete(self):
        service_class = DiagnosticReadScalingDataByIdentifierClass(_pkg(), "MyRsdibc")
        assert service_class.getShortName() == "MyRsdibc"

    def test_is_diagnostic_service_class_subclass(self):
        assert issubclass(DiagnosticReadScalingDataByIdentifierClass, DiagnosticServiceClass)
        assert issubclass(DiagnosticReadScalingDataByIdentifierClass, DiagnosticCommonElement)
        assert issubclass(DiagnosticReadScalingDataByIdentifierClass, ARObject)
        assert issubclass(DiagnosticReadScalingDataByIdentifierClass, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        assert inspect.cleandoc(DiagnosticReadScalingDataByIdentifierClass.__doc__) == self.DRSDIBC_CLASS_DOCSTRING

    def test_init_has_no_docstring(self):
        assert DiagnosticReadScalingDataByIdentifierClass.__init__.__doc__ is None

    def test_create_diagnostic_read_scaling_data_by_identifier_class(self):
        package = _pkg()
        service_class = package.createDiagnosticReadScalingDataByIdentifierClass("Rsdibc1")
        assert service_class is not None
        assert isinstance(service_class, DiagnosticReadScalingDataByIdentifierClass)
        assert service_class.getShortName() == "Rsdibc1"
        assert package.getElement("Rsdibc1", DiagnosticReadScalingDataByIdentifierClass) is service_class

        duplicate = package.createDiagnosticReadScalingDataByIdentifierClass("Rsdibc1")
        assert duplicate is service_class
