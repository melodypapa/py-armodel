"""
Regression tests for the Hw* heritage fix.

HwElement / HwType / HwPin / HwPinGroup are Identifiable per their own spec Base
rows (AUTOSAR_CP_TPS_ECUResourceTemplate Tables 2.4 / 2.3 / 2.7 / 2.5), while their
shared base HwDescriptionEntity is Referrable-only (Table 2.1). Because they used
to derive from HwDescriptionEntity alone, the shared reader stopped at
readReferrable and silently dropped the IDENTIFIABLE members — including the UUID
attributes these elements legitimately carry (5 live UUIDs in
tests/integration_tests/test_files/CanSystem.arxml).

The model-vs-model integration round-trip cannot detect that loss, so it is pinned
here.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR, HwElement, HwPinGroup, HwType
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import HwDescriptionEntity
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _snip(inner: str, root_tag: str = "HW-ELEMENT", **attribs) -> ET.Element:
    """Wrap an inner XML fragment in a root element bound to the AUTOSAR NS.

    `UUID` is an XML *attribute* of the element (XSD IDENTIFIABLE attributeGroup),
    so it is passed as a keyword argument, not as inner markup.
    """
    attrs = "".join(f' {k.replace("_", "-")}="{v}"' for k, v in attribs.items())
    return ET.fromstring(f"<{root_tag} xmlns='{NS}'{attrs}>{inner}</{root_tag}>")


class TestHwHeritageIsIdentifiable:
    """The concrete Hw* classes must be Identifiable even though their base is not."""

    @pytest.mark.parametrize("cls", [HwElement, HwType, HwPinGroup])
    def test_concrete_hw_classes_are_identifiable(self, cls):
        assert issubclass(cls, Identifiable)

    def test_hw_description_entity_stays_referrable_only(self):
        """Table 2.1: HwDescriptionEntity Base = ARObject, Referrable."""
        assert not issubclass(HwDescriptionEntity, Identifiable)


class TestReadHwIdentifiableMembers:
    def test_read_hw_element_identifiable_members(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>DemoECU</SHORT-NAME>"
            "<DESC><L-2 L='EN'>a demo ecu</L-2></DESC>"
            "<CATEGORY>ECU</CATEGORY>"
            "<ADMIN-DATA><LANGUAGE>EN</LANGUAGE></ADMIN-DATA>"
            "<INTRODUCTION><L-1>intro</L-1></INTRODUCTION>",
            UUID="DCE:9cbf9b19-2b21-4e71-b42a-0050d0871226",
        )

        obj = HwElement(AUTOSAR.getInstance(), "DemoECU")
        parser.readHwElement(element, obj)

        assert obj.getUuid().getValue() == "DCE:9cbf9b19-2b21-4e71-b42a-0050d0871226"
        assert obj.getDesc() is not None
        assert obj.getCategory().getValue() == "ECU"
        assert obj.getAdminData() is not None
        assert obj.getAdminData().getLanguage().getValue() == "EN"
        assert obj.getIntroduction() is not None

    def test_read_hw_type_uuid(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>AnalogInType</SHORT-NAME>",
            root_tag="HW-TYPE",
            UUID="DCE:f73f677c-1389-4425-83f8-921d567b2ad4",
        )

        obj = HwType(AUTOSAR.getInstance(), "AnalogInType")
        parser.readHwType(element, obj)

        assert obj.getUuid().getValue() == "DCE:f73f677c-1389-4425-83f8-921d567b2ad4"

    def test_read_hw_pin_group_uuid(self):
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>CAN1</SHORT-NAME>",
            root_tag="HW-PIN-GROUP",
            UUID="DCE:470adf34-a7c8-470b-9d3b-b843e01fa9a9",
        )

        obj = HwPinGroup(AUTOSAR.getInstance(), "CAN1")
        parser.readHwPinGroup(element, obj)

        assert obj.getUuid().getValue() == "DCE:470adf34-a7c8-470b-9d3b-b843e01fa9a9"

    def test_hw_description_entity_members_still_read(self):
        """Re-parenting must not drop the HwDescriptionEntity aggregations."""
        parser = ARXMLParser(options={"warning": True})
        element = _snip(
            "<SHORT-NAME>DemoECU</SHORT-NAME>"
            "<HW-TYPE-REF DEST='HW-TYPE'>/HwTypes/AnalogInType</HW-TYPE-REF>"
            "<HW-CATEGORY-REFS><HW-CATEGORY-REF DEST='HW-CATEGORY'>/HwCategories/Mcu</HW-CATEGORY-REF></HW-CATEGORY-REFS>",
        )

        obj = HwElement(AUTOSAR.getInstance(), "DemoECU")
        parser.readHwElement(element, obj)

        assert obj.getHwTypeRef() is not None
        assert obj.getHwTypeRef().getValue() == "/HwTypes/AnalogInType"
        assert len(obj.getHwCategoryRefs()) == 1
