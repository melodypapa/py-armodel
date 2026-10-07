"""Writer round-trip tests for ForbiddenSignalPath (Table 5.40, p.255).

Serialized through the FORBIDDEN-SIGNAL-PATH element (OPERATIONS /
PHYSICAL-CHANNEL-REFS / SIGNALS wrappers emitted only when non-empty) and the
SIGNAL-PATH-CONSTRAINTS wrapper of SystemMapping (AUTOSAR_00052.xsd l.119632).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import ForbiddenSignalPath, SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum, SwcToSwcSignal
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


class TestWriteForbiddenSignalPath:
    def test_empty_no_wrappers(self):
        path = ForbiddenSignalPath()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeForbiddenSignalPath(parent, path)

        node = parent.find("FORBIDDEN-SIGNAL-PATH")
        assert node is not None
        assert node.find("OPERATIONS") is None
        assert node.find("PHYSICAL-CHANNEL-REFS") is None
        assert node.find("SIGNALS") is None

    def test_full(self):
        path = ForbiddenSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        operation.setDirection(direction)
        path.addOperation(operation)
        path.addPhysicalChannelRef(_ref("/Topology/Cluster/Can1", "CAN-PHYSICAL-CHANNEL"))

        signal = SwcToSwcSignal()
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref)
        path.addSignal(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeForbiddenSignalPath(parent, path)

        node = parent.find("FORBIDDEN-SIGNAL-PATH")
        assert node.find("OPERATIONS/SWC-TO-SWC-OPERATION-ARGUMENTS/DIRECTION").text == "IN"
        assert node.find("PHYSICAL-CHANNEL-REFS/PHYSICAL-CHANNEL-REF").text == "/Topology/Cluster/Can1"
        assert node.find("PHYSICAL-CHANNEL-REFS/PHYSICAL-CHANNEL-REF").get("DEST") == "CAN-PHYSICAL-CHANNEL"
        assert node.find("SIGNALS/SWC-TO-SWC-SIGNAL/DATA-ELEMENT-IREFS/DATA-ELEMENT-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcA/Vdp1"

    def test_round_trip_full(self):
        path = ForbiddenSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.OUT)
        operation.setDirection(direction)
        path.addOperation(operation)
        path.addPhysicalChannelRef(_ref("/Topology/Cluster/Can1", "CAN-PHYSICAL-CHANNEL"))
        path.addPhysicalChannelRef(_ref("/Topology/Cluster/Lin1", "LIN-PHYSICAL-CHANNEL"))

        signal = SwcToSwcSignal()
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref)
        path.addSignal(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeForbiddenSignalPath(parent, path)

        reloaded = ForbiddenSignalPath()
        ARXMLParser().readForbiddenSignalPath(_with_ns(parent)[0], reloaded)

        operations = reloaded.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == SwcToSwcOperationArgumentsDirectionEnum.OUT
        refs = reloaded.getPhysicalChannelRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Topology/Cluster/Can1"
        assert refs[0].getDest() == "CAN-PHYSICAL-CHANNEL"
        assert refs[1].getValue() == "/Topology/Cluster/Lin1"
        signals = reloaded.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        path = ForbiddenSignalPath()
        path.addPhysicalChannelRef(_ref("/Topology/Cluster/Can1", "CAN-PHYSICAL-CHANNEL"))
        system_mapping.addSignalPathConstraint(path)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSignalPathConstraints(parent, system_mapping)

        wrapper = parent.find("SIGNAL-PATH-CONSTRAINTS")
        assert wrapper is not None
        assert wrapper.find("FORBIDDEN-SIGNAL-PATH") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSignalPathConstraints(_with_ns(parent), reloaded_mapping)
        constraints = reloaded_mapping.getSignalPathConstraints()
        assert len(constraints) == 1
        assert isinstance(constraints[0], ForbiddenSignalPath)
        assert constraints[0].getPhysicalChannelRefs()[0].getValue() == "/Topology/Cluster/Can1"
