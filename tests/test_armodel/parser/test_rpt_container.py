"""Reader tests for RptContainer (Swc TPS Table 14.2, p.847).

readRptContainer reads the RPT-CONTAINER group (AUTOSAR_00052.xsd l.99633) in
sequenceOffset order — BY-PASS-POINT-IREFS (unbounded BY-PASS-POINT-IREF, an
AnyInstanceRef iref list), EXPLICIT-RPT-PROFILE-SELECTION-REFS (unbounded ref
list), RPT-CONTAINERS (recursive sub-container wrapper), RPT-EXECUTABLE-ENTITY-
PROPERTIES, RPT-HOOKS, RPT-IMPL-POLICY, RPT-SW-PROTOTYPING-ACCESS,
VARIATION-POINT last (sequenceOffset 10000, Applicable for
RptContainer.rptContainer, Rule 0020) — and calls readIdentifiable exactly once
for the inherited Identifiable level (SHORT-NAME-FRAGMENTS, CATEGORY, UUID, ...,
Rule 0025). The RapidPrototypingScenario.rptContainer dispatch is that class's
own queued sync, so the helper is exercised directly.
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RptContainer
from tests.test_armodel.parser._helpers import _snip

FULL_RPT_CONTAINER = (
    '<RPT-CONTAINER S="1234" T="2024-01-01T00:00:00Z">'
    "<SHORT-NAME-FRAGMENTS>"
    "<SHORT-NAME-FRAGMENT>"
    "<FRAGMENT>RptContainer1</FRAGMENT>"
    "</SHORT-NAME-FRAGMENT>"
    "</SHORT-NAME-FRAGMENTS>"
    "<CATEGORY>WHATEVER</CATEGORY>"
    "<BY-PASS-POINT-IREFS>"
    "<BY-PASS-POINT-IREF>"
    '<CONTEXT-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/Data1</CONTEXT-ELEMENT-REF>'
    '<TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/Data2</TARGET-REF>'
    "</BY-PASS-POINT-IREF>"
    "<BY-PASS-POINT-IREF>"
    '<TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/Data3</TARGET-REF>'
    "</BY-PASS-POINT-IREF>"
    "</BY-PASS-POINT-IREFS>"
    "<EXPLICIT-RPT-PROFILE-SELECTION-REFS>"
    '<EXPLICIT-RPT-PROFILE-SELECTION-REF DEST="RPT-PROFILE">/RptScenario/RptProfile1</EXPLICIT-RPT-PROFILE-SELECTION-REF>'
    '<EXPLICIT-RPT-PROFILE-SELECTION-REF DEST="RPT-PROFILE">/RptScenario/RptProfile2</EXPLICIT-RPT-PROFILE-SELECTION-REF>'
    "</EXPLICIT-RPT-PROFILE-SELECTION-REFS>"
    "<RPT-CONTAINERS>"
    "<RPT-CONTAINER>"
    "<SHORT-NAME>Sub1</SHORT-NAME>"
    "<BY-PASS-POINT-IREFS>"
    "<BY-PASS-POINT-IREF>"
    '<TARGET-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Swc1/SubData</TARGET-REF>'
    "</BY-PASS-POINT-IREF>"
    "</BY-PASS-POINT-IREFS>"
    "</RPT-CONTAINER>"
    "</RPT-CONTAINERS>"
    "<RPT-EXECUTABLE-ENTITY-PROPERTIES>"
    "<MAX-RPT-EVENT-ID>100</MAX-RPT-EVENT-ID>"
    "<MIN-RPT-EVENT-ID>1</MIN-RPT-EVENT-ID>"
    "</RPT-EXECUTABLE-ENTITY-PROPERTIES>"
    "<RPT-HOOKS>"
    "<RPT-HOOK>"
    "<CODE-LABEL>RptHookFunc</CODE-LABEL>"
    "</RPT-HOOK>"
    "</RPT-HOOKS>"
    "<RPT-IMPL-POLICY>"
    "<RPT-PREPARATION-LEVEL>RPT-LEVEL-2</RPT-PREPARATION-LEVEL>"
    "</RPT-IMPL-POLICY>"
    "<RPT-SW-PROTOTYPING-ACCESS>"
    "<RPT-READ-ACCESS>PROTECTED</RPT-READ-ACCESS>"
    "</RPT-SW-PROTOTYPING-ACCESS>"
    "<VARIATION-POINT>"
    "<SHORT-LABEL>VP1</SHORT-LABEL>"
    "</VARIATION-POINT>"
    "</RPT-CONTAINER>"
)

EMPTY_WRAPPERS_RPT_CONTAINER = "<RPT-CONTAINER>" "<SHORT-NAME>RptContainer1</SHORT-NAME>" "<BY-PASS-POINT-IREFS/>" "<RPT-HOOKS/>" "</RPT-CONTAINER>"

BARE_RPT_CONTAINER = "<RPT-CONTAINER/>"


def _read_rpt_container(parser, xml):
    root = _snip(xml, root_tag="ROOT")
    container = RptContainer(None, "RptContainer1")
    parser.readRptContainer(root[0], container)
    return container


class TestReadRptContainer:
    def test_read_full_field_values(self, parser):
        container = _read_rpt_container(parser, FULL_RPT_CONTAINER)

        irefs = container.getByPassPointIRefs()
        assert len(irefs) == 2
        assert [ref.getValue() for ref in irefs[0].getContextElementRefs()] == ["/comp/Swc1/Data1"]
        assert irefs[0].getTargetRef().getValue() == "/comp/Swc1/Data2"
        assert irefs[1].getTargetRef().getValue() == "/comp/Swc1/Data3"

        refs = container.getExplicitRptProfileSelectionRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/RptScenario/RptProfile1"
        assert refs[0].getDest() == "RPT-PROFILE"
        assert refs[1].getValue() == "/RptScenario/RptProfile2"

        sub_containers = container.getRptContainers()
        assert len(sub_containers) == 1
        assert sub_containers[0].getShortName() == "Sub1"
        assert sub_containers[0].getParent() is container
        sub_irefs = sub_containers[0].getByPassPointIRefs()
        assert len(sub_irefs) == 1
        assert sub_irefs[0].getTargetRef().getValue() == "/comp/Swc1/SubData"

        properties = container.getRptExecutableEntityProperties()
        assert properties is not None
        assert properties.getMaxRptEventId().getValue() == 100
        assert properties.getMinRptEventId().getValue() == 1

        hook = container.getRptHook()
        assert hook is not None
        assert hook.getCodeLabel().getValue() == "RptHookFunc"

        policy = container.getRptImplPolicy()
        assert policy is not None
        assert policy.getRptPreparationLevel().getValue() == "RPT-LEVEL-2"

        access = container.getRptSwPrototypingAccess()
        assert access is not None
        assert access.getRptReadAccess().getValue() == "PROTECTED"

        assert container.getVariationPoint() is not None
        assert container.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_identifiable_level_attributes_exactly_once(self, parser):
        """SHORT-NAME-FRAGMENTS, CATEGORY and S/T (Identifiable level) round-trip via the readIdentifiable base helper (Rule 0025)."""
        container = _read_rpt_container(parser, FULL_RPT_CONTAINER)

        assert container.getChecksum().getValue() == "1234"
        assert container.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert [fragment.getFragment().getValue() for fragment in container.getShortNameFragments()] == ["RptContainer1"]
        assert container.getCategory().getValue() == "WHATEVER"

    def test_read_empty_wrappers(self, parser):
        container = _read_rpt_container(parser, EMPTY_WRAPPERS_RPT_CONTAINER)

        assert container.getByPassPointIRefs() == []
        assert container.getExplicitRptProfileSelectionRefs() == []
        assert container.getRptContainers() == []
        assert container.getRptHook() is None

    def test_read_bare_element(self, parser):
        container = _read_rpt_container(parser, BARE_RPT_CONTAINER)

        assert container.getByPassPointIRefs() == []
        assert container.getExplicitRptProfileSelectionRefs() == []
        assert container.getRptContainers() == []
        assert container.getRptExecutableEntityProperties() is None
        assert container.getRptHook() is None
        assert container.getRptImplPolicy() is None
        assert container.getRptSwPrototypingAccess() is None
        assert container.getVariationPoint() is None
