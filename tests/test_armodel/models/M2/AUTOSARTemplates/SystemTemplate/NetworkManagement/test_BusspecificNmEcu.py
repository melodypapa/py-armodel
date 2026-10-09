import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    BusspecificNmEcu,
    CanNmEcu,
    FlexrayNmEcu,
    J1939NmEcu,
    UdpNmEcu,
)


class _BareARObject(ARObject):
    pass


class TestBusspecificNmEcu:
    """
    Spec-driven tests for the abstract BusspecificNmEcu (Table 6.301, p.675).
    """

    def test_abstract(self):
        """
        BusspecificNmEcu is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            BusspecificNmEcu()

    def test_initialization(self):
        """
        A concrete subclass initializes with the ARObject base state only
        (Table 6.301 has zero attribute rows).
        """
        ecu = CanNmEcu()
        assert ecu is not None
        own_attributes = [name for name in vars(ecu) if name not in vars(_BareARObject())]
        assert own_attributes == []

    def test_subclasses_inherit_base(self):
        """
        Every spec subclass (CanNmEcu, FlexrayNmEcu, J1939NmEcu, UdpNmEcu)
        instantiates and is a BusspecificNmEcu and an ARObject.
        """
        for subclass in (CanNmEcu, FlexrayNmEcu, J1939NmEcu, UdpNmEcu):
            ecu = subclass()
            assert isinstance(ecu, BusspecificNmEcu)
            assert isinstance(ecu, ARObject)

    def test_class_docstring_is_spec_note(self):
        """
        The class docstring is the Table 6.301 Note verbatim.
        """
        assert BusspecificNmEcu.__doc__.strip() == "Busspecific NmEcu attributes."
