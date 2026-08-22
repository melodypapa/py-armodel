"""Tests for writer HW, Lin, Flexray, and transformation handlers."""

import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Filter import DataFilter
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate import (
    HwElement,
    HwPinGroup,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.HwElementCategory import (
    HwAttributeDef,
    HwCategory,
    HwType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa E501
    ARBoolean,
    ARLiteral,
    ARNumerical,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayCommunication import (
    FlexrayFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Flexray.FlexrayTopology import (
    FlexrayCommunicationController,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinMaster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (
    IPduTiming,
    ISignalIPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.Timing import (
    CyclicTiming,
    EventControlledTiming,
    TimeRangeType,
    TransmissionModeCondition,
    TransmissionModeDeclaration,
    TransmissionModeTiming,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    BufferProperties,
    DataTransformationSet,
    E2EProfileCompatibilityProps,
    EndToEndTransformationDescription,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    return ARXMLWriter()


def _parent():
    return ET.Element("PARENT")


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _bool(value):
    b = ARBoolean()
    b.setValue(value)
    return b


def _numerical(value):
    n = ARNumerical()
    n.setValue(str(value))
    return n


def _integer(value):
    i = Integer()
    i.setValue(value)
    return i


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _make_pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


class TestWriterHwDescriptionEntity:
    def test_writeHwDescriptionEntityHwCategoryRefs_with_refs(self, writer):
        pkg = _make_pkg()
        entity = HwElement(pkg, "HwElem")
        entity.addHwCategoryRef(_ref("/cat1", "HW-CATEGORY"))
        entity.addHwCategoryRef(_ref("/cat2", "HW-CATEGORY"))
        parent = _parent()
        writer.writeHwDescriptionEntityHwCategoryRefs(parent, entity)
        assert parent[0].tag == "HW-CATEGORY-REFS"
        refs = parent[0].findall("HW-CATEGORY-REF")
        assert len(refs) == 2

    def test_writeHwDescriptionEntityHwCategoryRefs_empty(self, writer):
        pkg = _make_pkg()
        entity = HwElement(pkg, "HwElem")
        parent = _parent()
        writer.writeHwDescriptionEntityHwCategoryRefs(parent, entity)
        assert len(parent) == 0

    def test_writeHwDescriptionEntity_full(self, writer):
        pkg = _make_pkg()
        entity = HwElement(pkg, "HwElem")
        entity.addHwCategoryRef(_ref("/cat", "HW-CATEGORY"))
        parent = _parent()
        writer.writeHwDescriptionEntity(parent, entity)
        assert parent.find("HW-CATEGORY-REFS") is not None

    def test_writeHwPinGroup_with_group(self, writer):
        pkg = _make_pkg()
        elem = HwElement(pkg, "Elem")
        pin_group = HwPinGroup(elem, "PinGrp")
        parent = _parent()
        writer.writeHwPinGroup(parent, pin_group)
        assert parent[0].tag == "HW-PIN-GROUP"

    def test_writeHwPinGroup_none(self, writer):
        parent = _parent()
        writer.writeHwPinGroup(parent, None)
        assert len(parent) == 0

    def test_writeHwElementHwPinGroups_with_groups(self, writer):
        pkg = _make_pkg()
        elem = HwElement(pkg, "Elem")
        elem.createHwPinGroup("Grp1")
        elem.createHwPinGroup("Grp2")
        parent = _parent()
        writer.writeHwElementHwPinGroups(parent, elem)
        assert parent[0].tag == "HW-PIN-GROUPS"
        groups = parent[0].findall("HW-PIN-GROUP")
        assert len(groups) == 2

    def test_writeHwElementHwPinGroups_empty(self, writer):
        pkg = _make_pkg()
        elem = HwElement(pkg, "Elem")
        parent = _parent()
        writer.writeHwElementHwPinGroups(parent, elem)
        assert len(parent) == 0

    def test_writeHwElement_full(self, writer):
        pkg = _make_pkg()
        elem = HwElement(pkg, "Elem")
        elem.addHwCategoryRef(_ref("/cat", "HW-CATEGORY"))
        elem.createHwPinGroup("PinGrp")
        parent = _parent()
        writer.writeHwElement(parent, elem)
        assert parent[0].tag == "HW-ELEMENT"
        assert parent[0].find("HW-CATEGORY-REFS") is not None
        assert parent[0].find("HW-PIN-GROUPS") is not None

    def test_writeHwElement_none(self, writer):
        parent = _parent()
        writer.writeHwElement(parent, None)
        assert len(parent) == 0


class TestWriterHwAttributeDef:
    def test_writeHwAttributeDef_with_unit(self, writer):
        pkg = _make_pkg()
        cat = HwCategory(pkg, "Cat")
        attr_def = HwAttributeDef(cat, "Attr")
        attr_def.setUnitRef(_ref("/unit", "UNIT"))
        parent = _parent()
        writer.writeHwAttributeDef(parent, attr_def)
        assert parent[0].tag == "HW-ATTRIBUTE-DEF"
        assert parent[0].find("UNIT-REF") is not None

    def test_writeHwAttributeDef_none(self, writer):
        parent = _parent()
        writer.writeHwAttributeDef(parent, None)
        assert len(parent) == 0

    def test_writeHwCategoryHwAttributeDef_with_defs(self, writer):
        pkg = _make_pkg()
        cat = HwCategory(pkg, "Cat")
        cat.createHwAttributeDef("Attr1")
        cat.createHwAttributeDef("Attr2")
        parent = _parent()
        writer.writeHwCategoryHwAttributeDef(parent, cat)
        assert parent[0].tag == "HW-ATTRIBUTE-DEFS"
        defs = parent[0].findall("HW-ATTRIBUTE-DEF")
        assert len(defs) == 2

    def test_writeHwCategoryHwAttributeDef_empty(self, writer):
        pkg = _make_pkg()
        cat = HwCategory(pkg, "Cat")
        parent = _parent()
        writer.writeHwCategoryHwAttributeDef(parent, cat)
        assert len(parent) == 0


class TestWriterHwCategoryAndType:
    def test_writeHwCategory_full(self, writer):
        pkg = _make_pkg()
        cat = HwCategory(pkg, "Cat")
        cat.createHwAttributeDef("Attr")
        parent = _parent()
        writer.writeHwCategory(parent, cat)
        assert parent[0].tag == "HW-CATEGORY"
        assert parent[0].find("HW-ATTRIBUTE-DEFS") is not None

    def test_writeHwType_full(self, writer):
        pkg = _make_pkg()
        hw_type = HwType(pkg, "HwType")
        parent = _parent()
        writer.writeHwType(parent, hw_type)
        assert parent[0].tag == "HW-TYPE"


class TestWriterLinCommunicationController:
    def test_writeLinCommunicationController_with_version(self, writer):
        pkg = _make_pkg()
        master = LinMaster(pkg, "LinMaster")
        master.setProtocolVersion(_literal("2.2"))
        parent = _parent()
        controller_elem = ET.SubElement(parent, "LIN-CONTROLLER")
        writer.writeLinCommunicationController(controller_elem, master)
        assert controller_elem.find("PROTOCOL-VERSION") is not None


class TestWriterLinMaster:
    def test_writeLinMaster_full(self, writer):
        pkg = _make_pkg()
        master = LinMaster(pkg, "LinMaster")
        master.setProtocolVersion(_literal("2.2"))
        master.setTimeBase(_time(0.01))
        master.setTimeBaseJitter(_time(0.001))
        parent = _parent()
        writer.writeLinMaster(parent, master)
        assert parent[0].tag == "LIN-MASTER"
        variants = parent[0].find("LIN-MASTER-VARIANTS")
        cond = variants.find("LIN-MASTER-CONDITIONAL")
        assert cond.find("PROTOCOL-VERSION") is not None
        assert cond.find("TIME-BASE") is not None
        assert cond.find("TIME-BASE-JITTER") is not None


class TestLinCommunicationControllerRoundTrip:
    def _round_trip(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        instance = pkg.createEcuInstance("EcuInst")
        master = instance.createLinMaster("Master")
        master.setProtocolVersion(_literal("LIN22"))
        out_file = tmp_path / "lin_master.arxml"
        writer = ARXMLWriter()
        writer.save(str(out_file), autosar)
        reload = AUTOSAR.getInstance()
        reload.clear()
        parser = ARXMLParser()
        parser.load(str(out_file), reload)
        return reload

    def test_round_trip_protocol_version(self, tmp_path):
        reload = self._round_trip(tmp_path)
        reloaded_pkg = reload.getARPackages()[0]
        reloaded_instance = reloaded_pkg.getElement("EcuInst", None)
        controllers = reloaded_instance.getCommControllers()
        assert len(controllers) == 1
        master = controllers[0]
        assert master.getProtocolVersion() is not None
        assert master.getProtocolVersion().getValue() == "LIN22"


class TestWriterISignalToPduMappings:
    def test_writeISignalToPduMappings_with_mappings(self, writer):
        pkg = _make_pkg()
        ipdu = ISignalIPdu(pkg, "IPdu")
        mapping1 = ipdu.createISignalToPduMappings("Map1")
        mapping1.setISignalRef(_ref("/sig1", "I-SIGNAL"))
        mapping1.setStartPosition(_numerical(0))
        mapping2 = ipdu.createISignalToPduMappings("Map2")
        mapping2.setISignalGroupRef(_ref("/grp", "I-SIGNAL-GROUP"))
        mapping2.setPackingByteOrder(_literal("MOST-SIGNIFICANT-BYTE-LAST"))
        mapping2.setTransferProperty(_literal("pending"))
        mapping2.setUpdateIndicationBitPosition(_numerical(8))
        parent = _parent()
        writer.writeISignalToPduMappings(parent, ipdu)
        assert parent[0].tag == "I-SIGNAL-TO-PDU-MAPPINGS"
        mappings = parent[0].findall("I-SIGNAL-TO-I-PDU-MAPPING")
        assert len(mappings) == 2
        assert mappings[0].find("I-SIGNAL-REF") is not None
        assert mappings[0].find("START-POSITION") is not None
        assert mappings[1].find("I-SIGNAL-GROUP-REF") is not None
        assert mappings[1].find("PACKING-BYTE-ORDER") is not None
        assert mappings[1].find("TRANSFER-PROPERTY") is not None
        assert mappings[1].find("UPDATE-INDICATION-BIT-POSITION") is not None

    def test_writeISignalToPduMappings_empty(self, writer):
        pkg = _make_pkg()
        ipdu = ISignalIPdu(pkg, "IPdu")
        parent = _parent()
        writer.writeISignalToPduMappings(parent, ipdu)
        assert len(parent) == 0


class TestWriterDataFilter:
    def test_setDataFilter_full(self, writer):
        filter_obj = DataFilter()
        filter_obj.setDataFilterType(_literal("maskedNewDiffersX"))
        filter_obj.setMask(_integer(0xFF))
        filter_obj.setX(_integer(0x01))
        parent = _parent()
        writer.setDataFilter(parent, "DATA-FILTER", filter_obj)
        assert parent[0].tag == "DATA-FILTER"
        assert parent[0].find("DATA-FILTER-TYPE") is not None
        assert parent[0].find("MASK") is not None
        assert parent[0].find("X") is not None

    def test_setDataFilter_none(self, writer):
        parent = _parent()
        writer.setDataFilter(parent, "DATA-FILTER", None)
        assert len(parent) == 0


class TestWriterTransmissionModeConditions:
    def test_setTransmissionModeConditions_with_conditions(self, writer):
        cond1 = TransmissionModeCondition()
        filter1 = DataFilter()
        filter1.setDataFilterType(_literal("maskedNewDiffersX"))
        cond1.setDataFilter(filter1)
        cond1.setISignalInIPduRef(_ref("/sig", "I-SIGNAL-IN-I-PDU"))
        cond2 = TransmissionModeCondition()
        filter2 = DataFilter()
        filter2.setDataFilterType(_literal("never"))
        cond2.setDataFilter(filter2)
        parent = _parent()
        writer.setTransmissionModeConditions(parent, "TRANSMISSION-MODE-CONDITIONS", [cond1, cond2])
        assert parent[0].tag == "TRANSMISSION-MODE-CONDITIONS"
        conditions = parent[0].findall("TRANSMISSION-MODE-CONDITION")
        assert len(conditions) == 2
        assert conditions[0].find("DATA-FILTER") is not None
        assert conditions[0].find("I-SIGNAL-IN-I-PDU-REF") is not None

    def test_setTransmissionModeConditions_empty(self, writer):
        parent = _parent()
        writer.setTransmissionModeConditions(parent, "TRANSMISSION-MODE-CONDITIONS", [])
        assert len(parent) == 0


class TestWriterTimeRangeType:
    def test_setTimeRangeType_full(self, writer):
        time_range = TimeRangeType()
        time_range.setValue(_time(0.1))
        parent = _parent()
        writer.setTimeRangeType(parent, "TIME-RANGE", time_range)
        assert parent[0].tag == "TIME-RANGE"
        assert parent[0].find("VALUE") is not None

    def test_setTimeRangeType_none(self, writer):
        parent = _parent()
        writer.setTimeRangeType(parent, "TIME-RANGE", None)
        assert len(parent) == 0


class TestWriterEventControlledTiming:
    def test_setEventControlledTiming_full(self, writer):
        timing = EventControlledTiming()
        timing.setNumberOfRepetitions(_integer(3))
        rep_period = TimeRangeType()
        rep_period.setValue(_time(0.01))
        timing.setRepetitionPeriod(rep_period)
        parent = _parent()
        writer.setEventControlledTiming(parent, "EVENT-CONTROLLED-TIMING", timing)
        assert parent[0].tag == "EVENT-CONTROLLED-TIMING"
        assert parent[0].find("NUMBER-OF-REPETITIONS") is not None
        assert parent[0].find("REPETITION-PERIOD") is not None

    def test_setEventControlledTiming_none(self, writer):
        parent = _parent()
        writer.setEventControlledTiming(parent, "EVENT-CONTROLLED-TIMING", None)
        assert len(parent) == 0


class TestWriterCyclicTiming:
    def test_setCyclicTiming_full(self, writer):
        timing = CyclicTiming()
        offset = TimeRangeType()
        offset.setValue(_time(0.0))
        timing.setTimeOffset(offset)
        period = TimeRangeType()
        period.setValue(_time(0.1))
        timing.setTimePeriod(period)
        parent = _parent()
        writer.setCyclicTiming(parent, "CYCLIC-TIMING", timing)
        assert parent[0].tag == "CYCLIC-TIMING"
        assert parent[0].find("TIME-OFFSET") is not None
        assert parent[0].find("TIME-PERIOD") is not None

    def test_setCyclicTiming_none(self, writer):
        parent = _parent()
        writer.setCyclicTiming(parent, "CYCLIC-TIMING", None)
        assert len(parent) == 0


class TestWriterTransmissionModeTiming:
    def test_setTransmissionModeTiming_full(self, writer):
        timing = TransmissionModeTiming()
        cyclic = CyclicTiming()
        cyclic_offset = TimeRangeType()
        cyclic_offset.setValue(_time(0.0))
        cyclic.setTimeOffset(cyclic_offset)
        cyclic_period = TimeRangeType()
        cyclic_period.setValue(_time(0.1))
        cyclic.setTimePeriod(cyclic_period)
        timing.setCyclicTiming(cyclic)
        event = EventControlledTiming()
        event.setNumberOfRepetitions(_integer(2))
        event_period = TimeRangeType()
        event_period.setValue(_time(0.01))
        event.setRepetitionPeriod(event_period)
        timing.setEventControlledTiming(event)
        parent = _parent()
        writer.setTransmissionModeTiming(parent, "TIMING", timing)
        assert parent[0].tag == "TIMING"
        assert parent[0].find("CYCLIC-TIMING") is not None
        assert parent[0].find("EVENT-CONTROLLED-TIMING") is not None

    def test_setTransmissionModeTiming_none(self, writer):
        parent = _parent()
        writer.setTransmissionModeTiming(parent, "TIMING", None)
        assert len(parent) == 0


class TestWriterTransmissionModeDeclaration:
    def test_setTransmissionModeDeclaration_full(self, writer):
        decl = TransmissionModeDeclaration()
        cond = TransmissionModeCondition()
        filter_obj = DataFilter()
        filter_obj.setDataFilterType(_literal("maskedNewDiffersX"))
        cond.setDataFilter(filter_obj)
        cond.setISignalInIPduRef(_ref("/sig", "I-SIGNAL-IN-I-PDU"))
        decl.addTransmissionModeCondition(cond)
        false_timing = TransmissionModeTiming()
        false_cyclic = CyclicTiming()
        false_period = TimeRangeType()
        false_period.setValue(_time(0.2))
        false_cyclic.setTimePeriod(false_period)
        false_timing.setCyclicTiming(false_cyclic)
        decl.setTransmissionModeFalseTiming(false_timing)
        true_timing = TransmissionModeTiming()
        true_cyclic = CyclicTiming()
        true_period = TimeRangeType()
        true_period.setValue(_time(0.1))
        true_cyclic.setTimePeriod(true_period)
        true_timing.setCyclicTiming(true_cyclic)
        decl.setTransmissionModeTrueTiming(true_timing)
        parent = _parent()
        writer.setTransmissionModeDeclaration(parent, "TRANSMISSION-MODE-DECLARATION", decl)
        assert parent[0].tag == "TRANSMISSION-MODE-DECLARATION"
        assert parent[0].find("TRANSMISSION-MODE-CONDITIONS") is not None
        assert parent[0].find("TRANSMISSION-MODE-FALSE-TIMING") is not None
        assert parent[0].find("TRANSMISSION-MODE-TRUE-TIMING") is not None

    def test_setTransmissionModeDeclaration_none(self, writer):
        parent = _parent()
        writer.setTransmissionModeDeclaration(parent, "TRANSMISSION-MODE-DECLARATION", None)
        assert len(parent) == 0


class TestWriterIPduTiming:
    def test_setISignalIPduIPduTimingSpecification_full(self, writer):
        timing = IPduTiming()
        timing.setMinimumDelay(_time(0.05))
        decl = TransmissionModeDeclaration()
        true_timing = TransmissionModeTiming()
        true_cyclic = CyclicTiming()
        true_period = TimeRangeType()
        true_period.setValue(_time(0.1))
        true_cyclic.setTimePeriod(true_period)
        true_timing.setCyclicTiming(true_cyclic)
        decl.setTransmissionModeTrueTiming(true_timing)
        timing.setTransmissionModeDeclaration(decl)
        parent = _parent()
        writer.setISignalIPduIPduTimingSpecification(parent, timing)
        assert parent[0].tag == "I-PDU-TIMING-SPECIFICATIONS"
        ipdu_timing = parent[0].find("I-PDU-TIMING")
        assert ipdu_timing.find("MINIMUM-DELAY") is not None
        assert ipdu_timing.find("TRANSMISSION-MODE-DECLARATION") is not None

    def test_setISignalIPduIPduTimingSpecification_none(self, writer):
        parent = _parent()
        writer.setISignalIPduIPduTimingSpecification(parent, None)
        assert len(parent) == 0


class TestWriterISignalIPdu:
    def test_writeISignalIPdu_full(self, writer):
        pkg = _make_pkg()
        ipdu = ISignalIPdu(pkg, "IPdu")
        ipdu.setLength(_numerical(64))
        timing = IPduTiming()
        timing.setMinimumDelay(_time(0.01))
        ipdu.setIPduTimingSpecification(timing)
        mapping = ipdu.createISignalToPduMappings("Map")
        mapping.setISignalRef(_ref("/sig", "I-SIGNAL"))
        ipdu.setUnusedBitPattern(_integer(0))
        parent = _parent()
        writer.writeISignalIPdu(parent, ipdu)
        assert parent[0].tag == "I-SIGNAL-I-PDU"
        assert parent[0].find("SHORT-NAME").text == "IPdu"
        assert parent[0].find("LENGTH").text == "64"
        assert parent[0].find("I-PDU-TIMING-SPECIFICATIONS") is not None
        assert parent[0].find("I-PDU-TIMING-SPECIFICATIONS/I-PDU-TIMING/MINIMUM-DELAY").text == "0.01"
        assert parent[0].find("I-SIGNAL-TO-PDU-MAPPINGS/I-SIGNAL-TO-I-PDU-MAPPING/I-SIGNAL-REF").text == "/sig"
        assert parent[0].find("UNUSED-BIT-PATTERN").text == "0"

    def test_writeISignalIPdu_no_mappings_omits_wrapper(self, writer):
        pkg = _make_pkg()
        ipdu = ISignalIPdu(pkg, "IPdu")
        ipdu.setUnusedBitPattern(_integer(0))
        parent = _parent()
        writer.writeISignalIPdu(parent, ipdu)
        assert parent[0].tag == "I-SIGNAL-I-PDU"
        assert parent[0].find("I-SIGNAL-TO-PDU-MAPPINGS") is None


class TestWriterFlexrayFrame:
    def test_writeFlexrayFrame_full(self, writer):
        pkg = _make_pkg()
        frame = FlexrayFrame(pkg, "FrFrame")
        frame.setFrameLength(_numerical(16))
        parent = _parent()
        writer.writeFlexrayFrame(parent, frame)
        assert parent[0].tag == "FLEXRAY-FRAME"

    def test_writeFlexrayFrame_none(self, writer):
        parent = _parent()
        writer.writeFlexrayFrame(parent, None)
        assert len(parent) == 0


class TestWriterFlexrayCommunicationController:
    def test_writeFlexrayCommunicationController_all_attrs(self, writer):
        pkg = _make_pkg()
        controller = FlexrayCommunicationController(pkg, "FrCtrl")
        controller.setAcceptedStartupRange(_integer(10))
        controller.setAllowHaltDueToClock(_bool(True))
        controller.setAllowPassiveToActive(_integer(5))
        controller.setClusterDriftDamping(_integer(2))
        controller.setDecodingCorrection(_integer(3))
        controller.setDelayCompensationA(_integer(4))
        controller.setDelayCompensationB(_integer(5))
        controller.setExternalSync(_bool(True))
        controller.setExternOffsetCorrection(_integer(6))
        controller.setExternRateCorrection(_integer(7))
        controller.setFallBackInternal(_bool(False))
        fifo = controller.createFlexrayFifo()
        fifo.setBaseCycle(_integer(1))
        fifo.setFifoDepth(_integer(8))
        controller.setKeySlotID(_posint(1))
        controller.setKeySlotOnlyEnabled(_bool(True))
        controller.setKeySlotUsedForStartUp(_bool(True))
        controller.setKeySlotUsedForSync(_bool(False))
        controller.setLatestTX(_integer(20))
        controller.setListenTimeout(_integer(100))
        controller.setMacroInitialOffsetA(_integer(30))
        controller.setMacroInitialOffsetB(_integer(31))
        controller.setMaximumDynamicPayloadLength(_integer(128))
        controller.setMicroInitialOffsetA(_integer(1))
        controller.setMicroInitialOffsetB(_integer(2))
        controller.setMicroPerCycle(_integer(5000))
        controller.setMicrotickDuration(_time(0.00001))
        controller.setNmVectorEarlyUpdate(_bool(True))
        controller.setOffsetCorrectionOut(_integer(50))
        controller.setRateCorrectionOut(_integer(60))
        controller.setSamplesPerMicrotick(_integer(2))
        controller.setSecondKeySlotId(_posint(3))
        controller.setTwoKeySlotMode(_bool(True))
        controller.setWakeUpPattern(_integer(0))
        parent = _parent()
        writer.writeFlexrayCommunicationController(parent, controller)
        assert parent[0].tag == "FLEXRAY-COMMUNICATION-CONTROLLER"
        cond = parent[0].find("FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS").find("FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert cond.find("ACCEPTED-STARTUP-RANGE").text == "10"
        assert cond.find("ALLOW-HALT-DUE-TO-CLOCK").text == "true"
        assert cond.find("ALLOW-PASSIVE-TO-ACTIVE").text == "5"
        assert cond.find("CLUSTER-DRIFT-DAMPING").text == "2"
        assert cond.find("DECODING-CORRECTION").text == "3"
        assert cond.find("DELAY-COMPENSATION-A").text == "4"
        assert cond.find("DELAY-COMPENSATION-B").text == "5"
        assert cond.find("EXTERNAL-SYNC").text == "true"
        assert cond.find("EXTERN-OFFSET-CORRECTION").text == "6"
        assert cond.find("EXTERN-RATE-CORRECTION").text == "7"
        assert cond.find("FALL-BACK-INTERNAL").text == "false"
        fifo_element = cond.find("FLEXRAY-FIFOS/FLEXRAY-FIFO-CONFIGURATION")
        assert fifo_element is not None
        assert fifo_element.find("BASE-CYCLE").text == "1"
        assert fifo_element.find("FIFO-DEPTH").text == "8"
        assert cond.find("KEY-SLOT-ID").text == "1"
        assert cond.find("KEY-SLOT-ONLY-ENABLED").text == "true"
        assert cond.find("KEY-SLOT-USED-FOR-START-UP").text == "true"
        assert cond.find("KEY-SLOT-USED-FOR-SYNC").text == "false"
        assert cond.find("LATEST-TX").text == "20"
        assert cond.find("LISTEN-TIMEOUT").text == "100"
        assert cond.find("MACRO-INITIAL-OFFSET-A").text == "30"
        assert cond.find("MACRO-INITIAL-OFFSET-B").text == "31"
        assert cond.find("MAXIMUM-DYNAMIC-PAYLOAD-LENGTH").text == "128"
        assert cond.find("MICRO-INITIAL-OFFSET-A").text == "1"
        assert cond.find("MICRO-INITIAL-OFFSET-B").text == "2"
        assert cond.find("MICRO-PER-CYCLE").text == "5000"
        assert float(cond.find("MICROTICK-DURATION").text) == pytest.approx(0.00001)
        assert cond.find("NM-VECTOR-EARLY-UPDATE").text == "true"
        assert cond.find("OFFSET-CORRECTION-OUT").text == "50"
        assert cond.find("RATE-CORRECTION-OUT").text == "60"
        assert cond.find("SAMPLES-PER-MICROTICK").text == "2"
        assert cond.find("SECOND-KEY-SLOT-ID").text == "3"
        assert cond.find("TWO-KEY-SLOT-MODE").text == "true"
        assert cond.find("WAKE-UP-PATTERN").text == "0"

    def test_writeFlexrayCommunicationController_none(self, writer):
        parent = _parent()
        writer.writeFlexrayCommunicationController(parent, None)
        assert len(parent) == 0

    def test_writeFlexrayCommunicationController_no_fifo_wrapper(self, writer):
        pkg = _make_pkg()
        controller = FlexrayCommunicationController(pkg, "FrCtrl")
        controller.setKeySlotID(_posint(1))
        parent = _parent()
        writer.writeFlexrayCommunicationController(parent, controller)
        cond = parent[0].find("FLEXRAY-COMMUNICATION-CONTROLLER-VARIANTS").find("FLEXRAY-COMMUNICATION-CONTROLLER-CONDITIONAL")
        assert cond.find("FLEXRAY-FIFOS") is None


class TestWriterDataTransformation:
    def test_writeDataTransformationTransformerChainRefs_with_refs(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf = dtf_set.createDataTransformation("Dtf")
        dtf.addTransformerChainRef(_ref("/chain1", "TRANSFORMER-CHAIN"))
        dtf.addTransformerChainRef(_ref("/chain2", "TRANSFORMER-CHAIN"))
        parent = _parent()
        writer.writeDataTransformationTransformerChainRefs(parent, dtf)
        assert parent[0].tag == "TRANSFORMER-CHAIN-REFS"
        refs = parent[0].findall("TRANSFORMER-CHAIN-REF")
        assert len(refs) == 2

    def test_writeDataTransformationTransformerChainRefs_empty(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf = dtf_set.createDataTransformation("Dtf")
        parent = _parent()
        writer.writeDataTransformationTransformerChainRefs(parent, dtf)
        assert len(parent) == 0

    def test_writeDataTransformation_full(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf = dtf_set.createDataTransformation("Dtf")
        dtf.setDataTransformationKind(_literal("SYMMETRIC"))
        dtf.setExecuteDespiteDataUnavailability(_bool(True))
        dtf.addTransformerChainRef(_ref("/chain", "TRANSFORMER-CHAIN"))
        parent = _parent()
        writer.writeDataTransformation(parent, dtf)
        assert parent[0].tag == "DATA-TRANSFORMATION"
        assert parent[0].find("DATA-TRANSFORMATION-KIND").text == "SYMMETRIC"
        assert parent[0].find("EXECUTE-DESPITE-DATA-UNAVAILABILITY").text == "true"
        assert parent[0].find("TRANSFORMER-CHAIN-REFS") is not None

    def test_writeDataTransformation_none(self, writer):
        parent = _parent()
        writer.writeDataTransformation(parent, None)
        assert len(parent) == 0


class TestWriterDataTransformationSet:
    def test_writeDataTransformationSetDataTransformations_with_dtfs(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf_set.createDataTransformation("Dtf1")
        dtf_set.createDataTransformation("Dtf2")
        parent = _parent()
        writer.writeDataTransformationSetDataTransformations(parent, dtf_set)
        assert parent[0].tag == "DATA-TRANSFORMATIONS"
        dtfs = parent[0].findall("DATA-TRANSFORMATION")
        assert len(dtfs) == 2

    def test_writeDataTransformationSetDataTransformations_empty(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        parent = _parent()
        writer.writeDataTransformationSetDataTransformations(parent, dtf_set)
        assert len(parent) == 0

    def test_writeDataTransformationSetTransformationTechnologies_with_techs(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf_set.createTransformationTechnology("Tech1")
        dtf_set.createTransformationTechnology("Tech2")
        parent = _parent()
        writer.writeDataTransformationSetTransformationTechnologies(parent, dtf_set)
        assert parent[0].tag == "TRANSFORMATION-TECHNOLOGYS"
        techs = parent[0].findall("TRANSFORMATION-TECHNOLOGY")
        assert len(techs) == 2

    def test_writeDataTransformationSetTransformationTechnologies_empty(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        parent = _parent()
        writer.writeDataTransformationSetTransformationTechnologies(parent, dtf_set)
        assert len(parent) == 0

    def test_writeDataTransformationSet_full(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        dtf_set.createDataTransformation("Dtf")
        dtf_set.createTransformationTechnology("Tech")
        parent = _parent()
        writer.writeDataTransformationSet(parent, dtf_set)
        assert parent[0].tag == "DATA-TRANSFORMATION-SET"
        assert parent[0].find("DATA-TRANSFORMATIONS") is not None
        assert parent[0].find("TRANSFORMATION-TECHNOLOGYS") is not None

    def test_writeDataTransformationSet_none(self, writer):
        parent = _parent()
        writer.writeDataTransformationSet(parent, None)
        assert len(parent) == 0


class TestWriterBufferProperties:
    def test_writeBufferPropertiesBufferComputation_removed(self, writer):
        assert not hasattr(writer, "writeBufferPropertiesBufferComputation")

    def test_setBufferProperties_full(self, writer):
        props = BufferProperties()
        props.setHeaderLength(Integer().setValue("4"))
        props.setInPlace(_bool(True))
        parent = _parent()
        writer.setBufferProperties(parent, "BUFFER-PROPERTIES", props)
        assert parent[0].tag == "BUFFER-PROPERTIES"
        assert parent[0].find("HEADER-LENGTH").text == "4"
        assert parent[0].find("IN-PLACE").text == "true"
        assert parent[0].find("BUFFER-COMPUTATION") is None

    def test_setBufferProperties_none(self, writer):
        parent = _parent()
        writer.setBufferProperties(parent, "BUFFER-PROPERTIES", None)
        assert len(parent) == 0


class TestWriterTransformationDescription:
    def test_writeDescribable(self, writer):
        desc = EndToEndTransformationDescription()
        desc.setCategory(_literal("category"))
        parent = _parent()
        writer.writeDescribable(parent, desc)
        assert parent.find("CATEGORY") is not None
        assert parent.find("CATEGORY").text == "category"

    def test_writeTransformationDescription(self, writer):
        desc = EndToEndTransformationDescription()
        desc.setCategory(_literal("category"))
        parent = _parent()
        writer.writeTransformationDescription(parent, desc)
        assert parent.find("CATEGORY") is not None
        assert parent.find("CATEGORY").text == "category"

    def test_writeEndToEndTransformationDescription_full(self, writer):
        desc = EndToEndTransformationDescription()
        desc.setDataIdMode(_literal("all16Bit"))
        desc.setMaxDeltaCounter(_posint(2))
        desc.setMaxErrorStateInit(_posint(1))
        desc.setMaxErrorStateInvalid(_posint(2))
        desc.setMaxErrorStateValid(_posint(3))
        desc.setMaxNoNewOrRepeatedData(_posint(2))
        desc.setMinOkStateInit(_posint(0))
        desc.setMinOkStateInvalid(_posint(1))
        desc.setMinOkStateValid(_posint(2))
        desc.setProfileBehavior(_literal("R4_2"))
        desc.setProfileName(_literal("Profile1"))
        desc.setSyncCounterInit(_posint(0))
        desc.setUpperHeaderBitsToShift(_posint(0))
        desc.setWindowSizeInit(_posint(1))
        desc.setWindowSizeInvalid(_posint(2))
        desc.setWindowSizeValid(_posint(3))
        parent = _parent()
        writer.writeEndToEndTransformationDescription(parent, desc)
        assert parent[0].tag == "END-TO-END-TRANSFORMATION-DESCRIPTION"
        assert parent[0].find("DATA-ID-MODE") is not None
        assert parent[0].find("MAX-DELTA-COUNTER") is not None
        assert parent[0].find("MAX-ERROR-STATE-INIT") is not None
        assert parent[0].find("MAX-ERROR-STATE-INVALID") is not None
        assert parent[0].find("MAX-ERROR-STATE-VALID") is not None
        assert parent[0].find("MAX-NO-NEW-OR-REPEATED-DATA") is not None
        assert parent[0].find("MIN-OK-STATE-INIT") is not None
        assert parent[0].find("MIN-OK-STATE-INVALID") is not None
        assert parent[0].find("MIN-OK-STATE-VALID") is not None
        assert parent[0].find("PROFILE-BEHAVIOR") is not None
        assert parent[0].find("PROFILE-NAME") is not None
        assert parent[0].find("SYNC-COUNTER-INIT") is not None
        assert parent[0].find("UPPER-HEADER-BITS-TO-SHIFT") is not None
        assert parent[0].find("WINDOW-SIZE-INIT") is not None
        assert parent[0].find("WINDOW-SIZE-INVALID") is not None
        assert parent[0].find("WINDOW-SIZE-VALID") is not None

    def test_writeEndToEndTransformationDescription_none(self, writer):
        parent = _parent()
        writer.writeEndToEndTransformationDescription(parent, None)
        assert len(parent) == 0


class TestWriterTransformationTechnology:
    def test_writeTransformationTechnologyTransformationDescriptions_with_e2e(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        tech = dtf_set.createTransformationTechnology("Tech")
        desc = EndToEndTransformationDescription()
        desc.setProfileName(_literal("Profile1"))
        tech.setTransformationDescription(desc)
        parent = _parent()
        writer.writeTransformationTechnologyTransformationDescriptions(parent, tech)
        assert parent[0].tag == "TRANSFORMATION-DESCRIPTIONS"
        assert parent[0].find("END-TO-END-TRANSFORMATION-DESCRIPTION") is not None

    def test_writeTransformationTechnologyTransformationDescriptions_none(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        tech = dtf_set.createTransformationTechnology("Tech")
        parent = _parent()
        writer.writeTransformationTechnologyTransformationDescriptions(parent, tech)
        assert len(parent) == 0

    def test_writeTransformationTechnology_full(self, writer):
        pkg = _make_pkg()
        dtf_set = DataTransformationSet(pkg, "DtfSet")
        tech = dtf_set.createTransformationTechnology("Tech")
        props = BufferProperties()
        props.setHeaderLength(_integer(4))
        tech.setBufferProperties(props)
        tech.setHasInternalState(_bool(True))
        tech.setNeedsOriginalData(_bool(True))
        tech.setProtocol(_literal("E2E"))
        desc = EndToEndTransformationDescription()
        desc.setProfileName(_literal("Profile1"))
        tech.setTransformationDescription(desc)
        tech.setTransformerClass(_literal("safety"))
        tech.setVersion(_literal("1.0"))
        parent = _parent()
        writer.writeTransformationTechnology(parent, tech)
        assert parent[0].tag == "TRANSFORMATION-TECHNOLOGY"
        assert parent[0].find("BUFFER-PROPERTIES") is not None
        assert parent[0].find("HAS-INTERNAL-STATE") is not None
        assert parent[0].find("NEEDS-ORIGINAL-DATA") is not None
        assert parent[0].find("PROTOCOL") is not None
        assert parent[0].find("TRANSFORMATION-DESCRIPTIONS") is not None
        assert parent[0].find("TRANSFORMER-CLASS") is not None
        assert parent[0].find("VERSION") is not None

    def test_writeTransformationTechnology_none(self, writer):
        parent = _parent()
        writer.writeTransformationTechnology(parent, None)
        assert len(parent) == 0


class TestE2EProfileCompatibilityPropsRoundTrip:
    def _round_trip(self, props, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        pkg.addElement(props)
        out_file = tmp_path / "e2e_compat.arxml"
        writer = ARXMLWriter()
        writer.save(str(out_file), autosar)
        reload = AUTOSAR.getInstance()
        reload.clear()
        parser = ARXMLParser()
        parser.load(str(out_file), reload)
        return reload

    def test_round_trip_with_transit_to_invalid_extended_true(self, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        props = pkg.createE2EProfileCompatibilityProps("Props")
        flag = Boolean()
        flag.setValue("true")
        props.setTransitToInvalidExtended(flag)
        reload = self._round_trip(props, tmp_path)
        reloaded_pkg = reload.getARPackages()[0]
        reloaded_props = reloaded_pkg.getElement("Props", E2EProfileCompatibilityProps)
        assert reloaded_props is not None
        assert reloaded_props.getTransitToInvalidExtended() is not None
        assert reloaded_props.getTransitToInvalidExtended().getValue() is True

    def test_round_trip_with_transit_to_invalid_extended_false(self, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        props = pkg.createE2EProfileCompatibilityProps("Props")
        flag = Boolean()
        flag.setValue("false")
        props.setTransitToInvalidExtended(flag)
        reload = self._round_trip(props, tmp_path)
        reloaded_pkg = reload.getARPackages()[0]
        reloaded_props = reloaded_pkg.getElement("Props", E2EProfileCompatibilityProps)
        assert reloaded_props is not None
        assert reloaded_props.getTransitToInvalidExtended() is not None
        assert reloaded_props.getTransitToInvalidExtended().getValue() is False

    def test_round_trip_empty_omits_attribute(self, tmp_path):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        props = pkg.createE2EProfileCompatibilityProps("Props")
        assert props.getTransitToInvalidExtended() is None
        reload = self._round_trip(props, tmp_path)
        reloaded_pkg = reload.getARPackages()[0]
        reloaded_props = reloaded_pkg.getElement("Props", E2EProfileCompatibilityProps)
        assert reloaded_props is not None
        assert reloaded_props.getTransitToInvalidExtended() is None


class TestEndToEndTransformationDescriptionRoundTrip:
    def _build(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        dtf_set = pkg.createDataTransformationSet("DtfSet")
        tech = dtf_set.createTransformationTechnology("Tech")
        desc = EndToEndTransformationDescription()
        flag = Boolean()
        flag.setValue("true")
        desc.setClearFromValidToInvalid(flag)
        desc.setCounterOffset(PositiveInteger().setValue("5"))
        desc.setCrcOffset(PositiveInteger().setValue("10"))
        desc.setDataIdMode(_literal("all16Bit"))
        desc.setDataIdNibbleOffset(PositiveInteger().setValue("2"))
        ref = RefType()
        ref.setValue("/E2E/Props")
        ref.setDest("E-2-E-PROFILE-COMPATIBILITY-PROPS")
        desc.setE2eProfileCompatibilityPropsRef(ref)
        desc.setMaxDeltaCounter(PositiveInteger().setValue("100"))
        desc.setMaxErrorStateInit(PositiveInteger().setValue("1"))
        desc.setMaxErrorStateInvalid(PositiveInteger().setValue("2"))
        desc.setMaxErrorStateValid(PositiveInteger().setValue("3"))
        desc.setMaxNoNewOrRepeatedData(PositiveInteger().setValue("2"))
        desc.setMinOkStateInit(PositiveInteger().setValue("0"))
        desc.setMinOkStateInvalid(PositiveInteger().setValue("1"))
        desc.setMinOkStateValid(PositiveInteger().setValue("2"))
        desc.setOffset(PositiveInteger().setValue("0"))
        desc.setProfileBehavior(_literal("R4_2"))
        desc.setProfileName(_literal("Profile1"))
        desc.setSyncCounterInit(PositiveInteger().setValue("0"))
        desc.setUpperHeaderBitsToShift(PositiveInteger().setValue("0"))
        desc.setWindowSizeInit(PositiveInteger().setValue("1"))
        desc.setWindowSizeInvalid(PositiveInteger().setValue("2"))
        desc.setWindowSizeValid(PositiveInteger().setValue("3"))
        tech.setTransformationDescription(desc)
        return autosar, desc

    def _round_trip(self, autosar, tmp_path):
        out_file = tmp_path / "e2e_desc.arxml"
        ARXMLWriter().save(str(out_file), autosar)
        reload = AUTOSAR.getInstance()
        reload.clear()
        ARXMLParser().load(str(out_file), reload)
        return reload

    def _reload_desc(self, reload):
        dtf_set = reload.getARPackages()[0].getElement("DtfSet", DataTransformationSet)
        tech = None
        for t in dtf_set.getTransformationTechnologies():
            if t.getShortName() == "Tech":
                tech = t
        return tech.getTransformationDescription()

    def test_round_trip_all_attributes(self, tmp_path):
        autosar, _ = self._build()
        reload = self._round_trip(autosar, tmp_path)
        desc = self._reload_desc(reload)
        assert isinstance(desc, EndToEndTransformationDescription)
        assert desc.getClearFromValidToInvalid().getValue() is True
        assert desc.getCounterOffset().getValue() == 5
        assert desc.getCrcOffset().getValue() == 10
        assert desc.getDataIdMode().getValue() == "all16Bit"
        assert desc.getDataIdNibbleOffset().getValue() == 2
        ref = desc.getE2eProfileCompatibilityPropsRef()
        assert ref is not None and ref.getValue() == "/E2E/Props"
        assert ref.getDest() == "E-2-E-PROFILE-COMPATIBILITY-PROPS"
        assert desc.getMaxDeltaCounter().getValue() == 100
        assert desc.getMaxErrorStateInit().getValue() == 1
        assert desc.getMaxErrorStateInvalid().getValue() == 2
        assert desc.getMaxErrorStateValid().getValue() == 3
        assert desc.getMaxNoNewOrRepeatedData().getValue() == 2
        assert desc.getMinOkStateInit().getValue() == 0
        assert desc.getMinOkStateInvalid().getValue() == 1
        assert desc.getMinOkStateValid().getValue() == 2
        assert desc.getOffset().getValue() == 0
        assert desc.getProfileBehavior().getValue() == "R4_2"
        assert desc.getProfileName().getValue() == "Profile1"
        assert desc.getSyncCounterInit().getValue() == 0
        assert desc.getUpperHeaderBitsToShift().getValue() == 0
        assert desc.getWindowSizeInit().getValue() == 1
        assert desc.getWindowSizeInvalid().getValue() == 2
        assert desc.getWindowSizeValid().getValue() == 3

    def test_round_trip_empty_omits_attributes(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        autosar = AUTOSAR.getInstance()
        pkg = autosar.createARPackage("Pkg")
        dtf_set = pkg.createDataTransformationSet("DtfSet")
        tech = dtf_set.createTransformationTechnology("Tech")
        tech.setTransformationDescription(EndToEndTransformationDescription())
        reload = self._round_trip(autosar, tmp_path)
        desc = self._reload_desc(reload)
        assert desc.getCounterOffset() is None
        assert desc.getCrcOffset() is None
        assert desc.getDataIdMode() is None
        assert desc.getE2eProfileCompatibilityPropsRef() is None
        assert desc.getProfileName() is None
        assert desc.getWindowSizeValid() is None
