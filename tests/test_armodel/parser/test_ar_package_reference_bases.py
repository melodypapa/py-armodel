"""
Tests for parsing ARPackage REFERENCE-BASES elements — Table 4.1 (referenceBase aggregation).

Round-trip counterpart: tests/test_armodel/writer/test_ar_package_reference_bases.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _make_package() -> ARPackage:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ARPackage(ar_root, "TestPackage")


class TestReadReferenceBases:
    """
    Test readReferenceBases (ARPackage.referenceBase, Table 4.1).
    """

    def test_read_reference_base_fields(self, parser):
        """
        Test that a REFERENCE-BASE element populates every field value.
        """
        package = _make_package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <REFERENCE-BASES>
                    <REFERENCE-BASE>
                        <SHORT-LABEL>DefaultBase</SHORT-LABEL>
                        <IS-DEFAULT>true</IS-DEFAULT>
                        <IS-GLOBAL>false</IS-GLOBAL>
                        <BASE-IS-THIS-PACKAGE>true</BASE-IS-THIS-PACKAGE>
                        <PACKAGE-REF DEST='AR-PACKAGE'>/AUTOSAR/TestPackage</PACKAGE-REF>
                    </REFERENCE-BASE>
                </REFERENCE-BASES>
            </AR-PACKAGE>"""
        )

        parser.readReferenceBases(element, package)

        bases = package.getReferenceBases()
        assert len(bases) == 1
        base = bases[0]
        assert base.getShortLabel().getValue() == "DefaultBase"
        assert base.getIsDefault().getValue() is True
        assert base.getIsGlobal().getValue() is False
        assert base.getBaseIsThisPackage().getValue() is True
        assert base.getPackageRef().getValue() == "/AUTOSAR/TestPackage"

    def test_read_multiple_reference_bases(self, parser):
        """
        Test that multiple REFERENCE-BASE elements are all appended.
        """
        package = _make_package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <REFERENCE-BASES>
                    <REFERENCE-BASE>
                        <SHORT-LABEL>Base1</SHORT-LABEL>
                    </REFERENCE-BASE>
                    <REFERENCE-BASE>
                        <SHORT-LABEL>Base2</SHORT-LABEL>
                    </REFERENCE-BASE>
                </REFERENCE-BASES>
            </AR-PACKAGE>"""
        )

        parser.readReferenceBases(element, package)

        bases = package.getReferenceBases()
        assert len(bases) == 2
        assert bases[0].getShortLabel().getValue() == "Base1"
        assert bases[1].getShortLabel().getValue() == "Base2"

    def test_read_empty_reference_bases(self, parser):
        """
        Test that an AR-PACKAGE without REFERENCE-BASES leaves the list empty.
        """
        package = _make_package()
        element = ET.fromstring(f"<AR-PACKAGE xmlns='{NS}'></AR-PACKAGE>")

        parser.readReferenceBases(element, package)

        assert package.getReferenceBases() == []

    def test_read_global_elements_and_in_package_refs(self, parser):
        """
        Test that GLOBAL-ELEMENTS and GLOBAL-IN-PACKAGE-REFS are populated.

        Spec: AUTOSAR_FO_TPS_GenericStructureTemplate.pdf, Table 4.14, p.72
        globalElement (ReferrableSubtypesEnum, *) and globalInPackage (ARPackage, *)
        XSD sequence: SHORT-LABEL, IS-DEFAULT, GLOBAL-IN-PACKAGE-REFS, GLOBAL-ELEMENTS, PACKAGE-REF
        """
        package = _make_package()
        element = ET.fromstring(
            f"""<AR-PACKAGE xmlns='{NS}'>
                <REFERENCE-BASES>
                    <REFERENCE-BASE>
                        <SHORT-LABEL>globals</SHORT-LABEL>
                        <GLOBAL-IN-PACKAGE-REFS>
                            <GLOBAL-IN-PACKAGE-REF DEST='AR-PACKAGE'>/AUTOSAR/TestPackage</GLOBAL-IN-PACKAGE-REF>
                            <GLOBAL-IN-PACKAGE-REF DEST='AR-PACKAGE'>/AUTOSAR/Other</GLOBAL-IN-PACKAGE-REF>
                        </GLOBAL-IN-PACKAGE-REFS>
                        <GLOBAL-ELEMENTS>
                            <GLOBAL-ELEMENT>TRACEABLE</GLOBAL-ELEMENT>
                            <GLOBAL-ELEMENT>CHAPTER</GLOBAL-ELEMENT>
                        </GLOBAL-ELEMENTS>
                    </REFERENCE-BASE>
                </REFERENCE-BASES>
            </AR-PACKAGE>"""
        )

        parser.readReferenceBases(element, package)

        base = package.getReferenceBases()[0]

        global_elements = base.getGlobalElements()
        assert len(global_elements) == 2
        assert global_elements[0].getValue() == "TRACEABLE"
        assert global_elements[1].getValue() == "CHAPTER"

        global_in_package_refs = base.getGlobalInPackageRefs()
        assert len(global_in_package_refs) == 2
        assert global_in_package_refs[0].getValue() == "/AUTOSAR/TestPackage"
        assert global_in_package_refs[0].getDest() == "AR-PACKAGE"
        assert global_in_package_refs[1].getValue() == "/AUTOSAR/Other"
