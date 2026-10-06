"""Writer round-trip tests for SwcToSwcOperationArguments (Table 5.38, p.254).

Serialized through the SWC-TO-SWC-OPERATION-ARGUMENTS element
(XSD group SWC-TO-SWC-OPERATION-ARGUMENTS, AUTOSAR_00052.xsd l.118132:
OPERATION-IREFS wrapper emitted only when non-empty).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import OperationInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSwcToSwcOperationArguments:
    def test_empty(self):
        arguments = SwcToSwcOperationArguments()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcOperationArguments(parent, arguments)

        node = parent.find("SWC-TO-SWC-OPERATION-ARGUMENTS")
        assert node is not None
        assert node.find("DIRECTION") is None
        assert node.find("OPERATION-IREFS") is None

    def test_full(self):
        arguments = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        arguments.setDirection(direction)
        iref1 = OperationInSystemInstanceRef()
        iref1.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref1.setTargetOperationRef(_ref("/Root/SwcA/Cso1", "CLIENT-SERVER-OPERATION"))
        iref2 = OperationInSystemInstanceRef()
        iref2.setTargetOperationRef(_ref("/Root/SwcB/Cso2", "CLIENT-SERVER-OPERATION"))
        arguments.addOperationIRef(iref1)
        arguments.addOperationIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcOperationArguments(parent, arguments)

        node = parent.find("SWC-TO-SWC-OPERATION-ARGUMENTS")
        assert node.find("DIRECTION").text == "IN"
        wrapper = node.find("OPERATION-IREFS")
        assert wrapper is not None
        items = wrapper.findall("OPERATION-IREF")
        assert len(items) == 2
        assert items[0].find("TARGET-OPERATION-REF").text == "/Root/SwcA/Cso1"
        assert items[1].find("TARGET-OPERATION-REF").text == "/Root/SwcB/Cso2"

    def test_round_trip_full(self):
        arguments = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.OUT)
        arguments.setDirection(direction)
        iref1 = OperationInSystemInstanceRef()
        iref1.setContextCompositionRef(_ref("/Root", "ROOT-SW-COMPOSITION-PROTOTYPE"))
        iref1.setTargetOperationRef(_ref("/Root/SwcA/Cso1", "CLIENT-SERVER-OPERATION"))
        iref2 = OperationInSystemInstanceRef()
        iref2.setTargetOperationRef(_ref("/Root/SwcB/Cso2", "CLIENT-SERVER-OPERATION"))
        arguments.addOperationIRef(iref1)
        arguments.addOperationIRef(iref2)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcOperationArguments(parent, arguments)

        reloaded = SwcToSwcOperationArguments()
        ARXMLParser().readSwcToSwcOperationArguments(_with_ns(parent)[0], reloaded)

        assert reloaded.getDirection().getValue() == SwcToSwcOperationArgumentsDirectionEnum.OUT
        irefs = reloaded.getOperationIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextCompositionRef().getValue() == "/Root"
        assert irefs[0].getTargetOperationRef().getValue() == "/Root/SwcA/Cso1"
        assert irefs[0].getTargetOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert irefs[1].getTargetOperationRef().getValue() == "/Root/SwcB/Cso2"

    def test_round_trip_empty(self):
        arguments = SwcToSwcOperationArguments()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSwcToSwcOperationArguments(parent, arguments)

        reloaded = SwcToSwcOperationArguments()
        ARXMLParser().readSwcToSwcOperationArguments(_with_ns(parent)[0], reloaded)
        assert reloaded.getDirection() is None
        assert reloaded.getOperationIRefs() == []
