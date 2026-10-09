from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Integer
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NodeName


def _int(value):
    integer = Integer()
    integer.setValue(value)
    return integer


def _bool(value):
    boolean = Boolean()
    boolean.setValue(value)
    return boolean


class Test_J1939NodeName:
    def test_instantiation(self):
        # concrete class per XSD (J-1939-NODE-NAME abstract="false") — no TypeError guard
        node_name = J1939NodeName()
        assert node_name.getArbitraryAddressCapable() is None
        assert node_name.getEcuInstance() is None

    def test_get_set_arbitrary_address_capable(self):
        node_name = J1939NodeName()
        assert node_name.setArbitraryAddressCapable(_bool(True)) is node_name
        assert node_name.getArbitraryAddressCapable().getValue() is True
        node_name.setArbitraryAddressCapable(None)
        assert node_name.getArbitraryAddressCapable().getValue() is True

    def test_get_set_integer_fields(self):
        node_name = J1939NodeName()
        assert node_name.setEcuInstance(_int(3)) is node_name
        assert node_name.setFunction(_int(170)) is node_name
        assert node_name.setFunctionInstance(_int(1)) is node_name
        assert node_name.setIdentitiyNumber(_int(4660)) is node_name
        assert node_name.setIndustryGroup(_int(4)) is node_name
        assert node_name.setManufacturerCode(_int(221)) is node_name
        assert node_name.setVehicleSystem(_int(4)) is node_name
        assert node_name.setVehicleSystemInstance(_int(2)) is node_name
        assert node_name.getEcuInstance().getValue() == 3
        assert node_name.getFunction().getValue() == 170
        assert node_name.getFunctionInstance().getValue() == 1
        assert node_name.getIdentitiyNumber().getValue() == 4660
        assert node_name.getIndustryGroup().getValue() == 4
        assert node_name.getManufacturerCode().getValue() == 221
        assert node_name.getVehicleSystem().getValue() == 4
        assert node_name.getVehicleSystemInstance().getValue() == 2

    def test_docstrings_are_spec_notes_verbatim(self):
        # Table 6.321, p.692 (metadata block renders above the caption in the markdown)
        assert J1939NodeName.__doc__.strip() == "This element contains attributes to configure the J1939NmNode NAME."
        for getter, note in [
            (J1939NodeName.getArbitraryAddressCapable, "Arbitrary Address Capable field of the NAME of this node."),
            (J1939NodeName.getEcuInstance, "ECU Instance field of the NAME of this node."),
            (J1939NodeName.getFunction, "Function field of the NAME of this node."),
            (J1939NodeName.getFunctionInstance, "Function Instance field of the NAME of this node."),
            (J1939NodeName.getIdentitiyNumber, "Identity Number field of the NAME of this node."),
            (J1939NodeName.getIndustryGroup, "Industry Group field of the NAME of this node."),
            (J1939NodeName.getManufacturerCode, "Manufacturer Code field of the NAME of this node."),
            (J1939NodeName.getVehicleSystem, "Vehicle System field of the NAME of this node."),
            (J1939NodeName.getVehicleSystemInstance, "Vehicle System Instance field of the NAME of this node."),
        ]:
            assert getter.__doc__.strip() == note
