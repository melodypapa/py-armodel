"""Tests for End-to-End Protection (E2E) handler methods.

Consolidates:
- ``readEndToEndProtectionEndToEndProtectionISignalIPdus`` (L2814-2822)
- ``readEndToEndProtection`` (L2824-2831)
- ``readEndToEndProtections`` orchestrator

Shared fixtures (``parser``, ``warning_parser``, ``reset_autosar``) are provided
by ``conftest.py``; helper functions (``_snip``, ``_autosar_root``) live in
``_helpers.py``.
"""

import logging

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.EndToEndProtection import EndToEndProtectionVariablePrototype
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_protection():
    pkg = _autosar_root().createARPackage("Pkg")
    protection_set = pkg.createEndToEndProtectionSet("E2eSet")
    return protection_set.createEndToEndProtection("Protection")


def _make_protection_set():
    pkg = _autosar_root().createARPackage("Pkg")
    return pkg.createEndToEndProtectionSet("E2eSet")


class TestReadEndToEndProtectionISignalIPdus:
    """Tests for readEndToEndProtectionEndToEndProtectionISignalIPdus (L2814-2822)."""

    def test_reads_isignal_ipdu_main_branch(self, parser):
        protection = _make_protection()
        element = _snip(
            """
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
                <END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
                    <DATA-OFFSET>8</DATA-OFFSET>
                    <I-SIGNAL-GROUP-REF DEST="I-SIGNAL-GROUP">/isg/Group1</I-SIGNAL-GROUP-REF>
                    <I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/ipdu/Pdu1</I-SIGNAL-I-PDU-REF>
                </END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
            </END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
            """,
        )
        parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(element, protection)
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 1
        assert ipdus[0].getDataOffset().getValue() == 8
        assert ipdus[0].getISignalGroupRef() is not None
        assert ipdus[0].getISignalIPduRef() is not None

    def test_empty_container_returns_no_ipdus(self, parser):
        protection = _make_protection()
        element = _snip("")
        parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(element, protection)
        assert len(protection.getEndToEndProtectionISignalIPdus()) == 0

    def test_unknown_tag_logs_warning(self, warning_parser, caplog):
        protection = _make_protection()
        element = _snip(
            """
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
                <UNKNOWN-IPDU>
                    <SHORT-NAME>Unknown</SHORT-NAME>
                </UNKNOWN-IPDU>
            </END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
            """,
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(element, protection)
        assert any("Unsupported EndToEndProtectionISignalIPdu" in rec.getMessage() for rec in caplog.records)
        assert len(protection.getEndToEndProtectionISignalIPdus()) == 0


class TestReadEndToEndProtection:
    """Tests for readEndToEndProtection (L2824-2831)."""

    def test_full_handler_creates_protection_with_profile_and_ipdus(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>MyProtection</SHORT-NAME>
            <END-TO-END-PROFILE>
                <CATEGORY>CATEGORY1</CATEGORY>
                <DATA-ID-MODE>1</DATA-ID-MODE>
                <DATA-LENGTH>64</DATA-LENGTH>
                <MAX-DELTA-COUNTER-INIT>2</MAX-DELTA-COUNTER-INIT>
                <CRC-OFFSET>0</CRC-OFFSET>
                <COUNTER-OFFSET>4</COUNTER-OFFSET>
                <DATA-IDS>
                    <DATA-ID>1</DATA-ID>
                    <DATA-ID>2</DATA-ID>
                </DATA-IDS>
            </END-TO-END-PROFILE>
            <END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
                <END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
                    <DATA-OFFSET>8</DATA-OFFSET>
                    <I-SIGNAL-GROUP-REF DEST="I-SIGNAL-GROUP">/isg/Group1</I-SIGNAL-GROUP-REF>
                    <I-SIGNAL-I-PDU-REF DEST="I-SIGNAL-I-PDU">/ipdu/Pdu1</I-SIGNAL-I-PDU-REF>
                </END-TO-END-PROTECTION-I-SIGNAL-I-PDU>
            </END-TO-END-PROTECTION-I-SIGNAL-I-PDUS>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protection = protection_set.getEndToEndProtections()
        assert len(protection) == 1
        assert protection[0].getShortName() == "MyProtection"
        assert protection[0].getEndToEndProfile() is not None
        category = protection[0].getEndToEndProfile().getCategory()
        assert category.getValue() == "CATEGORY1"
        assert len(protection[0].getEndToEndProfile().getDataIds()) == 2
        assert len(protection[0].getEndToEndProtectionISignalIPdus()) == 1

    def test_minimal_handler_no_optional_elements(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>MinimalProtection</SHORT-NAME>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protection = protection_set.getEndToEndProtections()
        assert len(protection) == 1
        assert protection[0].getShortName() == "MinimalProtection"
        assert protection[0].getEndToEndProfile() is None
        assert len(protection[0].getEndToEndProtectionISignalIPdus()) == 0
        assert len(protection[0].getEndToEndProtectionVariablePrototypes()) == 0

    def test_handler_reads_variable_prototypes(self, parser):
        protection_set = _make_protection_set()
        element = _snip(
            """
            <SHORT-NAME>VarProtection</SHORT-NAME>
            <END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>
                <END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>
                    <SENDER-IREF>
                        <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/comp/Comp</CONTEXT-COMPOSITION-REF>
                        <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</TARGET-DATA-PROTOTYPE-REF>
                    </SENDER-IREF>
                </END-TO-END-PROTECTION-VARIABLE-PROTOTYPE>
            </END-TO-END-PROTECTION-VARIABLE-PROTOTYPES>
            """,
            root_tag="END-TO-END-PROTECTION",
        )
        parser.readEndToEndProtection(element, protection_set)
        protection = protection_set.getEndToEndProtections()
        assert len(protection) == 1
        prototypes = protection[0].getEndToEndProtectionVariablePrototypes()
        assert len(prototypes) == 1


class TestReadEndToEndProtectionVariablePrototype:
    """Tests for readEndToEndProtectionVariablePrototype."""

    def test_read_prototype_receiver_sender_short_label_values(self, parser):
        prototype = EndToEndProtectionVariablePrototype()
        element = _snip(
            """
            <RECEIVER-IREFS>
                <RECEIVER-IREF>
                    <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Swc1</CONTEXT-COMPONENT-REF>
                    <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Recv1</TARGET-DATA-PROTOTYPE-REF>
                </RECEIVER-IREF>
                <RECEIVER-IREF>
                    <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Recv2</TARGET-DATA-PROTOTYPE-REF>
                </RECEIVER-IREF>
            </RECEIVER-IREFS>
            <SENDER-IREF>
                <CONTEXT-COMPOSITION-REF DEST="COMPOSITION-SW-COMPONENT-TYPE">/comp/Root</CONTEXT-COMPOSITION-REF>
                <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</TARGET-DATA-PROTOTYPE-REF>
            </SENDER-IREF>
            <SHORT-LABEL>Label1</SHORT-LABEL>
            """,
        )
        parser.readEndToEndProtectionVariablePrototype(element, prototype)
        receivers = prototype.getReceiverIrefs()
        assert len(receivers) == 2
        assert receivers[0].getContextComponentRefs()[0].getValue() == "/comp/Swc1"
        assert receivers[0].getTargetDataPrototypeRef().getValue() == "/vdp/Recv1"
        assert receivers[1].getTargetDataPrototypeRef().getValue() == "/vdp/Recv2"
        assert prototype.getSenderIref() is not None
        assert prototype.getSenderIref().getContextCompositionRef().getValue() == "/comp/Root"
        assert prototype.getSenderIref().getTargetDataPrototypeRef().getValue() == "/vdp/Var"
        assert prototype.getShortLabel() is not None
        assert prototype.getShortLabel().getValue() == "Label1"

    def test_read_prototype_without_optional_elements(self, parser):
        prototype = EndToEndProtectionVariablePrototype()
        element = _snip("")
        parser.readEndToEndProtectionVariablePrototype(element, prototype)
        assert prototype.getReceiverIrefs() == []
        assert prototype.getSenderIref() is None
        assert prototype.getShortLabel() is None
        assert prototype.getVariationPoint() is None

    def test_read_prototype_variation_point(self, parser):
        prototype = EndToEndProtectionVariablePrototype()
        element = _snip(
            """
            <RECEIVER-IREFS>
                <RECEIVER-IREF>
                    <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Recv1</TARGET-DATA-PROTOTYPE-REF>
                </RECEIVER-IREF>
            </RECEIVER-IREFS>
            <SHORT-LABEL>Label1</SHORT-LABEL>
            <VARIATION-POINT>
                <SHORT-LABEL>VPL</SHORT-LABEL>
            </VARIATION-POINT>
            """,
        )
        parser.readEndToEndProtectionVariablePrototype(element, prototype)
        assert prototype.getVariationPoint() is not None
        assert prototype.getVariationPoint().getShortLabel().getValue() == "VPL"


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestReadEndToEndProtections:
    def test_readEndToEndProtections_creates_protection(self, parser):

        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip("<END-TO-END-PROTECTIONS>" "<END-TO-END-PROTECTION>" "<SHORT-NAME>p</SHORT-NAME>" "</END-TO-END-PROTECTION>" "</END-TO-END-PROTECTIONS>")
        parser.readEndToEndProtections(element, protection_set)
        assert len(protection_set.getEndToEndProtections()) == 1

    def test_readEndToEndProtections_unsupported_warns(self, warning_parser, caplog):

        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip("<END-TO-END-PROTECTIONS><BAD/></END-TO-END-PROTECTIONS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtections(element, protection_set)
        assert any("Unsupported EndToEndProtectionSet" in r.getMessage() for r in caplog.records)


class TestReadEndToEndProtectionSet:
    """Tests for readEndToEndProtectionSet."""

    def test_read_set_populates_protections_with_values(self, parser):
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("ReadSet")
        element = _snip(
            """
            <SHORT-NAME>ReadSet</SHORT-NAME>
            <END-TO-END-PROTECTIONS>
                <END-TO-END-PROTECTION>
                    <SHORT-NAME>Zeta</SHORT-NAME>
                    <END-TO-END-PROFILE>
                        <CATEGORY>CATEGORY1</CATEGORY>
                    </END-TO-END-PROFILE>
                </END-TO-END-PROTECTION>
                <END-TO-END-PROTECTION>
                    <SHORT-NAME>Alpha</SHORT-NAME>
                </END-TO-END-PROTECTION>
            </END-TO-END-PROTECTIONS>
            """,
            root_tag="END-TO-END-PROTECTION-SET",
        )
        parser.readEndToEndProtectionSet(element, protection_set)
        protections = protection_set.getEndToEndProtections()
        assert [p.getShortName() for p in protections] == ["Zeta", "Alpha"]
        assert protections[0].getEndToEndProfile() is not None
        assert protections[0].getEndToEndProfile().getCategory().getValue() == "CATEGORY1"
        assert protections[1].getEndToEndProfile() is None

    def test_read_set_without_wrapper(self, parser):
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("ReadSetBare")
        element = _snip(
            """
            <SHORT-NAME>ReadSetBare</SHORT-NAME>
            """,
            root_tag="END-TO-END-PROTECTION-SET",
        )
        parser.readEndToEndProtectionSet(element, protection_set)
        assert protection_set.getEndToEndProtections() == []


# ==================== Timing (L2982, L2997) ====================
