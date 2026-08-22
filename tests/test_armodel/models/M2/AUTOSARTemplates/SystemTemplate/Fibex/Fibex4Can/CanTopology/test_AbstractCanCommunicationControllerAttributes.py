from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Can.CanTopology import (
    AbstractCanCommunicationControllerAttributes,
    CanControllerConfigurationRequirements,
    CanControllerFdConfiguration,
    CanControllerFdConfigurationRequirements,
    CanControllerXlConfiguration,
    CanControllerXlConfigurationRequirements,
)


class TestAbstractCanCommunicationControllerAttributes:
    """Tests for AbstractCanCommunicationControllerAttributes (Table 3.13, R23-11)."""

    def _make(self) -> CanControllerConfigurationRequirements:
        return CanControllerConfigurationRequirements()

    def test_initialization(self):
        attributes = self._make()
        assert isinstance(attributes, AbstractCanCommunicationControllerAttributes)
        assert attributes.getCanControllerFdAttributes() is None
        assert attributes.getCanControllerFdRequirements() is None
        assert attributes.getCanControllerXlAttributes() is None
        assert attributes.getCanControllerXlRequirements() is None

    def test_get_set_canControllerFdAttributes(self):
        attributes = self._make()
        value = CanControllerFdConfiguration()
        result = attributes.setCanControllerFdAttributes(value)
        assert attributes.getCanControllerFdAttributes() is value
        assert result == attributes
        assert attributes.setCanControllerFdAttributes(None) == attributes
        assert attributes.getCanControllerFdAttributes() is value

    def test_get_set_canControllerFdRequirements(self):
        attributes = self._make()
        value = CanControllerFdConfigurationRequirements()
        result = attributes.setCanControllerFdRequirements(value)
        assert attributes.getCanControllerFdRequirements() is value
        assert result == attributes
        assert attributes.setCanControllerFdRequirements(None) == attributes
        assert attributes.getCanControllerFdRequirements() is value

    def test_get_set_canControllerXlAttributes(self):
        attributes = self._make()
        value = CanControllerXlConfiguration()
        result = attributes.setCanControllerXlAttributes(value)
        assert attributes.getCanControllerXlAttributes() is value
        assert result == attributes
        assert attributes.setCanControllerXlAttributes(None) == attributes
        assert attributes.getCanControllerXlAttributes() is value

    def test_get_set_canControllerXlRequirements(self):
        attributes = self._make()
        value = CanControllerXlConfigurationRequirements()
        result = attributes.setCanControllerXlRequirements(value)
        assert attributes.getCanControllerXlRequirements() is value
        assert result == attributes
        assert attributes.setCanControllerXlRequirements(None) == attributes
        assert attributes.getCanControllerXlRequirements() is value
