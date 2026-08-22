"""Writer round-trip tests for DataPrototypeTransformationProps (Table 7.17)
and its DataPrototypeReference closure (Tables 7.18-7.22).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeTransformationProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
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


def _ref(value: str):
    r = RefType()
    r.setValue(value)
    return r


def _build_props():
    props = DataPrototypeTransformationProps()

    ref = DataPrototypeInPortInterfaceRef()
    ref.setTagId(PositiveInteger().setValue("5"))
    cs = DataPrototypeInClientServerInterfaceInstanceRef()
    cs.setBase(RefType().setValue("/Cs").setDest("CLIENT-SERVER-INTERFACE"))
    cs.setRootDataPrototypeInCs(RefType().setValue("/Cs/Root").setDest("DATA-PROTOTYPE"))
    cs.setTargetDataPrototypeInCs(RefType().setValue("/Cs/MyArg").setDest("DATA-PROTOTYPE"))
    ref.setDataPrototypeInClientServerInterface(cs)
    props.setDataPrototypeInPortInterfaceRef(ref)

    net = SwDataDefProps()
    from armodel.models.M2.MSR.DataDictionary.DataDefProperties import AlignmentType

    net.setSwAlignment(AlignmentType().setValue("4"))
    props.setNetworkRepresentationProps(net)

    tp = RefType()
    tp.setValue("/Tp/MyProps")
    tp.setDest("TRANSFORMATION-PROPS")
    props.setTransformationProps(tp)
    return props


def test_write_data_prototype_transformation_props_all_fields(writer):
    parent = _parent()
    props = _build_props()

    writer.writeDataPrototypeTransformationProps(parent, props)

    dp_tp = parent.find("DATA-PROTOTYPE-TRANSFORMATION-PROPS")
    assert dp_tp is not None

    # dataPrototypeInPortInterfaceRef aggregation
    dp_ref = dp_tp.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
    assert dp_ref is not None
    assert dp_ref.find("TAG-ID").text == "5"
    cs_ref = dp_ref.find("DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-REF")
    assert cs_ref is not None
    assert cs_ref.find("BASE").text == "/Cs"
    assert cs_ref.find("ROOT-DATA-PROTOTYPE-IN-CS").text == "/Cs/Root"
    assert cs_ref.find("TARGET-DATA-PROTOTYPE-IN-CS").text == "/Cs/MyArg"

    # networkRepresentationProps aggregation
    net = dp_tp.find("NETWORK-REPRESENTATION-PROPS/SW-DATA-DEF-PROPS-VARIANTS/SW-DATA-DEF-PROPS-CONDITIONAL")
    assert net is not None
    assert net.find("SW-ALIGNMENT").text == "4"

    # transformationProps ref
    tp = dp_tp.find("TRANSFORMATION-PROPS")
    assert tp is not None
    assert tp.text == "/Tp/MyProps"


def test_write_data_prototype_transformation_props_empty(writer):
    parent = _parent()
    props = DataPrototypeTransformationProps()

    writer.writeDataPrototypeTransformationProps(parent, props)

    # Element is written but has no meaningful child elements
    dp_tp = parent.find("DATA-PROTOTYPE-TRANSFORMATION-PROPS")
    assert dp_tp is not None
    assert dp_tp.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF") is None
    assert dp_tp.find("NETWORK-REPRESENTATION-PROPS") is None
    assert dp_tp.find("TRANSFORMATION-PROPS") is None


def test_write_data_prototype_in_port_interface_ref_tag_id(writer):
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInPortInterfaceRef

    parent = _parent()
    ref = DataPrototypeInPortInterfaceRef()
    ref.setTagId(PositiveInteger().setValue("7"))

    writer.writeDataPrototypeInPortInterfaceRef(parent, ref)

    el = parent.find("DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
    assert el is not None
    assert el.find("TAG-ID").text == "7"
