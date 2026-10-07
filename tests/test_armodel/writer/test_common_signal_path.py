"""Writer round-trip tests for CommonSignalPath (Table 5.36, p.253).

Serialized through the COMMON-SIGNAL-PATH element (OPERATIONS / SIGNALS wrappers
emitted only when non-empty) and the SIGNAL-PATH-CONSTRAINTS wrapper of
SystemMapping (AUTOSAR_00052.xsd l.119632).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import System
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import VariableDataPrototypeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SignalPaths import CommonSignalPath, SwcToSwcOperationArguments, SwcToSwcOperationArgumentsDirectionEnum, SwcToSwcSignal
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


class TestWriteCommonSignalPath:
    def test_empty_no_wrappers(self):
        path = CommonSignalPath()
        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommonSignalPath(parent, path)

        node = parent.find("COMMON-SIGNAL-PATH")
        assert node is not None
        assert node.find("OPERATIONS") is None
        assert node.find("SIGNALS") is None

    def test_full(self):
        path = CommonSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.IN)
        operation.setDirection(direction)
        path.addOperation(operation)

        signal = SwcToSwcSignal()
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref)
        path.addSignal(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommonSignalPath(parent, path)

        node = parent.find("COMMON-SIGNAL-PATH")
        assert node.find("OPERATIONS/SWC-TO-SWC-OPERATION-ARGUMENTS/DIRECTION").text == "IN"
        assert node.find("SIGNALS/SWC-TO-SWC-SIGNAL/DATA-ELEMENT-IREFS/DATA-ELEMENT-IREF/TARGET-DATA-PROTOTYPE-REF").text == "/Root/SwcA/Vdp1"

    def test_round_trip_full(self):
        path = CommonSignalPath()
        operation = SwcToSwcOperationArguments()
        direction = SwcToSwcOperationArgumentsDirectionEnum()
        direction.setValue(SwcToSwcOperationArgumentsDirectionEnum.OUT)
        operation.setDirection(direction)
        path.addOperation(operation)

        signal = SwcToSwcSignal()
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref)
        path.addSignal(signal)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeCommonSignalPath(parent, path)

        reloaded = CommonSignalPath()
        ARXMLParser().readCommonSignalPath(_with_ns(parent)[0], reloaded)

        operations = reloaded.getOperations()
        assert len(operations) == 1
        assert operations[0].getDirection().getValue() == SwcToSwcOperationArgumentsDirectionEnum.OUT
        signals = reloaded.getSignals()
        assert len(signals) == 1
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"
        assert signals[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"

    def test_round_trip_via_system_mapping(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")
        path = CommonSignalPath()
        signal = SwcToSwcSignal()
        iref = VariableDataPrototypeInSystemInstanceRef()
        iref.setTargetDataPrototypeRef(_ref("/Root/SwcA/Vdp1", "VARIABLE-DATA-PROTOTYPE"))
        signal.addDataElementIRef(iref)
        path.addSignal(signal)
        system_mapping.addSignalPathConstraint(path)

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSignalPathConstraints(parent, system_mapping)

        wrapper = parent.find("SIGNAL-PATH-CONSTRAINTS")
        assert wrapper is not None
        assert wrapper.find("COMMON-SIGNAL-PATH") is not None

        reloaded_system = System(parent=None, short_name="sys")
        reloaded_mapping = reloaded_system.createSystemMapping("sm")
        ARXMLParser().readSystemMappingSignalPathConstraints(_with_ns(parent), reloaded_mapping)
        constraints = reloaded_mapping.getSignalPathConstraints()
        assert len(constraints) == 1
        assert isinstance(constraints[0], CommonSignalPath)
        assert constraints[0].getSignals()[0].getDataElementIRefs()[0].getTargetDataPrototypeRef().getValue() == "/Root/SwcA/Vdp1"

    def test_empty_aggregation_no_wrapper(self):
        system = System(parent=None, short_name="sys")
        system_mapping = system.createSystemMapping("sm")

        parent = ET.Element("PARENT")
        ARXMLWriter().writeSystemMappingSignalPathConstraints(parent, system_mapping)

        assert parent.find("SIGNAL-PATH-CONSTRAINTS") is None
