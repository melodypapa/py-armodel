"""
Tests for reading SW-DATA-DEF-PROPS — SWCT Table 5.39 (p.332, R23-11).

SwDataDefProps (Base = ARObject) is the heavily shared data-definition property bag read by
AutosarDataType, DataPrototype, ImplementationDataTypeElement, ParameterAccess, FlatInstanceDescriptor,
PerInstanceMemory, DiagnosticDataElement, McDataInstance and the *ComSpec network representations.
The reader walks SW-DATA-DEF-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL and
populates the model via its mutators in the XSD element order of the AUTOSAR_00052.xsd group
SW-DATA-DEF-PROPS-CONTENT (sequenceOffset 20..355, plus the unoffset leading elements).

Round-trip counterpart: tests/test_armodel/writer/test_sw_data_def_props.py
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.CommonStructure import NumericalValueSpecification
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ImplementationDataTypes import ImplementationDataType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Integer
from armodel.models.M2.MSR.DataDictionary.CalibrationParameter import SwCalprmAxisSet
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import (
    SwBitRepresentation,
    SwPointerTargetProps,
    SwTextProps,
    SwVariableRefProxy,
)
from armodel.models.M2.MSR.Documentation.Annotation import Annotation
from armodel.parser.arxml_parser import ARXMLParser

CONDITIONAL_XML = """
    <SW-DATA-DEF-PROPS-CONDITIONAL>
        <DISPLAY-PRESENTATION>PRESENTATION-CONTINUOUS</DISPLAY-PRESENTATION>
        <STEP-SIZE>0.5</STEP-SIZE>
        <SW-VALUE-BLOCK-SIZE-MULTS>
            <NUMERICAL-VALUE-VARIATION-POINT>3</NUMERICAL-VALUE-VARIATION-POINT>
            <NUMERICAL-VALUE-VARIATION-POINT>5</NUMERICAL-VALUE-VARIATION-POINT>
        </SW-VALUE-BLOCK-SIZE-MULTS>
        <ANNOTATIONS>
            <ANNOTATION><ANNOTATION-ORIGIN>sync-test</ANNOTATION-ORIGIN></ANNOTATION>
        </ANNOTATIONS>
        <SW-ADDR-METHOD-REF DEST="SW-ADDR-METHOD">/SwAddrMethods/ram</SW-ADDR-METHOD-REF>
        <SW-ALIGNMENT>8</SW-ALIGNMENT>
        <BASE-TYPE-REF DEST="SW-BASE-TYPE">/BaseTypes/uint8</BASE-TYPE-REF>
        <SW-BIT-REPRESENTATION>
            <BIT-POSITION>3</BIT-POSITION>
            <NUMBER-OF-BITS>5</NUMBER-OF-BITS>
        </SW-BIT-REPRESENTATION>
        <SW-CALIBRATION-ACCESS>READ-WRITE</SW-CALIBRATION-ACCESS>
        <SW-VALUE-BLOCK-SIZE>16</SW-VALUE-BLOCK-SIZE>
        <SW-CALPRM-AXIS-SET>
            <SW-CALPRM-AXIS>
                <SW-AXIS-INDEX>1</SW-AXIS-INDEX>
            </SW-CALPRM-AXIS>
        </SW-CALPRM-AXIS-SET>
        <SW-TEXT-PROPS>
            <ARRAY-SIZE-SEMANTICS>FIXED-SIZE</ARRAY-SIZE-SEMANTICS>
            <SW-MAX-TEXT-SIZE>200</SW-MAX-TEXT-SIZE>
            <BASE-TYPE-REF DEST="SW-BASE-TYPE">/BaseTypes/char</BASE-TYPE-REF>
        </SW-TEXT-PROPS>
        <SW-COMPARISON-VARIABLES>
            <MC-DATA-INSTANCE-VAR-REF DEST="MC-DATA-INSTANCE">/McDataInstances/v</MC-DATA-INSTANCE-VAR-REF>
        </SW-COMPARISON-VARIABLES>
        <COMPU-METHOD-REF DEST="COMPU-METHOD">/CompuMethods/cm</COMPU-METHOD-REF>
        <DATA-CONSTR-REF DEST="DATA-CONSTR">/DataConstrs/dc</DATA-CONSTR-REF>
        <SW-DATA-DEPENDENCY>
            <SW-DATA-DEPENDENCY-FORMULA>input1 + input2</SW-DATA-DEPENDENCY-FORMULA>
            <SW-DATA-DEPENDENCY-ARGS>
                <MC-DATA-INSTANCE-VAR-REF DEST="MC-DATA-INSTANCE">/McDataInstances/input1</MC-DATA-INSTANCE-VAR-REF>
            </SW-DATA-DEPENDENCY-ARGS>
        </SW-DATA-DEPENDENCY>
        <DISPLAY-FORMAT>%5.2f</DISPLAY-FORMAT>
        <IMPLEMENTATION-DATA-TYPE-REF DEST="IMPLEMENTATION-DATA-TYPE">/ImplementationDataTypes/idt</IMPLEMENTATION-DATA-TYPE-REF>
        <SW-HOST-VARIABLE>
            <MC-DATA-INSTANCE-VAR-REF DEST="MC-DATA-INSTANCE">/McDataInstances/host</MC-DATA-INSTANCE-VAR-REF>
        </SW-HOST-VARIABLE>
        <SW-IMPL-POLICY>STANDARD</SW-IMPL-POLICY>
        <ADDITIONAL-NATIVE-TYPE-QUALIFIER>volatile</ADDITIONAL-NATIVE-TYPE-QUALIFIER>
        <SW-INTENDED-RESOLUTION>0.01</SW-INTENDED-RESOLUTION>
        <SW-INTERPOLATION-METHOD>linear</SW-INTERPOLATION-METHOD>
        <INVALID-VALUE>
            <NUMERICAL-VALUE-SPECIFICATION>
                <VALUE>42</VALUE>
            </NUMERICAL-VALUE-SPECIFICATION>
        </INVALID-VALUE>
        <SW-IS-VIRTUAL>true</SW-IS-VIRTUAL>
        <SW-POINTER-TARGET-PROPS>
            <TARGET-CATEGORY>VALUE</TARGET-CATEGORY>
            <FUNCTION-POINTER-SIGNATURE-REF DEST="BSW-MODULE-ENTRY">/BswEntries/entry</FUNCTION-POINTER-SIGNATURE-REF>
        </SW-POINTER-TARGET-PROPS>
        <SW-RECORD-LAYOUT-REF DEST="SW-RECORD-LAYOUT">/RecordLayouts/rl</SW-RECORD-LAYOUT-REF>
        <SW-REFRESH-TIMING>
            <CSE-CODE-FACTOR>2</CSE-CODE-FACTOR>
        </SW-REFRESH-TIMING>
        <UNIT-REF DEST="UNIT">/Units/second</UNIT-REF>
        <VALUE-AXIS-DATA-TYPE-REF DEST="APPLICATION-PRIMITIVE-DATA-TYPE">/ApplicationDataTypes/adt</VALUE-AXIS-DATA-TYPE-REF>
    </SW-DATA-DEF-PROPS-CONDITIONAL>
