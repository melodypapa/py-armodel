"""
Reader coverage for the CollectableElement inheritance path (Table 13.3).

CollectableElement contributes no XML of its own: Table 13.3 has no Attribute rows
and the AUTOSAR_00052.xsd group COLLECTABLE-ELEMENT is an empty `<xsd:sequence/>`.
Its reader coverage is therefore the shared readIdentifiable chain plus the
element-collection registry, both reached through its concrete subclass ARPackage
(and PackageableElement/ARElement below it).

Round-trip counterpart: tests/test_armodel/writer/test_ar_package_collectable_element.py
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.MSR.AsamHdo.BaseTypes import SwBaseType
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

UUID_VALUE = "DCE:6f1c0e0e-1111-2222-3333-444455556666"

PACKAGE_XML = """<AR-PACKAGE xmlns='%s' UUID='%s'>
    <SHORT-NAME>TestPackage</SHORT-NAME>
    <CATEGORY>STANDARD</CATEGORY>
    <DESC><L-2 L='EN'>Package description</L-2></DESC>
    <AR-PACKAGES>
        <AR-PACKAGE><SHORT-NAME>SubPackage</SHORT-NAME></AR-PACKAGE>
    </AR-PACKAGES>
    <ELEMENTS>
        <SW-BASE-TYPE><SHORT-NAME>MyBaseType</SHORT-NAME></SW-BASE-TYPE>
    </ELEMENTS>
</AR-PACKAGE>""" % (
    NS,
    UUID_VALUE,
)


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


def _read_package(parser) -> ARPackage:
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    package = ARPackage(ar_root, "TestPackage")
    parser.readARPackage(ET.fromstring(PACKAGE_XML), package)
    return package


class TestReadCollectableElementPath:
    """
    Test the Identifiable members and the element-collection registry inherited by
    a concrete CollectableElement subclass (ARPackage).
    """

    def test_read_identifiable_members(self, parser):
        """
        The Identifiable attributes reach the ARPackage through the
        CollectableElement -> Identifiable chain.
        """
        package = _read_package(parser)

        assert package.getShortName() == "TestPackage"
        assert package.getUuid() is not None
        assert package.getUuid().getValue() == UUID_VALUE
        assert package.getCategory() is not None
        assert package.getCategory().getValue() == "STANDARD"
        assert package.getDesc() is not None

    def test_read_element_registry_lookup(self, parser):
        """
        Sub-packages and contained elements are both reachable through getElement,
        with and without a type filter.
        """
        package = _read_package(parser)

        sub_package = package.getElement("SubPackage")
        assert isinstance(sub_package, ARPackage)
        assert sub_package.getShortName() == "SubPackage"
        assert package.getElement("SubPackage", ARPackage) is sub_package

        base_type = package.getElement("MyBaseType")
        assert isinstance(base_type, SwBaseType)
        assert package.getElement("MyBaseType", SwBaseType) is base_type
        assert package.getElement("MyBaseType", ARPackage) is None

        assert package.getElement("MissingElement") is None
        assert package.IsElementExists("MyBaseType") is True
        assert package.IsElementExists("MissingElement") is False

    def test_read_element_registry_contents(self, parser):
        """
        Sub-packages are kept out of the element list, so only the SW-BASE-TYPE is
        in the registry.
        """
        package = _read_package(parser)

        assert package.getTotalElement() == 1
        assert package.getElements() == [package.getElement("MyBaseType")]

    def test_read_root_element_lookup(self, parser):
        """
        AbstractAUTOSAR.getElement resolves a top level package.
        """
        _read_package(parser)

        root = AUTOSAR.getInstance()
        assert root.getElement("AUTOSAR") is root.getARPackages()[0]
        assert root.getElement("MissingPackage") is None
