"""Reader/writer round-trip tests for the SwDataDefProps meta-class (Table 5.39)."""

import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure import TextValueSpecification
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    AlignmentType,
    ARLiteral,
    Boolean,
    CseCodeType,
    DateTime,
    DisplayFormatString,
    Float,
    Identifier,
    Integer,
    NativeDeclarationString,
    Numerical,
    PrimitiveIdentifier,
    RefType,
    String,
    TRefType,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import AutosarVariableRef
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    CompuGenericMath,
    DisplayPresentationEnum,
    SwBitRepresentation,
    SwCalibrationAccessEnum,
    SwDataDefProps,
    SwDataDependency,
    SwDataDependencyArgs,
    SwImplPolicyEnum,
    SwVariableRefProxy,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


class TestSwDataDefPropsRoundTrip:
    def _build(self, document):
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("MyType")

        props = SwDataDefProps()
        props.setDisplayPresentation(DisplayPresentationEnum().setValue(DisplayPresentationEnum.PRESENTATION_CONTINUOUS))
        props.setSwAlignment(AlignmentType().setValue("4"))
        props.setSwCalibrationAccess(SwCalibrationAccessEnum().setValue(SwCalibrationAccessEnum.READ_WRITE))
        props.setDisplayFormat(DisplayFormatString().setValue("%5.2f"))
        props.setAdditionalNativeTypeQualifier(NativeDeclarationString().setValue("VOLATILE"))
        props.setSwInterpolationMethod(Identifier().setValue("linear"))
        props.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD))
        props.setStepSize(Float().setValue("0.5"))
        props.setSwIntendedResolution(Numerical().setValue("0.01"))
        props.setSwValueBlockSize(Numerical().setValue("10"))
        props.addSwValueBlockSizeMult(Numerical().setValue("2"))
        props.addSwValueBlockSizeMult(Numerical().setValue("3"))
        props.setSwIsVirtual(Boolean().setValue("true"))
        props.setBaseTypeRef(RefType().setValue("/AUTOSAR/BaseTypes/uint8").setDest("SW-BASE-TYPE"))
        props.setSwAddrMethodRef(RefType().setValue("/AUTOSAR/SwAddrMethods/ram").setDest("SW-ADDR-METHOD"))
        props.setCompuMethodRef(RefType().setValue("/AUTOSAR/CompuMethods/cm").setDest("COMPU-METHOD"))
        props.setDataConstrRef(RefType().setValue("/AUTOSAR/DataConstrs/dc").setDest("DATA-CONSTR"))
        props.setImplementationDataTypeRef(RefType().setValue("/AUTOSAR/ImplementationDataTypes/idt").setDest("IMPLEMENTATION-DATA-TYPE"))
        props.setSwRecordLayoutRef(RefType().setValue("/AUTOSAR/RecordLayouts/rl").setDest("SW-RECORD-LAYOUT"))
        props.setUnitRef(RefType().setValue("/AUTOSAR/Units/second").setDest("UNIT"))
        props.setValueAxisDataTypeRef(RefType().setValue("/AUTOSAR/ApplicationDataTypes/adt").setDest("APPLICATION-PRIMITIVE-DATA-TYPE"))

        bit_representation = SwBitRepresentation()
        bit_representation.setBitPosition(Integer().setValue("3"))
        bit_representation.setNumberOfBits(Integer().setValue("5"))
        props.setSwBitRepresentation(bit_representation)

        comparison_variable = SwVariableRefProxy()
        comparison_variable.setAutosarVariable(AutosarVariableRef().setLocalVariableRef(RefType().setValue("/AUTOSAR/Variables/var1").setDest("VARIABLE-DATA-PROTOTYPE")))
        props.addSwComparisonVariable(comparison_variable)

        host_variable = SwVariableRefProxy()
        host_variable.setAutosarVariable(AutosarVariableRef().setLocalVariableRef(RefType().setValue("/AUTOSAR/Variables/host").setDest("VARIABLE-DATA-PROTOTYPE")))
        props.setSwHostVariable(host_variable)

        dependency = SwDataDependency()
        formula = CompuGenericMath()
        formula.setLevel(PrimitiveIdentifier().setValue("INFORMAL"))
        dependency.setSwDataDependencyFormula(formula)
        args = SwDataDependencyArgs()
        args.setSwVariable(SwVariableRefProxy())
        dependency.setSwDataDependencyArgs(args)
        props.setSwDataDependency(dependency)

        refresh_timing = MultidimensionalTime()
        refresh_timing.setCseCode(CseCodeType().setValue("100"))
        refresh_timing.setCseCodeFactor(Integer().setValue("1"))
        props.setSwRefreshTiming(refresh_timing)

        data_type.setSwDataDefProps(props)
        return data_type

    def test_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        self._build(document)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            props = data_type_2.getSwDataDefProps()
            assert props is not None
            assert props.getDisplayPresentation().getValue() == DisplayPresentationEnum.PRESENTATION_CONTINUOUS
            assert props.getSwAlignment().getValue() == "4"
            assert props.getSwCalibrationAccess().getValue() == "READ-WRITE"
            assert props.getDisplayFormat().getValue() == "%5.2f"
            assert props.getAdditionalNativeTypeQualifier().getValue() == "VOLATILE"
            assert props.getSwInterpolationMethod().getValue() == "linear"
            assert props.getSwImplPolicy().getValue() == "STANDARD"
            assert props.getStepSize().getValue() == 0.5
            assert props.getSwIntendedResolution().getValue() == 0.01
            assert props.getSwValueBlockSize().getValue() == 10
            assert [m.getValue() for m in props.getSwValueBlockSizeMults()] == [2, 3]
            assert props.getSwIsVirtual().getValue() is True
            assert props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
            assert props.getSwAddrMethodRef().getDest() == "SW-ADDR-METHOD"
            assert props.getCompuMethodRef().getDest() == "COMPU-METHOD"
            assert props.getDataConstrRef().getDest() == "DATA-CONSTR"
            assert props.getImplementationDataTypeRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
            assert props.getSwRecordLayoutRef().getDest() == "SW-RECORD-LAYOUT"
            assert props.getUnitRef().getDest() == "UNIT"
            assert props.getValueAxisDataTypeRef().getDest() == "APPLICATION-PRIMITIVE-DATA-TYPE"
            assert props.getSwBitRepresentation().getBitPosition().getValue() == 3
            assert props.getSwBitRepresentation().getNumberOfBits().getValue() == 5
            assert len(props.getSwComparisonVariables()) == 1
            assert props.getSwComparisonVariables()[0].getAutosarVariable().getLocalVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
            assert props.getSwHostVariable().getAutosarVariable().getLocalVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
            assert props.getSwDataDependency().getSwDataDependencyFormula().getLevel().getValue() == "INFORMAL"
            assert props.getSwDataDependency().getSwDataDependencyArgs() is not None
            assert props.getSwRefreshTiming().getCseCode().getValue() == "100"
            assert props.getSwRefreshTiming().getCseCodeFactor().getValue() == 1
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_no_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        pkg.createApplicationPrimitiveDataType("MyType")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            assert data_type_2.getSwDataDefProps() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestDataPrototypeSwDataDefPropsRoundTrip:
    def test_round_trip_shared_parameter_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")
        parameter = behavior.createSharedParameter("sp1")

        props = SwDataDefProps()
        props.setCompuMethodRef(RefType().setValue("/AUTOSAR/CompuMethods/cm").setDest("COMPU-METHOD"))
        props.setSwAddrMethodRef(RefType().setValue("/AUTOSAR/SwAddrMethods/ram").setDest("SW-ADDR-METHOD"))
        parameter.setSwDataDefProps(props)
        parameter.setTypeTRef(TRefType().setValue("/AUTOSAR/DataTypes/uint8").setDest("IMPLEMENTATION-DATA-TYPE"))
        parameter.setInitValue(TextValueSpecification().setValue(ARLiteral().setValue("42")))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            parameter_2 = component_2.getInternalBehavior().getSharedParameters()[0]
            assert parameter_2.getShortName() == "sp1"
            props_2 = parameter_2.getSwDataDefProps()
            assert props_2 is not None
            assert props_2.getCompuMethodRef().getDest() == "COMPU-METHOD"
            assert props_2.getSwAddrMethodRef().getDest() == "SW-ADDR-METHOD"
            assert parameter_2.getTypeTRef().getDest() == "IMPLEMENTATION-DATA-TYPE"
            assert parameter_2.getInitValue().getValue().getValue() == "42"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_round_trip_shared_parameter_no_sw_data_def_props(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("AUTOSAR")
        component = pkg.createApplicationSwComponentType("MyComponent")
        behavior = component.createSwcInternalBehavior("Behavior")
        behavior.createSharedParameter("sp1")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            parameter_2 = component_2.getInternalBehavior().getSharedParameters()[0]
            assert parameter_2.getSwDataDefProps() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


class TestSwDataDependencyFormulaRoundTrip:
    def _build(self, document, formula=None):
        pkg = document.createARPackage("AUTOSAR")
        data_type = pkg.createApplicationPrimitiveDataType("MyType")
        props = SwDataDefProps()
        if formula is not None:
            dependency = SwDataDependency()
            dependency.setSwDataDependencyFormula(formula)
            props.setSwDataDependency(dependency)
        data_type.setSwDataDefProps(props)
        return data_type

    def test_formula_level_text_and_attributes_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        formula = CompuGenericMath()
        formula.setLevel(PrimitiveIdentifier().setValue("INFORMAL"))
        formula.setMixedString("X1+X2")
        formula.setChecksum(String().setValue("deadbeef"))
        formula.setTimestamp(DateTime().setValue("2024-01-01T00:00:00Z"))
        self._build(document, formula)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            written = ET.parse(file_path).getroot()
            formula_element = next(el for el in written.iter() if el.tag.endswith("SW-DATA-DEPENDENCY-FORMULA"))
            assert formula_element.get("LEVEL") == "INFORMAL"
            assert formula_element.text == "X1+X2"
            assert formula_element.get("S") == "deadbeef"
            assert formula_element.get("T") == "2024-01-01T00:00:00Z"

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            formula_2 = data_type_2.getSwDataDefProps().getSwDataDependency().getSwDataDependencyFormula()
            assert isinstance(formula_2, CompuGenericMath)
            assert isinstance(formula_2.getLevel(), PrimitiveIdentifier)
            assert formula_2.getLevel().getValue() == "INFORMAL"
            assert formula_2.getMixedString() == "X1+X2"
            assert formula_2.getChecksum().getValue() == "deadbeef"
            assert formula_2.getTimestamp().getValue() == "2024-01-01T00:00:00Z"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_formula_without_level_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        formula = CompuGenericMath()
        formula.setMixedString("X1+X2")
        self._build(document, formula)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            written = ET.parse(file_path).getroot()
            formula_element = next(el for el in written.iter() if el.tag.endswith("SW-DATA-DEPENDENCY-FORMULA"))
            assert formula_element.get("LEVEL") is None

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            formula_2 = data_type_2.getSwDataDefProps().getSwDataDependency().getSwDataDependencyFormula()
            assert isinstance(formula_2, CompuGenericMath)
            assert formula_2.getLevel() is None
            assert formula_2.getMixedString() == "X1+X2"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_formula_without_text_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        formula = CompuGenericMath()
        formula.setLevel(PrimitiveIdentifier().setValue("INFORMAL"))
        self._build(document, formula)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            written = ET.parse(file_path).getroot()
            formula_element = next(el for el in written.iter() if el.tag.endswith("SW-DATA-DEPENDENCY-FORMULA"))
            assert formula_element.text is None or formula_element.text.strip() == ""

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            formula_2 = data_type_2.getSwDataDefProps().getSwDataDependency().getSwDataDependencyFormula()
            assert formula_2.getMixedString() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_props_without_sw_data_dependency_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        self._build(document, formula=None)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            data_type_2 = document_2.getARPackages()[0].getApplicationPrimitiveDataTypes()[0]
            props_2 = data_type_2.getSwDataDefProps()
            assert props_2 is not None
            assert props_2.getSwDataDependency() is None
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
