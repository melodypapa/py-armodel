
from abc import ABCMeta
from typing import List
from colorama import Fore

import re
import logging
import xml.etree.ElementTree as ET

from ..models.m2.autosar_templates.autosar_top_level_structure import AUTOSAR
from ..models.ar_ref import RefType
from ..models.ar_object import ARBoolean, ARFloat, ARLiteral, ARNumerical, ARObject
from ..models.general_structure import Limit


class AbstractARXMLParser:
    __metaclass__ = ABCMeta
     
    def __init__(self, options = None) -> None:
        if type(self) == AbstractARXMLParser:
            raise NotImplementedError("AbstractArxmlParser is an abstract class.")
        
        self.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        self.options = {}
        self.options['warning'] = False
        self.logger = logging.getLogger()
        
        self._processOptions(options=options)

    def getTagName(self, tag: ET.Element) -> str:
        if isinstance(tag, ET.Element):
            tag = tag.tag
        if isinstance(tag, str):
            return tag.replace("{%s}" % self.nsmap["xmlns"], "")
        raise ValueError("Invalid Tag type <%s>" % type(tag))

    def _processOptions(self, options):
        if options:
            if 'warning' in options:
                self.options['warning'] = options['warning']

    def _raiseError(self, error_msg):
        if (self.options['warning'] == True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)
        
    def _raiseWarning(self, error_msg):
        self.logger.warning(error_msg)
        
    def getPureTagName(self, tag):
        return re.sub(r'\{[\w:\/.]+\}(\w+)', r'\1', tag)

    '''
    def getChildElement(self, short_name: str, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            return child_element.text
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))
    '''
    '''
    def getChildElementOptionalValue(self, element: ET.Element, key: str) -> str:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            if child_element.text is None:
                return ""
            return child_element.text
        return None
    '''
    
    def getChildElementLiteral(self, short_name: str, element: ET.Element, key: str) -> ARLiteral:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            literal = ARLiteral()
            self.readElementAttributes(child_element, literal)
            literal._value = child_element.text
            return literal
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))
        
    def getChildElementLiteralValueList(self, element: ET.Element, key: str) -> ARFloat:
        child_elements = element.findall("./xmlns:%s" % key, self.nsmap)
        results = []
        for child_element in child_elements:
            literal = ARLiteral()
            literal.setValue(child_element.text)
            results.append(literal)
        return results

    def getChildElementOptionalLiteral(self, element: ET.Element, key: str) -> ARLiteral:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        literal = None
        if (child_element is not None):
            self.logger.debug("readChildOptionalElementLiteral : %s" % child_element.text)
            literal = ARLiteral()
            self.readElementAttributes(child_element, literal)
            # Patch for empty element <USED-CODE-GENERATOR></USED-CODE-GENERATOR>
            if child_element.text is None:      
                literal.setValue("")
            else:
                literal.setValue(child_element.text)
        return literal

    def _convertStringToBooleanValue(self, value: str) -> bool:
        if (value == "true"):
            return True
        return False
    
    def getChildElementOptionalFloatValue(self, element: ET.Element, key: str) -> ARFloat:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        float_value = None
        if (child_element is not None) and (child_element.text is not None):
            float_value = ARFloat()
            float_value.setValue(child_element.text)
        return float_value
    
    def getChildElementFloatValueList(self, element: ET.Element, key: str) -> ARFloat:
        child_elements = element.findall("./xmlns:%s" % key, self.nsmap)
        results = []
        for child_element in child_elements:
            float_value = ARFloat()
            float_value.setValue(child_element.text)
            results.append(float_value)
        return results

    def getChildElementBooleanValue(self, short_name: str, element: ET.Element, key: str) -> ARBoolean:
        literal = self.getChildElementLiteral(short_name, element, key)
        bool_value = ARBoolean()
        bool_value.timestamp = literal.timestamp
        bool_value.value = self._convertStringToBooleanValue(literal._value)
        return bool_value

    def getChildElementOptionalBooleanValue(self, element: ET.Element, key: str) -> ARBoolean:
        literal = self.getChildElementOptionalLiteral(element, key)
        if (literal == None):
            return None
        bool_value = ARBoolean()
        bool_value.timestamp = literal.timestamp
        bool_value.setValue(literal.getValue())
        return bool_value

    def _convertStringToNumberValue(self, value) -> int:
        m = re.match(r"0x([0-9a-f]+)", value, re.I)
        if (m):
            return int(m.group(1), 16)
        return int(value)

    '''
    def getChildElementNumberValue(self, short_name: str, element: ET.Element, key: str) -> int:
        value = self.getChildElement(short_name, element, key)
        return self._convertStringToNumberValue(value)
    

    def getChildElementOptionalNumberValue(self, element: ET.Element, key: str) -> int:
        value = self.getChildElementOptionalValue(element, key)
        if (value == None):
            return None
        return self._convertStringToNumberValue(value)
    '''
    
    def getChildElementOptionalNumericalValue(self, element: ET.Element, key: str) -> ARNumerical:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if child_element == None:
            return None
        numerical = ARNumerical()
        self.readElementAttributes(child_element, numerical)
        numerical.setValue(child_element.text)
        return numerical
        
    def getChildElementNumericalValueList(self, element: ET.Element, key: str) -> List[ARNumerical]:
        child_elements = element.findall("./xmlns:%s" % key, self.nsmap)
        results = []
        for child_element in child_elements:
            numerical = ARNumerical()
            numerical.setValue(child_element.text)
            results.append(numerical)
        return results
    
    def getChildLimitElement(self, element: ET.Element, key: str) -> Limit:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            limit = Limit()
            self.readElementAttributes(child_element, limit)
            if ('INTERVAL-TYPE' in child_element.attrib):
                limit.intervalType = child_element.attrib['INTERVAL-TYPE']
            else:
                limit.intervalType = None
            limit.value = child_element.text
            return limit
        return None
    
    def _getChildElementRefTypeDestAndValue(self, element) -> RefType:
        ref = RefType()
        ref.dest = element.attrib['DEST']
        ref.value = element.text
        return ref

    def getChildElementRefType(self, short_name: str, element: ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        self._raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def getChildElementOptionalRefType(self, element:ET.Element, key: str) -> RefType:
        child_element = element.find("./xmlns:%s" % key, self.nsmap)
        if (child_element is not None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        return None

    def getChildElementRefTypeList(self, element: ET.Element, key: str) -> List[RefType]:
        child_elements = self.findall(element, key)
        results = []
        for child_element in child_elements:
            ref = RefType()
            ref.dest = child_element.attrib['DEST']
            ref.value = child_element.text
            results.append(ref)
        return results
    
    def readElementOptionalAttrib(self, element: ET.Element, key: str) -> str:
        if key in element.attrib:
            return element.attrib[key]
        return None
    
    def readElementAttributes(self, element: ET.Element, ar_object: ARObject):
        ar_object.timestamp = self.readElementOptionalAttrib(element, "T")             # read the timestamp
        ar_object.uuid      = self.readElementOptionalAttrib(element, "UUID")          # read the uuid

        if ar_object.timestamp is not None:
            self.logger.debug("Timestamp: %s" % ar_object.timestamp)
        if ar_object.uuid is not None:
            self.logger.debug("UUID: %s" % ar_object.uuid)
    
    def getAUTOSARInfo(self, element: ET.Element, document: AUTOSAR):
        key = "{http://www.w3.org/2001/XMLSchema-instance}schemaLocation"
        if key in element.attrib:
            document.schema_location = element.attrib[key]
        
        self.logger.debug("schemaLocation %s" % document.schema_location)

    def getShortName(self, element: ET.Element) -> str:
        child_element = self.find(element, "SHORT-NAME")
        if child_element is None:
            raise ValueError("Short Name is required")
        return child_element.text

    def convert_find_key(self, key: str) -> str:
        keys = key.split("/")
        for idx, item in enumerate(keys):
            if item != "*" and item != ".":
                keys[idx] = "xmlns:%s" % item
        return "/".join(keys)
    
    def find(self, parent:ET.Element, key: str) -> ET.Element:
        return parent.find(self.convert_find_key(key), self.nsmap)
    
    def findall(self, parent: ET.Element, key: str) -> List[ET.Element]:
        return parent.findall(self.convert_find_key(key), self.nsmap)