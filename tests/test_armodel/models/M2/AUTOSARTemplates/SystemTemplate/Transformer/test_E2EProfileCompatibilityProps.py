from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import E2EProfileCompatibilityProps


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestE2EProfileCompatibilityProps:
    """
    Model tests for E2EProfileCompatibilityProps (Table 4.93).
    """

    def test_initialization(self):
        parent = MockParent()
        props = E2EProfileCompatibilityProps(parent, "E2eCompatProps")

        assert isinstance(props, ARElement)
        assert isinstance(props, ARObject)
        assert props.getShortName() == "E2eCompatProps"
        assert props.getParent() is parent
        assert props.getTransitToInvalidExtended() is None

    def test_get_set_transit_to_invalid_extended(self):
        parent = MockParent()
        props = E2EProfileCompatibilityProps(parent, "E2eCompatProps")
        flag = Boolean().setValue("true")

        assert props == props.setTransitToInvalidExtended(None)
        assert props.getTransitToInvalidExtended() is None

        assert props == props.setTransitToInvalidExtended(flag)
        assert props.getTransitToInvalidExtended() == flag
        assert props.getTransitToInvalidExtended().getValue() is True

        assert props == props.setTransitToInvalidExtended(None)  # None no-op
        assert props.getTransitToInvalidExtended() == flag
        assert props.getTransitToInvalidExtended().getValue() is True
