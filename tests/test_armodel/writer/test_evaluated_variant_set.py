"""
Tests for writing EVALUATED-VARIANT-SET elements (EvaluatedVariantSet, Table 7.23).

Round-trip counterpart: tests/test_armodel/parser/test_evaluated_variant_set.py
"""

import os
import tempfile

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    RefType,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestWriteEvaluatedVariantSetRoundTrip:
    """
    Write an EvaluatedVariantSet, re-parse it and compare field values.
    """

    def test_round_trip(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        ar_root = document.createARPackage("AUTOSAR")
        variant_set = ar_root.createEvaluatedVariantSet("MyEvaluatedVariantSet")
        variant_set.setApprovalStatus(NameToken().setValue("APPROVED"))
        variant_set.addEvaluatedElementRef(RefType().setValue("/AUTOSAR/Foo").setDest("SWC-IMPLEMENTATION"))
        variant_set.addEvaluatedVariantRef(RefType().setValue("/AUTOSAR/MyVariant").setDest("PREDEFINED-VARIANT"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            writer = ARXMLWriter()
            writer.save(file_path, document)

            reload_doc = AUTOSAR.getInstance()
            reload_doc.new()
            reload_doc.setARRelease("R23-11")
            parser = ARXMLParser()
            parser.load(file_path, reload_doc)

            reloaded = reload_doc.getARPackages()[0].getElement("MyEvaluatedVariantSet")
            assert reloaded is not None
            assert reloaded.getApprovalStatus().getValue() == "APPROVED"
            assert len(reloaded.getEvaluatedElementRefs()) == 1
            assert reloaded.getEvaluatedElementRefs()[0].getValue() == "/AUTOSAR/Foo"
            assert reloaded.getEvaluatedElementRefs()[0].getDest() == "SWC-IMPLEMENTATION"
            assert len(reloaded.getEvaluatedVariantRefs()) == 1
            assert reloaded.getEvaluatedVariantRefs()[0].getValue() == "/AUTOSAR/MyVariant"
            assert reloaded.getEvaluatedVariantRefs()[0].getDest() == "PREDEFINED-VARIANT"
        finally:
            os.remove(file_path)
