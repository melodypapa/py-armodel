"""
Tests for parsing SDG-DEF elements (SdgDef family, Tables 4.24-4.35).

Round-trip counterpart: tests/test_armodel/writer/test_sdg_def.py
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
            <SHORT-NAME>SdgDefs</SHORT-NAME>
            <ELEMENTS>
                <SDG-DEF>
                    <SHORT-NAME>MySdgDef</SHORT-NAME>
                    <SDG-CLASSES>
                        <SDG-CLASS>
                            <SHORT-NAME>MySdgClass</SHORT-NAME>
                            <GID>MY-CLASS-GID</GID>
                            <EXTENDS-META-CLASS>ArPackage</EXTENDS-META-CLASS>
                            <CAPTION>true</CAPTION>
                            <ATTRIBUTES>
                                <SDG-PRIMITIVE-ATTRIBUTE>
                                    <SHORT-NAME>Severity</SHORT-NAME>
                                    <GID>SEVERITY</GID>
                                    <MAX INTERVAL-TYPE="CLOSED">3</MAX>
                                    <PATTERN>critical|significant|minor|low</PATTERN>
                                </SDG-PRIMITIVE-ATTRIBUTE>
                                <SDG-PRIMITIVE-ATTRIBUTE-WITH-VARIATION>
                                    <SHORT-NAME>VarAttr</SHORT-NAME>
                                    <VARIATION>false</VARIATION>
                                    <VALID-BINDING-TIMES>
                                        <VALID-BINDING-TIME>POST-BUILD</VALID-BINDING-TIME>
                                    </VALID-BINDING-TIMES>
                                </SDG-PRIMITIVE-ATTRIBUTE-WITH-VARIATION>
                                <SDG-REFERENCE>
                                    <SHORT-NAME>ClassRef</SHORT-NAME>
                                    <DEST-SDG-REF DEST="SDG-CLASS">/AUTOSAR/SdgDefs/MySdgDef/MySdgClass</DEST-SDG-REF>
                                </SDG-REFERENCE>
                                <SDG-AGGREGATION-WITH-VARIATION>
                                    <SHORT-NAME>SubSdg</SHORT-NAME>
                                    <GID>SUB-SDG</GID>
                                    <SUB-SDG-REF DEST="SDG-CLASS">/AUTOSAR/SdgDefs/MySdgDef/MySdgClass</SUB-SDG-REF>
                                </SDG-AGGREGATION-WITH-VARIATION>
                                <SDG-FOREIGN-REFERENCE>
                                    <SHORT-NAME>PackageRef</SHORT-NAME>
                                    <DEST-META-CLASS>ARPackage</DEST-META-CLASS>
                                </SDG-FOREIGN-REFERENCE>
                                <SDG-FOREIGN-REFERENCE-WITH-VARIATION>
                                    <SHORT-NAME>PackageRefWV</SHORT-NAME>
                                    <DEST-META-CLASS>ARPackage</DEST-META-CLASS>
                                </SDG-FOREIGN-REFERENCE-WITH-VARIATION>
                            </ATTRIBUTES>
                            <SDG-CONSTRAINT-REFS>
                                <SDG-CONSTRAINT-REF DEST="TRACEABLE-TEXT">/AUTOSAR/MyConstraint</SDG-CONSTRAINT-REF>
                            </SDG-CONSTRAINT-REFS>
                        </SDG-CLASS>
                    </SDG-CLASSES>
                </SDG-DEF>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestReadSdgDef:
    """
    Test readSdgDef and the whole SdgDef family.
    """

    def test_read_family(self):
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(CONTENT)

            document = AUTOSAR.getInstance()
            document.clear()
            parser = ARXMLParser()
            parser.load(file_path, document)

            pkg = document.getARPackages()[0]
            sdg_def = pkg.getReferrableElement("MySdgDef")
            assert sdg_def is not None

            sdg_classes = sdg_def.getSdgClasses()
            assert len(sdg_classes) == 1
            sdg_class = sdg_classes[0]
            assert sdg_class.getShortName() == "MySdgClass"
            assert sdg_class.getGid().getValue() == "MY-CLASS-GID"
            assert sdg_class.getExtendsMetaClass() == "ArPackage"
            assert sdg_class.getCaption().getValue() is True

            attributes = sdg_class.getAttributes()
            assert len(attributes) == 6

            by_type = {}
            for attribute in attributes:
                by_type.setdefault(type(attribute).__name__, []).append(attribute)

            prim = by_type["SdgPrimitiveAttribute"][0]
            assert prim.getShortName() == "Severity"
            assert prim.getGid().getValue() == "SEVERITY"
            assert prim.getMax().getValue() == "3"
            assert prim.getPattern().getValue() == "critical|significant|minor|low"

            prim_wv = by_type["SdgPrimitiveAttributeWithVariation"][0]
            assert prim_wv.getVariation().getValue() is False
            assert prim_wv.getValidBindingTimes()[0].getValue() == "POST-BUILD"

            sdg_ref = by_type["SdgReference"][0]
            assert sdg_ref.getDestSdgRef().getValue() == "/AUTOSAR/SdgDefs/MySdgDef/MySdgClass"
            assert sdg_ref.getDestSdgRef().getDest() == "SDG-CLASS"

            agg = by_type["SdgAggregationWithVariation"][0]
            assert agg.getGid().getValue() == "SUB-SDG"
            assert agg.getSubSdgRef().getValue() == "/AUTOSAR/SdgDefs/MySdgDef/MySdgClass"

            fref = by_type["SdgForeignReference"][0]
            assert fref.getDestMetaClass() == "ARPackage"

            fref_wv = by_type["SdgForeignReferenceWithVariation"][0]
            assert fref_wv.getDestMetaClass() == "ARPackage"

            refs = sdg_class.getSdgConstraintRefs()
            assert len(refs) == 1
            assert refs[0].getValue() == "/AUTOSAR/MyConstraint"
            assert refs[0].getDest() == "TRACEABLE-TEXT"
        finally:
            os.remove(file_path)
