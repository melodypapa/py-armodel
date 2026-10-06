"""Reader tests for EndToEndProtection (Swc TPS Table 4.97, p.215).

readEndToEndProtection populates the model via createEndToEndProtection +
setEndToEndProfile / addEndToEndProtectionISignalIPdu /
addEndToEndProtectionVariablePrototype, with VARIATION-POINT last per the XSD
group END-TO-END-PROTECTION (AUTOSAR_00052.xsd, sequenceOffset 10000).
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionVariablePrototype
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.EndToEndProtection import EndToEndProtectionISignalIPdu
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_protection_set():
    pkg = _autosar_root().createARPackage("Pkg")
    protection_set = pkg.createEndToEndProtectionSet("E2eSet")
    return protection_set


class TestEndToEndProtectionReader:
    def test_read_full_protection_field_values(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>FullProtection</SHORT-NAME>
            <END-TO-END-PROFILE>
                <CATEGORY>CATEGORY1</CATEGORY>
                <DATA-ID-MODE>1</DATA-ID-MODE>
                <DATA-LENGTH>64</DATA-LENGTH>
            </END-TO-END-PROFILE>
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
                <END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
                    <SHORT-NAME>Pdu1</SHORT-NAME>
                    <DATA-OFFSET>8</DATA-OFFSET>
                    <I-SIGNAL-GROUP-REF DEST="I-SIGNAL-GROUP">/isg/Group1</I-SIGNAL-GROUP-REF>
                    <I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/ipdu/Pdu1</I-SIGNAL-I-PDU-REF>
                </END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
            </END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
            <END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>
                <END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>
                    <SHORT-LABEL>SegA</SHORT-LABEL>
                    <SENDER-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/comp/Root</CONTEXT-COMPOSITION-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</TARGET-DATA-PROTOTYPE-REF>
                    </SENDER-IREF>
                </END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>
            </END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>
            <VARIATION-POINT>
                <SHORT-LABEL>VP1</SHORT-LABEL>
            </VARIATION-POINT>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protections = protection_set.getEndToEndProtections()
        assert len(protections) == 1
        protection = protections[0]
        assert protection.getShortName() == "FullProtection"
        assert protection.getEndToEndProfile() is not None
        assert protection.getEndToEndProfile().getCategory().getValue() == "CATEGORY1"
        assert protection.getEndToEndProfile().getDataIdMode().getValue() == 1
        assert protection.getEndToEndProfile().getDataLength().getValue() == 64
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 1
        assert isinstance(ipdus[0], EndToEndProtectionISignalIPdu)
        assert ipdus[0].getDataOffset().getValue() == 8
        assert ipdus[0].getISignalGroupRef().getValue() == "/isg/Group1"
        assert ipdus[0].getISignalIPduRef().getValue() == "/ipdu/Pdu1"
        prototypes = protection.getEndToEndProtectionVariablePrototypes()
        assert len(prototypes) == 1
        assert isinstance(prototypes[0], EndToEndProtectionVariablePrototype)
        assert prototypes[0].getShortLabel().getValue() == "SegA"
        assert prototypes[0].getSenderIref().getTargetDataPrototypeRef().getValue() == "/vdp/Var"
        assert protection.getVariationPoint() is not None
        assert protection.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_empty_wrappers(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>EmptyProtection</SHORT-NAME>
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS/>
            <END-TO-END-PROTECTION-VARIABLE-PROTOTYPES/>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protection = protection_set.getEndToEndProtections()[0]
        assert protection.getEndToEndProfile() is None
        assert protection.getEndToEndProtectionISignalIPdus() == []
        assert protection.getEndToEndProtectionVariablePrototypes() == []
        assert protection.getVariationPoint() is None

    def test_read_absent_wrappers(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>BareProtection</SHORT-NAME>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protection = protection_set.getEndToEndProtections()[0]
        assert protection.getEndToEndProfile() is None
        assert protection.getEndToEndProtectionISignalIPdus() == []
        assert protection.getEndToEndProtectionVariablePrototypes() == []
        assert protection.getVariationPoint() is None
