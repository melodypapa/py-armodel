"""Writer round-trip tests for SenderReceiverInterface (SWCT Table 4.1)."""

import os
import tempfile

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import MetaDataItemSet
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture
def writer():
    return ARXMLWriter()


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


def _literal(text):
    literal = ARLiteral()
    literal.setValue(text)
    return literal


def _round_trip(document, writer):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        writer.save(file_path, document)
        doc2 = AUTOSAR.getInstance()
        doc2.clear()
        ARXMLParser().load(file_path, doc2)
        return doc2
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestWriteSenderReceiverInterfaceRoundTrip:
    def test_round_trip_all_aggregations(self, writer):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        document.clear()
        pkg = document.createARPackage("Pkg")
        sr = pkg.createSenderReceiverInterface("SR")

        sr.createDataElement("de1")

        policy = sr.createInvalidationPolicy()
        policy.setDataElementRef(_ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/SR/de1"))
        policy.setHandleInvalid(_literal("DISABLE"))

        mapping_set = MetaDataItemSet()
        mapping_set.addDataElementRef(_ref("VARIABLE-DATA-PROTOTYPE", "/Pkg/SR/de1"))
        sr.addMetaDataItemSet(mapping_set)

        doc2 = _round_trip(document, writer)
        sr2 = doc2.getARPackages()[0].getSenderReceiverInterfaces()[0]

        assert [e.getShortName() for e in sr2.getDataElements()] == ["de1"]

        policies = sr2.getInvalidationPolicies()
        assert len(policies) == 1
        assert policies[0].getDataElementRef().getValue() == "/Pkg/SR/de1"
        assert policies[0].getHandleInvalid().getValue() == "DISABLE"

        sets = sr2.getMetaDataItemSets()
        assert len(sets) == 1
        assert sets[0].getDataElementRefs()[0].getValue() == "/Pkg/SR/de1"

    def test_round_trip_empty_aggregations(self, writer):
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        document.clear()
        pkg = document.createARPackage("Pkg")
        pkg.createSenderReceiverInterface("SR")

        doc2 = _round_trip(document, writer)
        sr2 = doc2.getARPackages()[0].getSenderReceiverInterfaces()[0]

        assert sr2.getDataElements() == []
        assert sr2.getInvalidationPolicies() == []
        assert sr2.getMetaDataItemSets() == []
