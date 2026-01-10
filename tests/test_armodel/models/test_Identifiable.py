import pytest

from src.armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement, Referrable


class MockReferrable1(Referrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class MockReferrable2(Referrable):
    def __init__(self, parent, short_name):
        super().__init__(parent, short_name)


class MockCollectableElement(CollectableElement):
    def __init__(self):
        super().__init__()


class TestCollectableElement:

    def setup_method(self):
        '''
            CollectableElement instance for testing.
        '''
        self.collectable_element = MockCollectableElement()
        self.mock_referrable1 = MockReferrable1(None, "referrable")
        self.mock_referrable2 = MockReferrable2(None, "referrable")

    def test_getTotalElement(self):
        assert self.collectable_element.getTotalElement() == 0
        self.collectable_element.addElement(self.mock_referrable1)
        assert self.collectable_element.getTotalElement() == 1

    def test_addElement(self):
        self.collectable_element.addElement(self.mock_referrable1)
        assert self.collectable_element.getTotalElement() == 1
        assert self.collectable_element.getElement("referrable", MockReferrable1) == self.mock_referrable1
        self.collectable_element.addElement(self.mock_referrable2)
        assert self.collectable_element.getTotalElement() == 2
        assert self.collectable_element.getElement("referrable", MockReferrable2) == self.mock_referrable2

    def test_removeElement(self):
        self.collectable_element.addElement(self.mock_referrable1)
        assert self.collectable_element.getTotalElement() == 1
        self.collectable_element.addElement(self.mock_referrable2)
        assert self.collectable_element.getTotalElement() == 2
        self.collectable_element.removeElement("referrable", MockReferrable2)
        assert self.collectable_element.getTotalElement() == 1
        self.collectable_element.removeElement("referrable", MockReferrable1)
        assert self.collectable_element.getTotalElement() == 0

    def test_removeElement_non_existent_key(self):
        self.collectable_element.addElement(self.mock_referrable1)
        assert self.collectable_element.getTotalElement() == 1
        try:
            self.collectable_element.removeElement("non_existent", MockReferrable1)
        except KeyError as ex:
            assert str(ex) == "'Invalid key <non_existent> for removing element'"
        assert self.collectable_element.getTotalElement() == 1

    def test_getElements(self):
        self.collectable_element.addElement(self.mock_referrable1)
        self.collectable_element.addElement(self.mock_referrable1)
        self.collectable_element.addElement(self.mock_referrable2)
        elements = list(self.collectable_element.getElements())
        assert len(elements) == 2
        assert elements[0] == self.mock_referrable1
        assert elements[1] == self.mock_referrable2

    def test_getElement(self):
        self.collectable_element.addElement(self.mock_referrable1)
        element = self.collectable_element.getElement("referrable", MockReferrable1)
        assert element == self.mock_referrable1
        assert self.collectable_element.getElement("referrable", MockReferrable2) is None
        assert self.collectable_element.getElement("non_existent", MockReferrable1) is None

    def test_IsElementExists(self):
        assert not self.collectable_element.IsElementExists("test_element")
        self.collectable_element.addElement(self.mock_referrable1)
        assert not self.collectable_element.IsElementExists("test_element")
        assert self.collectable_element.IsElementExists("referrable")
        assert self.collectable_element.IsElementExists("referrable", MockReferrable1)
        assert not self.collectable_element.IsElementExists("referrable", MockReferrable2)
