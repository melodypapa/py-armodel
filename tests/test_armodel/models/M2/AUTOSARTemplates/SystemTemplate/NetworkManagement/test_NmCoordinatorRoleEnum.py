from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import NmCoordinatorRoleEnum


class Test_NmCoordinatorRoleEnum:
    def test_members(self):
        # spec literals per Table 6.304, p.676 (Active idx0, Passive idx1); values = XSD
        # NM-COORDINATOR-ROLE-ENUM--SIMPLE facets
        assert NmCoordinatorRoleEnum.ACTIVE == "ACTIVE"
        assert NmCoordinatorRoleEnum.PASSIVE == "PASSIVE"

    def test_literal_order(self):
        # XSD facet order (= EnumerationLiteralIndex 0/1)
        e = NmCoordinatorRoleEnum()
        assert e.getEnumValues() == [
            NmCoordinatorRoleEnum.ACTIVE,
            NmCoordinatorRoleEnum.PASSIVE,
        ]

    def test_instantiation_and_set_value(self):
        e = NmCoordinatorRoleEnum()
        assert e.setValue(NmCoordinatorRoleEnum.PASSIVE) is e
        assert e.getValue() == NmCoordinatorRoleEnum.PASSIVE
        e.setValue(NmCoordinatorRoleEnum.ACTIVE)
        assert e.getValue() == NmCoordinatorRoleEnum.ACTIVE

    def test_docstring_is_spec_note_verbatim(self):
        note = "Supported NmCoordinator roles."
        assert NmCoordinatorRoleEnum.__doc__.strip() == note
