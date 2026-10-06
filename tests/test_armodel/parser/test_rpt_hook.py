"""Reader tests for RptHook (Swc TPS Table 14.3, p.848).

readRptHook reads the RPT-HOOK group (AUTOSAR_00052.xsd l.100040) in
sequenceOffset order — CODE-LABEL, MCD-IDENTIFIER, RPT-AR-HOOK-IREF (an
AnyInstanceRef iref), SDGS wrapper (unbounded SDG), VARIATION-POINT last
(sequenceOffset 10000, Applicable for RptContainer.rptHook, Rule 0020) —
and calls readARObject exactly once for the inherited S/T attributes
(Rule 0025). RptHook is aggregated by RptContainer.rptHook; the RptContainer
dispatch is that class's own queued sync, so the helper is exercised directly.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptHook
from tests.test_armodel.parser._helpers import _snip

FULL_RPT_HOOK = (
    '<RPT-HOOK S="1234" T="2024-01-01T00:00:00Z">'
    "<CODE-LABEL>RptHookFunc</CODE-LABEL>"
    "<MCD-IDENTIFIER>McdHook</MCD-IDENTIFIER>"
    "<RPT-AR-HOOK-IREF>"
    '<CONTEXT-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/Data1</CONTEXT-ELEMENT-REF>'
    '<TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/Data2</TARGET-REF>'
    "</RPT-AR-HOOK-IREF>"
    "<SDGS>"
    '<SDG GID="toolData">'
    '<SD GID="key1">value1</SD>'
    "</SDG>"
    "</SDGS>"
    "<VARIATION-POINT>"
    "<SHORT-LABEL>VP1</SHORT-LABEL>"
    "</VARIATION-POINT>"
    "</RPT-HOOK>"
)

EMPTY_WRAPPERS_RPT_HOOK = "<RPT-HOOK>" "<CODE-LABEL>RptHookFunc</CODE-LABEL>" "<SDGS/>" "</RPT-HOOK>"

BARE_RPT_HOOK = "<RPT-HOOK/>"


def _read_rpt_hook(parser, xml):
    root = _snip(xml, root_tag="ROOT")
    hook = RptHook()
    parser.readRptHook(root[0], hook)
    return hook


class TestReadRptHook:
    def test_read_full_field_values(self, parser):
        hook = _read_rpt_hook(parser, FULL_RPT_HOOK)

        assert hook.getCodeLabel().getValue() == "RptHookFunc"
        assert hook.getMcdIdentifier().getValue() == "McdHook"

        iref = hook.getRptArHookIRef()
        assert iref is not None
        assert [ref.getValue() for ref in iref.getContextElementRefs()] == ["/comp/Swc1/Data1"]
        assert iref.getTargetRef().getValue() == "/comp/Swc1/Data2"

        sdgs = hook.getSdgs()
        assert len(sdgs) == 1
        assert sdgs[0].getGID().getValue() == "toolData"
        assert sdgs[0].getSdgContentsType().getSds()[0].getValue().getValue() == "value1"

        assert hook.getVariationPoint() is not None
        assert hook.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_inherited_ar_object_attributes_exactly_once(self, parser):
        """S/T (ARObject level) round-trip via the readARObject base helper (Rule 0025)."""
        hook = _read_rpt_hook(parser, FULL_RPT_HOOK)

        assert hook.getChecksum().getValue() == "1234"
        assert hook.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_read_empty_wrappers(self, parser):
        hook = _read_rpt_hook(parser, EMPTY_WRAPPERS_RPT_HOOK)

        assert hook.getCodeLabel().getValue() == "RptHookFunc"
        assert hook.getSdgs() == []
        assert hook.getVariationPoint() is None

    def test_read_bare_element(self, parser):
        hook = _read_rpt_hook(parser, BARE_RPT_HOOK)

        assert hook.getCodeLabel() is None
        assert hook.getMcdIdentifier() is None
        assert hook.getRptArHookIRef() is None
        assert hook.getSdgs() == []
        assert hook.getVariationPoint() is None
