"""Tests for Communication Specification (ComSpec) handler methods.

Covers:
- ``getClientComSpec`` (L2005-2009)
- ``getParameterRequireComSpec`` (L2011-2016)
- ``getQueuedReceiverComSpec`` (L2025-2030)
- ``getModeSwitchReceiverComSpec`` (L2032-2038)
- ``getNonqueuedReceiverComSpec`` (L2040-2050)
- ``readRequiredComSpec`` (L2052-2068)
- ``getQueuedSenderComSpec`` (L2162-2165)
- ``getModeSwitchedAckRequest`` (L2167-2173)
- ``getModeSwitchSenderComSpec`` (L2175-2180)
- ``getNvProvideComSpec`` (L2182-2188)
- ``readProvidedComSpec`` (L2190-2204)

Shared fixtures (``parser``, ``warning_parser``, ``reset_autosar``) are provided
by ``conftest.py``; helper functions (``_snip``, ``_autosar_root``) live in
``_helpers.py``.
"""

import logging
from unittest.mock import MagicMock

import pytest

from armodel.models import AUTOSAR, ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication import UserDefinedTransformationComSpecProps
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_r_port():
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    return app.createRPortPrototype("RPort")


def _make_p_port():
    app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
    return app.createPPortPrototype("PPort")


class TestGetClientComSpec:
    """Tests for getClientComSpec (L2005-2009)."""

    def test_with_operation_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/if/Op</OPERATION-REF>',
            root_tag="CLIENT-COM-SPEC",
        )
        result = parser.getClientComSpec(element)
        assert result is not None
        assert result.getOperationRef() is not None
        assert result.getOperationRef().getValue() == "/if/Op"
        assert result.getOperationRef().getDest() == "CLIENT-SERVER-OPERATION"

    def test_without_operation_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="CLIENT-COM-SPEC")
        result = parser.getClientComSpec(element)
        assert result is not None
        assert result.getOperationRef() is None

    def test_with_end_to_end_call_response_timeout(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <END-TO-END-CALL-RESPONSE-TIMEOUT>1.5</END-TO-END-CALL-RESPONSE-TIMEOUT>
            """,
            root_tag="CLIENT-COM-SPEC",
        )
        result = parser.getClientComSpec(element)
        assert result.getEndToEndCallResponseTimeout() is not None
        assert result.getEndToEndCallResponseTimeout().getValue() == 1.5

    def test_with_transformation_com_spec_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <TRANSFORMATION-COM-SPEC-PROPSS>
                <USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS></USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS>
            </TRANSFORMATION-COM-SPEC-PROPSS>
            """,
            root_tag="CLIENT-COM-SPEC",
        )
        result = parser.getClientComSpec(element)
        assert len(result.getTransformationComSpecProps()) == 1
        assert isinstance(result.getTransformationComSpecProps()[0], UserDefinedTransformationComSpecProps)


class TestGetNonqueuedSenderComSpec:
    """Tests for getNonqueuedSenderComSpec."""

    def test_with_data_filter(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/if/De</DATA-ELEMENT-REF>
            <DATA-FILTER>
                <DATA-FILTER-TYPE>ONE-EVERY-N</DATA-FILTER-TYPE>
            </DATA-FILTER>
            """,
            root_tag="NONQUEUED-SENDER-COM-SPEC",
        )
        result = parser.getNonqueuedSenderComSpec(element)
        assert result.getDataFilter() is not None
        assert result.getDataFilter().getDataFilterType() is not None
        assert result.getDataElementRef().getValue() == "/if/De"

    def test_with_transmission_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <TRANSMISSION-PROPS>
                <DATA-UPDATE-PERIOD>0.01</DATA-UPDATE-PERIOD>
                <MINIMUM-SEND-INTERVAL>0.1</MINIMUM-SEND-INTERVAL>
                <TRANSMISSION-MODE>triggered</TRANSMISSION-MODE>
            </TRANSMISSION-PROPS>
            <TRANSMISSION-ACKNOWLEDGE>
                <TIMEOUT>0.5</TIMEOUT>
            </TRANSMISSION-ACKNOWLEDGE>
            """,
            root_tag="NONQUEUED-SENDER-COM-SPEC",
        )
        result = parser.getNonqueuedSenderComSpec(element)
        props = result.getTransmissionProps()
        assert props is not None
        assert props.getDataUpdatePeriod().getValue() == 0.01
        assert props.getMinimumSendInterval().getValue() == 0.1
        assert props.getTransmissionMode().getValue() == "triggered"
        assert result.getTransmissionAcknowledge() is not None
        assert result.getTransmissionAcknowledge().getTimeout().getValue() == 0.5

    def test_without_transmission_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="NONQUEUED-SENDER-COM-SPEC")
        result = parser.getNonqueuedSenderComSpec(element)
        assert result.getTransmissionProps() is None
        assert result.getTransmissionAcknowledge() is None


