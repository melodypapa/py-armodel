"""
Parser for AUTOSAR data type elements.

Handles:
- ApplicationDataType
- ImplementationDataType
- ApplicationRecordElement
- ApplicationArrayElement
- CompuMethod
- DataConstr
- Unit
- UnitGroup
- SwTextProps
- SwSystemconst
"""
import xml.etree.ElementTree as ET
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype import (
    Datatypes,
)
from ...models.M2.AUTOSARTemplates.CommonStructure import (
    ImplementationDataTypes,
)
from ...models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior import (
    InternalBehavior,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import (
    CompositionSwComponentType,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype import (
    DataPrototypes,
)
from ...models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ...models.M2.MSR.AsamHdo.ComputationMethod import (
    CompuMethod,
    CompuScale,
    CompuConst,
    CompuRationalCoeffs,
    CompuNominatorDenominator,
    CompuScaleConstantContents,
    CompuConstTextContent,
    CompuScaleRationalFormula,
)
from ...models.M2.AUTOSARTemplates.GenericStructure import (
    GeneralTemplateClasses,
)
from ...models.M2.MSR.AsamHdo.Constraints.GlobalConstraints import (
    DataConstr,
    DataConstrRule,
    InternalConstrs,
    PhysConstrs,
)
from ...models.M2.MSR.AsamHdo.Units import Unit
from ...models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    ImplementationProps,
)
from ...models.M2.AUTOSARTemplates.SWComponentTemplate.Components import (
    SymbolProps as CommonSymbolProps,
)
from ..base_arxml_parser import BaseARXMLParser

# Type aliases for imported classes
ApplicationPrimitiveDataType = Datatypes.ApplicationPrimitiveDataType
ApplicationRecordDataType = Datatypes.ApplicationRecordDataType
ApplicationRecordElement = Datatypes.ApplicationRecordElement
ApplicationArrayDataType = Datatypes.ApplicationArrayDataType
ApplicationCompositeDataType = \
    Datatypes.ApplicationCompositeDataType
ApplicationDataType = Datatypes.ApplicationDataType
AutosarDataType = Datatypes.AutosarDataType
DataTypeMap = Datatypes.DataTypeMap
DataTypeMappingSet = Datatypes.DataTypeMappingSet
ModeRequestTypeMap = Datatypes.ModeRequestTypeMap
ImplementationDataType = ImplementationDataTypes.ImplementationDataType
ImplementationDataTypeElement = \
    ImplementationDataTypes.ImplementationDataTypeElement
ApplicationCompositeElementDataPrototype = \
    DataPrototypes.ApplicationCompositeElementDataPrototype
DataPrototype = DataPrototypes.DataPrototype
ARLiteral = GeneralTemplateClasses.PrimitiveTypes.ARLiteral


class DataTypeParser(BaseARXMLParser):
    """
    Parser for AUTOSAR data type elements.

    Handles all data type definitions and related elements including
    application and implementation data types, compu-methods, units,
    and constraints.
    """

    def __init__(self, options=None, parent_parser=None):
        """Initialize DataTypeParser."""
        super().__init__(options)
        self._parent_parser = parent_parser

    # Core DataType Methods
    def readAutosarDataType(
        self,
        element: ET.Element,
        data_type: AutosarDataType
    ):
        """Read AutosarDataType attributes."""
        self._parent_parser.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(
            self._parent_parser.getSwDataDefProps(
                element,
                "SW-DATA-DEF-PROPS"
            )
        )

    def readApplicationPrimitiveDataType(
        self,
        element: ET.Element,
        data_type: ApplicationPrimitiveDataType
    ):
        """Read ApplicationPrimitiveDataType."""
        self.logger.debug(
            "Read ApplicationPrimitiveDataType <%s>" % data_type.getShortName()
        )
        self.readAutosarDataType(element, data_type)

    def readApplicationRecordElement(
        self,
        element: ET.Element,
        record_element: ApplicationRecordElement
    ):
        """Read ApplicationRecordElement."""
        self.readApplicationCompositeElementDataPrototype(
            element,
            record_element
        )

    def readApplicationRecordDataTypeElements(
        self,
        element: ET.Element,
        parent: ApplicationRecordDataType
    ):
        """Read elements of ApplicationRecordDataType."""
        for child_element in self.findall(element, "ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "APPLICATION-RECORD-ELEMENT":
                record_element = parent.createApplicationRecordElement(
                    self.getShortName(child_element)
                )
                self.readApplicationRecordElement(child_element,
                                                  record_element)
            else:
                self.notImplemented(
                    "Unsupported ApplicationRecordDataType Element <%s>"
                    % tag_name
                )

    def readApplicationRecordDataType(
        self,
        element: ET.Element,
        data_type: ApplicationRecordDataType
    ):
        """Read ApplicationRecordDataType."""
        self.logger.debug(
            "Read ApplicationRecordDataType <%s>" % data_type.getShortName()
        )
        self._parent_parser.readIdentifiable(element, data_type)
        data_type.setSwDataDefProps(
            self._parent_parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        )
        self.readApplicationRecordDataTypeElements(element, data_type)

    def readImplementationDataTypeElement(
        self,
        element: ET.Element,
        impl_data_type_element: ImplementationDataTypeElement
    ):
        """Read ImplementationDataTypeElement."""
        self.readAutosarDataType(element, impl_data_type_element)
        impl_data_type_element.setArraySize(
            self.getChildElementOptionalPositiveInteger(element, "ARRAY-SIZE")
        )
        impl_data_type_element.setArraySizeHandling(
            self.getChildElementOptionalLiteral(element, "ARRAY-SIZE-HANDLING")
        )
        impl_data_type_element.setArraySizeSemantics(
            self.getChildElementOptionalLiteral(element,
                                                "ARRAY-SIZE-SEMANTICS")
        )
        self.readImplementationDataTypeSubElements(element,
                                                   impl_data_type_element)

    def readImplementationDataTypeSubElements(
        self,
        element: ET.Element,
        parent: ImplementationDataType
    ):
        """Read sub-elements of ImplementationDataType."""
        for child_element in self.findall(element, "SUB-ELEMENTS/*"):
            tag_name = self.getTagName(child_element)
            if tag_name == "IMPLEMENTATION-DATA-TYPE-ELEMENT":
                impl_data_type_element = \
                    parent.createImplementationDataTypeElement(
                        self.getShortName(child_element)
                    )
                self.readImplementationDataTypeElement(
                    child_element,
                    impl_data_type_element
                )
            else:
                self.notImplemented(
                    "Unsupported ImplementationDataType SubElement <%s>" %
                    tag_name
                )

    def readImplementationDataType(
        self,
        element: ET.Element,
        data_type: ImplementationDataType
    ):
        """Read ImplementationDataType."""
        self.logger.debug(
            "Read ImplementationDataType <%s>" % data_type.getShortName()
        )
        self.readAutosarDataType(element, data_type)
        data_type.setDynamicArraySizeProfile(
            self.getChildElementOptionalLiteral(element,
                                                "DYNAMIC-ARRAY-SIZE-PROFILE")
        )
        self.readImplementationDataTypeSubElements(element, data_type)
        self.readImplementationDataTypeSymbolProps(element, data_type)
        data_type.setTypeEmitter(
            self.getChildElementOptionalLiteral(element, "TYPE-EMITTER")
        )

    def readImplementationDataTypeSymbolProps(
        self,
        element: ET.Element,
        data_type: ImplementationDataType
    ):
        """Read symbol props of ImplementationDataType."""
        child_element = self.find(element, "SYMBOL-PROPS")
        if child_element is not None:
            props = data_type.createSymbolProps(
                self.getShortName(child_element)
            )
            self.readSymbolProps(child_element, props)

    def readApplicationDataType(
        self,
        element: ET.Element,
        data_type: ApplicationDataType
    ):
        """Read ApplicationDataType."""
        self.readAutosarDataType(element, data_type)

    def readApplicationCompositeDataType(
        self,
        element: ET.Element,
        data_type: ApplicationCompositeDataType
    ):
        """Read ApplicationCompositeDataType."""
        self.readApplicationDataType(element, data_type)

    def readDataPrototype(
        self,
        element: ET.Element,
        prototype: DataPrototype
    ):
        """Read DataPrototype."""
        self._parent_parser.readIdentifiable(element, prototype)
        prototype.setSwDataDefProps(
            self._parent_parser.getSwDataDefProps(element, "SW-DATA-DEF-PROPS")
        )

    def readApplicationCompositeElementDataPrototype(
        self,
        element: ET.Element,
        prototype: ApplicationCompositeElementDataPrototype
    ):
        """Read ApplicationCompositeElementDataPrototype."""
        self.readDataPrototype(element, prototype)
        prototype.typeTRef = self.getChildElementOptionalRefType(
            element,
            "TYPE-TREF"
        )

    def readApplicationArrayElement(
        self,
        element: ET.Element,
        parent: ApplicationArrayDataType
    ):
        """Read ApplicationArrayElement."""
        child_element = self.find(element, "ELEMENT")
        if child_element is not None:
            short_name = self.getShortName(child_element)
            self.logger.debug("Read ApplicationArrayElement %s" % short_name)
            array_element = parent.createApplicationArrayElement(short_name)
            self.readApplicationCompositeElementDataPrototype(
                child_element,
                array_element
            )
            array_element.setArraySizeHandling(
                self._parent_parser.getChildElementOptionalLiteral(
                    child_element,
                    "ARRAY-SIZE-HANDLING"
                )
            )
            array_element.setArraySizeSemantics(
                self._parent_parser.getChildElementOptionalLiteral(
                    child_element,
                    "ARRAY-SIZE-SEMANTICS"
                )
            )
            array_element.setMaxNumberOfElements(
                self.getChildElementOptionalNumericalValue(
                    child_element,
                    "MAX-NUMBER-OF-ELEMENTS"
                )
            )

    def readApplicationArrayDataType(
        self,
        element: ET.Element,
        data_type: ApplicationArrayDataType
    ):
        """Read ApplicationArrayDataType."""
        self.logger.debug(
            "Read ApplicationArrayDataType <%s>" % data_type.getShortName()
        )
        self.readApplicationCompositeDataType(element, data_type)
        data_type.setDynamicArraySizeProfile(
            self.getChildElementOptionalLiteral(element,
                                                "DYNAMIC-ARRAY-SIZE-PROFILE")
        )
        self.readApplicationArrayElement(element, data_type)

    def readDataTypeMappingRefs(
        self,
        element: ET.Element,
        behavior: InternalBehavior
    ):
        """Read DataTypeMappingRefs for InternalBehavior."""
        child_element = self.find(element, "DATA-TYPE-MAPPING-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(
                child_element,
                "DATA-TYPE-MAPPING-REF"
            ):
                behavior.addDataTypeMappingRef(ref)

    def readDataTypeMaps(
        self,
        element: ET.Element,
        parent: DataTypeMappingSet
    ):
        """Read DataTypeMaps."""
        for child_element in element.findall(
            "./xmlns:DATA-TYPE-MAPS/xmlns:DATA-TYPE-MAP",
            self.nsmap
        ):
            data_type_map = DataTypeMap()
            self._parent_parser.readARObjectAttributes(
                child_element,
                data_type_map
            )
            data_type_map.applicationDataTypeRef = \
                self.getChildElementOptionalRefType(
                    child_element,
                    "APPLICATION-DATA-TYPE-REF"
                )
            data_type_map.implementationDataTypeRef = \
                self.getChildElementOptionalRefType(
                    child_element,
                    "IMPLEMENTATION-DATA-TYPE-REF"
                )
            parent.addDataTypeMap(data_type_map)
            # add the data type map to global namespace
            AUTOSAR.getInstance().addDataTypeMap(data_type_map)

    def readModeRequestTypeMaps(
        self,
        element: ET.Element,
        parent: DataTypeMappingSet
    ):
        """Read ModeRequestTypeMaps."""
        for child_element in element.findall(
            "./xmlns:MODE-REQUEST-TYPE-MAPS/xmlns:MODE-REQUEST-TYPE-MAP",
            self.nsmap
        ):
            mode_map = ModeRequestTypeMap()
            self._parent_parser.readARObjectAttributes(child_element, mode_map)
            mode_map.implementationDataTypeRef = \
                self.getChildElementOptionalRefType(
                    child_element,
                    "IMPLEMENTATION-DATA-TYPE-REF"
                )
            mode_map.modeGroupRef = self.getChildElementOptionalRefType(
                child_element,
                "MODE-GROUP-REF"
            )
            parent.addModeRequestTypeMap(mode_map)

    def readDataTypeMappingSet(
        self,
        element: ET.Element,
        mapping_set: DataTypeMappingSet
    ):
        """Read DataTypeMappingSet."""
        self.logger.debug(
            "Read DataTypeMappingSet: <%s>" % mapping_set.getShortName()
        )
        self._parent_parser.readIdentifiable(element, mapping_set)
        self.readDataTypeMaps(element, mapping_set)
        self.readModeRequestTypeMaps(element, mapping_set)

    def readCompositionSwComponentTypeDataTypeMappingSet(
        self,
        element: ET.Element,
        parent: CompositionSwComponentType
    ):
        """Read DataTypeMappingSet for CompositionSwComponentType."""
        child_element = self.find(element, "DATA-TYPE-MAPPING-REFS")
        if child_element is not None:
            for ref in self.getChildElementRefTypeList(
                child_element,
                "DATA-TYPE-MAPPING-REF"
            ):
                parent.addDataTypeMapping(ref)

    # CompuMethod Methods
    def readCompuConst(self, element: ET.Element, parent: CompuScale):
        """Read CompuConst."""
        child_element = self.find(element, "COMPU-CONST/VT")
        if child_element is not None:
            contents = CompuScaleConstantContents()
            contents.compuConst = CompuConst()
            contents.compuConst.compuConstContentType = CompuConstTextContent()
            contents.compuConst.compuConstContentType.vt = ARLiteral()
            contents.compuConst.compuConstContentType.vt.setValue(
                child_element.text
            )
            parent.compuScaleContents = contents

    def readCompuNominatorDenominator(
        self,
        element: ET.Element,
        key: str,
        parent: CompuNominatorDenominator
    ):
        """Read CompuNominatorDenominator."""
        for child_element in self.findall(element, "%s/V" % key):
            parent.add_v(child_element.text)

    def readCompuRationCoeffs(
        self,
        element: ET.Element,
        parent: CompuScale
    ):
        """Read CompuRationCoeffs."""
        child_element = self.find(element, "COMPU-RATIONAL-COEFFS")
        if child_element is not None:
            contents = CompuScaleRationalFormula()
            contents.compuRationalCoeffs = CompuRationalCoeffs()
            contents.compuRationalCoeffs.compuDenominator = \
                CompuNominatorDenominator()
            contents.compuRationalCoeffs.compuNumerator = \
                CompuNominatorDenominator()
            self.readCompuNominatorDenominator(
                child_element,
                "COMPU-DENOMINATOR",
                contents.compuRationalCoeffs.compuDenominator
            )
            self.readCompuNominatorDenominator(
                child_element,
                "COMPU-NUMERATOR",
                contents.compuRationalCoeffs.compuNumerator
            )
            parent.compuScaleContents = contents

    def readCompuScaleContents(
        self,
        element: ET.Element,
        parent: CompuScale
    ):
        """Read CompuScaleContents."""
        self.readCompuConst(element, parent)
        self.readCompuRationCoeffs(element, parent)

    def readCompuScale(self, element: ET.Element, compu_scale: CompuScale):
        """Read CompuScale."""
        self._parent_parser.readARObjectAttributes(element, compu_scale)
        compu_scale.setShortLabel(
            self.getChildElementOptionalLiteral(element, "SHORT-LABEL")
        )
        compu_scale.setSymbol(
            self.getChildElementOptionalLiteral(element, "SYMBOL")
        )
        compu_scale.setDesc(
            self._parent_parser.getMultiLanguageOverviewParagraph(
                element,
                "DESC"
            )
        )
        compu_scale.setMask(
            self.getChildElementOptionalPositiveInteger(element, "MASK")
        )
        compu_scale.setLowerLimit(
            self.getChildLimitElement(element, "LOWER-LIMIT")
        )
        compu_scale.setUpperLimit(
            self.getChildLimitElement(element, "UPPER-LIMIT")
        )
        self.readCompuScaleContents(element, compu_scale)

    def readCompuMethod(self, element: ET.Element, compu_method: CompuMethod):
        """Read CompuMethod."""
        self.logger.debug(
            "Read CompuMethod <%s>" % compu_method.getShortName()
        )
        self._parent_parser.readIdentifiable(element, compu_method)
        compu_method.setUnitRef(
            self.getChildElementOptionalRefType(element, "UNIT-REF")
        ).setCompuInternalToPhys(
            self._parent_parser.getCompu(element, "COMPU-INTERNAL-TO-PHYS")
        ).setCompuPhysToInternal(
            self._parent_parser.getCompu(element, "COMPU-PHYS-TO-INTERNAL")
        )

    # DataConstr Methods
    def readInternalConstrs(
        self,
        element: ET.Element,
        parent: DataConstrRule
    ):
        """Read InternalConstrs."""
        child_element = element.find("./xmlns:INTERNAL-CONSTRS", self.nsmap)
        if child_element is not None:
            constrs = InternalConstrs()
            self._parent_parser.readARObjectAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(
                child_element,
                "LOWER-LIMIT"
            )
            constrs.upper_limit = self.getChildLimitElement(
                child_element,
                "UPPER-LIMIT"
            )
            parent.internalConstrs = constrs

    def readPhysConstrs(self, element: ET.Element, parent: DataConstrRule):
        """Read PhysConstrs."""
        child_element = self.find(element, "PHYS-CONSTRS")
        if child_element is not None:
            constrs = PhysConstrs()
            self._parent_parser.readARObjectAttributes(child_element, constrs)
            constrs.lower_limit = self.getChildLimitElement(
                child_element,
                "LOWER-LIMIT"
            )
            constrs.upper_limit = self.getChildLimitElement(
                child_element,
                "UPPER-LIMIT"
            )
            constrs.unit_ref = self.getChildElementOptionalRefType(
                child_element,
                "UNIT-REF"
            )
            parent.physConstrs = constrs

    def readDataConstrRule(self, element: ET.Element, parent: DataConstr):
        """Read DataConstrRule."""
        for child_element in self.findall(
            element,
            "DATA-CONSTR-RULES/DATA-CONSTR-RULE"
        ):
            rule = DataConstrRule()
            self._parent_parser.readARObjectAttributes(child_element, rule)
            rule.constrLevel = self.getChildElementOptionalNumericalValue(
                child_element,
                "CONSTR-LEVEL"
            )
            self.readInternalConstrs(child_element, rule)
            self.readPhysConstrs(child_element, rule)
            parent.addDataConstrRule(rule)

    def readDataConstr(self, element: ET.Element, constr: DataConstr):
        """Read DataConstr."""
        self._parent_parser.readIdentifiable(element, constr)
        self.readDataConstrRule(element, constr)

    # Unit Methods
    def readUnit(self, element: ET.Element, unit: Unit):
        """Read Unit."""
        self.logger.debug("Read Unit <%s>" % unit.getShortName())
        self._parent_parser.readIdentifiable(element, unit)
        unit.setDisplayName(
            self.getChildElementOptionalLiteral(element, "DISPLAY-NAME")
        ).setFactorSiToUnit(
            self.getChildElementOptionalFloatValue(
                element,
                "FACTOR-SI-TO-UNIT"
            )
        ).setOffsetSiToUnit(
            self.getChildElementOptionalFloatValue(
                element,
                "OFFSET-SI-TO-UNIT"
            )
        ).setPhysicalDimensionRef(
            self.getChildElementOptionalRefType(
                element,
                "PHYSICAL-DIMENSION-REF"
            )
        )

    # SymbolProps Methods
    def readImplementationProps(
        self,
        element: ET.Element,
        props: ImplementationProps
    ):
        """Read ImplementationProps."""
        props.setSymbol(self.getChildElementOptionalLiteral(element, "SYMBOL"))

    def readSymbolProps(
        self,
        element: ET.Element,
        props: CommonSymbolProps
    ):
        """Read SymbolProps."""
        self.readImplementationProps(element, props)
