from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import J1939NmAddressConfigurationCapabilityEnum


class Test_J1939NmAddressConfigurationCapabilityEnum:
    def test_members(self):
        # spec literals per Table 6.322, p.692 (J1939NM_AAC/CCA/NCA/SCA/SVCA); values = exact
        # XSD J-1939-NM-ADDRESS-CONFIGURATION-CAPABILITY-ENUM--SIMPLE facets (double-hyphen
        # tokens reproduced verbatim per Rule 0011)
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC == "J-1939-NM--AAC"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_CCA == "J-1939-NM--CCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA == "J-1939-NM--NCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA == "J-1939-NM--SCA"
        assert J1939NmAddressConfigurationCapabilityEnum.J1939NM_SVCA == "J-1939-NM--SVCA"

    def test_literal_order(self):
        # XSD facet order (= displayed markdown order; ≠ EnumerationLiteralIndex 4/3/0/2/1)
        e = J1939NmAddressConfigurationCapabilityEnum()
        assert e.getEnumValues() == [
            J1939NmAddressConfigurationCapabilityEnum.J1939NM_AAC,
            J1939NmAddressConfigurationCapabilityEnum.J1939NM_CCA,
            J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA,
            J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA,
            J1939NmAddressConfigurationCapabilityEnum.J1939NM_SVCA,
        ]

    def test_instantiation_and_set_value(self):
        e = J1939NmAddressConfigurationCapabilityEnum()
        assert e.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA) is e
        assert e.getValue() == J1939NmAddressConfigurationCapabilityEnum.J1939NM_SCA
        e.setValue(J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA)
        assert e.getValue() == J1939NmAddressConfigurationCapabilityEnum.J1939NM_NCA

    def test_docstring_is_spec_note_verbatim(self):
        note = "Defines the Address Configuration Capability options for the J1939NmNode."
        assert J1939NmAddressConfigurationCapabilityEnum.__doc__.strip() == note
