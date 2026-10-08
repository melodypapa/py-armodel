import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import ComponentInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import J1939ControllerApplication


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestJ1939ControllerApplication:
    """Test cases for J1939ControllerApplication (Table 5.13, p.207)."""

    def test_inheritance(self):
        assert issubclass(J1939ControllerApplication, ARElement)

    def test_class_docstring_note(self):
        expected = (
            "This element represents a J1939 controller application. Tags: atp.recommendedPackage=J1939ControllerApplications\n"
            "\n"
            "[constr_5493] Existence of J1939ControllerApplication.functionId: For each J1939ControllerApplication, "
            "the attribute functionId shall exist at the time when the System Description is complete."
        )
        assert inspect.cleandoc(J1939ControllerApplication.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert J1939ControllerApplication.__init__.__doc__ is None

    def test_initialization(self):
        parent = MockParent()
        controller_application = J1939ControllerApplication(parent, "Ca1")
        assert controller_application.getShortName() == "Ca1"
        assert controller_application.getParent() is parent
        assert controller_application.getFunctionId() is None
        assert controller_application.getSwComponentPrototypeIRef() is None

    def test_get_set_function_id(self):
        parent = MockParent()
        controller_application = J1939ControllerApplication(parent, "Ca1")

        result = controller_application.setFunctionId(PositiveInteger().setValue("42"))
        assert result is controller_application
        assert controller_application.getFunctionId().getValue() == 42

        controller_application.setFunctionId(None)
        assert controller_application.getFunctionId().getValue() == 42

    def test_get_set_sw_component_prototype_i_ref(self):
        parent = MockParent()
        controller_application = J1939ControllerApplication(parent, "Ca1")

        iref = ComponentInSystemInstanceRef()
        target_ref = _ref("/Root/Composition/Swc1", "SW-COMPONENT-PROTOTYPE")
        iref.setTargetComponentRef(target_ref)
        result = controller_application.setSwComponentPrototypeIRef(iref)
        assert result is controller_application
        assert controller_application.getSwComponentPrototypeIRef() is iref
        assert controller_application.getSwComponentPrototypeIRef().getTargetComponentRef().getValue() == "/Root/Composition/Swc1"

        controller_application.setSwComponentPrototypeIRef(None)
        assert controller_application.getSwComponentPrototypeIRef() is iref

    def test_create_via_ar_package(self):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("J1939ControllerApplications")
        controller_application = pkg.createJ1939ControllerApplication("Ca1")
        assert isinstance(controller_application, J1939ControllerApplication)
        assert controller_application.getShortName() == "Ca1"
        duplicate = pkg.createJ1939ControllerApplication("Ca1")
        assert duplicate is controller_application

    def test_type_hints(self):
        hints = typing.get_type_hints(J1939ControllerApplication.setFunctionId)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is J1939ControllerApplication
        hints = typing.get_type_hints(J1939ControllerApplication.getFunctionId)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(J1939ControllerApplication.setSwComponentPrototypeIRef)
        assert hints.get("value") == typing.Optional[ComponentInSystemInstanceRef]
        assert hints.get("return") is J1939ControllerApplication
        hints = typing.get_type_hints(J1939ControllerApplication.getSwComponentPrototypeIRef)
        assert hints.get("return") == typing.Optional[ComponentInSystemInstanceRef]


def _ref(value: str, dest: str):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref
