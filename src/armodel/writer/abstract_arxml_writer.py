import logging
import re
import sys
import xml.etree.cElementTree as ET
from abc import ABC
from typing import Any, Dict, Optional
from xml.dom import minidom

from colorama import Fore

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    ARLiteral,
    ARType,
    Boolean,
    CIdentifier,
    CseCodeType,
    DateTime,
    Identifier,
    NameToken,
    Numerical,
    PositiveUnlimitedInteger,
    RefType,
    RegularExpression,
    RevisionLabelString,
    String,
    TimeValue,
    UriString,
    VerbatimString,
)
from armodel.models.M2.MSR.DataDictionary.RecordLayout import AxisIndexType


class AbstractARXMLWriter(ABC):
    """
    Abstract base class for ARXML writers providing common XML
    serialization utilities, namespace handling, and error/warning
    management.
    """

    # Legacy R3.x documents use the pre-R4 namespace and different package
    # wrappers (TOP-LEVEL-PACKAGES at root, SUB-PACKAGES inside AR-PACKAGE);
    # set by save() from the document's schema_location.
    _legacy_namespace = False

    def __init__(self, options=None) -> None:
        if type(self) is AbstractARXMLWriter:
            raise TypeError("AbstractARXMLWriter is an abstract class.")

        self.options: Dict[str, Any] = {}
        self.options["warning"] = False
        self.options["version"] = "4.2.2"
        self.options["unescape_entities"] = False
        self.options["validate"] = True
        self.logger = logging.getLogger()

        self._processOptions(options=options)

        self.nsmap = {
            "xmlns": "http://autosar.org/schema/r4.0",
        }

    def _processOptions(self, options):
        if options:
            if "warning" in options:
                self.options["warning"] = options["warning"]
            if "unescape_entities" in options:
                self.options["unescape_entities"] = options["unescape_entities"]
            if "validate" in options:
                self.options["validate"] = options["validate"]

    def _raiseError(self, error_msg):
        if self.options["warning"] is True:
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)

    def notImplemented(self, error_msg):
        if self.options["warning"] is True:
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise NotImplementedError(error_msg)

    def writeARObject(self, element: ET.Element, ar_obj: ARObject):
        checksum = ar_obj.getChecksum()
        if checksum is not None:
            value = checksum.getValue()
            if value is not None:
                element.attrib["S"] = value
        timestamp = ar_obj.getTimestamp()
        if timestamp is not None:
            value = timestamp.getValue()
            if value is not None:
                element.attrib["T"] = value
        # The uuid attribute (Table 4.4) is owned by Identifiable (see
        # Identifiable.py) and is emitted by writeIdentifiable.

    def writeARType(self, element: ET.Element, ar_type: ARType):
        # The ARType hierarchy (AUTOSAR primitive types) carries the timestamp as a
        # plain string. Per the XSD (AUTOSAR_00052.xsd, AR-OBJECT attributeGroup)
        # primitives carry only S/T — the uuid attribute lives in the IDENTIFIABLE
        # attributeGroup and is emitted by writeIdentifiable (see the uuid move in
        # docs/plan/sync-todo/Group1.md).
        if ar_type.timestamp is not None:
            element.attrib["T"] = ar_type.timestamp

    """
    def setChildElementOptionalValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value
    """

    def setChildElementOptionalStringValue(self, element: ET.Element, key: str, value: Optional[str]):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value

    def setChildElementOptionalNumericalValue(self, element: ET.Element, key: str, numerical: Optional[Numerical]):
        if numerical is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, numerical)
            short_label = numerical.getShortLabel()
            if short_label is not None:
                child_element.attrib["SHORT-LABEL"] = short_label
            if numerical._text is not None:
                child_element.text = numerical._text
            elif numerical._value is not None:
                child_element.text = str(numerical._value)

    def setChildElementOptionalIntegerValue(self, element: ET.Element, key: str, value: Optional[Numerical]):
        self.setChildElementOptionalNumericalValue(element, key, value)

    def setChildElementOptionalPositiveInteger(self, element: ET.Element, key: str, value: Optional[Numerical]):
        self.setChildElementOptionalNumericalValue(element, key, value)

    def setChildElementOptionalPositiveUnlimitedInteger(self, element: ET.Element, key: str, value: Optional[PositiveUnlimitedInteger]):
        self.setChildElementOptionalNumericalValue(element, key, value)

    def setChildElementOptionalNameToken(self, element: ET.Element, key: str, value: Optional[NameToken]):
        self.setChildElementOptionalLiteral(element, key, value)

    def setChildElementOptionalRevisionLabelString(self, element: ET.Element, key: str, literal: Optional[RevisionLabelString]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalAxisIndexType(self, element: ET.Element, key: str, value: Optional[AxisIndexType]):
        self.setChildElementOptionalLiteral(element, key, value)

    def setChildElementOptionalCseCodeType(self, element: ET.Element, key: str, literal: Optional[CseCodeType]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalAlignmentType(self, element: ET.Element, key: str, literal: Optional[AlignmentType]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalRegularExpression(self, element: ET.Element, key: str, literal: Optional[RegularExpression]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalCIdentifier(self, element: ET.Element, key: str, literal: Optional[CIdentifier]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalString(self, element: ET.Element, key: str, value: Optional[String]):
        self.setChildElementOptionalLiteral(element, key, value)

    def setChildElementOptionalDateTime(self, element: ET.Element, key: str, literal: Optional[DateTime]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalVerbatimString(self, element: ET.Element, key: str, literal: Optional[VerbatimString]):
        self.setChildElementOptionalLiteral(element, key, literal)

    def setChildElementOptionalRefType(self, parent: ET.Element, child_tag_name: str, ref: Optional[RefType]):
        if ref is not None:
            child_tag = ET.SubElement(parent, child_tag_name)
            base = ref.getBase()
            if base is not None:
                child_tag.attrib["BASE"] = base
            dest = ref.getDest()
            if dest is not None:
                child_tag.attrib["DEST"] = dest
            if ref.value is not None:
                child_tag.text = ref.value

    def setChildElementOptionalFloatValue(self, element: ET.Element, key: str, value: Optional[Numerical]):
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()

    def setChildElementOptionalTimeValue(self, element: ET.Element, key: str, value: Optional[TimeValue]):
        self.setChildElementOptionalFloatValue(element, key, value)

    def setChildElementOptionalBooleanValue(self, element: ET.Element, key: str, value: Optional[Boolean]) -> ET.Element:
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()
        return element

    def setChildElementOptionalUriString(self, element: ET.Element, key: str, value: Optional[UriString]):
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()
        return element

    def setChildElementOptionalLiteral(self, element: ET.Element, key: str, value: Optional[ARLiteral]) -> ET.Element:
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()
        return element

    def setChildElementOptionalNumerical(self, element: ET.Element, key: str, value: Optional[Numerical]) -> ET.Element:
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()
        return element

    def setChildElementOptionalIdentifier(self, element: ET.Element, key: str, value: Optional[Identifier]) -> ET.Element:
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.writeARType(child_element, value)
            child_element.text = value.getText()
        return element

    def patch_xml(self, xml: str) -> str:
        xml = re.sub(r"\<([\w-]+)\/\>", r"<\1></\1>", xml)

        if self.options.get("unescape_entities", False):
            xml = xml.replace("&quot;", '"')
            xml = xml.replace("&apos;", "'")

        return xml

    def saveToFile(self, filename, root: ET.Element):
        if sys.version_info <= (3, 9):
            xml = ET.tostring(root, encoding="UTF-8", short_empty_elements=False)
        else:
            xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True, short_empty_elements=False)

        dom = minidom.parseString(xml.decode())
        xml = dom.toprettyxml(indent="  ", encoding="UTF-8")

        text = self.patch_xml(xml.decode())

        with open(filename, "w", encoding="utf-8") as f_out:
            # f_out.write(xml.decode())
            f_out.write(text)
