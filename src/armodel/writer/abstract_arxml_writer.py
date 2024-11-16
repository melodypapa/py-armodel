import sys
from abc import ABCMeta
import re
from xml.dom import minidom
from colorama import Fore

import logging
import xml.etree.cElementTree as ET

from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARLiteral, ARNumerical
from armodel.models.ar_ref import TRefType

from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean

class AbstractARXMLWriter:
    __metaclass__ = ABCMeta
     
    def __init__(self, options = None) -> None:
        if type(self) == AbstractARXMLWriter:
            raise NotImplementedError("AbstractARXMLWriter is an abstract class.")
        
        self.options = {}
        self.options['warning'] = False
        self.options['version'] = "4.2.2"
        self.logger = logging.getLogger()
        
        self._processOptions(options=options)

        self.nsmap = {
            "xmlns": "http://autosar.org/schema/r4.0", 
        }

    def _processOptions(self, options):
        if options:
            if 'warning' in options:
                self.options['warning'] = options['warning']

    def _raiseError(self, error_msg):
        if (self.options['warning'] == True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)
        
    def setARObjectAttributes(self, element: ET.Element, ar_obj: ARObject):
        if ar_obj.timestamp is not None:
            self.logger.debug("Timestamp: %s" % ar_obj.timestamp)
            element.attrib['T'] = ar_obj.timestamp
        if ar_obj.uuid is not None:
            self.logger.debug("UUID: %s" % ar_obj.uuid)
            element.attrib['UUID'] = ar_obj.uuid

    '''
    def setChildElementOptionalValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value
    '''

    '''
    def setChildElementOptionalNumberValue(self, element: ET.Element, key: str, value: str):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = str(value)
    '''

    def setChildElementOptionalNumericalValue(self, element: ET.Element, key: str, numerical: ARNumerical):
        if numerical is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, numerical)
            child_element.text = numerical._text

    def setChildElementOptionalLiteral(self, element: ET.Element, key: str, literal: ARLiteral):
        if literal is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, literal)
            if literal._value is not None:
                child_element.text = str(literal._value)

    def setChildElementOptionalRefType(self, parent: ET.Element, child_tag_name: str, ref: TRefType):
        if ref is not None:
            child_tag = ET.SubElement(parent, child_tag_name)
            if ref.dest is not None:
                child_tag.attrib['DEST'] = ref.dest
            if ref.value is not None:
                child_tag.text = ref.value

    def setChildElementOptionalFloatValue(self, element: ET.Element, key: str, value: ARFloat):
        if value is not None:
            child_element = ET.SubElement(element, key)
            child_element.text = value.getText()

    def setChildElementOptionalBooleanValue(self, element: ET.Element, key: str, value: ARBoolean) -> ET.Element:
        child_element = None
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, value)
            child_element.text = value.getText()
        return element

    def setChildElementOptionalLiteral(self, element: ET.Element, key: str, value: ARLiteral) -> ET.Element:
        child_element = None
        if value is not None:
            child_element = ET.SubElement(element, key)
            self.setARObjectAttributes(child_element, value)
            child_element.text = value.getText()
        return element      
        
    def patch_xml(self, xml: str) -> str:
        #xml = xml.replace("<SW-DATA-DEF-PROPS-CONDITIONAL/>","<SW-DATA-DEF-PROPS-CONDITIONAL></SW-DATA-DEF-PROPS-CONDITIONAL>")
        xml = re.sub(r"\<([\w-]+)\/\>",r"<\1></\1>", xml)
        xml = re.sub(r"<((\w+)\s+\w+=\"\w+\")\/>", r"<\1></\2>", xml)
        #xml = xml.replace("<USES-END-TO-END-PROTECTION>false</USES-END-TO-END-PROTECTION>", "<USES-END-TO-END-PROTECTION>0</USES-END-TO-END-PROTECTION>")
        return xml

    def saveToFile(self, filename, root: ET.Element):
        if sys.version_info <= (3,9):
            xml = ET.tostring(root, encoding = "UTF-8", short_empty_elements = False)
        else:
            xml = ET.tostring(root, encoding = "UTF-8", xml_declaration = True, short_empty_elements = False)
        
        dom = minidom.parseString(xml.decode())
        xml = dom.toprettyxml(indent = "  ", encoding = "UTF-8")

        text = self.patch_xml(xml.decode())
    
        with open(filename, "w", encoding="utf-8") as f_out:
            #f_out.write(xml.decode())
            f_out.write(text)