import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationControllerAttributes,
    CanControllerConfiguration,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)

CLASS_NOTE = "For the configuration of the CanController parameters two different approaches can be used: 1. Providing exact values which are taken by the ECU developer (CanControllerConfiguration). 2. Providing ranges of values which are taken as requirements and have to be respected by the ECU developer (CanControllerConfigurationRequirements)."
CAN_CONTROLLER_FD_ATTRIBUTES_NOTE = "Bit timing related configuration of a CAN controller for payload and CRC of a CanFD frame. If this element exists the controller supports CanFD frames and the ECU developer shall take these values for the configuration of the CanFD controller."
CAN_CONTROLLER_FD_REQUIREMENTS_NOTE = "Additional CanFD ranges of the bit timing related configuration of a CanFD controller. If this element exists the controller supports CanFD frames and the ECU developer shall take these ranges as requirements for the configuration of the CanFD controller."
CAN_CONTROLLER_XL_ATTRIBUTES_NOTE = "Bit timing related configuration of a CAN controller for payload and CRC of a CanXL frame. If this element exists the controller supports CanXL frames and the ECU developer shall take these values for the configuration of the CanXL controller."
CAN_CONTROLLER_XL_REQUIREMENTS_NOTE = "Additional CanXL ranges of the bit timing related configuration of a CanXL controller. If this element exists the controller supports CanXL frames and the ECU developer shall take these ranges as requirements for the configuration of the CanXL controller."