"""

DOCUMENT_XML = (
    """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>DataDefProps</SHORT-NAME>
            <ELEMENTS>
                <IMPLEMENTATION-DATA-TYPE>
                    <SHORT-NAME>MyDataType</SHORT-NAME>
                    <CATEGORY>VALUE</CATEGORY>
                    <SW-DATA-DEF-PROPS>
                        <SW-DATA-DEF-PROPS-VARIANTS>
%s
                        </SW-DATA-DEF-PROPS-VARIANTS>
                    </SW-DATA-DEF-PROPS>
                </IMPLEMENTATION-DATA-TYPE>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""
    % CONDITIONAL_XML
)  # noqa E501

PARTIAL_BIT_REPRESENTATION_XML = """
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-3-0.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>DataDefProps</SHORT-NAME>
            <ELEMENTS>
                <IMPLEMENTATION-DATA-TYPE>
                    <SHORT-NAME>PartialBits</SHORT-NAME>
                    <SW-DATA-DEF-PROPS>
                        <SW-DATA-DEF-PROPS-VARIANTS>
                            <SW-DATA-DEF-PROPS-CONDITIONAL>
                                <SW-BIT-REPRESENTATION>
                                    <NUMBER-OF-BITS>5</NUMBER-OF-BITS>
                                </SW-BIT-REPRESENTATION>
                            </SW-DATA-DEF-PROPS-CONDITIONAL>
                        </SW-DATA-DEF-PROPS-VARIANTS>
                    </SW-DATA-DEF-PROPS>
                </IMPLEMENTATION-DATA-TYPE>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>
"""  # noqa E501


def _load_props():
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(DOCUMENT_XML)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    data_type = ar_package.getImplementationDataTypes()[0]
    assert isinstance(data_type, ImplementationDataType)
    return data_type.getSwDataDefProps()


def _load_partial_bit_representation():
    parser = ARXMLParser()
    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = ET.fromstring(PARTIAL_BIT_REPRESENTATION_XML)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    ar_package = document.getARPackages()[0]
    data_type = ar_package.getImplementationDataTypes()[0]
    return data_type.getSwDataDefProps().getSwBitRepresentation()


