"""Reader/writer round-trip tests for the SwDataDefProps meta-class (Table 5.39)."""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARFloat,
    ARNumerical,
    AlignmentType,
    Boolean,
    CseCodeType,
    DisplayFormatString,
    Identifier,
    Integer,
    NativeDeclarationString,
    PrimitiveIdentifier,
    RefType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.MultidimensionalTime import MultidimensionalTime
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AutosarVariableRef import AutosarVariableRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.InstanceRefsUsage import AutosarParameterRef
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
        props.setAdditionalNativeTypeQualifier(NativeDeclarationString().setValue("volatile"))
        props.setSwInterpolationMethod(Identifier().setValue("linear"))
        props.setSwImplPolicy(SwImplPolicyEnum().setValue(SwImplPolicyEnum.STANDARD))
        props.setStepSize(ARFloat().setValue("0.5"))
        props.setSwIntendedResolution(ARNumerical().setValue("0.01"))
        props.setSwValueBlockSize(ARNumerical().setValue("10"))
        props.addSwValueBlockSizeMult(ARNumerical().setValue("2"))
        props.addSwValueBlockSizeMult(ARNumerical().setValue("3"))
        props.setSwIsVirtual(Boolean().setValue("true"))
        props.setBaseTypeRef(RefType().setDest("AUTOSAR/BaseTypes/uint8"))
        props.setSwAddrMethodRef(RefType().setDest("AUTOSAR/SwAddrMethods/ram"))
        props.setCompuMethodRef(RefType().setDest("AUTOSAR/CompuMethods/cm"))
        props.setDataConstrRef(RefType().setDest("AUTOSAR/DataConstrs/dc"))
        props.setImplementationDataTypeRef(RefType().setDest("AUTOSAR/ImplementationDataTypes/idt"))
        props.setSwRecordLayoutRef(RefType().setDest("AUTOSAR/RecordLayouts/rl"))
        props.setUnitRef(RefType().setDest("AUTOSAR/Units/second"))
        props.setValueAxisDataTypeRef(RefType().setDest("AUTOSAR/ApplicationDataTypes/adt"))

        bit_representation = SwBitRepresentation()
        bit_representation.setBitPosition(Integer().setValue("3"))
        bit_representation.setNumberOfBits(Integer().setValue("5"))
        props.setSwBitRepresentation(bit_representation)

        comparison_variable = SwVariableRefProxy()
        comparison_variable.setAutosarVariable(AutosarVariableRef().setLocalVariableRef(RefType().setDest("AUTOSAR/Variables/var1")))
        props.addSwComparisonVariable(comparison_variable)

        host_variable = SwVariableRefProxy()
        host_variable.setAutosarVariable(AutosarVariableRef().setLocalVariableRef(RefType().setDest("AUTOSAR/Variables/host")))
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
        refresh_timing.setCseCode(CseCodeType().setValue("100ms"))
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
            assert props.getDisplayPresentation().getValue() == "presentationContinuous"
            assert props.getSwAlignment().getValue() == "4"
            assert props.getSwCalibrationAccess().getValue() == "readWrite"
            assert props.getDisplayFormat().getValue() == "%5.2f"
            assert props.getAdditionalNativeTypeQualifier().getValue() == "volatile"
            assert props.getSwInterpolationMethod().getValue() == "linear"
            assert props.getSwImplPolicy().getValue() == "standard"
            assert props.getStepSize().getValue() == 0.5
            assert props.getSwIntendedResolution().getValue() == 0.01
            assert props.getSwValueBlockSize().getValue() == 10
            assert [m.getValue() for m in props.getSwValueBlockSizeMults()] == [2, 3]
            assert props.getSwIsVirtual().getValue() is True
            assert props.getBaseTypeRef().getDest() == "AUTOSAR/BaseTypes/uint8"
            assert props.getSwAddrMethodRef().getDest() == "AUTOSAR/SwAddrMethods/ram"
            assert props.getCompuMethodRef().getDest() == "AUTOSAR/CompuMethods/cm"
            assert props.getDataConstrRef().getDest() == "AUTOSAR/DataConstrs/dc"
            assert props.getImplementationDataTypeRef().getDest() == "AUTOSAR/ImplementationDataTypes/idt"
            assert props.getSwRecordLayoutRef().getDest() == "AUTOSAR/RecordLayouts/rl"
            assert props.getUnitRef().getDest() == "AUTOSAR/Units/second"
            assert props.getValueAxisDataTypeRef().getDest() == "AUTOSAR/ApplicationDataTypes/adt"
            assert props.getSwBitRepresentation().getBitPosition().getValue() == 3
            assert props.getSwBitRepresentation().getNumberOfBits().getValue() == 5
            assert len(props.getSwComparisonVariables()) == 1
            assert props.getSwComparisonVariables()[0].getAutosarVariable().getLocalVariableRef().getDest() == "AUTOSAR/Variables/var1"
            assert props.getSwHostVariable().getAutosarVariable().getLocalVariableRef().getDest() == "AUTOSAR/Variables/host"
            assert props.getSwDataDependency().getSwDataDependencyFormula().getLevel().getValue() == "INFORMAL"
            assert props.getSwDataDependency().getSwDataDependencyArgs() is not None
            assert props.getSwRefreshTiming().getCseCode().getValue() == "100ms"
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
