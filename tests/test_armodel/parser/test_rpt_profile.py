"""Reader tests for RptProfile (Swc TPS Table 14.7, p.854).

readRptProfile reads the RPT-PROFILE group (AUTOSAR_00052.xsd l.100138) in
sequenceOffset order — MAX-SERVICE-POINT-ID, MIN-SERVICE-POINT-ID,
SERVICE-POINT-SYMBOL-POST, SERVICE-POINT-SYMBOL-PRE, STIM-ENABLER — and calls
readIdentifiable exactly once for the inherited Identifiable level
(SHORT-NAME-FRAGMENTS, CATEGORY, UUID, ..., Rule 0025). RptProfile is
aggregated by RapidPrototypingScenario.rptProfile; the
RapidPrototypingScenario dispatch is that class's own queued sync, so the
helper is exercised directly.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptProfile
from tests.test_armodel.parser._helpers import _snip

FULL_RPT_PROFILE = (
    '<RPT-PROFILE S="1234" T="2024-01-01T00:00:00Z">'
    "<SHORT-NAME-FRAGMENTS>"
    "<SHORT-NAME-FRAGMENT>"
    "<FRAGMENT>RptProfile1</FRAGMENT>"
    "</SHORT-NAME-FRAGMENT>"
    "</SHORT-NAME-FRAGMENTS>"
    "<CATEGORY>WHATEVER</CATEGORY>"
    "<MAX-SERVICE-POINT-ID>4</MAX-SERVICE-POINT-ID>"
    "<MIN-SERVICE-POINT-ID>2</MIN-SERVICE-POINT-ID>"
    "<SERVICE-POINT-SYMBOL-POST>Rpt_PostServicePoint</SERVICE-POINT-SYMBOL-POST>"
    "<SERVICE-POINT-SYMBOL-PRE>Rpt_PreServicePoint</SERVICE-POINT-SYMBOL-PRE>"
    "<STIM-ENABLER>RPT-ENABLER-RAM</STIM-ENABLER>"
    "</RPT-PROFILE>"
)

BARE_RPT_PROFILE = "<RPT-PROFILE/>"


def _read_rpt_profile(parser, xml):
    root = _snip(xml, root_tag="ROOT")
    profile = RptProfile(None, "RptProfile1")
    parser.readRptProfile(root[0], profile)
    return profile


class TestReadRptProfile:
    def test_read_full_field_values(self, parser):
        profile = _read_rpt_profile(parser, FULL_RPT_PROFILE)

        assert profile.getMaxServicePointId().getValue() == 4
        assert profile.getMinServicePointId().getValue() == 2
        assert profile.getServicePointSymbolPost().getValue() == "Rpt_PostServicePoint"
        assert profile.getServicePointSymbolPre().getValue() == "Rpt_PreServicePoint"
        assert profile.getStimEnabler().getValue() == "RPT-ENABLER-RAM"

    def test_read_identifiable_level_attributes_exactly_once(self, parser):
        """SHORT-NAME-FRAGMENTS, CATEGORY and S/T (Identifiable level) round-trip via the readIdentifiable base helper (Rule 0025)."""
        profile = _read_rpt_profile(parser, FULL_RPT_PROFILE)

        assert profile.getChecksum().getValue() == "1234"
        assert profile.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert [fragment.getFragment().getValue() for fragment in profile.getShortNameFragments()] == ["RptProfile1"]
        assert profile.getCategory().getValue() == "WHATEVER"

    def test_read_bare_element(self, parser):
        profile = _read_rpt_profile(parser, BARE_RPT_PROFILE)

        assert profile.getMaxServicePointId() is None
        assert profile.getMinServicePointId() is None
        assert profile.getServicePointSymbolPost() is None
        assert profile.getServicePointSymbolPre() is None
        assert profile.getStimEnabler() is None
