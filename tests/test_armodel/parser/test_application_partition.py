"""Parser tests for ApplicationPartition (Table 5.5, p.201).

Empty-attribute ARElement aggregated by ARPackage.element: the XSD complexType
APPLICATION-PARTITION (AUTOSAR_00052.xsd l.3761) carries only the base groups
(AR-OBJECT -> REFERRABLE -> MULTILANGUAGE-REFERRABLE -> IDENTIFIABLE ->
COLLECTABLE-ELEMENT -> PACKAGEABLE-ELEMENT -> AR-ELEMENT) and an empty
APPLICATION-PARTITION group, so the reader owns the IDENTIFIABLE base level
(SHORT-NAME/UUID/CATEGORY/DESC) via readIdentifiable exactly once.
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR as AutosarDocument
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import ApplicationPartition
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


FULL_AUTOSAR = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>ApplicationPartitions</SHORT-NAME>
            <ELEMENTS>
                <APPLICATION-PARTITION UUID="7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b">
                    <SHORT-NAME>AP1</SHORT-NAME>
                    <CATEGORY>APPLICATION_PARTITION</CATEGORY>
                </APPLICATION-PARTITION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


EMPTY_AUTOSAR = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>ApplicationPartitions</SHORT-NAME>
            <ELEMENTS/>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


def _load(content: str):
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        document = AutosarDocument.getInstance()
        document.clear()
        ARXMLParser(options={"warning": True}).load(file_path, document)
        return document
    finally:
        os.remove(file_path)


class TestReadApplicationPartition:
    def test_read_identifiable_base_level(self):
        parser = ARXMLParser(options={"warning": True})
        element = ET.fromstring(
            f"<APPLICATION-PARTITION xmlns='{NS}' UUID='7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b'>" "<SHORT-NAME>AP1</SHORT-NAME>" "<CATEGORY>APPLICATION_PARTITION</CATEGORY>" "</APPLICATION-PARTITION>"
        )
        app_partition = ApplicationPartition(AutosarDocument.getInstance(), "Initial")
        parser.readApplicationPartition(element, app_partition)

        assert app_partition.getUuid().getValue() == "7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b"
        assert app_partition.getCategory().getValue() == "APPLICATION_PARTITION"

    def test_load_via_ar_package(self):
        """The ARPackage ELEMENTS dispatch reads an APPLICATION-PARTITION."""
        document = _load(FULL_AUTOSAR)

        pkg = document.getARPackages()[0]
        partitions = [e for e in pkg.getReferrableElements() if isinstance(e, ApplicationPartition)]
        assert len(partitions) == 1
        app_partition = partitions[0]
        assert app_partition.getShortName() == "AP1"
        assert app_partition.getUuid().getValue() == "7a1f2b3c-4d5e-4f60-8a9b-0c1d2e3f4a5b"
        assert app_partition.getCategory().getValue() == "APPLICATION_PARTITION"

    def test_read_empty_elements(self):
        """A package with an empty ELEMENTS wrapper creates no ApplicationPartition."""
        document = _load(EMPTY_AUTOSAR)

        pkg = document.getARPackages()[0]
        partitions = [e for e in pkg.getReferrableElements() if isinstance(e, ApplicationPartition)]
        assert partitions == []
