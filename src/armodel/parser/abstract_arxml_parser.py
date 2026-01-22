from abc import ABCMeta
from typing import List
from colorama import Fore

import re
import logging
import xml.etree.ElementTree as ET

from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARFloat, ARLiteral, ARNumerical, Boolean, DateTime
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer, PositiveInteger, TimeValue
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, Limit, RevisionLabelString


class AbstractARXMLParser:
    __metaclass__ = ABCMeta
     
    def __init__(self, options=None) -> None:
        if type(self) is AbstractARXMLParser:
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
        self.raiseError("Invalid Tag type <%s>" % type(tag))

    def _processOptions(self, options):
        if options:
            if 'warning' in options:
                self.options['warning'] = options['warning']

    def raiseError(self, error_msg):
        if (self.options['warning'] is True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise ValueError(error_msg)
        
    def notImplemented(self, error_msg):
        if (self.options['warning'] is True):
            self.logger.error(Fore.RED + error_msg + Fore.WHITE)
        else:
            raise NotImplementedError(error_msg)
        
    def raiseWarning(self, error_msg):
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
        child_element = self.find(element, key)
        if (child_element is not None):
            literal = ARLiteral()
            self.readARObjectAttributes(child_element, literal)
            literal._value = child_element.text
            return literal
        self.raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))
        
    def getChildElementLiteralValueList(self, element: ET.Element, key: str) -> List[ARLiteral]:
        child_elements = self.findall(element, key)
        results = []
        for child_element in child_elements:
            literal = ARLiteral()
            literal.setValue(child_element.text)
            results.append(literal)
        return results

    def getChildElementOptionalLiteral(self, element: ET.Element, key: str) -> ARLiteral:
        child_element = self.find(element, key)
        literal = None
        if (child_element is not None):
            # self.logger.debug("getChildElementOptionalLiteral : %s" % child_element.text)
            literal = ARLiteral()
            self.readARObjectAttributes(child_element, literal)
            # Patch for empty element <USED-CODE-GENERATOR></USED-CODE-GENERATOR>
            if child_element.text is None:
                literal.setValue("")
            else:
                literal.setValue(child_element.text)
        return literal
    
    def getChildElementOptionalRevisionLabelString(self, element: ET.Element, key: str) -> RevisionLabelString:
        child_element = self.find(element, key)
        literal = None
        if (child_element is not None) and (child_element.text is not None):
            # self.logger.debug("getChildElementOptionalRevisionLabelString : %s" % child_element.text)
            m = re.match(r'[0-9]+\.[0-9]+\.[0-9]+([\._;].*)?', child_element.text)
            if not m:
                raise ValueError("Invalid RevisionLabelString <%s>" % child_element.text)
            literal = RevisionLabelString()
            self.readARObjectAttributes(child_element, literal)
            # Patch for empty element <USED-CODE-GENERATOR></USED-CODE-GENERATOR>
            if child_element.text is None:
                literal.setValue("")
            else:
                literal.setValue(child_element.text)
        return literal
    
    def getChildElementOptionalDataTime(self, element: ET.Element, key: str) -> DateTime:
        return self.getChildElementOptionalLiteral(element, key)
    
    def _convertStringToBooleanValue(self, value: str) -> bool:
        if (value == "true"):
            return True
        return False
    
    def getChildElementOptionalFloatValue(self, element: ET.Element, key: str) -> ARFloat:
        child_element = self.find(element, key)
        float_value = None
        if (child_element is not None) and (child_element.text is not None):
            float_value = ARFloat()
            self.readARObjectAttributes(child_element, float_value)
            float_value.setValue(child_element.text)
        return float_value
    
    def getChildElementFloatValueList(self, element: ET.Element, key: str) -> ARFloat:
        child_elements = self.findall(element, key)
        results = []
        for child_element in child_elements:
            float_value = ARFloat()
            float_value.setValue(child_element.text)
            results.append(float_value)
        return results
    
    def getChildElementOptionalTimeValue(self, element: ET.Element, key: str) -> TimeValue:
        child_element = self.find(element, key)
        time_value = None
        if (child_element is not None) and (child_element.text is not None):
            time_value = TimeValue()
            time_value.setValue(child_element.text)
        return time_value

    '''
    def getChildElementBooleanValue(self, short_name: str, element: ET.Element, key: str) -> Boolean:
        literal = self.getChildElementLiteral(short_name, element, key)
        bool_value = Boolean()
        bool_value.timestamp = literal.timestamp
        bool_value.value = self._convertStringToBooleanValue(literal._value)
        return bool_value
    '''

    def getChildElementOptionalBooleanValue(self, element: ET.Element, key: str) -> Boolean:
        literal = self.getChildElementOptionalLiteral(element, key)
        if literal is None:
            return None
        if literal.getText() == "":
            return None
        bool_value = Boolean()
        bool_value.timestamp = literal.timestamp
        bool_value.setValue(literal.getText())
        return bool_value

    def _convertStringToNumberValue(self, value) -> int:
        m = re.match(r"0x([0-9a-f]+)", value, re.I)
        if (m):
            return int(m.group(1), 16)
        return int(value)

    def getChildElementOptionalNumericalValue(self, element: ET.Element, key: str) -> ARNumerical:
        child_element = self.find(element, key)
        if child_element is None:
            return None
        numerical = ARNumerical()
        self.readARObjectAttributes(child_element, numerical)
        if "SHORT-LABEL" in child_element.attrib:
            numerical.setShortLabel(child_element.attrib["SHORT-LABEL"])
        numerical.setValue(child_element.text)
        return numerical
    
    def getChildElementOptionalIntegerValue(self, element: ET.Element, key: str) -> Integer:
        child_element = self.find(element, key)
        if child_element is None:
            return None
        numerical = Integer()
        self.readARObjectAttributes(child_element, numerical)
        numerical.setValue(child_element.text)
        return numerical
    
    def getChildElementOptionalPositiveInteger(self, element: ET.Element, key: str) -> PositiveInteger:
        child_element = self.find(element, key)
        if child_element is None:
            return None
        if child_element.text is None:
            return None
        numerical = PositiveInteger()
        self.readARObjectAttributes(child_element, numerical)
        numerical.setValue(child_element.text)
        if numerical.getValue() < 0:
            raise ValueError("Invalid PositiveInteger <%s>" % child_element.text)
        return numerical
        
    def getChildElementNumericalValueList(self, element: ET.Element, key: str) -> List[ARNumerical]:
        child_elements = self.findall(element, key)
        results = []
        for child_element in child_elements:
            numerical = ARNumerical()
            numerical.setValue(child_element.text)
            results.append(numerical)
        return results
    
    def getChildLimitElement(self, element: ET.Element, key: str) -> Limit:
        child_element = self.find(element, key)
        if (child_element is not None):
            limit = Limit()
            self.readARObjectAttributes(child_element, limit)
            if ('INTERVAL-TYPE' in child_element.attrib):
                limit.intervalType = child_element.attrib['INTERVAL-TYPE']
            else:
                limit.intervalType = None
            limit.value = child_element.text
            return limit
        return None
    
    def _getChildElementRefTypeDestAndValue(self, element: ET.Element) -> RefType:
        ref = RefType()
        if 'BASE' in element.attrib:
            ref.setBase(element.attrib['BASE'])
        if 'DEST' in element.attrib:
            ref.setDest(element.attrib['DEST'])
        ref.setValue(element.text)
        return ref

    def getChildElementRefType(self, short_name: str, element: ET.Element, key: str) -> RefType:
        child_element = self.find(element, key)
        if (child_element is not None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        self.raiseError("The attribute %s of <%s> has not been defined" % (key, short_name))

    def getChildElementOptionalRefType(self, element: ET.Element, key: str) -> RefType:
        child_element = self.find(element, key)
        if (child_element is not None):
            return self._getChildElementRefTypeDestAndValue(child_element)
        return None

    def getChildElementRefTypeList(self, element: ET.Element, key: str) -> List[RefType]:
        child_elements = self.findall(element, key)
        results = []
        for child_element in child_elements:
            ref = RefType()
            if 'BASE' in child_element.attrib:
                ref.setBase(child_element.attrib['BASE'])
            if 'DEST' in child_element.attrib:
                ref.setDest(child_element.attrib['DEST'])
            ref.setValue(child_element.text)
            results.append(ref)
        return results
    
    def readElementOptionalAttrib(self, element: ET.Element, key: str) -> str:
        if key in element.attrib:
            return element.attrib[key]
        return None
    
    def readARObjectAttributes(self, element: ET.Element, ar_object: ARObject):
        ar_object.timestamp = self.readElementOptionalAttrib(element, "T")              # read the timestamp
        ar_object.uuid = self.readElementOptionalAttrib(element, "UUID")                # read the uuid

        AUTOSAR.getInstance().addARObject(ar_object)

        # if ar_object.timestamp is not None:
        #    self.logger.debug("Timestamp: %s" % ar_object.timestamp)

        '''
        if ar_object.uuid is not None:
            instance = AUTOSAR.getInstance()
            old_ar_object = instance.getARObjectByUUID(ar_object.uuid)
            if old_ar_object is not None:
                self.logger.warning(Fore.YELLOW + "Duplicate UUID <%s> / type <%s>" % (ar_object.uuid, type(old_ar_object)) + Fore.WHITE)
            else:
                instance.addARObject(ar_object)
            # self.logger.debug("UUID: %s" % ar_object.uuid)
        '''
    
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
       
    def find(self, parent: ET.Element, key: str) -> ET.Element:
        return parent.find(self.convert_find_key(key), self.nsmap)
    
    def findall(self, parent: ET.Element, key: str) -> List[ET.Element]:
        return parent.findall(self.convert_find_key(key), self.nsmap)
