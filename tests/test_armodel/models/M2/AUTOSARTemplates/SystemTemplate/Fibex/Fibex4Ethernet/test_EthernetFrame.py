import pytest

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import (
    AbstractEthernetFrame,
    GenericEthernetFrame
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import Frame
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class Test_Fibex4EthernetFrame:
    """Test cases for Fibex4Ethernet Frame classes."""
    
    def test_AbstractEthernetFrame(self):
        """Test AbstractEthernetFrame abstract class instantiation."""
        parent = MockParent()
        with pytest.raises(TypeError):
            AbstractEthernetFrame(parent, "test_abstract_eth_frame")

    def test_GenericEthernetFrame(self):
        """Test GenericEthernetFrame class functionality."""
        parent = MockParent()
        frame = GenericEthernetFrame(parent, "test_generic_eth_frame")

        assert isinstance(frame, Frame)
        assert isinstance(frame, AbstractEthernetFrame)