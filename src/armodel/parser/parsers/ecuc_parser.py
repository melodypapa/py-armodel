"""
Parser for AUTOSAR ECUC configuration elements.

Handles:
- EcucValueCollection
- EcucModuleConfigurationValues
- EcucContainerValue
- EcucParameterValue
- EcucModuleDef
- EcucParamDef (Boolean, String, Integer, Float, Enumeration)
- EcucAddInfoParamDef
- EcucConditionFormula
- EcucDefinitionCollection
- EcucDestinationUriDef
- EcucDestinationUriDefSet
- EcucDestinationUriPolicy
- EcucLinkerSymbolDef
- EcucMultilineStringParamDef
- EcucParameterDerivationFormula
- EcucQuery
- EcucQueryExpression
- EcucParamConfContainerDef
"""
from typing import List
import xml.etree.ElementTree as ET

from ..base_arxml_parser import BaseARXMLParser
from ...models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucAbstractReferenceValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucContainerValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucInstanceReferenceValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucModuleConfigurationValues
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucNumericalParamValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucParameterValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucReferenceValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucTextualParamValue
from ...models.M2.AUTOSARTemplates.ECUCDescriptionTemplate import EcucValueCollection
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractConfigurationClass
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractInternalReferenceDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractReferenceDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucAbstractStringParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucBooleanParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucChoiceContainerDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucCommonAttributes
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucContainerDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucDefinitionElement
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucEnumerationLiteralDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucEnumerationParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFloatParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucFunctionNameDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucIntegerParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucModuleDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucMultiplicityConfigurationClass
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParamConfContainerDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucParameterDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucReferenceDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucStringParamDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucSymbolicNameReferenceDef
from ...models.M2.AUTOSARTemplates.ECUCParameterDefTemplate import EcucValueConfigurationClass