class TestGetServerComSpec:
    """Tests for getServerComSpec."""

    def test_with_queue_length_and_props(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/if/Op</OPERATION-REF>
            <QUEUE-LENGTH>4</QUEUE-LENGTH>
            <TRANSFORMATION-COM-SPEC-PROPSS>
                <USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS></USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS>
            </TRANSFORMATION-COM-SPEC-PROPSS>
            """,
            root_tag="SERVER-COM-SPEC",
        )
        result = parser.getServerComSpec(element)
        assert result.getOperationRef().getValue() == "/if/Op"
        assert result.getQueueLength().getValue() == 4
        assert len(result.getTransformationComSpecProps()) == 1


class TestGetParameterProvideComSpec:
    """Tests for getParameterProvideComSpec."""

    def test_with_init_value_and_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <INIT-VALUE>
                <TEXT-VALUE-SPECIFICATION>
                    <VALUE>init</VALUE>
                </TEXT-VALUE-SPECIFICATION>
            </INIT-VALUE>
            <PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/if/Param</PARAMETER-REF>
            """,
            root_tag="PARAMETER-PROVIDE-COM-SPEC",
        )
        result = parser.getParameterProvideComSpec(element)
        assert result.getInitValue() is not None
        assert result.getParameterRef() is not None
        assert result.getParameterRef().getValue() == "/if/Param"
        assert result.getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"

    def test_empty(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="PARAMETER-PROVIDE-COM-SPEC")
        result = parser.getParameterProvideComSpec(element)
        assert result.getInitValue() is None
        assert result.getParameterRef() is None


class TestGetParameterRequireComSpec:
    """Tests for getParameterRequireComSpec (L2011-2016)."""

    def test_with_parameter_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/pdp/Param</PARAMETER-REF>',
            root_tag="PARAMETER-REQUIRE-COM-SPEC",
        )
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getParameterRef() is not None
        assert result.getParameterRef().getDest() == "PARAMETER-DATA-PROTOTYPE"
        assert result.getParameterRef().getValue() == "/pdp/Param"

    def test_without_refs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="PARAMETER-REQUIRE-COM-SPEC")
        result = parser.getParameterRequireComSpec(element)
        assert result is not None
        assert result.getParameterRef() is None
        assert result.getInitValue() is None


class TestGetQueuedReceiverComSpec:
    """Tests for getQueuedReceiverComSpec (L2025-2030)."""

    def test_with_queue_length(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            "<QUEUE-LENGTH>10</QUEUE-LENGTH>",
            root_tag="QUEUED-RECEIVER-COM-SPEC",
        )
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getQueueLength() is not None
        assert result.getQueueLength().getValue() == 10.0

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="QUEUED-RECEIVER-COM-SPEC")
        result = parser.getQueuedReceiverComSpec(element)
        assert result is not None
        assert result.getQueueLength() is None


