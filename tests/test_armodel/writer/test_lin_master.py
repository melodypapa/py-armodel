"""Writer round-trip tests for LinMaster (Table 3.38, p.94).

Verifies that a LinMaster created on an EcuInstance survives a full
set -> save -> reload cycle, including its aggregated LinSlaveConfig
list and inherited PROTOCOL-VERSION, with empty-wrapper omission.
"""

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import (
    LinConfigurableFrame,
    LinMaster,
    LinOrderedConfigurableFrame,
    LinSlaveConfig,
    LinSlaveConfigIdent,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology import EcuInstance
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
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    return ARXMLWriter()


@pytest.fixture
def parser():
    return ARXMLParser(options={"warning": True})


def _reload(parser, path):
    AUTOSAR.getInstance().new()
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(path, document)
    return document


def _literal(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _int(value):
    n = Integer()
    n.setValue(value)
    return n


def _pint(value):
    n = PositiveInteger()
    n.setValue(value)
    return n


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t


def _ref(value):
    ref = RefType()
    ref.setValue(value)
    return ref


def _build_master(pkg):
    instance = pkg.createEcuInstance("EcuInst")
    master = instance.createLinMaster("LinMaster")
    master.setProtocolVersion(_literal("2.1"))
    master.setTimeBase(_time(0.01))
    master.setTimeBaseJitter(_time(0.001))

    slave1 = LinSlaveConfig()
    slave1.setIdent(LinSlaveConfigIdent(slave1, "SlaveIdent"))
    slave1.setInitialNad(_int(1))
    slave1.setConfiguredNad(_int(3))
    master.addLinSlave(slave1)

    slave2 = LinSlaveConfig()

    frame = LinConfigurableFrame()
    frame.setFrameRef(_ref("/Pkg/LinFrame"))
    frame.setMessageId(_pint(42))
    slave2.addLinConfigurableFrame(frame)

    response = LinErrorResponse()
    response.setResponseErrorRef(_ref("/Pkg/ISignalTriggering"))
    slave2.setLinErrorResponse(response)

    ordered = LinOrderedConfigurableFrame()
    ordered.setFrameRef(_ref("/Pkg/LinFrame2"))
    ordered.setIndex(_int(7))
    slave2.addLinOrderedConfigurableFrame(ordered)

    slave2.setSupplierId(_pint(17))
    master.addLinSlave(slave2)
    return instance, master


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    _build_master(pkg)

    out_file = str(tmp_path / "lin_master.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_instance = re_pkg.getElement("EcuInst", EcuInstance)
    assert re_instance is not None

    re_master = re_instance.getElement("LinMaster", LinMaster)
    assert re_master is not None
    assert isinstance(re_master, LinMaster)
    assert re_master.getProtocolVersion().getValue() == "2.1"
    assert re_master.getTimeBase().getValue() == 0.01
    assert re_master.getTimeBaseJitter().getValue() == 0.001

    slaves = re_master.getLinSlaves()
    assert len(slaves) == 2

    assert isinstance(slaves[0], LinSlaveConfig)
    assert slaves[0].getIdent().getShortName() == "SlaveIdent"
    assert slaves[0].getInitialNad().getValue() == 1
    assert slaves[0].getConfiguredNad().getValue() == 3

    assert len(slaves[1].getLinConfigurableFrames()) == 1
    assert slaves[1].getLinConfigurableFrames()[0].getFrameRef().getValue() == "/Pkg/LinFrame"
    assert slaves[1].getLinConfigurableFrames()[0].getMessageId().getValue() == 42
    assert slaves[1].getLinErrorResponse().getResponseErrorRef().getValue() == "/Pkg/ISignalTriggering"
    assert len(slaves[1].getLinOrderedConfigurableFrames()) == 1
    assert slaves[1].getLinOrderedConfigurableFrames()[0].getIndex().getValue() == 7
    assert slaves[1].getSupplierId().getValue() == 17


def test_round_trip_empty_wrapper_list(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = pkg.createEcuInstance("EcuInst")
    instance.createLinMaster("EmptyMaster")

    out_file = str(tmp_path / "lin_master_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_instance = document.find("Pkg").getElement("EcuInst", EcuInstance)
    re_master = re_instance.getElement("EmptyMaster", LinMaster)
    assert re_master is not None
    assert re_master.getLinSlaves() == []
    assert re_master.getTimeBase() is None
    assert re_master.getTimeBaseJitter() is None