class TestSwDataDefPropsParser:
    """Reader coverage for the SW-DATA-DEF-PROPS-CONDITIONAL content (Table 5.39)."""

    def test_read_sw_data_def_props_is_present(self):
        props = _load_props()
        assert props is not None

    def test_read_sw_data_def_props_scalar_attrs(self):
        props = _load_props()
        assert props.getAdditionalNativeTypeQualifier().getValue() == "volatile"
        assert props.getDisplayFormat().getValue() == "%5.2f"
        assert props.getDisplayPresentation().getValue() == "presentationContinuous"
        assert props.getStepSize().getValue() == 0.5
        assert props.getSwAlignment().getValue() == "8"
        assert props.getSwCalibrationAccess().getValue() == "readWrite"
        assert props.getSwImplPolicy().getValue() == "standard"
        assert props.getSwInterpolationMethod().getValue() == "linear"
        assert props.getSwIsVirtual().getValue() is True
        assert props.getSwIntendedResolution().getValue() == 0.01
        assert props.getSwValueBlockSize().getValue() == 16

    def test_read_sw_data_def_props_refs(self):
        props = _load_props()
        assert props.getBaseTypeRef().getValue() == "/BaseTypes/uint8"
        assert props.getBaseTypeRef().getDest() == "SW-BASE-TYPE"
        assert props.getCompuMethodRef().getValue() == "/CompuMethods/cm"
        assert props.getDataConstrRef().getValue() == "/DataConstrs/dc"
        assert props.getImplementationDataTypeRef().getValue() == "/ImplementationDataTypes/idt"
        assert props.getSwAddrMethodRef().getValue() == "/SwAddrMethods/ram"
        assert props.getSwRecordLayoutRef().getValue() == "/RecordLayouts/rl"
        assert props.getUnitRef().getValue() == "/Units/second"
        assert props.getValueAxisDataTypeRef().getValue() == "/ApplicationDataTypes/adt"

    def test_read_sw_data_def_props_annotations(self):
        props = _load_props()
        annotations = props.getAnnotations()
        assert len(annotations) == 1
        assert isinstance(annotations[0], Annotation)
        assert annotations[0].getAnnotationOrigin().getValue() == "sync-test"

    def test_read_sw_data_def_props_sw_bit_representation(self):
        props = _load_props()
        bit_repr = props.getSwBitRepresentation()
        assert isinstance(bit_repr, SwBitRepresentation)
        assert isinstance(bit_repr.getBitPosition(), Integer)
        assert bit_repr.getBitPosition().getValue() == 3
        assert isinstance(bit_repr.getNumberOfBits(), Integer)
        assert bit_repr.getNumberOfBits().getValue() == 5

    def test_read_sw_bit_representation_partial_fields(self):
        """A SW-BIT-REPRESENTATION carrying only NUMBER-OF-BITS leaves bitPosition unset (Table 5.41, both attrs 0..1)."""
        bit_repr = _load_partial_bit_representation()
        assert isinstance(bit_repr, SwBitRepresentation)
        assert bit_repr.getBitPosition() is None
        assert bit_repr.getNumberOfBits().getValue() == 5

    def test_read_sw_data_def_props_sw_value_block_size_mults(self):
        props = _load_props()
        mults = props.getSwValueBlockSizeMults()
        assert [m.getValue() for m in mults] == [3, 5]

    def test_read_sw_data_def_props_sw_calprm_axis_set(self):
        props = _load_props()
        axis_set = props.getSwCalprmAxisSet()
        assert isinstance(axis_set, SwCalprmAxisSet)
        axes = axis_set.getSwCalprmAxises()
        assert len(axes) == 1
        assert axes[0].getSwAxisIndex().getValue() == "1"

    def test_read_sw_data_def_props_sw_text_props(self):
        props = _load_props()
        text_props = props.getSwTextProps()
        assert isinstance(text_props, SwTextProps)
        assert text_props.getSwMaxTextSize().getValue() == 200
        assert text_props.getBaseTypeRef().getValue() == "/BaseTypes/char"

    def test_read_sw_data_def_props_sw_comparison_variables(self):
        props = _load_props()
        variables = props.getSwComparisonVariables()
        assert len(variables) == 1
        assert isinstance(variables[0], SwVariableRefProxy)
        assert variables[0].getMcDataInstanceVarRef().getValue() == "/McDataInstances/v"

    def test_read_sw_data_def_props_sw_data_dependency(self):
        props = _load_props()
        dependency = props.getSwDataDependency()
        assert dependency is not None
        assert dependency.getSwDataDependencyFormula() is not None
        args = dependency.getSwDataDependencyArgs()
        assert args is not None
        assert args.getSwVariable().getMcDataInstanceVarRef().getValue() == "/McDataInstances/input1"

    def test_read_sw_data_def_props_sw_host_variable(self):
        props = _load_props()
        host_variable = props.getSwHostVariable()
        assert isinstance(host_variable, SwVariableRefProxy)
        assert host_variable.getMcDataInstanceVarRef().getValue() == "/McDataInstances/host"

    def test_read_sw_data_def_props_invalid_value(self):
        props = _load_props()
        invalid_value = props.getInvalidValue()
        assert isinstance(invalid_value, NumericalValueSpecification)
        assert invalid_value.getValue().getValue() == 42

    def test_read_sw_data_def_props_sw_pointer_target_props(self):
        props = _load_props()
        pointer_props = props.getSwPointerTargetProps()
        assert isinstance(pointer_props, SwPointerTargetProps)
        assert pointer_props.getTargetCategory().getValue() == "VALUE"
        assert pointer_props.getFunctionPointerSignatureRef().getValue() == "/BswEntries/entry"

    def test_read_sw_data_def_props_sw_refresh_timing(self):
        props = _load_props()
        refresh_timing = props.getSwRefreshTiming()
        assert refresh_timing is not None
        assert refresh_timing.getCseCodeFactor().getValue() == 2