class TestGetModeSwitchReceiverComSpec:
    """Tests for getModeSwitchReceiverComSpec (L2032-2038)."""

    def test_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <ENHANCED-MODE-API>true</ENHANCED-MODE-API>
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>false</SUPPORTS-ASYNCHRONOUS-MODE-SWITCH>
            """,
            root_tag="MODE-SWITCH-RECEIVER-COM-SPEC",
        )
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is not None
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getSupportsAsynchronousModeSwitch() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="MODE-SWITCH-RECEIVER-COM-SPEC")
        result = parser.getModeSwitchReceiverComSpec(element)
        assert result is not None
        assert result.getEnhancedModeApi() is None
        assert result.getModeGroupRef() is None
        assert result.getSupportsAsynchronousModeSwitch() is None


class TestGetNonqueuedReceiverComSpec:
    """Tests for getNonqueuedReceiverComSpec (L2040-2050)."""

    def test_with_data_element_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Elem</DATA-ELEMENT-REF>
            <ALIVE-TIMEOUT>0.5</ALIVE-TIMEOUT>
            <ENABLE-UPDATE>true</ENABLE-UPDATE>
            <HANDLE-DATA-STATUS>true</HANDLE-DATA-STATUS>
            <HANDLE-NEVER-RECEIVED>false</HANDLE-NEVER-RECEIVED>
            <HANDLE-TIMEOUT-TYPE>REPLACE</HANDLE-TIMEOUT-TYPE>
            """,
            root_tag="NONQUEUED-RECEIVER-COM-SPEC",
        )
        result = parser.getNonqueuedReceiverComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is not None
        assert result.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert result.getAliveTimeout() is not None
        assert result.getEnableUpdate() is not None
        assert result.getHandleDataStatus() is not None
        assert result.getHandleDataStatus().getValue() is True
        assert result.getHandleNeverReceived() is not None
        assert result.getHandleTimeoutType() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="NONQUEUED-RECEIVER-COM-SPEC")
        result = parser.getNonqueuedReceiverComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is None
        assert result.getAliveTimeout() is None
        assert result.getFilter() is None
        assert result.getInitValue() is None


class TestReadRequiredComSpec:
    """Tests for readRequiredComSpec (L2052-2068)."""

    @pytest.mark.parametrize(
        "tag",
        [
            "MODE-SWITCH-RECEIVER-COM-SPEC",
            "PARAMETER-REQUIRE-COM-SPEC",
        ],
    )
    def test_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            f"""
            <REQUIRED-COM-SPECS>
                <{tag}></{tag}>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, r_port)
        specs = r_port.getRequiredComSpecs()
        assert len(specs) == 1

    def test_nv_require_branch_with_mock_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        mock_parent = MagicMock()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <NV-REQUIRE-COM-SPEC></NV-REQUIRE-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        parser.readRequiredComSpec(element, mock_parent)
        assert mock_parent.addRequiredComSpec.called
        com_spec = mock_parent.addRequiredComSpec.call_args[0][0]
        assert com_spec is not None

    def test_unknown_branch_raises(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        with pytest.raises(ValueError):
            parser.readRequiredComSpec(element, r_port)

    def test_unknown_branch_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip(
            """
            <REQUIRED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </REQUIRED-COM-SPECS>
            """
        )
        warning_parser.readRequiredComSpec(element, r_port)
        assert len(r_port.getRequiredComSpecs()) == 0

    def test_empty_required_com_specs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        r_port = _make_r_port()
        element = _snip("")
        parser.readRequiredComSpec(element, r_port)
        assert len(r_port.getRequiredComSpecs()) == 0


class TestGetQueuedSenderComSpec:
    """Tests for getQueuedSenderComSpec (L2162-2165)."""

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="QUEUED-SENDER-COM-SPEC")
        result = parser.getQueuedSenderComSpec(element)
        assert result is not None

    def test_with_data_element_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Elem</DATA-ELEMENT-REF>',
            root_tag="QUEUED-SENDER-COM-SPEC",
        )
        result = parser.getQueuedSenderComSpec(element)
        assert result is not None
        assert result.getDataElementRef() is not None
        assert result.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"


class TestGetModeSwitchedAckRequest:
    """Tests for getModeSwitchedAckRequest (L2167-2173)."""

    def test_with_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-SWITCHED-ACK>
                <TIMEOUT>0.5</TIMEOUT>
            </MODE-SWITCHED-ACK>
            """
        )
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is not None
        assert result.getTimeout() is not None

    def test_without_element(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("")
        result = parser.getModeSwitchedAckRequest(element, "MODE-SWITCHED-ACK")
        assert result is None


class TestGetModeSwitchSenderComSpec:
    """Tests for getModeSwitchSenderComSpec (L2175-2180)."""

    def test_with_all_fields(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            """
            <MODE-GROUP-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/mdg/Group</MODE-GROUP-REF>
            <MODE-SWITCHED-ACK>
                <TIMEOUT>1.0</TIMEOUT>
            </MODE-SWITCHED-ACK>
            <QUEUE-LENGTH>5</QUEUE-LENGTH>
            """,
            root_tag="MODE-SWITCH-SENDER-COM-SPEC",
        )
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getModeGroupRef() is not None
        assert result.getModeGroupRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert result.getModeSwitchedAck() is not None
        assert result.getModeSwitchedAck().getTimeout() is not None
        assert result.getQueueLength() is not None

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="MODE-SWITCH-SENDER-COM-SPEC")
        result = parser.getModeSwitchSenderComSpec(element)
        assert result is not None
        assert result.getModeGroupRef() is None
        assert result.getModeSwitchedAck() is None
        assert result.getQueueLength() is None


