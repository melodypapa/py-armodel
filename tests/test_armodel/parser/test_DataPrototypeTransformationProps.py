"""Parser round-trip tests for DataPrototypeTransformationProps (Table 7.17)
and its DataPrototypeReference closure (Tables 7.18-7.22).
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeTransformationProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _snip(inner: str) -> ET.Element:
    return ET.fromstring(f"<ROOT xmlns='{NS}'>{inner}</ROOT>")


def _ref(value: str):
    from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

    r = RefType()
    r.setValue(value)
    return r


def test_read_data_prototype_transformation_props_all_fields(parser):
    xml = """
      <DATA-PROTOTYPE-TRANSFORMATION-PROPS>
        <DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
          <TAG-ID>5</TAG-ID>
          <DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-REF>
            <BASE DEST="CLIENT-SERVER-INTERFACE">/Cs</BASE>
            <ROOT-DATA-PROTOTYPE-IN-CS DEST="DATA-PROTOTYPE">/Cs/Root</ROOT-DATA-PROTOTYPE-IN-CS>
            <TARGET-DATA-PROTOTYPE-IN-CS DEST="DATA-PROTOTYPE">/Cs/MyArg</TARGET-DATA-PROTOTYPE-IN-CS>
          </DATA-PROTOTYPE-IN-CLIENT-SERVER-INTERFACE-REF>
        </DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>
        <NETWORK-REPRESENTATION-PROPS>
          <SW-DATA-DEF-PROPS-VARIANTS>
            <SW-DATA-DEF-PROPS-CONDITIONAL>
              <SW-ALIGNMENT>4</SW-ALIGNMENT>
            </SW-DATA-DEF-PROPS-CONDITIONAL>
          </SW-DATA-DEF-PROPS-VARIANTS>
        </NETWORK-REPRESENTATION-PROPS>
        <TRANSFORMATION-PROPS DEST="TRANSFORMATION-PROPS">/Tp/MyProps</TRANSFORMATION-PROPS>
      </DATA-PROTOTYPE-TRANSFORMATION-PROPS>
    """
    root = _snip(xml)
    element = parser.find(root, "DATA-PROTOTYPE-TRANSFORMATION-PROPS")
    props = DataPrototypeTransformationProps()
    parser.readDataPrototypeTransformationProps(element, props)

    # dataPrototypeInPortInterfaceRef (aggr -> DataPrototypeInPortInterfaceRef with tagId + iref InstanceRef)
    ref = props.getDataPrototypeInPortInterfaceRef()
    assert isinstance(ref, DataPrototypeInPortInterfaceRef)
    assert ref.getTagId() is not None
    assert ref.getTagId().getValue() == 5
    cs_ref = ref.getDataPrototypeInClientServerInterface()
    assert isinstance(cs_ref, DataPrototypeInClientServerInterfaceInstanceRef)
    assert cs_ref.getBase() is not None
    assert cs_ref.getBase().getValue() == "/Cs"
    assert cs_ref.getRootDataPrototypeInCs() is not None
    assert cs_ref.getRootDataPrototypeInCs().getValue() == "/Cs/Root"
    assert cs_ref.getTargetDataPrototypeInCs() is not None
    assert cs_ref.getTargetDataPrototypeInCs().getValue() == "/Cs/MyArg"

    # networkRepresentationProps (aggr -> SwDataDefProps)
    net = props.getNetworkRepresentationProps()
    assert isinstance(net, SwDataDefProps)
    assert net.getSwAlignment() is not None
    assert net.getSwAlignment().getValue() == "4"

    # transformationProps (ref)
    tp = props.getTransformationProps()
    assert tp is not None
    assert tp.getValue() == "/Tp/MyProps"


def test_read_data_prototype_transformation_props_empty(parser):
    root = _snip("<DATA-PROTOTYPE-TRANSFORMATION-PROPS></DATA-PROTOTYPE-TRANSFORMATION-PROPS>")
    element = parser.find(root, "DATA-PROTOTYPE-TRANSFORMATION-PROPS")
    props = DataPrototypeTransformationProps()
    parser.readDataPrototypeTransformationProps(element, props)

    assert props.getDataPrototypeInPortInterfaceRef() is None
    assert props.getNetworkRepresentationProps() is None
    assert props.getTransformationProps() is None


def test_read_data_prototype_reference_tag_id_only(parser):
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import DataPrototypeInPortInterfaceRef

    root = _snip("<DATA-PROTOTYPE-IN-PORT-INTERFACE-REF><TAG-ID>7</TAG-ID></DATA-PROTOTYPE-IN-PORT-INTERFACE-REF>")
    element = parser.find(root, "DATA-PROTOTYPE-IN-PORT-INTERFACE-REF")
    ref = DataPrototypeInPortInterfaceRef()
    parser.readDataPrototypeInPortInterfaceRef(element, ref)

    assert ref.getTagId() is not None
    assert ref.getTagId().getValue() == 7
    assert ref.getDataPrototypeInClientServerInterface() is None
