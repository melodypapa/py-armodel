"""Writer round-trip tests for SeparateSignalPath (Table 5.42, p.257).

Serialized through the SEPARATE-SIGNAL-PATH element (OPERATIONS / SIGNALS wrappers
emitted only when non-empty) and the SIGNAL-PATH-CONSTRAINTS wrapper of
SystemMapping (AUTOSAR_00052.xsd l.119632).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import SeparateSignalPath, SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum, SwcToSwcSignal
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


def _with_ns(parent: ET.Element) -> ET.Element:
    return ET.fromstring(ET.tostring(parent).decode("utf-8").replace("<PARENT>", "<PARENT xmlns='%s'>" % NS, 1))


class TestWriteSeparateSignalPath:
    def test_empty_no_wrappers(self):
        path = SeparateSignalPath()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeSeparateSignalPath(parent, path)

        node = parent.find("SEPARATE-SIGNAL-PATH")
        assert node is not None
        assert node.find("OPERATIONS") is None
        assert node.find("SIGNALS") is None

    def test_full(self):
        path = SeparateSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.OUT)
        operation.setDirection(direction)
        path.addOperation(operation)
        path.addSignal(SwcToSwcSignal())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSeparateSignalPath(parent, path)

        node = parent.find("SEPARATE-SIGNAL-PATH")
        assert node.find("OPERATIONS/SWC-TO-SWC-OPERATION-ARGUMENTS/DIRECTION").text == "OUT"
        assert node.find("SIGNALS/SWC-TO-SWC-SIGNAL") is not None

    def test_round_trip_full(self):
        path = SeparateSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        operation.setDirection(direction)
        path.addOperation(operation)
        path.addSignal(SwcToSwcSignal())
        path.addSignal(SwcToSwcSignal())

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSeparateSignalPath(parent, path)

        reloaded = SeparateSignalPath()
        ARXMLParser().readSeparateSignalPath(_with_ns(parent)[0], reloaded)

        operations = reloaded.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == SwcToSwcOperationArgumentsDirectionEnum.IN
        assert len(reloaded.getSignals()) == 2

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        path = SeparateSignalPath()
        path.addSignal(SwcToSwcSignal())
        system_mapping.addSignalPathConstraint(path)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSignalPathConstraints(parent, system_mapping)

        wrapper = parent.find("SIGNAL-PATH-CONSTRAINTS")
        assert wrapper is not None
        assert wrapper.find("SEPARATE-SIGNAL-PATH") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSignalPathConstraints(_with_ns(parent), reloaded_mapping)
        constraints = reloaded_mapping.getSignalPathConstraints()
        assert len(constraints) == 1
        assert isinstance(constraints[0], SeparateSignalPath)
        assert len(constraints[0].getSignals()) == 1