class TestGetNvProvideComSpec:
    """Tests for getNvProvideComSpec (L2182-2188)."""

    def test_with_variable_ref(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip(
            '<VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var</VARIABLE-REF>',
            root_tag="NV-PROVIDE-COM-SPEC",
        )
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getVariableRef() is not None
        assert result.getVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert result.getVariableRef().getValue() == "/vdp/Var"

    def test_minimal(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        element = _snip("", root_tag="NV-PROVIDE-COM-SPEC")
        result = parser.getNvProvideComSpec(element)
        assert result is not None
        assert result.getVariableRef() is None
        assert result.getRamBlockInitValue() is None
        assert result.getRomBlockInitValue() is None


class TestReadProvidedComSpec:
    """Tests for readProvidedComSpec (L2190-2204)."""

    @pytest.mark.parametrize(
        "tag",
        [
            "QUEUED-SENDER-COM-SPEC",
            "MODE-SWITCH-SENDER-COM-SPEC",
        ],
    )
    def test_branches(self, parser, tag):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            f"""
            <PROVIDED-COM-SPECS>
                <{tag}></{tag}>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, p_port)
        specs = p_port.getProvidedComSpecs()
        assert len(specs) == 1

    def test_parameter_provide_branch(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <PARAMETER-PROVIDE-COM-SPEC>
                    <PARAMETER-REF DEST="PARAMETER-DATA-PROTOTYPE">/if/Param</PARAMETER-REF>
                </PARAMETER-PROVIDE-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, p_port)
        specs = p_port.getProvidedComSpecs()
        assert len(specs) == 1
        assert specs[0].getParameterRef().getValue() == "/if/Param"

    def test_nv_provide_branch_with_mock_parent(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        mock_parent = MagicMock()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <NV-PROVIDE-COM-SPEC></NV-PROVIDE-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        parser.readProvidedComSpec(element, mock_parent)
        assert mock_parent.addProvidedComSpec.called
        com_spec = mock_parent.addProvidedComSpec.call_args[0][0]
        assert com_spec is not None

    def test_unknown_branch_raises(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        with pytest.raises(ValueError):
            parser.readProvidedComSpec(element, p_port)

    def test_unknown_branch_warning(self, warning_parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip(
            """
            <PROVIDED-COM-SPECS>
                <UNKNOWN-COM-SPEC></UNKNOWN-COM-SPEC>
            </PROVIDED-COM-SPECS>
            """
        )
        warning_parser.readProvidedComSpec(element, p_port)
        assert len(p_port.getProvidedComSpecs()) == 0

    def test_empty_provided_com_specs(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        p_port = _make_p_port()
        element = _snip("")
        parser.readProvidedComSpec(element, p_port)
        assert len(p_port.getProvidedComSpecs()) == 0


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestCompositeNetworkRepresentation:
    def test_readReceiverComSpec_adds_composite_repr(self, parser):
        from armodel.models import NonqueuedReceiverComSpec

        com_spec = NonqueuedReceiverComSpec()
        element = _snip(
            "<COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<COMPOSITE-NETWORK-REPRESENTATION>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL/>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATIONS>"
        )
        parser.readReceiverComSpec(element, com_spec)
        assert len(com_spec.getCompositeNetworkRepresentations()) == 1

    def test_readSenderComSpec_adds_composite_repr(self, parser):
        from armodel.models import NonqueuedSenderComSpec

        com_spec = NonqueuedSenderComSpec()
        element = _snip(
            "<COMPOSITE-NETWORK-REPRESENTATIONS>"
            "<COMPOSITE-NETWORK-REPRESENTATION>"
            "<NETWORK-REPRESENTATION>"
            "<SW-DATA-DEF-PROPS-VARIANTS>"
            "<SW-DATA-DEF-PROPS-CONDITIONAL/>"
            "</SW-DATA-DEF-PROPS-VARIANTS>"
            "</NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATION>"
            "</COMPOSITE-NETWORK-REPRESENTATIONS>"
        )
        parser.readSenderComSpec(element, com_spec)
        assert len(com_spec.getCompositeNetworkRepresentations()) == 1


# ==================== RequiredComSpecs (L2058) ====================


# === Migrated from remaining_gaps.py as TestReadRequiredComSpecExtras (originally TestReadRequiredComSpec) ===


class TestReadRequiredComSpecExtras:
    def test_readRequiredComSpec_client_com_spec(self, parser):
        app = ApplicationSwComponentType(parent=_autosar_root(), short_name="App")
        port = app.createRPortPrototype("RPort")
        element = _snip("<REQUIRED-COM-SPECS>" "<CLIENT-COM-SPEC>" '<OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/op</OPERATION-REF>' "</CLIENT-COM-SPEC>" "</REQUIRED-COM-SPECS>")
        parser.readRequiredComSpec(element, port)
        assert len(port.getRequiredComSpecs()) == 1


# ==================== TransformationComSpecProps (L2136, L2139, L2143-2149) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestTransformationComSpecProps:
    def test_readTransformationComSpecProps_sets_attrs(self, parser):
        from armodel.models import UserDefinedTransformationComSpecProps

        props = UserDefinedTransformationComSpecProps()
        element = _snip("")
        parser.readTransformationComSpecProps(element, props)

    def test_readUserDefinedTransformationComSpecProps(self, parser):
        from armodel.models import UserDefinedTransformationComSpecProps

        props = UserDefinedTransformationComSpecProps()
        element = _snip("")
        parser.readUserDefinedTransformationComSpecProps(element, props)

    def test_readServerComSpecTransformationComSpecProps_adds_props(self, parser):
        from armodel.models import ServerComSpec

        com_spec = ServerComSpec()
        element = _snip("<TRANSFORMATION-COM-SPEC-PROPSS>" "<USER-DEFINED-TRANSFORMATION-COM-SPEC-PROPS/>" "</TRANSFORMATION-COM-SPEC-PROPSS>")
        parser.readTransformationComSpecPropss(element, com_spec)
        assert len(com_spec.getTransformationComSpecProps()) == 1

    def test_readServerComSpecTransformationComSpecProps_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ServerComSpec

        com_spec = ServerComSpec()
        element = _snip("<TRANSFORMATION-COM-SPEC-PROPSS><BAD/></TRANSFORMATION-COM-SPEC-PROPSS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readTransformationComSpecPropss(element, com_spec)
        assert any("Unsupported TransformationComSpecProps" in r.getMessage() for r in caplog.records)

    def test_readEndToEndTransformationComSpecProps_full(self, parser):
        from armodel.models import ServerComSpec

        com_spec = ServerComSpec()
        element = _snip(
            "<TRANSFORMATION-COM-SPEC-PROPSS>"
            "<END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>"
            "<CLEAR-FROM-VALID-TO-INVALID>true</CLEAR-FROM-VALID-TO-INVALID>"
            "<DISABLE-END-TO-END-CHECK>true</DISABLE-END-TO-END-CHECK>"
            "<DISABLE-END-TO-END-STATE-MACHINE>true</DISABLE-END-TO-END-STATE-MACHINE>"
            "<E2E-PROFILE-COMPATIBILITY-PROPS-REF DEST='E2E-PROFILE-COMPATIBILITY-PROPS'>/Pkg/Props</E2E-PROFILE-COMPATIBILITY-PROPS-REF>"
            "<MAX-DELTA-COUNTER>3</MAX-DELTA-COUNTER>"
            "<MAX-ERROR-STATE-INIT>2</MAX-ERROR-STATE-INIT>"
            "<MAX-ERROR-STATE-INVALID>2</MAX-ERROR-STATE-INVALID>"
            "<MAX-ERROR-STATE-VALID>2</MAX-ERROR-STATE-VALID>"
            "<MAX-NO-NEW-OR-REPEATED-DATA>2</MAX-NO-NEW-OR-REPEATED-DATA>"
            "<MIN-OK-STATE-INIT>1</MIN-OK-STATE-INIT>"
            "<MIN-OK-STATE-INVALID>1</MIN-OK-STATE-INVALID>"
            "<MIN-OK-STATE-VALID>1</MIN-OK-STATE-VALID>"
            "<SYNC-COUNTER-INIT>0</SYNC-COUNTER-INIT>"
            "<WINDOW-SIZE-INIT>5</WINDOW-SIZE-INIT>"
            "<WINDOW-SIZE-INVALID>5</WINDOW-SIZE-INVALID>"
            "<WINDOW-SIZE-VALID>5</WINDOW-SIZE-VALID>"
            "</END-TO-END-TRANSFORMATION-COM-SPEC-PROPS>"
            "</TRANSFORMATION-COM-SPEC-PROPSS>",
            root_tag="SERVER-COM-SPEC",
        )
        parser.readTransformationComSpecPropss(element, com_spec)
        props = com_spec.getTransformationComSpecProps()[0]
        assert props.getClearFromValidToInvalid().getValue() is True
        assert props.getDisableEndToEndCheck().getValue() is True
        assert props.getDisableEndToEndStateMachine().getValue() is True
        assert props.getE2eProfileCompatibilityPropsRef().getValue() == "/Pkg/Props"
        assert props.getMaxDeltaCounter().getValue() == 3
        assert props.getMaxErrorStateInit().getValue() == 2
        assert props.getMaxErrorStateInvalid().getValue() == 2
        assert props.getMaxErrorStateValid().getValue() == 2
        assert props.getMaxNoNewOrRepeatedData().getValue() == 2
        assert props.getMinOkStateInit().getValue() == 1
        assert props.getMinOkStateInvalid().getValue() == 1
        assert props.getMinOkStateValid().getValue() == 1
        assert props.getSyncCounterInit().getValue() == 0
        assert props.getWindowSizeInit().getValue() == 5
        assert props.getWindowSizeInvalid().getValue() == 5
        assert props.getWindowSizeValid().getValue() == 5


# ==================== PortGroup / InnerPortIRef / Composition (L2231, L2345, L2370) ====================


# === Migrated from test_arxml_parser_remaining_gaps.py ===


class TestInvalidationPolicies:
    def test_readSenderReceiverInterfaceInvalidationPolicies_adds(self, parser):
        from armodel.models import SenderReceiverInterface

        sr = SenderReceiverInterface(parent=_autosar_root(), short_name="Sr")
        element = _snip(
            "<INVALIDATION-POLICYS>"
            "<INVALIDATION-POLICY>"
            '<DATA-ELEMENT-REF DEST="VARIABLE-DATA-PROTOTYPE">/de</DATA-ELEMENT-REF>'
            "<HANDLE-INVALID>DISABLE</HANDLE-INVALID>"
            "</INVALIDATION-POLICY>"
            "</INVALIDATION-POLICYS>"
        )
        parser.readSenderReceiverInterfaceInvalidationPolicies(element, sr)
        assert len(sr.getInvalidationPolicies()) == 1

    def test_readClientServerOperationArguments_unsupported_warns(self, warning_parser, caplog):
        from armodel.models import ClientServerInterface

        iface = ClientServerInterface(parent=_autosar_root(), short_name="Csi")
        op = iface.createOperation("Op")
        element = _snip("<ARGUMENTS><BAD/></ARGUMENTS>")
        with caplog.at_level(logging.ERROR):
            warning_parser.readClientServerOperationArguments(element, op)
        assert any("Unsupported Argument" in r.getMessage() for r in caplog.records)


# ==================== getValueSpecification (L2685, 2687, 2691, 2693, 2697) ====================
