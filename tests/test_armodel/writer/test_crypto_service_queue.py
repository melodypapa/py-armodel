"""Writer round-trip tests for CryptoServiceQueue (Table 6.53, p.381).

Top-level ARElement dispatched by writeARPackageElement (isinstance chain);
XSD child order QUEUE-SIZE (CRYPTO-SERVICE-QUEUE group, AUTOSAR_00052.xsd
l.26525). The QUEUE-SIZE element is omitted when the field is unset.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage, CryptoServiceQueue
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    PositiveInteger,
    String,
)
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"

XSD_CHILD_ORDER = [
    "QUEUE-SIZE",
]

UUID_VALUE = "7a1b2c3d-4e5f-4a6b-8c9d-0e1f2a3b4c5d"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _populate(queue: CryptoServiceQueue):
    size = PositiveInteger()
    size.setValue("32")
    queue.setQueueSize(size)


def _write_ar_package_element(queue: CryptoServiceQueue) -> ET.Element:
    parent = ET.Element("ELEMENTS")
    ARXMLWriter().writeARPackageElement(parent, queue)
    return parent


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<AR-PACKAGE>", "<AR-PACKAGE xmlns='%s'>" % NS, 1))


class TestCryptoServiceQueueWriter:
    def test_write_dispatch_creates_correct_tag(self):
        queue = AUTOSAR.getInstance().createARPackage("CryptoQueues").createCryptoServiceQueue("Queue1")
        parent = _write_ar_package_element(queue)

        assert len(parent) == 1
        child = parent.find("CRYPTO-SERVICE-QUEUE")
        assert child is not None
        assert child.find("SHORT-NAME").text == "Queue1"

    def test_write_field_values_and_xsd_element_order(self):
        queue = AUTOSAR.getInstance().createARPackage("CryptoQueues").createCryptoServiceQueue("Queue1")
        _populate(queue)

        child = _write_ar_package_element(queue).find("CRYPTO-SERVICE-QUEUE")
        assert child.find("QUEUE-SIZE").text == "32"
        children = [c.tag for c in child]
        assert children == ["SHORT-NAME"] + XSD_CHILD_ORDER

    def test_write_empty_omits_optional_elements(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoQueues")
        pkg.createCryptoServiceQueue("Empty")
        child = _write_ar_package_element(pkg.getReferrableElement("Empty", CryptoServiceQueue)).find("CRYPTO-SERVICE-QUEUE")

        assert child is not None
        for tag in XSD_CHILD_ORDER:
            assert child.find(tag) is None, tag

    def test_create_duplicate_returns_existing(self):
        pkg = AUTOSAR.getInstance().createARPackage("CryptoQueues")
        first = pkg.createCryptoServiceQueue("Queue1")
        second = pkg.createCryptoServiceQueue("Queue1")
        assert first is second
        assert isinstance(first, CryptoServiceQueue)

    def test_write_then_reparse_round_trip(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoQueues")
        queue = pkg.createCryptoServiceQueue("Queue1")
        _populate(queue)

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoQueues")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)

        re_queue = reloaded.getReferrableElement("Queue1", CryptoServiceQueue)
        assert re_queue is not None
        assert isinstance(re_queue, CryptoServiceQueue)
        assert re_queue.getQueueSize().getValue() == 32

    def test_round_trip_base_level_attributes(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoQueues")
        queue = pkg.createCryptoServiceQueue("Queue1")
        queue.setUuid(String().setValue(UUID_VALUE))
        queue.setChecksum(String().setValue("7"))
        queue.setTimestamp(DateTime().setValue("2025-04-04T00:00:00Z"))
        queue.setCategory("CRYPTO")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)
        node = _with_ns(parent).find("{%s}ELEMENTS" % NS).find("{%s}CRYPTO-SERVICE-QUEUE" % NS)
        assert node.attrib["UUID"] == UUID_VALUE
        assert node.attrib["S"] == "7"
        assert node.attrib["T"] == "2025-04-04T00:00:00Z"
        assert node.find("{%s}CATEGORY" % NS).text == "CRYPTO"

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoQueues")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)
        re_queue = reloaded.getReferrableElement("Queue1", CryptoServiceQueue)
        assert re_queue.getUuid().getValue() == UUID_VALUE
        assert re_queue.getChecksum().getValue() == "7"
        assert re_queue.getTimestamp().getValue() == "2025-04-04T00:00:00Z"
        assert re_queue.getCategory().getValue() == "CRYPTO"

    def test_round_trip_empty(self):
        from armodel.parser.arxml_parser import ARXMLParser

        pkg = AUTOSAR.getInstance().createARPackage("CryptoQueues")
        pkg.createCryptoServiceQueue("Queue1")

        parent = ET.Element("AR-PACKAGE")
        ARXMLWriter().writeARPackageElements(parent, pkg)

        reloaded = ARPackage(parent=AUTOSAR.getInstance(), short_name="CryptoQueues")
        ARXMLParser().readARPackageElements(_with_ns(parent), reloaded)

        re_queue = reloaded.getReferrableElement("Queue1", CryptoServiceQueue)
        assert re_queue is not None
        assert re_queue.getQueueSize() is None
