"""
Tests for reading END-TO-END-PROFILE elements — EndToEndDescription, Table 4.95 (p.206, R23-11).

EndToEndDescription (Base = ARObject) carries ten own attributes in XSD group order
(AUTOSAR_00052.xsd group END-TO-END-DESCRIPTION): CATEGORY, DATA-IDS (wrapper of DATA-ID
items), DATA-ID-MODE, DATA-LENGTH, MAX-DELTA-COUNTER-INIT, CRC-OFFSET, COUNTER-OFFSET,
MAX-NO-NEW-OR-REPEATED-DATA, SYNC-COUNTER-INIT, DATA-ID-NIBBLE-OFFSET. It is aggregated by
EndToEndProtection.endToEndProfile and read through readEndToEndProtection →
getEndToEndDescription.

Round-trip counterpart: tests/test_armodel/writer/test_end_to_end_description.py
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import NameToken, PositiveInteger
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndDescription, EndToEndProtection, EndToEndProtectionSet
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _profile_element() -> str:
    return (
        "<END-TO-END-PROFILE>"
        "<CATEGORY>PROFILE1</CATEGORY>"
        "<DATA-IDS><DATA-ID>1</DATA-ID><DATA-ID>2</DATA-ID></DATA-IDS>"
        "<DATA-ID-MODE>1</DATA-ID-MODE>"
        "<DATA-LENGTH>120</DATA-LENGTH>"
        "<MAX-DELTA-COUNTER-INIT>2</MAX-DELTA-COUNTER-INIT>"
        "<CRC-OFFSET>0</CRC-OFFSET>"
        "<COUNTER-OFFSET>8</COUNTER-OFFSET>"
        "<MAX-NO-NEW-OR-REPEATED-DATA>3</MAX-NO-NEW-OR-REPEATED-DATA>"
        "<SYNC-COUNTER-INIT>3</SYNC-COUNTER-INIT>"
        "<DATA-ID-NIBBLE-OFFSET>4</DATA-ID-NIBBLE-OFFSET>"
        "</END-TO-END-PROFILE>"
    )


class TestGetEndToEndDescription:
    """Tests for getEndToEndDescription — own element field values (Table 4.95)."""

    def test_own_element_field_values(self, parser):
        """Test that all ten attribute elements are read with their field values."""
        element = _snip(_profile_element(), root_tag="ROOT")

        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")

        assert desc is not None
        assert isinstance(desc, EndToEndDescription)
        assert isinstance(desc.getCategory(), NameToken)
        assert desc.getCategory().getValue() == "PROFILE1"
        data_ids = desc.getDataIds()
        assert len(data_ids) == 2
        assert all(isinstance(data_id, PositiveInteger) for data_id in data_ids)
        assert [data_id.getValue() for data_id in data_ids] == [1, 2]
        assert desc.getDataIdMode().getValue() == 1
        assert desc.getDataLength().getValue() == 120
        assert desc.getMaxDeltaCounterInit().getValue() == 2
        assert desc.getCrcOffset().getValue() == 0
        assert desc.getCounterOffset().getValue() == 8
        assert desc.getMaxNoNewOrRepeatedData().getValue() == 3
        assert desc.getSyncCounterInit().getValue() == 3
        assert desc.getDataIdNibbleOffset().getValue() == 4

    def test_empty_element(self, parser):
        """Test that an empty END-TO-END-PROFILE element yields an instance with all fields unset."""
        element = _snip("<END-TO-END-PROFILE></END-TO-END-PROFILE>", root_tag="ROOT")

        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")

        assert desc is not None
        assert desc.getCategory() is None
        assert desc.getDataIds() == []
        assert desc.getDataIdMode() is None
        assert desc.getDataLength() is None
        assert desc.getMaxDeltaCounterInit() is None
        assert desc.getCrcOffset() is None
        assert desc.getCounterOffset() is None
        assert desc.getMaxNoNewOrRepeatedData() is None
        assert desc.getSyncCounterInit() is None
        assert desc.getDataIdNibbleOffset() is None

    def test_absent_element_yields_none(self, parser):
        """Test that a missing END-TO-END-PROFILE element yields None."""
        element = _snip("<OTHER></OTHER>", root_tag="ROOT")

        assert parser.getEndToEndDescription(element, "END-TO-END-PROFILE") is None

    def test_ar_object_attributes_read(self, parser):
        """Test that the ARObject base attributes (S checksum, T timestamp) are read."""
        element = _snip(
            '<END-TO-END-PROFILE S="abc123" T="2024-01-01T12:00:00+00:00"></END-TO-END-PROFILE>',
            root_tag="ROOT",
        )

        desc = parser.getEndToEndDescription(element, "END-TO-END-PROFILE")

        assert desc is not None
        assert desc.getChecksum() is not None
        assert desc.getChecksum().getValue() == "abc123"
        assert desc.getTimestamp() is not None


class TestReadEndToEndProtectionDispatch:
    """Tests for the EndToEndProtection.endToEndProfile aggregation dispatch."""

    def test_dispatch_via_read_end_to_end_protection(self, parser):
        """Test that readEndToEndProtection reads the profile with field values, absent elements skipped."""
        protection_set = EndToEndProtectionSet(_autosar_root(), "Set")
        element = _snip(
            "<SHORT-NAME>e2e</SHORT-NAME>" + _profile_element(),
            root_tag="END-TO-END-PROTECTION",
        )

        parser.readEndToEndProtection(element, protection_set)

        protections = protection_set.getEndToEndProtections()
        assert len(protections) == 1
        protection = protections[0]
        assert isinstance(protection, EndToEndProtection)
        assert protection.getShortName() == "e2e"
        profile = protection.getEndToEndProfile()
        assert isinstance(profile, EndToEndDescription)
        assert profile.getCategory().getValue() == "PROFILE1"
        assert [data_id.getValue() for data_id in profile.getDataIds()] == [1, 2]
        assert profile.getDataIdMode().getValue() == 1
        assert profile.getMaxNoNewOrRepeatedData().getValue() == 3
        assert profile.getSyncCounterInit().getValue() == 3
        assert profile.getDataIdNibbleOffset().getValue() == 4

    def test_dispatch_absent_profile(self, parser):
        """Test that a protection without an END-TO-END-PROFILE keeps endToEndProfile None."""
        protection_set = EndToEndProtectionSet(_autosar_root(), "Set")
        element = _snip("<SHORT-NAME>e2e</SHORT-NAME>", root_tag="END-TO-END-PROTECTION")

        parser.readEndToEndProtection(element, protection_set)

        protection = protection_set.getEndToEndProtections()[0]
        assert protection.getEndToEndProfile() is None
