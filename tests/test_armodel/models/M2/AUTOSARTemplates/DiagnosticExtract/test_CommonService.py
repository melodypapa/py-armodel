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
    DiagnosticCustomServiceClass,
    DiagnosticSecurityAccessClass,
    DiagnosticServiceClass,
    DiagnosticServiceInstance,
    DiagnosticSessionControlClass,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType, TimeValue

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
