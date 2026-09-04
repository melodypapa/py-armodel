"""Tests for InvalidationPolicy reader (readSenderReceiverInterfaceInvalidationPolicies)."""

from armodel.models import AUTOSAR, SenderReceiverInterface
from tests.test_armodel.parser._helpers import _autosar_root, _snip


class TestReadInvalidationPolicy:
    def test_read_sets_data_element_ref_and_handle_invalid(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
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
        policies = sr.getInvalidationPolicies()
        assert len(policies) == 1
        policy = policies[0]
        assert policy.getDataElementRef().getValue() == "/de"
        assert policy.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert policy.getHandleInvalid().getValue() == "DISABLE"

    def test_read_missing_optionals_leaves_none(self, parser):
        AUTOSAR.getInstance().setARRelease("R23-11")
        sr = SenderReceiverInterface(parent=_autosar_root(), short_name="Sr")
        element = _snip("<INVALIDATION-POLICYS>" "<INVALIDATION-POLICY>" "</INVALIDATION-POLICY>" "</INVALIDATION-POLICYS>")
        parser.readSenderReceiverInterfaceInvalidationPolicies(element, sr)
        policy = sr.getInvalidationPolicies()[0]
        assert policy.getDataElementRef() is None
        assert policy.getHandleInvalid() is None
