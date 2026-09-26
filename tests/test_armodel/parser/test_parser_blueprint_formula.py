"""Reader tests for the BlueprintFormula element (BLUEPRINT-FORMULA).

Spec: R23-11 AUTOSAR_FO_TPS_StandardizationTemplate, Table C.16, p.163
(appendix C caption-shift: the body renders above the caption). XSD 00052 group
BLUEPRINT-FORMULA (line 9023): choice ECUC-REF / VERBATIM (+ the inherited
SW-SYSTEMCONST-DEPENDENT-FORMULA choice SYSC-STRING-REF / SYSC-REF); mixed="true".

NOTE: the sole consuming element VariationPoint.formalBlueprintCondition
(FORMAL-BLUEPRINT-CONDITION, XSD line 130040) is atp.Status="removed" in R23-11
and is deliberately not dispatched by readVariationPoint — this helper is pinned
at element level (PostBuildVariantCriterionValue precedent).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintFormula import (
    BlueprintFormula,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


class TestReadBlueprintFormula:
    def test_read_full_ecuc_verbatim_sysc_and_text(self):
        xml = (
            "<BLUEPRINT-FORMULA xmlns='%s'>"
            "defined(&amp;) informal term"
            "<ECUC-REF DEST='ECUC-MODULE-DEF'>/EcucDefs/MyModule</ECUC-REF>"
            "<VERBATIM><L-5 L='EN'>max(3, x)</L-5></VERBATIM>"
            "<SYSC-REF DEST='SW-SYSTEMCONST'>/SystemConstants/MyConst</SYSC-REF>"
            "</BLUEPRINT-FORMULA>" % NS
        )
        element = ET.fromstring(xml)

        formula = ARXMLParser().readBlueprintFormula(element, BlueprintFormula())

        assert isinstance(formula, BlueprintFormula)
        assert formula.getMixedString() == "defined(&) informal term"
        ecuc_ref = formula.getEcucRef()
        assert ecuc_ref is not None
        assert ecuc_ref.getValue() == "/EcucDefs/MyModule"
        assert ecuc_ref.getDest() == "ECUC-MODULE-DEF"
        verbatim = formula.getVerbatim()
        assert verbatim is not None
        assert verbatim.getL5s()[0].getValue() == "max(3, x)"
        assert formula.getSyscRef().getValue() == "/SystemConstants/MyConst"
        assert formula.getSyscStringRef() is None

    def test_read_ecuc_ref_only(self):
        xml = "<BLUEPRINT-FORMULA xmlns='%s'><ECUC-REF DEST='ECUC-PARAMETER-DEF'>/EcucDefs/MyModule/MyParam</ECUC-REF></BLUEPRINT-FORMULA>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readBlueprintFormula(element, BlueprintFormula())

        assert formula.getEcucRef().getValue() == "/EcucDefs/MyModule/MyParam"
        assert formula.getEcucRef().getDest() == "ECUC-PARAMETER-DEF"
        assert formula.getVerbatim() is None
        assert formula.getSyscRef() is None
        assert formula.getSyscStringRef() is None

    def test_read_verbatim_only(self):
        xml = "<BLUEPRINT-FORMULA xmlns='%s'><VERBATIM><L-5 L='DE'>Term</L-5></VERBATIM></BLUEPRINT-FORMULA>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readBlueprintFormula(element, BlueprintFormula())

        assert formula.getEcucRef() is None
        assert formula.getVerbatim().getL5s()[0].getValue() == "Term"

    def test_read_mixed_text_only(self):
        xml = "<BLUEPRINT-FORMULA xmlns='%s'>1 + 2</BLUEPRINT-FORMULA>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readBlueprintFormula(element, BlueprintFormula())

        assert formula.getMixedString() == "1 + 2"
        assert formula.getEcucRef() is None
        assert formula.getVerbatim() is None

    def test_read_empty_formula_leaves_all_none(self):
        xml = "<BLUEPRINT-FORMULA xmlns='%s'/>" % NS
        element = ET.fromstring(xml)

        formula = ARXMLParser().readBlueprintFormula(element, BlueprintFormula())

        assert isinstance(formula, BlueprintFormula)
        assert formula.getEcucRef() is None
        assert formula.getVerbatim() is None
        assert formula.getMixedString() is None
