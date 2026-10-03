"""Reader tests for EthernetPriorityRegeneration (Table 3.74, p.128)."""

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology import (
    EthernetPriorityRegeneration,
)
from tests.test_armodel.parser._helpers import _snip


class TestEthernetPriorityRegenerationReader:
    """readEthernetPriorityRegeneration (Table 3.74, p.128)."""

    def _obj(self):
        return EthernetPriorityRegeneration(None, "placeholder")

    def test_reads_attribute_values(self, parser):
        obj = self._obj()
        element = _snip(
            "<SHORT-NAME>regen1</SHORT-NAME>" "<INGRESS-PRIORITY>3</INGRESS-PRIORITY>" "<REGENERATED-PRIORITY>7</REGENERATED-PRIORITY>",
            root_tag="ETHERNET-PRIORITY-REGENERATION",
        )
        parser.readEthernetPriorityRegeneration(element, obj)
        assert obj.getIngressPriority().getValue() == 3
        assert obj.getRegeneratedPriority().getValue() == 7

    def test_read_preserves_arobject_checksum_and_timestamp(self, parser):
        obj = self._obj()
        element = _snip(
            "<SHORT-NAME>regen1</SHORT-NAME>" "<INGRESS-PRIORITY>3</INGRESS-PRIORITY>" "<REGENERATED-PRIORITY>7</REGENERATED-PRIORITY>",
            root_tag="ETHERNET-PRIORITY-REGENERATION",
        )
        element.attrib["S"] = "0x1"
        element.attrib["T"] = "2024-01-01T00:00:00Z"
        parser.readEthernetPriorityRegeneration(element, obj)
        assert obj.getChecksum() is not None
        assert obj.getChecksum().getValue() == "0x1"
        assert obj.getTimestamp() is not None
        assert obj.getTimestamp().getValue() == "2024-01-01T00:00:00Z"

    def test_read_absent_optional_fields(self, parser):
        obj = self._obj()
        element = _snip("", root_tag="ETHERNET-PRIORITY-REGENERATION")
        parser.readEthernetPriorityRegeneration(element, obj)
        assert obj.getIngressPriority() is None
        assert obj.getRegeneratedPriority() is None
        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None

    def test_aggregator_preserves_short_name_and_values(self, parser):
        from armodel.models import CouplingPortDetails

        details = CouplingPortDetails()
        element = _snip(
            "<ETHERNET-PRIORITY-REGENERATIONS>"
            "<ETHERNET-PRIORITY-REGENERATION>"
            "<SHORT-NAME>regen1</SHORT-NAME>"
            "<INGRESS-PRIORITY>1</INGRESS-PRIORITY>"
            "<REGENERATED-PRIORITY>2</REGENERATED-PRIORITY>"
            "</ETHERNET-PRIORITY-REGENERATION>"
            "</ETHERNET-PRIORITY-REGENERATIONS>"
        )
        parser.readCouplingPortDetailsEthernetPriorityRegenerations(element, details)
        regens = details.getEthernetPriorityRegenerations()
        assert len(regens) == 1
        assert regens[0].getShortName() == "regen1"
        assert regens[0].getIngressPriority().getValue() == 1
        assert regens[0].getRegeneratedPriority().getValue() == 2
