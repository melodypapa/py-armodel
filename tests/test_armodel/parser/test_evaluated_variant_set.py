"""
Tests for parsing EVALUATED-VARIANT-SET elements (EvaluatedVariantSet, Table 7.23).

Round-trip counterpart: tests/test_armodel/writer/test_evaluated_variant_set.py
"""

import os
import tempfile

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

CONTENT = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns='{NS}'>
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>VariantSets</SHORT-NAME>
            <ELEMENTS>
                <EVALUATED-VARIANT-SET>
                    <SHORT-NAME>MyEvaluatedVariantSet</SHORT-NAME>
                    <APPROVAL-STATUS>APPROVED</APPROVAL-STATUS>
                    <EVALUATED-ELEMENT-REFS>
                        <EVALUATED-ELEMENT-REF DEST="SWC-IMPLEMENTATION">/AUTOSAR/Foo</EVALUATED-ELEMENT-REF>
                    </EVALUATED-ELEMENT-REFS>
                    <EVALUATED-VARIANT-REFS>
                        <EVALUATED-VARIANT-REF DEST="PREDEFINED-VARIANT">/AUTOSAR/MyVariant</EVALUATED-VARIANT-REF>
                    </EVALUATED-VARIANT-REFS>
                </EVALUATED-VARIANT-SET>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestReadEvaluatedVariantSet:
    """
    Test readEvaluatedVariantSet (EvaluatedVariantSet, Table 7.23).
    """

    def test_read_members(self):
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(CONTENT)

            document = AUTOSAR.getInstance()
            document.clear()
            parser = ARXMLParser()
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            variant_set = pkg.getReferrableElement("MyEvaluatedVariantSet")
            assert variant_set is not None
            assert variant_set.getApprovalStatus().getValue() == "APPROVED"
            assert len(variant_set.getEvaluatedElementRefs()) == 1
            assert variant_set.getEvaluatedElementRefs()[0].getValue() == "/AUTOSAR/Foo"
            assert variant_set.getEvaluatedElementRefs()[0].getDest() == "SWC-IMPLEMENTATION"
            assert len(variant_set.getEvaluatedVariantRefs()) == 1
            assert variant_set.getEvaluatedVariantRefs()[0].getValue() == "/AUTOSAR/MyVariant"
        finally:
            os.remove(file_path)
