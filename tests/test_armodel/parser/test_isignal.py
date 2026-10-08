"""Parser tests for ISignal (Table 6.7, p.321).

Child set and order per the I-SIGNAL group of AUTOSAR_00052.xsd (l.66683).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants import (
    NumericalValueSpecification,
    TextValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignal
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    SOMEIPTransformationISignalProps,
    UserDefinedTransformationISignalProps,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"

FULL_XML = f"""<I-SIGNAL xmlns='{NS}'>
    <SHORT-NAME>ISig1</SHORT-NAME>
    <DATA-TRANSFORMATIONS>
        <DATA-TRANSFORMATION-REF-CONDITIONAL>
            <DATA-TRANSFORMATION-REF DEST='DATA-TRANSFORMATION'>/AUTOSAR/DataTransformation</DATA-TRANSFORMATION-REF>
        </DATA-TRANSFORMATION-REF-CONDITIONAL>
    </DATA-TRANSFORMATIONS>
    <DATA-TYPE-POLICY>OVERRIDE</DATA-TYPE-POLICY>
    <I-SIGNAL-PROPS>
        <HANDLE-OUT-OF-RANGE>SATURATE</HANDLE-OUT-OF-RANGE>
    </I-SIGNAL-PROPS>
    <I-SIGNAL-TYPE>ARRAY</I-SIGNAL-TYPE>
    <INIT-VALUE>
        <TEXT-VALUE-SPECIFICATION>
            <VALUE>42</VALUE>
        </TEXT-VALUE-SPECIFICATION>
    </INIT-VALUE>
    <LENGTH>8</LENGTH>
    <NETWORK-REPRESENTATION-PROPS>
        <SW-DATA-DEF-PROPS-VARIANTS>
            <SW-DATA-DEF-PROPS-CONDITIONAL>
                <BASE-TYPE-REF DEST='SW-BASE-TYPE'>/AUTOSAR/BaseType/uint8</BASE-TYPE-REF>
            </SW-DATA-DEF-PROPS-CONDITIONAL>
        </SW-DATA-DEF-PROPS-VARIANTS>
    </NETWORK-REPRESENTATION-PROPS>
    <SYSTEM-SIGNAL-REF DEST='SYSTEM-SIGNAL'>/AUTOSAR/SystemSignal</SYSTEM-SIGNAL-REF>
    <TIMEOUT-SUBSTITUTION-VALUE>
        <NUMERICAL-VALUE-SPECIFICATION>
            <VALUE>3.5</VALUE>
        </NUMERICAL-VALUE-SPECIFICATION>
    </TIMEOUT-SUBSTITUTION-VALUE>
    <TRANSFORMATION-I-SIGNAL-PROPSS>
        <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
            <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
                <END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
                    <DATA-LENGTH>64</DATA-LENGTH>
                </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL>
            </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS>
        </END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS>
        <SOMEIP-TRANSFORMATION-I-SIGNAL-PROPS/>
        <USER-DEFINED-TRANSFORMATION-I-SIGNAL-PROPS/>
    </TRANSFORMATION-I-SIGNAL-PROPSS>
</I-SIGNAL>"""


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestReadISignal:
    def test_read_full(self):
        signal = ISignal(None, "ISig1")
        ARXMLParser().readISignal(ET.fromstring(FULL_XML), signal)

        assert signal.getShortName() == "ISig1"
        assert signal.getDataTransformationRef().getValue() == "/AUTOSAR/DataTransformation"
        assert signal.getDataTransformationRef().getDest() == "DATA-TRANSFORMATION"
        assert signal.getDataTypePolicy().value == "OVERRIDE"
        assert signal.getISignalProps().getHandleOutOfRange().value == "SATURATE"
        assert signal.getISignalType().value == "ARRAY"
        assert isinstance(signal.getInitValue(), TextValueSpecification)
        assert signal.getInitValue().getValue().getValue() == "42"
        assert signal.getLength().getValue() == 8
        assert signal.getNetworkRepresentationProps() is not None
        assert signal.getNetworkRepresentationProps().getBaseTypeRef().getValue() == "/AUTOSAR/BaseType/uint8"
        assert signal.getSystemSignalRef().getValue() == "/AUTOSAR/SystemSignal"
        assert signal.getSystemSignalRef().getDest() == "SYSTEM-SIGNAL"
        assert isinstance(signal.getTimeoutSubstitutionValue(), NumericalValueSpecification)
        assert signal.getTimeoutSubstitutionValue().getValue().getValue() == 3.5

        props_list = signal.getTransformationISignalProps()
        assert len(props_list) == 3
        assert isinstance(props_list[0], EndToEndTransformationISignalProps)
        assert props_list[0].getDataLength().getValue() == 64
        assert isinstance(props_list[1], SOMEIPTransformationISignalProps)
        assert isinstance(props_list[2], UserDefinedTransformationISignalProps)

    def test_read_minimal(self):
        signal = ISignal(None, "ISig1")
        element = ET.fromstring(f"<I-SIGNAL xmlns='{NS}'><SHORT-NAME>ISig1</SHORT-NAME></I-SIGNAL>")
        ARXMLParser().readISignal(element, signal)

        assert signal.getShortName() == "ISig1"
        assert signal.getDataTransformationRef() is None
        assert signal.getDataTypePolicy() is None
        assert signal.getISignalProps() is None
        assert signal.getISignalType() is None
        assert signal.getInitValue() is None
        assert signal.getLength() is None
        assert signal.getNetworkRepresentationProps() is None
        assert signal.getSystemSignalRef() is None
        assert signal.getTimeoutSubstitutionValue() is None
        assert signal.getTransformationISignalProps() == []

    def test_read_empty_wrapper_lists(self):
        signal = ISignal(None, "ISig1")
        element = ET.fromstring(f"<I-SIGNAL xmlns='{NS}'>" "<SHORT-NAME>ISig1</SHORT-NAME>" "<DATA-TRANSFORMATIONS/>" "<TRANSFORMATION-I-SIGNAL-PROPSS/>" "</I-SIGNAL>")
        ARXMLParser().readISignal(element, signal)

        assert signal.getDataTransformationRef() is None
        assert signal.getTransformationISignalProps() == []
