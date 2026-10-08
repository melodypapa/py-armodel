from armodel.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import FlexrayNmScheduleVariant


class Test_FlexrayNmScheduleVariant:
    def test_members(self):
        # spec literals per Table 6.310, p.680 (scheduleVariant1-7, idx 0-6); values = XSD
        # FLEXRAY-NM-SCHEDULE-VARIANT--SIMPLE facets
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1 == "SCHEDULE-VARIANT-1"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2 == "SCHEDULE-VARIANT-2"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_3 == "SCHEDULE-VARIANT-3"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4 == "SCHEDULE-VARIANT-4"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_5 == "SCHEDULE-VARIANT-5"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_6 == "SCHEDULE-VARIANT-6"
        assert FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7 == "SCHEDULE-VARIANT-7"

    def test_literal_order(self):
        # XSD facet order (= displayed order = EnumerationLiteralIndex 0-6)
        e = FlexrayNmScheduleVariant()
        assert e.getEnumValues() == [
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_2,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_3,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_5,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_6,
            FlexrayNmScheduleVariant.SCHEDULE_VARIANT_7,
        ]

    def test_instantiation_and_set_value(self):
        e = FlexrayNmScheduleVariant()
        assert e.setValue(FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4) is e
        assert e.getValue() == FlexrayNmScheduleVariant.SCHEDULE_VARIANT_4
        e.setValue(FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1)
        assert e.getValue() == FlexrayNmScheduleVariant.SCHEDULE_VARIANT_1

    def test_docstring_is_spec_note_verbatim(self):
        note = "FrNm schedule variant according to FrNm SWS."
        assert FlexrayNmScheduleVariant.__doc__.strip() == note
