"""Writer round-trip tests for ApplicationPartition (Table 5.5, p.201).

Empty-attribute ARElement aggregated by ARPackage.element: writeApplicationPartition
calls writeIdentifiable on the APPLICATION-PARTITION element exactly once (the XSD
complexType AUTOSAR_00052.xsd l.3761 owns no elements beyond the base groups, so the
IDENTIFIABLE emission order SHORT-NAME, DESC, CATEGORY governs the children) and the
writeARPackageElement dispatch emits the element into the package ELEMENTS.

Round-trip counterpart: tests/test_armodel/parser/test_application_partition.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartition
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _full_partition() -> ApplicationPartition:
    pkg = AUTOSAR.getInstance().createARPackage("ApplicationPartitions")
    app_partition = pkg.createApplicationPartition("AP1")
    category = app_partition.getCategory()
    assert category is None
    app_partition.setCategory(_category("APPLICATION_PARTITION"))
    return app_partition


def _category(value: str):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString

    category = CategoryString()
    category.setValue(value)
    return category


def _write_partition(app_partition):
    parent = ET.Element("PARENT")
    ARXMLWriter().writeApplicationPartition(parent, app_partition)
    return parent


class TestWriteApplicationPartition:
    def test_entry_point_emits_identifiable_level(self):
        parent = _write_partition(_full_partition())

        app_partition_element = parent.find("APPLICATION-PARTITION")
        assert app_partition_element is not None
        assert [child.tag for child in app_partition_element] == ["SHORT-NAME", "CATEGORY"]
        assert app_partition_element.find("SHORT-NAME").text == "AP1"
        assert app_partition_element.find("CATEGORY").text == "APPLICATION_PARTITION"

    def test_bare_partition_emits_short_name_only(self):
        pkg = AUTOSAR.getInstance().createARPackage("ApplicationPartitions")
        app_partition = pkg.createApplicationPartition("AP2")

        parent = _write_partition(app_partition)
        app_partition_element = parent.find("APPLICATION-PARTITION")

        assert [child.tag for child in app_partition_element] == ["SHORT-NAME"]
        assert app_partition_element.find("SHORT-NAME").text == "AP2"


class TestApplicationPartitionRoundTrip:
    def test_round_trip_through_ar_package_save_load(self):
        """The full ARPackage ELEMENTS path: writeARPackageElement emits the APPLICATION-PARTITION and the parser dispatch reads it back."""
        source = _full_partition()
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, AUTOSAR.getInstance())

            document = AUTOSAR.getInstance()
            document.clear()
            ARXMLParser(options={"warning": True}).load(file_path, document)

            pkg = document.getARPackages()[0]
            partitions = [e for e in pkg.getReferrableElements() if isinstance(e, ApplicationPartition)]
            assert len(partitions) == 1
            round_tripped = partitions[0]
            assert round_tripped.getShortName() == source.getShortName()
            assert round_tripped.getCategory().getValue() == "APPLICATION_PARTITION"
        finally:
            os.remove(file_path)
