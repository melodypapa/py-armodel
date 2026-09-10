import xml.etree.ElementTree as ET

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


def _element(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def test_read_ar_variable_implementation_data_instance_ref_fields():
    parser = ARXMLParser(options={"warning": True})
    element = _element(
        "<AUTOSAR-VARIABLE-REF>"
        "<AUTOSAR-VARIABLE-IN-IMPL-DATATYPE>"
        "<PORT-PROTOTYPE-REF DEST='P-PORT-PROTOTYPE'>/Port</PORT-PROTOTYPE-REF>"
        "<ROOT-VARIABLE-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/Root</ROOT-VARIABLE-DATA-PROTOTYPE-REF>"
        "<CONTEXT-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/Context1</CONTEXT-DATA-PROTOTYPE-REF>"
        "<CONTEXT-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/Context2</CONTEXT-DATA-PROTOTYPE-REF>"
        "<TARGET-DATA-PROTOTYPE-REF DEST='IMPLEMENTATION-DATA-TYPE-ELEMENT'>/Target</TARGET-DATA-PROTOTYPE-REF>"
        "</AUTOSAR-VARIABLE-IN-IMPL-DATATYPE></AUTOSAR-VARIABLE-REF>"
    )

    AUTOSAR.getInstance().new()
    parsed = parser.getAutosarVariableRef(element, "AUTOSAR-VARIABLE-REF")

    assert parsed is not None
    implementation_ref = parsed.getAutosarVariableInImplDatatype()
    assert implementation_ref is not None
    assert implementation_ref.getPortPrototypeRef().getValue() == "/Port"
    assert implementation_ref.getRootVariableDataPrototypeRef().getValue() == "/Root"
    assert [ref.getValue() for ref in implementation_ref.getContextDataPrototypeRefs()] == ["/Context1", "/Context2"]
    assert implementation_ref.getTargetDataPrototypeRef().getValue() == "/Target"
