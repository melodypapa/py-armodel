"""Writer round-trip tests for LinSlave (Table 3.41, p.97).

Verifies that a LinSlave created on an EcuInstance survives a full
set -> save -> reload cycle, including its aggregated LinErrorResponse
and inherited PROTOCOL-VERSION, with empty-wrapper omission. XML
element order per XSD LIN-SLAVE-CONTENT (AUTOSAR_00052.xsd line 77893):
ASSIGN-NAD, CONFIGURED-NAD, FUNCTION-ID, INITIAL-NAD, LIN-ERROR-RESPONSE,
NAS-TIMEOUT, SUPPLIER-ID, VARIANT-ID, preceded inside the
LIN-SLAVE-CONDITIONAL wrapper by the inherited
LIN-COMMUNICATION-CONTROLLER-CONTENT (PROTOCOL-VERSION); the
LIN-SLAVE-VARIANTS/LIN-SLAVE-CONDITIONAL wrapper is always emitted.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    Boolean,
    Integer,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication import LinErrorResponse
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology import LinSlave
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


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


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


def _typed_ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


def _build_slave(pkg):
    instance = pkg.createEcuInstance("EcuInst")
    slave = instance.createLinSlave("LinSlave")
    slave.setProtocolVersion(_literal("2.0"))
    slave.setAssignNad(_bool(True))
    slave.setConfiguredNad(_int(3))
    slave.setFunctionId(_pint(17))
    slave.setInitialNad(_int(1))

    response = LinErrorResponse()
    response.setResponseErrorRef(_typed_ref("/Pkg/ISignalTriggering", "I-SIGNAL-TRIGGERING"))
    slave.setLinErrorResponse(response)

    slave.setNasTimeout(_time(0.1))
    slave.setSupplierId(_pint(2721))
    slave.setVariantId(_pint(5))
    return instance, slave


def test_round_trip_full(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    _build_slave(pkg)

    out_file = str(tmp_path / "lin_slave.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_pkg = document.find("Pkg")
    assert re_pkg is not None

    re_instance = re_pkg.getReferrableElement("EcuInst", EcuInstance)
    assert re_instance is not None

    re_slave = re_instance.getReferrableElement("LinSlave", LinSlave)
    assert re_slave is not None
    assert isinstance(re_slave, LinSlave)
    assert re_slave.getProtocolVersion().getValue() == "2.0"
    assert re_slave.getAssignNad().getValue() is True
    assert re_slave.getConfiguredNad().getValue() == 3
    assert re_slave.getFunctionId().getValue() == 17
    assert re_slave.getInitialNad().getValue() == 1
    assert re_slave.getLinErrorResponse() is not None
    assert re_slave.getLinErrorResponse().getResponseErrorRef().getValue() == "/Pkg/ISignalTriggering"
    assert re_slave.getNasTimeout().getValue() == 0.1
    assert re_slave.getSupplierId().getValue() == 2721
    assert re_slave.getVariantId().getValue() == 5


def test_round_trip_empty_wrapper_list(writer, parser, tmp_path):
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    instance = pkg.createEcuInstance("EcuInst")
    instance.createLinSlave("EmptySlave")

    out_file = str(tmp_path / "lin_slave_empty.arxml")
    writer.save(out_file, AUTOSAR.getInstance())

    document = _reload(parser, out_file)
    re_instance = document.find("Pkg").getReferrableElement("EcuInst", EcuInstance)
    re_slave = re_instance.getReferrableElement("EmptySlave", LinSlave)
    assert re_slave is not None
    assert isinstance(re_slave, LinSlave)
    assert re_slave.getProtocolVersion() is None
    assert re_slave.getAssignNad() is None
    assert re_slave.getConfiguredNad() is None
    assert re_slave.getFunctionId() is None
    assert re_slave.getInitialNad() is None
    assert re_slave.getLinErrorResponse() is None
    assert re_slave.getNasTimeout() is None
    assert re_slave.getSupplierId() is None
    assert re_slave.getVariantId() is None


class TestWriteLinSlaveXmlShape:
    def _write_slave(self, slave):
        parent = ET.Element("PARENT")
        ARXMLWriter().writeLinSlave(parent, slave)
        return parent.find("LIN-SLAVE")

    def test_write_conditional_children_in_xsd_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        _, slave = _build_slave(pkg)
        lin_slave = self._write_slave(slave)

        cond = lin_slave.find("LIN-SLAVE-VARIANTS/LIN-SLAVE-CONDITIONAL")
        assert cond is not None
        tags = [child.tag for child in cond]
        assert tags.index("PROTOCOL-VERSION") < tags.index("ASSIGN-NAD")
        assert tags.index("ASSIGN-NAD") < tags.index("CONFIGURED-NAD")
        assert tags.index("CONFIGURED-NAD") < tags.index("FUNCTION-ID")
        assert tags.index("FUNCTION-ID") < tags.index("INITIAL-NAD")
        assert tags.index("INITIAL-NAD") < tags.index("LIN-ERROR-RESPONSE")
        assert tags.index("LIN-ERROR-RESPONSE") < tags.index("NAS-TIMEOUT")
        assert tags.index("NAS-TIMEOUT") < tags.index("SUPPLIER-ID")
        assert tags.index("SUPPLIER-ID") < tags.index("VARIANT-ID")

    def test_write_wraps_in_variants_conditional(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        instance = pkg.createEcuInstance("EcuInst")
        slave = instance.createLinSlave("BareSlave")
        lin_slave = self._write_slave(slave)

        cond = lin_slave.find("LIN-SLAVE-VARIANTS/LIN-SLAVE-CONDITIONAL")
        assert cond is not None
        assert len(cond) == 0

    def test_write_base_helper_called_exactly_once(self):
        pkg = AUTOSAR.getInstance().createARPackage("Pkg")
        _, slave = _build_slave(pkg)
        lin_slave = self._write_slave(slave)

        assert len(lin_slave.findall(".//PROTOCOL-VERSION")) == 1
        assert len(lin_slave.findall(".//ASSIGN-NAD")) == 1
        assert len(lin_slave.findall(".//CONFIGURED-NAD")) == 1
        assert len(lin_slave.findall(".//FUNCTION-ID")) == 1
        assert len(lin_slave.findall(".//INITIAL-NAD")) == 1
        assert len(lin_slave.findall(".//LIN-ERROR-RESPONSE")) == 1
        assert len(lin_slave.findall(".//NAS-TIMEOUT")) == 1
        assert len(lin_slave.findall(".//SUPPLIER-ID")) == 1
        assert len(lin_slave.findall(".//VARIANT-ID")) == 1
