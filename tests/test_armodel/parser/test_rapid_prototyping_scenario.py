"""Reader tests for RapidPrototypingScenario (Swc TPS Table 14.1, p.846).

readRapidPrototypingScenario reads the RAPID-PROTOTYPING-SCENARIO group
(AUTOSAR_00052.xsd l.95550) in sequenceOffset order — HOST-SYSTEM-REF,
RPT-CONTAINERS (unbounded RPT-CONTAINER), RPT-PROFILES (unbounded RPT-PROFILE),
RPT-SYSTEM-REF — and calls readIdentifiable exactly once for the inherited
Identifiable level (SHORT-NAME-FRAGMENTS, CATEGORY, UUID, ..., Rule 0025).
NOT VP-capable (Rule 0020: the group declares no VARIATION-POINT; the anchor
for RapidPrototypingScenario.rptContainer lives on RptContainer). The class is
aggregated by ARPackage.element, so the ELEMENTS dispatch branch and the
createRapidPrototypingScenario factory are covered here too.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import RapidPrototypingScenario
from tests.test_armodel.parser._helpers import _snip

FULL_SCENARIO = (
    '<RAPID-PROTOTYPING-SCENARIO S="1234" T="2024-01-01T00:00:00Z">'
    "<SHORT-NAME-FRAGMENTS>"
    "<SHORT-NAME-FRAGMENT>"
    "<FRAGMENT>Scenario1</FRAGMENT>"
    "</SHORT-NAME-FRAGMENT>"
    "</SHORT-NAME-FRAGMENTS>"
    "<CATEGORY>WHATEVER</CATEGORY>"
    '<HOST-SYSTEM-REF DEST="SYSTEM">/System/HostSystem</HOST-SYSTEM-REF>'
    "<RPT-CONTAINERS>"
    "<RPT-CONTAINER>"
    "<SHORT-NAME>Top1</SHORT-NAME>"
    "<RPT-HOOKS>"
    "<RPT-HOOK>"
    "<CODE-LABEL>RptHookFunc</CODE-LABEL>"
    "</RPT-HOOK>"
    "</RPT-HOOKS>"
    "</RPT-CONTAINER>"
    "</RPT-CONTAINERS>"
    "<RPT-PROFILES>"
    "<RPT-PROFILE>"
    "<SHORT-NAME>Profile1</SHORT-NAME>"
    "<MAX-SERVICE-POINT-ID>10</MAX-SERVICE-POINT-ID>"
    "<MIN-SERVICE-POINT-ID>1</MIN-SERVICE-POINT-ID>"
    "<STIM-ENABLER>RPT-ENABLER-RAM</STIM-ENABLER>"
    "</RPT-PROFILE>"
    "</RPT-PROFILES>"
    '<RPT-SYSTEM-REF DEST="SYSTEM">/System/RptSystem</RPT-SYSTEM-REF>'
    "</RAPID-PROTOTYPING-SCENARIO>"
)

EMPTY_WRAPPERS_SCENARIO = "<RAPID-PROTOTYPING-SCENARIO>" "<SHORT-NAME>Scenario1</SHORT-NAME>" "<RPT-CONTAINERS/>" "<RPT-PROFILES/>" "</RAPID-PROTOTYPING-SCENARIO>"

BARE_SCENARIO = "<RAPID-PROTOTYPING-SCENARIO/>"


def _read_scenario(parser, xml):
    root = _snip(xml, root_tag="ROOT")
    scenario = RapidPrototypingScenario(None, "Scenario1")
    parser.readRapidPrototypingScenario(root[0], scenario)
    return scenario


class TestReadRapidPrototypingScenario:
    def test_read_full_field_values(self, parser):
        scenario = _read_scenario(parser, FULL_SCENARIO)

        host_ref = scenario.getHostSystemRef()
        assert host_ref is not None
        assert host_ref.getValue() == "/System/HostSystem"
        assert host_ref.getDest() == "SYSTEM"

        containers = scenario.getRptContainers()
        assert len(containers) == 1
        assert containers[0].getShortName() == "Top1"
        assert containers[0].getParent() is scenario
        assert containers[0].getRptHook().getCodeLabel().getValue() == "RptHookFunc"

        profiles = scenario.getRptProfiles()
        assert len(profiles) == 1
        assert profiles[0].getShortName() == "Profile1"
        assert profiles[0].getMaxServicePointId().getValue() == 10
        assert profiles[0].getMinServicePointId().getValue() == 1
        assert profiles[0].getStimEnabler().getValue() == "RPT-ENABLER-RAM"

        rpt_ref = scenario.getRptSystemRef()
        assert rpt_ref is not None
        assert rpt_ref.getValue() == "/System/RptSystem"
        assert rpt_ref.getDest() == "SYSTEM"

    def test_read_identifiable_level_attributes_exactly_once(self, parser):
        """UUID, SHORT-NAME-FRAGMENTS, CATEGORY and S/T (Identifiable level) round-trip via the readIdentifiable base helper (Rule 0025)."""
        scenario = _read_scenario(parser, FULL_SCENARIO)

        assert scenario.getChecksum().getValue() == "1234"
        assert scenario.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        assert [fragment.getFragment().getValue() for fragment in scenario.getShortNameFragments()] == ["Scenario1"]
        assert scenario.getCategory().getValue() == "WHATEVER"

    def test_read_empty_wrappers(self, parser):
        scenario = _read_scenario(parser, EMPTY_WRAPPERS_SCENARIO)

        assert scenario.getHostSystemRef() is None
        assert scenario.getRptContainers() == []
        assert scenario.getRptProfiles() == []
        assert scenario.getRptSystemRef() is None

    def test_read_bare_element(self, parser):
        scenario = _read_scenario(parser, BARE_SCENARIO)

        assert scenario.getHostSystemRef() is None
        assert scenario.getRptContainers() == []
        assert scenario.getRptProfiles() == []
        assert scenario.getRptSystemRef() is None

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a RAPID-PROTOTYPING-SCENARIO into getRapidPrototypingScenarios()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = """<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <RAPID-PROTOTYPING-SCENARIO>
                    <SHORT-NAME>Scenario1</SHORT-NAME>
                    <HOST-SYSTEM-REF DEST="SYSTEM">/System/HostSystem</HOST-SYSTEM-REF>
                    <RPT-PROFILES>
                        <RPT-PROFILE>
                            <SHORT-NAME>Profile1</SHORT-NAME>
                            <STIM-ENABLER>RPT-ENABLER-RAM</STIM-ENABLER>
                        </RPT-PROFILE>
                    </RPT-PROFILES>
                </RAPID-PROTOTYPING-SCENARIO>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            scenarios = document.getARPackages()[0].getRapidPrototypingScenarios()
            assert len(scenarios) == 1
            assert isinstance(scenarios[0], RapidPrototypingScenario)
            assert scenarios[0].getShortName() == "Scenario1"
            assert scenarios[0].getHostSystemRef().getValue() == "/System/HostSystem"
            assert scenarios[0].getRptProfiles()[0].getStimEnabler().getValue() == "RPT-ENABLER-RAM"
        finally:
            os.remove(file_path)
