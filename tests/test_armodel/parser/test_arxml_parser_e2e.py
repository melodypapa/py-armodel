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
        parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(
            element, protection
        )
        ipdus = protection.getEndToEndProtectionISignalIPdus()
        assert len(ipdus) == 1
        assert ipdus[0].getDataOffset().getValue() == 8
        assert ipdus[0].getISignalGroupRef() is not None
        assert ipdus[0].getISignalIPduRef() is not None

    def test_empty_container_returns_no_ipdus(self, parser):
        protection = _make_protection()
        element = _snip("")
        parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(
            element, protection
        )
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
            warning_parser.readEndToEndProtectionEndToEndProtectionISignalIPdus(
                element, protection
            )
        assert any(
            "Unsupported EndToEndProtectionISignalIPdu" in rec.getMessage()
            for rec in caplog.records
        )
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


# === Migrated from test_arxml_parser_remaining_gaps.py ===

class TestReadEndToEndProtections:
    def test_readEndToEndProtections_creates_protection(self, parser):
        from armodel.models import EndToEndProtectionSet
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip(
            "<END-TO-END-PROTECTIONS>"
            "<END-TO-END-PROTECTION>"
            "<SHORT-NAME>p</SHORT-NAME>"
            "</END-TO-END-PROTECTION>"
            "</END-TO-END-PROTECTIONS>"
        )
        parser.readEndToEndProtections(element, protection_set)
        assert len(protection_set.getEndToEndProtections()) == 1

    def test_readEndToEndProtections_unsupported_warns(
        self, warning_parser, caplog
    ):
        from armodel.models import EndToEndProtectionSet
        pkg = _autosar_root().createARPackage("Pkg")
        protection_set = pkg.createEndToEndProtectionSet("E2eSet")
        element = _snip(
            "<END-TO-END-PROTECTIONS><BAD/></END-TO-END-PROTECTIONS>"
        )
        with caplog.at_level(logging.ERROR):
            warning_parser.readEndToEndProtections(
                element, protection_set
            )
        assert any("Unsupported EndToEndProtectionSet"
                   in r.getMessage() for r in caplog.records)


# ==================== Timing (L2982, L2997) ====================

