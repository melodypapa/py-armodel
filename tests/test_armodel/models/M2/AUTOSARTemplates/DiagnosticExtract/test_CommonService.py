"""Model tests for DiagnosticExtract CommonService classes.

DiagnosticServiceInstance (Table 4.26, p.70) and the in-pass created ref
target DiagnosticServiceClass (Table 4.25, p.69).
"""

import inspect

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics import DiagnosticCommonElement
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonService import DiagnosticServiceClass, DiagnosticServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

DSI_NOTE = "This represents a concrete instance of a diagnostic service."
DSC_NOTE = "This meta-class provides the ability to define common properties that are shared among all instances of sub-classes of DiagnosticServiceInstance."
ACCESS_PERMISSION_NOTE = "This represents the collection of DiagnosticAccessPermissions that allow for the execution of the referencing DiagnosticServiceInstance.."
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
