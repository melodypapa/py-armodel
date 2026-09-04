"""Tests for InvalidationPolicy writer (writeSenderReceiverInterfaceInvalidationPolicies) and round-trip."""

import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral, RefType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture
def writer():
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _make_ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _make_literal(text):
    literal = ARLiteral()
    literal.setValue(text)
    return literal


class TestWriteInvalidationPolicy:
    def test_write_empty_emits_no_wrapper(self, writer):
        autosar = AUTOSAR.getInstance()
        autosar.setARRelease("R23-11")
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        parent = _parent()
        writer.writeSenderReceiverInterfaceInvalidationPolicies(parent, sr)
        assert len(parent) == 0

    def test_write_policy_emits_field_values(self, writer):
        autosar = AUTOSAR.getInstance()
        autosar.setARRelease("R23-11")
        pkg = autosar.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        policy = sr.createInvalidationPolicy()
        policy.setDataElementRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/de"))
        policy.setHandleInvalid(_make_literal("DISABLE"))
        parent = _parent()
        writer.writeSenderReceiverInterfaceInvalidationPolicies(parent, sr)
        assert len(parent) == 1
        policies_tag = parent[0]
        assert policies_tag.tag == "INVALIDATION-POLICYS"
        policy_tag = policies_tag[0]
        assert policy_tag.tag == "INVALIDATION-POLICY"
        de_ref = policy_tag.find("DATA-ELEMENT-REF")
        assert de_ref.text == "/de"
        assert de_ref.get("DEST") == "VARIABLE-DATA-PROTOTYPE"
        assert policy_tag.find("HANDLE-INVALID").text == "DISABLE"


class TestInvalidationPolicyRoundTrip:
    def test_write_then_parse_preserves_field_values(self, writer):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")
        policy = sr.createInvalidationPolicy()
        policy.setDataElementRef(_make_ref("VARIABLE-DATA-PROTOTYPE", "/de"))
        policy.setHandleInvalid(_make_literal("DISABLE"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            writer.save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            sr_2 = document_2.getARPackages()[0].getSenderReceiverInterfaces()[0]
            assert len(sr_2.getInvalidationPolicies()) == 1
            reparsed = sr_2.getInvalidationPolicies()[0]
            assert reparsed.getDataElementRef().getValue() == "/de"
            assert reparsed.getDataElementRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
            assert reparsed.getHandleInvalid().getValue() == "DISABLE"
        finally:
            import os

            if os.path.exists(file_path):
                os.remove(file_path)