class EcucParser(BaseARXMLParser):
    """
    Parser for AUTOSAR ECUC configuration elements.

    Handles ECU configuration values and parameter definitions
    for the ECU Configuration (ECUC) template.
    """

    def __init__(self, options=None):
        """Initialize EcucParser."""
        super().__init__(options)

    # ========================================================================
    # ECUC Definition Elements
    # ========================================================================

    def readEcucDefinitionElement(
        self, element: ET.Element, def_element: EcucDefinitionElement
    ):
        def_element.setLowerMultiplicity(
            self.getChildElementOptionalPositiveInteger(element, "LOWER-MULTIPLICITY")
        )
        def_element.setUpperMultiplicity(
            self.getChildElementOptionalPositiveInteger(element, "UPPER-MULTIPLICITY")
        )
        def_element.setScope(self.getChildElementOptionalLiteral(element, "SCOPE"))

    def readEcucModuleDefSupportedConfigVariants(
        self, element: ET.Element, module_def: EcucModuleDef
    ):
        for variant in self.getChildElementLiteralValueList(
            element, "SUPPORTED-CONFIG-VARIANTS/SUPPORTED-CONFIG-VARIANT"
        ):
            module_def.addSupportedConfigVariant(variant)

    def readEcucAbstractConfigurationClass(
        self, element: ET.Element, cfg_class: EcucAbstractConfigurationClass
    ):
        self.readARObjectAttributes(element, cfg_class)
        cfg_class.setConfigClass(self.getChildElementOptionalLiteral(element, "CONFIG-CLASS"))
        cfg_class.setConfigVariant(
            self.getChildElementOptionalLiteral(element, "CONFIG-VARIANT")
        )

    def readEcucMultiplicityConfigurationClass(
        self, element: ET.Element, cfg_class: EcucMultiplicityConfigurationClass
    ):
        self.readEcucAbstractConfigurationClass(element, cfg_class)

    def getEcucMultiplicityConfigurationClasses(
        self, element: ET.Element,
    ) -> List[EcucMultiplicityConfigurationClass]:
        cfg_classes = []
        for child_element in self.findall(element, "MULTIPLICITY-CONFIG-CLASSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-MULTIPLICITY-CONFIGURATION-CLASS":
                cfg_class = EcucMultiplicityConfigurationClass()
                self.readEcucMultiplicityConfigurationClass(child_element, cfg_class)
                cfg_classes.append(cfg_class)
            else:
                self.notImplemented(
                    "Unsupported MultiplicityConfigClass <%s>" % tag_name
                )
        return cfg_classes

    def readEcucContainerDef(self, element: ET.Element, container_def: EcucContainerDef):
        self.readEcucDefinitionElement(element, container_def)
        for cfg_class in self.getEcucMultiplicityConfigurationClasses(element):
            container_def.addMultiplicityConfigClass(cfg_class)
        container_def.setPostBuildVariantMultiplicity(
            self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY")
        )
        container_def.setRequiresIndex(
            self.getChildElementOptionalBooleanValue(element, "REQUIRES-INDEX")
        )
        container_def.setMultipleConfigurationContainer(
            self.getChildElementOptionalBooleanValue(element, "MULTIPLE-CONFIGURATION-CONTAINER")
        )

    def readEcucValueConfigurationClass(
        self, element: ET.Element, cfg_class: EcucValueConfigurationClass
    ):
        self.readEcucAbstractConfigurationClass(element, cfg_class)

    def getEcucValueConfigurationClasses(
        self, element: ET.Element,
    ) -> List[EcucValueConfigurationClass]:
        cfg_classes = []
        for child_element in self.findall(element, "VALUE-CONFIG-CLASSES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-VALUE-CONFIGURATION-CLASS":
                cfg_class = EcucValueConfigurationClass()
                self.readEcucValueConfigurationClass(child_element, cfg_class)
                cfg_classes.append(cfg_class)
            else:
                self.notImplemented("Unsupported ValueConfigClass <%s>" % tag_name)
        return cfg_classes

    def readEcucCommonAttributes(
        self, element: ET.Element, common_attrs: EcucCommonAttributes
    ):
        self.readEcucDefinitionElement(element, common_attrs)
        for cfg_class in self.getEcucMultiplicityConfigurationClasses(element):
            common_attrs.addMultiplicityConfigClass(cfg_class)
        common_attrs.setOrigin(self.getChildElementOptionalLiteral(element, "ORIGIN"))
        common_attrs.setPostBuildVariantMultiplicity(
            self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-MULTIPLICITY")
        )
        common_attrs.setPostBuildVariantValue(
            self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-VALUE")
        )
        common_attrs.setRequiresIndex(
            self.getChildElementOptionalBooleanValue(element, "REQUIRES-INDEX")
        )
        for cfg_class in self.getEcucValueConfigurationClasses(element):
            common_attrs.addValueConfigClass(cfg_class)

    def readEcucParameterDef(self, element: ET.Element, param_def: EcucParameterDef):
        self.readEcucCommonAttributes(element, param_def)
        param_def.setDerivation(self.getChildElementOptionalLiteral(element, "DERIVATION"))
        param_def.setSymbolicNameValue(
            self.getChildElementOptionalBooleanValue(element, "SYMBOLIC-NAME-VALUE")
        )
        param_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))

    def readEcucBooleanParamDef(
        self, element: ET.Element, param_def: EcucBooleanParamDef
    ):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(
            self.getChildElementOptionalBooleanValue(element, "DEFAULT-VALUE")
        )

    def readEcucAbstractStringParamDef(
        self, element: ET.Element, param_def: EcucAbstractStringParamDef
    ):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(
            self.getChildElementOptionalLiteral(element, "DEFAULT-VALUE")
        )
        param_def.setMaxLength(
            self.getChildElementOptionalIntegerValue(element, "MAX-LENGTH")
        )
        param_def.setMinLength(
            self.getChildElementOptionalIntegerValue(element, "MIN-LENGTH")
        )
        param_def.setRegularExpression(
            self.getChildElementOptionalLiteral(element, "REGULAR-EXPRESSION")
        )

    def readEcucStringParamDef(self, element: ET.Element, param_def: EcucStringParamDef):
        self.readEcucAbstractStringParamDef(element, param_def)

    def readEcucIntegerParamDef(
        self, element: ET.Element, param_def: EcucIntegerParamDef
    ):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(
            self.getChildElementOptionalIntegerValue(element, "DEFAULT-VALUE")
        )
        param_def.setMax(self.getChildElementOptionalIntegerValue(element, "MAX"))
        param_def.setMin(self.getChildElementOptionalIntegerValue(element, "MIN"))

    def readEcucFloatParamDef(self, element: ET.Element, param_def: EcucFloatParamDef):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(
            self.getChildElementOptionalFloatValue(element, "DEFAULT-VALUE")
        )
        param_def.setMax(self.getChildLimitElement(element, "MAX"))
        param_def.setMin(self.getChildLimitElement(element, "MIN"))

    def readEcucEnumerationLiteral(
        self, element: ET.Element, literal: EcucEnumerationLiteralDef
    ):
        self.readIdentifiable(element, literal)
        literal.setOrigin(self.getChildElementOptionalLiteral(element, "ORIGIN"))

    def readEcucEnumerationParamDefLiterals(
        self, element: ET.Element, literal_def: EcucEnumerationParamDef
    ):
        for child_element in self.findall(element, "LITERALS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-ENUMERATION-LITERAL-DEF":
                literal = literal_def.createLiteral(self.getShortName(child_element))
                self.readEcucEnumerationLiteral(child_element, literal)
            else:
                self.notImplemented("Unsupported EnumerationLiteral <%s>" % tag_name)

    def readEcucEnumerationParamDef(
        self, element: ET.Element, param_def: EcucEnumerationParamDef
    ):
        self.readEcucParameterDef(element, param_def)
        param_def.setDefaultValue(
            self.getChildElementOptionalLiteral(element, "DEFAULT-VALUE")
        )
        self.readEcucEnumerationParamDefLiterals(element, param_def)

    def readEcucFunctionNameDef(self, element: ET.Element, ref_def: EcucFunctionNameDef):
        self.readEcucAbstractStringParamDef(element, ref_def)
        child_element = self.find(
            element, "ECUC-FUNCTION-NAME-DEF-VARIANTS/ECUC-FUNCTION-NAME-DEF-CONDITIONAL"
        )
        if child_element is not None:
            ref_def.setDefaultValue(
                self.getChildElementOptionalLiteral(child_element, "DEFAULT-VALUE")
            )
            ref_def.setMinLength(
                self.getChildElementOptionalIntegerValue(child_element, "MIN-LENGTH")
            )
            ref_def.setMaxLength(
                self.getChildElementOptionalIntegerValue(child_element, "MAX-LENGTH")
            )

    def readEcucContainerDefParameters(
        self, element: ET.Element, container_def: EcucParamConfContainerDef
    ):
        for child_element in self.findall(element, "PARAMETERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-BOOLEAN-PARAM-DEF":
                param_def = container_def.createEcucBooleanParamDef(
                    self.getShortName(child_element)
                )
                self.readEcucBooleanParamDef(child_element, param_def)
            elif tag_name == "ECUC-STRING-PARAM-DEF":
                param_def = container_def.createEcucStringParamDef(
                    self.getShortName(child_element)
                )
                self.readEcucStringParamDef(child_element, param_def)
            elif tag_name == "ECUC-INTEGER-PARAM-DEF":
                param_def = container_def.createEcucIntegerParamDef(
                    self.getShortName(child_element)
                )
                self.readEcucIntegerParamDef(child_element, param_def)
            elif tag_name == "ECUC-FLOAT-PARAM-DEF":
                param_def = container_def.createEcucFloatParamDef(
                    self.getShortName(child_element)
                )
                self.readEcucFloatParamDef(child_element, param_def)
            elif tag_name == "ECUC-ENUMERATION-PARAM-DEF":
                param_def = container_def.createEcucEnumerationParamDef(
                    self.getShortName(child_element)
                )
                self.readEcucEnumerationParamDef(child_element, param_def)
            elif tag_name == "ECUC-FUNCTION-NAME-DEF":
                param_def = container_def.createEcucFunctionNameDef(
                    self.getShortName(child_element)
                )
                self.readEcucFunctionNameDef(child_element, param_def)
            else:
                self.notImplemented("Unsupported Parameter <%s>" % tag_name)

    def readEcucAbstractReferenceDef(
        self, element: ET.Element, ref_def: EcucAbstractReferenceDef
    ):
        self.readEcucCommonAttributes(element, ref_def)
        ref_def.setWithAuto(self.getChildElementOptionalBooleanValue(element, "WITH-AUTO"))

    def readEcucAbstractInternalReferenceDef(
        self, element: ET.Element, ref_def: EcucAbstractInternalReferenceDef
    ):
        self.readEcucAbstractReferenceDef(element, ref_def)

    def readEcucSymbolicNameReferenceDef(
        self, element: ET.Element, ref_def: EcucSymbolicNameReferenceDef
    ):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(
            self.getChildElementOptionalRefType(element, "DESTINATION-REF")
        )

    def readEcucReferenceDef(self, element: ET.Element, ref_def: EcucReferenceDef):
        self.readEcucAbstractInternalReferenceDef(element, ref_def)
        ref_def.setDestinationRef(
            self.getChildElementOptionalRefType(element, "DESTINATION-REF")
        )

    def readEcucContainerDefReferences(
        self, element: ET.Element, container_def: EcucParamConfContainerDef
    ):
        for child_element in self.findall(element, "REFERENCES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-SYMBOLIC-NAME-REFERENCE-DEF":
                ref_def = container_def.createEcucSymbolicNameReferenceDef(
                    self.getShortName(child_element)
                )
                self.readEcucSymbolicNameReferenceDef(child_element, ref_def)
            elif tag_name == "ECUC-REFERENCE-DEF":
                ref_def = container_def.createEcucReferenceDef(
                    self.getShortName(child_element)
                )
                self.readEcucReferenceDef(child_element, ref_def)
            else:
                self.notImplemented("Unsupported EcucReferenceDef <%s>" % tag_name)

    def readEcucContainerDefSubContainers(
        self, element: ET.Element, container_def: EcucParamConfContainerDef
    ):
        for child_element in self.findall(element, "SUB-CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                sub_container_def = container_def.createEcucParamConfContainerDef(
                    self.getShortName(child_element)
                )
                self.readEcucParamConfContainerDef(child_element, sub_container_def)
            elif tag_name == "ECUC-CHOICE-CONTAINER-DEF":
                sub_container_def = container_def.createEcucChoiceContainerDef(
                    self.getShortName(child_element)
                )
                self.readEcucChoiceContainerDef(child_element, sub_container_def)
            else:
                self.notImplemented("Unsupported SubContainer <%s>" % tag_name)

    def readEcucParamConfContainerDef(
        self, element: ET.Element, container_def: EcucParamConfContainerDef
    ):
        self.readEcucContainerDef(element, container_def)
        self.readEcucContainerDefParameters(element, container_def)
        self.readEcucContainerDefReferences(element, container_def)
        self.readEcucContainerDefSubContainers(element, container_def)

    def readEcucChoiceContainerDefChoices(
        self, element: ET.Element, container_def: EcucChoiceContainerDef
    ):
        for child_element in self.findall(element, "CHOICES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                ref_def = container_def.createEcucParamConfContainerDef(
                    self.getShortName(child_element)
                )
                self.readEcucParamConfContainerDef(child_element, ref_def)
            else:
                self.notImplemented("Unsupported Choice <%s>" % tag_name)

    def readEcucChoiceContainerDef(
        self, element: ET.Element, container_def: EcucChoiceContainerDef
    ):
        self.readEcucContainerDef(element, container_def)
        self.readEcucChoiceContainerDefChoices(element, container_def)

    def readEcucModuleDefContainers(self, element: ET.Element, module_def: EcucModuleDef):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-PARAM-CONF-CONTAINER-DEF":
                container_def = module_def.createEcucParamConfContainerDef(
                    self.getShortName(child_element)
                )
                self.readEcucParamConfContainerDef(child_element, container_def)
            elif tag_name == "ECUC-CHOICE-CONTAINER-DEF":
                container_def = module_def.createEcucChoiceContainerDef(
                    self.getShortName(child_element)
                )
                self.readEcucChoiceContainerDef(child_element, container_def)
            else:
                self.notImplemented("Unsupported Container <%s>" % tag_name)

    def readEcucModuleDef(self, element: ET.Element, module_def: EcucModuleDef):
        self.logger.debug("Read EcucModuleDef <%s>" % module_def.getShortName())
        self.readEcucDefinitionElement(element, module_def)
        module_def.setPostBuildVariantSupport(
            self.getChildElementOptionalBooleanValue(element, "POST-BUILD-VARIANT-SUPPORT")
        )
        self.readEcucModuleDefSupportedConfigVariants(element, module_def)
        self.readEcucModuleDefContainers(element, module_def)

    # ========================================================================
    # ECUC Value Collection
    # ========================================================================

    def readEcucValueCollectionEcucValues(
        self, element: ET.Element, parent: EcucValueCollection
    ):
        for child_element in self.findall(
            element, "ECUC-VALUES/ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL"
        ):
            ref = self.getChildElementOptionalRefType(
                child_element, "ECUC-MODULE-CONFIGURATION-VALUES-REF"
            )
            if ref is not None:
                parent.addEcucValueRef(ref)
            self.logger.debug(
                "EcucValue <%s> of EcucValueCollection <%s> has been added",
                ref.value,
                parent.getShortName(),
            )

    def readEcucValueCollection(
        self, element: ET.Element, collection: EcucValueCollection
    ):
        self.logger.debug("Read EcucValueCollection <%s>" % collection.getShortName())
        self.readIdentifiable(element, collection)
        collection.setEcuExtractRef(
            self.getChildElementOptionalRefType(element, "ECU-EXTRACT-REF")
        )
        self.readEcucValueCollectionEcucValues(element, collection)

    # ========================================================================
    # ECUC Parameter Values
    # ========================================================================

    def readEcucParameterValue(
        self, element: ET.Element, param_value: EcucParameterValue
    ):
        param_value.setDefinitionRef(
            self.getChildElementOptionalRefType(element, "DEFINITION-REF")
        )
        for annotation in self.getAnnotations(element):
            param_value.addAnnotation(annotation)

    def getEcucTextualParamValue(self, element: ET.Element) -> EcucTextualParamValue:
        param_value = EcucTextualParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(self.getChildElementOptionalLiteral(element, "VALUE"))
        return param_value

    def getEcucNumericalParamValue(self, element: ET.Element) -> EcucNumericalParamValue:
        param_value = EcucNumericalParamValue()
        self.readEcucParameterValue(element, param_value)
        param_value.setValue(
            self.getChildElementOptionalNumericalValue(element, "VALUE")
        )
        return param_value

    # ========================================================================
    # ECUC Container Values
    # ========================================================================

    def readEcucContainerValueParameterValues(
        self, element: ET.Element, container_value: EcucContainerValue
    ):
        for child_element in self.findall(element, "PARAMETER-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-TEXTUAL-PARAM-VALUE":
                container_value.addParameterValue(self.getEcucTextualParamValue(child_element))
            elif tag_name == "ECUC-NUMERICAL-PARAM-VALUE":
                container_value.addParameterValue(
                    self.getEcucNumericalParamValue(child_element)
                )
            else:
                self.notImplemented("Unsupported EcucParameterValue <%s>" % tag_name)

    def readEcucAbstractReferenceValue(
        self, element: ET.Element, value: EcucAbstractReferenceValue
    ):
        value.setDefinitionRef(
            self.getChildElementOptionalRefType(element, "DEFINITION-REF")
        )
        for annotation in self.getAnnotations(element):
            value.addAnnotation(annotation)

    def getEcucReferenceValue(self, element: ET.Element) -> EcucReferenceValue:
        value = EcucReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueRef(self.getChildElementOptionalRefType(element, "VALUE-REF"))
        return value

    def getAnyInstanceRef(self, element: ET.Element, key) -> AnyInstanceRef:
        instance_ref = None
        child_element = self.find(element, key)
        if child_element is not None:
            instance_ref = AnyInstanceRef()
            instance_ref.setBaseRef(
                self.getChildElementOptionalRefType(child_element, "BASE-REF")
            )
            for ref in self.getChildElementRefTypeList(
                child_element, "CONTEXT-ELEMENT-REF"
            ):
                instance_ref.addContextElementRef(ref)
            instance_ref.setTargetRef(
                self.getChildElementOptionalRefType(child_element, "TARGET-REF")
            )
        return instance_ref

    def getEcucInstanceReferenceValue(
        self, element: ET.Element,
    ) -> EcucInstanceReferenceValue:
        value = EcucInstanceReferenceValue()
        self.readEcucAbstractReferenceValue(element, value)
        value.setValueIRef(self.getAnyInstanceRef(element, "VALUE-IREF"))
        return value

    def readEcucContainerValueReferenceValues(
        self, element: ET.Element, container_value: EcucContainerValue
    ):
        for child_element in self.findall(element, "REFERENCE-VALUES/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-REFERENCE-VALUE":
                container_value.addReferenceValue(self.getEcucReferenceValue(child_element))
            elif tag_name == "ECUC-INSTANCE-REFERENCE-VALUE":
                container_value.addReferenceValue(
                    self.getEcucInstanceReferenceValue(child_element)
                )
            else:
                self.notImplemented("Unsupported EcucParameterValue <%s>" % tag_name)

    def readEcucContainerValue(self, element: ET.Element, container_value: EcucContainerValue):
        self.readIdentifiable(element, container_value)
        container_value.setDefinitionRef(
            self.getChildElementOptionalRefType(element, "DEFINITION-REF")
        )
        self.readEcucContainerValueParameterValues(element, container_value)
        self.readEcucContainerValueReferenceValues(element, container_value)
        self.readEcucContainerValueSubContainers(element, container_value)

    def readEcucContainerValueEcucContainerValue(
        self, element: ET.Element, parent: EcucContainerValue
    ):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createSubContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucContainerValueSubContainers(
        self, element: ET.Element, parent: EcucContainerValue
    ):
        for child_element in self.findall(element, "SUB-CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucContainerValueEcucContainerValue(child_element, parent)
            else:
                self.notImplemented("Unsupported Sub Container %s" % tag_name)

    # ========================================================================
    # ECUC Module Configuration Values
    # ========================================================================

    def readEcucModuleConfigurationValuesEcucContainerValue(
        self, element: ET.Element, parent: EcucModuleConfigurationValues
    ):
        short_name = self.getShortName(element)
        self.logger.debug("EcucContainerValue %s" % short_name)
        container_value = parent.createContainer(short_name)
        self.readEcucContainerValue(element, container_value)

    def readEcucModuleConfigurationValuesContainers(
        self, element: ET.Element, values: EcucModuleConfigurationValues
    ):
        for child_element in self.findall(element, "CONTAINERS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "ECUC-CONTAINER-VALUE":
                self.readEcucModuleConfigurationValuesEcucContainerValue(
                    child_element, values
                )
            else:
                self.notImplemented("Unsupported Container %s" % tag_name)

    def readEcucModuleConfigurationValues(
        self, element: ET.Element, values: EcucModuleConfigurationValues
    ):
        self.logger.debug("Read EcucModuleConfigurationValues %s" % values.getShortName())
        self.readIdentifiable(element, values)
        values.setDefinitionRef(
            self.getChildElementOptionalRefType(element, "DEFINITION-REF")
        )
        values.setImplementationConfigVariant(
            self.getChildElementOptionalLiteral(element, "IMPLEMENTATION-CONFIG-VARIANT")
        )
        values.setModuleDescriptionRef(
            self.getChildElementOptionalRefType(element, "MODULE-DESCRIPTION-REF")
        )
        self.readEcucModuleConfigurationValuesContainers(element, values)
