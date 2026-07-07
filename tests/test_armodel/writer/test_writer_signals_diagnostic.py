"""Tests for writer signal, lifecycle and diagnostic handlers."""
import xml.etree.cElementTree as ET
import pytest

from armodel.writer.arxml_writer import ARXMLWriter
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import (  # noqa: E501
    ISignalGroup,
    ISignalIPduGroup,
    SystemSignal,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetFrame import (  # noqa: E501
    GenericEthernetFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    EndToEndTransformationISignalProps,
    TransformationISignalProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.LifeCycles import (
    LifeCycleInfo,
    LifeCycleInfoSet,
    LifeCyclePeriod,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection import (  # noqa: E501
    DiagnosticConnection,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticContribution import (  # noqa: E501
    DiagnosticServiceTable,
)
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import (
    DocumentationBlock,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (  # noqa: E501
    ARBoolean,
    ARLiteral,
    PositiveInteger,
    RefType,
    RevisionLabelString,
)


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


def _pkg():
    return AUTOSAR.getInstance().createARPackage("Pkg")


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


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _revision_label(value):
    r = RevisionLabelString()
    r.setValue(value)
    return r


def _make_isignal_group():
    return _pkg().createISignalGroup("ISigGrp")


def _make_isignal_ipdu_group():
    return _pkg().createISignalIPduGroup("ISigIPduGrp")


def _make_system_signal():
    return _pkg().createSystemSignal("SysSig")


def _make_ethernet_frame():
    return _pkg().createGenericEthernetFrame("EthFrame")


def _make_life_cycle_info_set():
    return _pkg().createLifeCycleInfoSet("LcSet")


def _make_diagnostic_connection():
    return _pkg().createDiagnosticConnection("DiagConn")


def _make_diagnostic_service_table():
    return _pkg().createDiagnosticServiceTable("DiagTable")


class TestWriterISignalGroupISignalRef:
    def test_with_refs(self, writer):
        group = _make_isignal_group()
        group.addISignalRef(_ref("/s1", "I-SIGNAL"))
        group.addISignalRef(_ref("/s2", "I-SIGNAL"))
        parent = _parent()
        writer.writeISignalGroupISignalRef(parent, group)
        assert parent[0].tag == "I-SIGNAL-REFS"
        refs = parent[0].findall("I-SIGNAL-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        group = _make_isignal_group()
        parent = _parent()
        writer.writeISignalGroupISignalRef(parent, group)
        assert len(parent) == 0


class TestWriterISignalGroupComBasedSignalGroupTransformation:
    def test_with_refs(self, writer):
        group = _make_isignal_group()
        group.addComBasedSignalGroupTransformationRef(
            _ref("/dt1", "DATA-TRANSFORMATION")
        )
        group.addComBasedSignalGroupTransformationRef(
            _ref("/dt2", "DATA-TRANSFORMATION")
        )
        parent = _parent()
        writer.writeISignalGroupComBasedSignalGroupTransformation(
            parent, group
        )
        assert parent[0].tag == "COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS"
        cond = parent[0].find("DATA-TRANSFORMATION-REF-CONDITIONAL")
        assert cond is not None
        refs = cond.findall("DATA-TRANSFORMATION-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        group = _make_isignal_group()
        parent = _parent()
        writer.writeISignalGroupComBasedSignalGroupTransformation(
            parent, group
        )
        assert len(parent) == 0


class TestWriterTransformationISignalProps:
    def test_dispatch_writes_describable(self, writer):
        props = EndToEndTransformationISignalProps()
        parent = _parent()
        writer.writeTransformationISignalProps(parent, props)
        assert len(parent) == 0


class TestWriterEndToEndTransformationISignalPropsDataIds:
    def test_with_ids(self, writer):
        props = EndToEndTransformationISignalProps()
        props.addDataId(_posint(1))
        props.addDataId(_posint(2))
        parent = _parent()
        writer.writeEndToEndTransformationISignalPropsDataIds(parent, props)
        assert parent[0].tag == "DATA-IDS"
        ids = parent[0].findall("DATA-ID")
        assert len(ids) == 2

    def test_empty(self, writer):
        props = EndToEndTransformationISignalProps()
        parent = _parent()
        writer.writeEndToEndTransformationISignalPropsDataIds(parent, props)
        assert len(parent) == 0


class TestWriterEndToEndTransformationISignalProps:
    def test_full(self, writer):
        props = EndToEndTransformationISignalProps()
        props.setTransformerRef(_ref("/tr", "TRANSFORMATION-PROPS"))
        props.addDataId(_posint(10))
        props.setDataLength(_posint(64))
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, props)
        assert parent[0].tag == "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS"
        variants = parent[0].find(
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-VARIANTS"
        )
        assert variants is not None
        cond = variants.find(
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS-CONDITIONAL"
        )
        assert cond is not None
        assert cond.find("TRANSFORMER-REF") is not None
        assert cond.find("DATA-IDS") is not None
        assert cond.find("DATA-LENGTH") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeEndToEndTransformationISignalProps(parent, None)
        assert len(parent) == 0


class TestWriterISignalGroupTransformationISignalProps:
    def test_with_end_to_end_props(self, writer):
        group = _make_isignal_group()
        props = EndToEndTransformationISignalProps()
        props.setTransformerRef(_ref("/tr", "TRANSFORMATION-PROPS"))
        group.setTransformationISignalProps(props)
        parent = _parent()
        writer.writeISignalGroupTransformationISignalProps(parent, group)
        assert parent[0].tag == "TRANSFORMATION-I-SIGNAL-PROPSS"
        assert parent[0].find(
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS"
        ) is not None

    def test_none(self, writer):
        group = _make_isignal_group()
        parent = _parent()
        writer.writeISignalGroupTransformationISignalProps(parent, group)
        assert len(parent) == 0

    def test_unsupported_props_warns(self, caplog):
        warn_writer = ARXMLWriter(options={"warning": True})

        class _OtherProps(TransformationISignalProps):
            def __init__(self):
                super().__init__()

        group = _make_isignal_group()
        group.setTransformationISignalProps(_OtherProps())
        parent = _parent()
        warn_writer.writeISignalGroupTransformationISignalProps(parent, group)
        assert parent[0].tag == "TRANSFORMATION-I-SIGNAL-PROPSS"
        assert parent[0].find(
            "END-TO-END-TRANSFORMATION-I-SIGNAL-PROPS"
        ) is None
        assert "Unsupported TransformationISignalProps" in caplog.text


class TestWriterISignalGroup:
    def test_full(self, writer):
        group = _make_isignal_group()
        group.addISignalRef(_ref("/s1", "I-SIGNAL"))
        group.addComBasedSignalGroupTransformationRef(
            _ref("/dt", "DATA-TRANSFORMATION")
        )
        group.setSystemSignalGroupRef(
            _ref("/ssg", "SYSTEM-SIGNAL-GROUP")
        )
        props = EndToEndTransformationISignalProps()
        props.setTransformerRef(_ref("/tr", "TRANSFORMATION-PROPS"))
        props.addDataId(_posint(5))
        props.setDataLength(_posint(32))
        group.setTransformationISignalProps(props)
        parent = _parent()
        writer.writeISignalGroup(parent, group)
        elem = parent.find("I-SIGNAL-GROUP")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("I-SIGNAL-REFS") is not None
        assert elem.find("COM-BASED-SIGNAL-GROUP-TRANSFORMATIONS") is not None
        assert elem.find("SYSTEM-SIGNAL-GROUP-REF") is not None
        assert elem.find("TRANSFORMATION-I-SIGNAL-PROPSS") is not None


class TestWriterISignalIPduGroup:
    def test_full(self, writer):
        group = _make_isignal_ipdu_group()
        group.setCommunicationDirection(_literal("OUT"))
        group.setCommunicationMode(_literal("PERIODIC"))
        group.addContainedISignalIPduGroupRef(
            _ref("/g", "I-SIGNAL-I-PDU-GROUP")
        )
        group.addISignalIPduRef(_ref("/p", "I-SIGNAL-I-PDU"))
        parent = _parent()
        writer.writeISignalIPduGroup(parent, group)
        elem = parent.find("I-SIGNAL-I-PDU-GROUP")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("COMMUNICATION-DIRECTION").text == "OUT"
        assert elem.find("COMMUNICATION-MODE").text == "PERIODIC"
        assert elem.find("CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS") is not None
        assert elem.find("I-SIGNAL-I-PDUS") is not None
        cond = elem.find("I-SIGNAL-I-PDUS/I-SIGNAL-I-PDU-REF-CONDITIONAL")
        assert cond is not None

    def test_empty(self, writer):
        group = _make_isignal_ipdu_group()
        parent = _parent()
        writer.writeISignalIPduGroup(parent, group)
        elem = parent.find("I-SIGNAL-I-PDU-GROUP")
        assert elem is not None
        assert elem.find("COMMUNICATION-DIRECTION") is None
        assert elem.find("COMMUNICATION-MODE") is None
        assert elem.find("CONTAINED-I-SIGNAL-I-PDU-GROUP-REFS") is None
        assert elem.find("I-SIGNAL-I-PDUS") is None


class TestWriterSystemSignal:
    def test_full(self, writer):
        signal = _make_system_signal()
        signal.setDynamicLength(_bool(True))
        parent = _parent()
        writer.writeSystemSignal(parent, signal)
        elem = parent.find("SYSTEM-SIGNAL")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("DYNAMIC-LENGTH") is not None

    def test_without_dynamic_length(self, writer):
        signal = _make_system_signal()
        parent = _parent()
        writer.writeSystemSignal(parent, signal)
        elem = parent.find("SYSTEM-SIGNAL")
        assert elem is not None
        assert elem.find("DYNAMIC-LENGTH") is None


class TestWriterGenericEthernetFrame:
    def test_full(self, writer):
        frame = _make_ethernet_frame()
        parent = _parent()
        writer.writeGenericEthernetFrame(parent, frame)
        elem = parent.find("ETHERNET-FRAME")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None


class TestWriterSetLifeCyclePeriod:
    def test_with_period(self, writer):
        period = LifeCyclePeriod()
        period.setArReleaseVersion(_revision_label("R23-11"))
        parent = _parent()
        writer.setLifeCyclePeriod(parent, "PERIOD-BEGIN", period)
        assert parent[0].tag == "PERIOD-BEGIN"
        assert parent[0].find("AR-RELEASE-VERSION") is not None
        assert parent[0].find("AR-RELEASE-VERSION").text == "R23-11"

    def test_none(self, writer):
        parent = _parent()
        writer.setLifeCyclePeriod(parent, "PERIOD-BEGIN", None)
        assert len(parent) == 0


class TestWriterLifeCycleInfoUseInsteadRefs:
    def test_with_refs(self, writer):
        info = LifeCycleInfo()
        info.addUseInsteadRef(_ref("/u1", "LIFE-CYCLE-INFO"))
        info.addUseInsteadRef(_ref("/u2", "LIFE-CYCLE-INFO"))
        parent = _parent()
        writer.writeLifeCycleInfoUseInsteadRefs(parent, info)
        assert parent[0].tag == "USE-INSTEAD-REFS"
        refs = parent[0].findall("USE-INSTEAD-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        info = LifeCycleInfo()
        parent = _parent()
        writer.writeLifeCycleInfoUseInsteadRefs(parent, info)
        assert len(parent) == 0


class TestWriterLifeCycleInfo:
    def test_full(self, writer):
        info = LifeCycleInfo()
        info.setLcObjectRef(_ref("/obj", "REFERRABLE"))
        info.setLcStateRef(_ref("/state", "LIFE-CYCLE-STATE"))
        period = LifeCyclePeriod()
        period.setArReleaseVersion(_revision_label("R23-11"))
        info.setPeriodBegin(period)
        info.setRemark(DocumentationBlock())
        info.addUseInsteadRef(_ref("/u", "LIFE-CYCLE-INFO"))
        parent = _parent()
        writer.writeLifeCycleInfo(parent, info)
        elem = parent.find("LIFE-CYCLE-INFO")
        assert elem is not None
        assert elem.find("LC-OBJECT-REF") is not None
        assert elem.find("LC-STATE-REF") is not None
        assert elem.find("PERIOD-BEGIN") is not None
        assert elem.find("REMARK") is not None
        assert elem.find("USE-INSTEAD-REFS") is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeLifeCycleInfo(parent, None)
        assert len(parent) == 0


class TestWriterLifeCycleInfoSetLifeCycleInfos:
    def test_with_infos(self, writer):
        info_set = _make_life_cycle_info_set()
        info1 = LifeCycleInfo()
        info1.setLcObjectRef(_ref("/o1", "REFERRABLE"))
        info2 = LifeCycleInfo()
        info2.setLcObjectRef(_ref("/o2", "REFERRABLE"))
        info_set.addLifeCycleInfo(info1)
        info_set.addLifeCycleInfo(info2)
        parent = _parent()
        writer.writeLifeCycleInfoSetLifeCycleInfos(parent, info_set)
        assert parent[0].tag == "LIFE-CYCLE-INFOS"
        infos = parent[0].findall("LIFE-CYCLE-INFO")
        assert len(infos) == 2

    def test_empty(self, writer):
        info_set = _make_life_cycle_info_set()
        parent = _parent()
        writer.writeLifeCycleInfoSetLifeCycleInfos(parent, info_set)
        assert len(parent) == 0


class TestWriterLifeCycleInfoSet:
    def test_full(self, writer):
        info_set = _make_life_cycle_info_set()
        info_set.setDefaultLcStateRef(
            _ref("/dstate", "LIFE-CYCLE-STATE-DEFINITION")
        )
        info = LifeCycleInfo()
        info.setLcObjectRef(_ref("/obj", "REFERRABLE"))
        info_set.addLifeCycleInfo(info)
        info_set.setUsedLifeCycleStateDefinitionGroupRef(
            _ref("/grp", "LIFE-CYCLE-STATE-DEFINITION-GROUP")
        )
        parent = _parent()
        writer.writeLifeCycleInfoSet(parent, info_set)
        elem = parent.find("LIFE-CYCLE-INFO-SET")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("DEFAULT-LC-STATE-REF") is not None
        assert elem.find("LIFE-CYCLE-INFOS") is not None
        assert elem.find(
            "USED-LIFE-CYCLE-STATE-DEFINITION-GROUP-REF"
        ) is not None

    def test_none(self, writer):
        parent = _parent()
        writer.writeLifeCycleInfoSet(parent, None)
        assert len(parent) == 0


class TestWriterDiagnosticConnectionFunctionalRequestRefs:
    def test_with_refs(self, writer):
        conn = _make_diagnostic_connection()
        conn.addFunctionalRequestRef(_ref("/f1", "DIAGNOSTIC-REQUEST"))
        conn.addFunctionalRequestRef(_ref("/f2", "DIAGNOSTIC-REQUEST"))
        parent = _parent()
        writer.writeDiagnosticConnectionFunctionalRequestRefs(parent, conn)
        assert parent[0].tag == "FUNCTIONAL-REQUEST-REFS"
        refs = parent[0].findall("FUNCTIONAL-REQUEST-REF")
        assert len(refs) == 2

    def test_empty(self, writer):
        conn = _make_diagnostic_connection()
        parent = _parent()
        writer.writeDiagnosticConnectionFunctionalRequestRefs(parent, conn)
        assert len(parent) == 0


class TestWriterDiagnosticConnection:
    def test_full(self, writer):
        conn = _make_diagnostic_connection()
        conn.addFunctionalRequestRef(_ref("/f", "DIAGNOSTIC-REQUEST"))
        conn.setPhysicalRequestRef(_ref("/p", "DIAGNOSTIC-REQUEST"))
        conn.setResponseOnEventRef(_ref("/r", "DIAGNOSTIC-RESPONSE"))
        parent = _parent()
        writer.writeDiagnosticConnection(parent, conn)
        elem = parent.find("DIAGNOSTIC-CONNECTION")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("FUNCTIONAL-REQUEST-REFS") is not None
        assert elem.find("PHYSICAL-REQUEST-REF") is not None
        assert elem.find("RESPONSE-REF") is not None


class TestWriterDiagnosticServiceTableDiagnosticConnectionRefs:
    def test_with_refs(self, writer):
        table = _make_diagnostic_service_table()
        table.addDiagnosticConnectionRef(_ref("/c1", "DIAGNOSTIC-CONNECTION"))
        table.addDiagnosticConnectionRef(_ref("/c2", "DIAGNOSTIC-CONNECTION"))
        parent = _parent()
        writer.writeDiagnosticServiceTableDiagnosticConnectionRefs(
            parent, table
        )
        assert parent[0].tag == "DIAGNOSTIC-CONNECTIONS"
        conds = parent[0].findall("DIAGNOSTIC-CONNECTION-REF-CONDITIONAL")
        assert len(conds) == 2

    def test_empty(self, writer):
        table = _make_diagnostic_service_table()
        parent = _parent()
        writer.writeDiagnosticServiceTableDiagnosticConnectionRefs(
            parent, table
        )
        assert len(parent) == 0


class TestWriterDiagnosticServiceTable:
    def test_full(self, writer):
        table = _make_diagnostic_service_table()
        table.addDiagnosticConnectionRef(
            _ref("/c", "DIAGNOSTIC-CONNECTION")
        )
        table.setEcuInstanceRef(_ref("/ecu", "ECU-INSTANCE"))
        parent = _parent()
        writer.writeDiagnosticServiceTable(parent, table)
        elem = parent.find("DIAGNOSTIC-SERVICE-TABLE")
        assert elem is not None
        assert elem.find("SHORT-NAME") is not None
        assert elem.find("DIAGNOSTIC-CONNECTIONS") is not None
        assert elem.find("ECU-INSTANCE-REF") is not None