class TestAbstractCanCommunicationControllerAttributes:
    """Tests for AbstractCanCommunicationControllerAttributes (Table 3.13, R23-11)."""

    def _make(self) -> CanControllerConfigurationRequirements:
        return CanControllerConfigurationRequirements()

    def test_instantiation_is_abstract(self):
        """Test that the abstract class cannot be instantiated directly (Table 3.13 marks it abstract)"""
        with pytest.raises(TypeError):
            AbstractCanCommunicationControllerAttributes()

    def test_initialization(self):
        """Test that all __init__ fields default to None via a concrete subclass"""
        attributes = self._make()

        assert isinstance(attributes, ARObject)
        assert isinstance(attributes, AbstractCanCommunicationControllerAttributes)
        assert attributes.getCanControllerFdAttributes() is None
        assert attributes.getCanControllerFdRequirements() is None
        assert attributes.getCanControllerXlAttributes() is None
        assert attributes.getCanControllerXlRequirements() is None

    def test_subclasses_inherit_attributes(self):
        """Test that both concrete subclasses expose the inherited aggregate attributes"""
        configuration = CanControllerConfiguration()
        requirements = CanControllerConfigurationRequirements()

        assert isinstance(configuration, AbstractCanCommunicationControllerAttributes)
        assert isinstance(requirements, AbstractCanCommunicationControllerAttributes)
        assert configuration.getCanControllerFdAttributes() is None
        assert configuration.getCanControllerFdRequirements() is None
        assert configuration.getCanControllerXlAttributes() is None
        assert configuration.getCanControllerXlRequirements() is None
        assert requirements.getCanControllerFdAttributes() is None
        assert requirements.getCanControllerFdRequirements() is None
        assert requirements.getCanControllerXlAttributes() is None
        assert requirements.getCanControllerXlRequirements() is None

    def test_class_docstring_is_spec_note(self):
        """Test that the class docstring carries the spec Note verbatim (Table 3.13)"""
        assert inspect.cleandoc(AbstractCanCommunicationControllerAttributes.__doc__).strip() == CLASS_NOTE

    def test_init_has_no_docstring(self):
        """Test that __init__ carries no docstring"""
        assert AbstractCanCommunicationControllerAttributes.__init__.__doc__ is None

    def test_member_order_matches_spec(self):
        """Test member declaration order follows the R23-11 displayed row order (Table 3.13)"""
        source = inspect.getsource(AbstractCanCommunicationControllerAttributes.__init__)
        assert source.index("self.canControllerFdAttributes") < source.index("self.canControllerFdRequirements")
        assert source.index("self.canControllerFdRequirements") < source.index("self.canControllerXlAttributes")
        assert source.index("self.canControllerXlAttributes") < source.index("self.canControllerXlRequirements")

    def _assert_docstring(self, method, note, attr_name=None):
        doc = method.__doc__
        expected = note if attr_name is None else note + "\nA None value is a no-op and does not overwrite an existing %s." % attr_name
        assert doc is not None
        assert inspect.cleandoc(doc).strip() == expected

    def test_get_set_can_controller_fd_attributes(self):
        """Test canControllerFdAttributes default, guarded set chaining, None no-op and typing"""
        attributes = self._make()

        assert attributes.getCanControllerFdAttributes() is None

        value = CanControllerFdConfiguration()
        assert attributes == attributes.setCanControllerFdAttributes(value)
        assert attributes.getCanControllerFdAttributes() is value

        assert attributes == attributes.setCanControllerFdAttributes(None)
        assert attributes.getCanControllerFdAttributes() is value

        getter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.getCanControllerFdAttributes)
        assert getter_hints.get("return") == typing.Optional[CanControllerFdConfiguration]

        setter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.setCanControllerFdAttributes)
        assert setter_hints.get("value") == typing.Optional[CanControllerFdConfiguration]
        assert setter_hints.get("return") is AbstractCanCommunicationControllerAttributes

    def test_can_controller_fd_attributes_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.13)"""
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.getCanControllerFdAttributes, CAN_CONTROLLER_FD_ATTRIBUTES_NOTE)
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.setCanControllerFdAttributes, CAN_CONTROLLER_FD_ATTRIBUTES_NOTE, "canControllerFdAttributes")

    def test_get_set_can_controller_fd_requirements(self):
        """Test canControllerFdRequirements default, guarded set chaining, None no-op and typing"""
        attributes = self._make()

        assert attributes.getCanControllerFdRequirements() is None

        value = CanControllerFdConfigurationRequirements()
        assert attributes == attributes.setCanControllerFdRequirements(value)
        assert attributes.getCanControllerFdRequirements() is value

        assert attributes == attributes.setCanControllerFdRequirements(None)
        assert attributes.getCanControllerFdRequirements() is value

        getter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.getCanControllerFdRequirements)
        assert getter_hints.get("return") == typing.Optional[CanControllerFdConfigurationRequirements]

        setter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.setCanControllerFdRequirements)
        assert setter_hints.get("value") == typing.Optional[CanControllerFdConfigurationRequirements]
        assert setter_hints.get("return") is AbstractCanCommunicationControllerAttributes

    def test_can_controller_fd_requirements_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.13)"""
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.getCanControllerFdRequirements, CAN_CONTROLLER_FD_REQUIREMENTS_NOTE)
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.setCanControllerFdRequirements, CAN_CONTROLLER_FD_REQUIREMENTS_NOTE, "canControllerFdRequirements")

    def test_get_set_can_controller_xl_attributes(self):
        """Test canControllerXlAttributes default, guarded set chaining, None no-op and typing"""
        attributes = self._make()

        assert attributes.getCanControllerXlAttributes() is None

        value = CanControllerXlConfiguration()
        assert attributes == attributes.setCanControllerXlAttributes(value)
        assert attributes.getCanControllerXlAttributes() is value

        assert attributes == attributes.setCanControllerXlAttributes(None)
        assert attributes.getCanControllerXlAttributes() is value

        getter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.getCanControllerXlAttributes)
        assert getter_hints.get("return") == typing.Optional[CanControllerXlConfiguration]

        setter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.setCanControllerXlAttributes)
        assert setter_hints.get("value") == typing.Optional[CanControllerXlConfiguration]
        assert setter_hints.get("return") is AbstractCanCommunicationControllerAttributes

    def test_can_controller_xl_attributes_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.13)"""
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.getCanControllerXlAttributes, CAN_CONTROLLER_XL_ATTRIBUTES_NOTE)
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.setCanControllerXlAttributes, CAN_CONTROLLER_XL_ATTRIBUTES_NOTE, "canControllerXlAttributes")

    def test_get_set_can_controller_xl_requirements(self):
        """Test canControllerXlRequirements default, guarded set chaining, None no-op and typing"""
        attributes = self._make()

        assert attributes.getCanControllerXlRequirements() is None

        value = CanControllerXlConfigurationRequirements()
        assert attributes == attributes.setCanControllerXlRequirements(value)
        assert attributes.getCanControllerXlRequirements() is value

        assert attributes == attributes.setCanControllerXlRequirements(None)
        assert attributes.getCanControllerXlRequirements() is value

        getter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.getCanControllerXlRequirements)
        assert getter_hints.get("return") == typing.Optional[CanControllerXlConfigurationRequirements]

        setter_hints = typing.get_type_hints(AbstractCanCommunicationControllerAttributes.setCanControllerXlRequirements)
        assert setter_hints.get("value") == typing.Optional[CanControllerXlConfigurationRequirements]
        assert setter_hints.get("return") is AbstractCanCommunicationControllerAttributes

    def test_can_controller_xl_requirements_docstrings_are_spec_note(self):
        """Test getter/setter docstrings carry the spec Note verbatim (Table 3.13)"""
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.getCanControllerXlRequirements, CAN_CONTROLLER_XL_REQUIREMENTS_NOTE)
        self._assert_docstring(AbstractCanCommunicationControllerAttributes.setCanControllerXlRequirements, CAN_CONTROLLER_XL_REQUIREMENTS_NOTE, "canControllerXlRequirements")
