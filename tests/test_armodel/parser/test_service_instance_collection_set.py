"""Reader tests for ServiceInstanceCollectionSet (R23-11 CP_TPS_SystemTemplate, Table 6.157, p.476).

XSD group SERVICE-INSTANCE-COLLECTION-SET (AUTOSAR_00052.xsd l.105332): the SERVICE-INSTANCES
wrapper aggregates an unbounded choice of CONSUMED-SERVICE-INSTANCE, DDS-CP-CONSUMED-SERVICE-INSTANCE,
DDS-CP-PROVIDED-SERVICE-INSTANCE and PROVIDED-SERVICE-INSTANCE children. Aggregated by
ARPackage.element - the ARPackage ELEMENTS choice instantiates the FibexElement subclass.
"""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import DdsCpProvidedServiceInstance
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpConsumedServiceInstance
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    ConsumedServiceInstance,
    ProvidedServiceInstance,
    ServiceInstanceCollectionSet,
)
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


def test_read_service_instance_collection_set(parser):
    root = ET.fromstring(
        "<ROOT xmlns='{ns}'>"
        "<ELEMENTS>"
        "<SERVICE-INSTANCE-COLLECTION-SET>"
        "<SHORT-NAME>ServiceInstances</SHORT-NAME>"
        "<SERVICE-INSTANCES>"
        "<CONSUMED-SERVICE-INSTANCE>"
        "<SHORT-NAME>Consumed_1</SHORT-NAME>"
        "<MAJOR-VERSION>2</MAJOR-VERSION>"
        "<MINOR-VERSION>1</MINOR-VERSION>"
        "</CONSUMED-SERVICE-INSTANCE>"
        "<DDS-CP-CONSUMED-SERVICE-INSTANCE>"
        "<SHORT-NAME>DdsConsumed_1</SHORT-NAME>"
        "<MINOR-VERSION>3</MINOR-VERSION>"
        "</DDS-CP-CONSUMED-SERVICE-INSTANCE>"
        "<DDS-CP-PROVIDED-SERVICE-INSTANCE>"
        "<MINOR-VERSION>4</MINOR-VERSION>"
        "</DDS-CP-PROVIDED-SERVICE-INSTANCE>"
        "<PROVIDED-SERVICE-INSTANCE>"
        "<SHORT-NAME>Provided_1</SHORT-NAME>"
        "<MAJOR-VERSION>5</MAJOR-VERSION>"
        "<SERVICE-IDENTIFIER>7</SERVICE-IDENTIFIER>"
        "</PROVIDED-SERVICE-INSTANCE>"
        "</SERVICE-INSTANCES>"
        "</SERVICE-INSTANCE-COLLECTION-SET>"
        "</ELEMENTS>"
        "</ROOT>".format(ns=NS)
    )
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    parser.readARPackageElements(root, package)

    collection_set = package.getReferrableElement("ServiceInstances", ServiceInstanceCollectionSet)
    assert isinstance(collection_set, ServiceInstanceCollectionSet)
    instances = collection_set.getServiceInstances()
    assert len(instances) == 4

    consumed = instances[0]
    assert isinstance(consumed, ConsumedServiceInstance)
    assert consumed.getShortName() == "Consumed_1"
    assert consumed.getMajorVersion().getValue() == 2
    assert consumed.getMinorVersion().getValue() == "1"

    dds_consumed = instances[1]
    assert isinstance(dds_consumed, DdsCpConsumedServiceInstance)
    assert dds_consumed.getShortName() == "DdsConsumed_1"
    assert dds_consumed.getMinorVersion().getValue() == "3"

    dds_provided = instances[2]
    assert isinstance(dds_provided, DdsCpProvidedServiceInstance)
    assert dds_provided.getMinorVersion().getValue() == 4

    provided = instances[3]
    assert isinstance(provided, ProvidedServiceInstance)
    assert provided.getShortName() == "Provided_1"
    assert provided.getMajorVersion().getValue() == 5
    assert provided.getServiceIdentifier().getValue() == 7


def test_read_empty_set(parser):
    root = ET.fromstring(
        "<ROOT xmlns='{ns}'>" "<ELEMENTS>" "<SERVICE-INSTANCE-COLLECTION-SET>" "<SHORT-NAME>EmptySet</SHORT-NAME>" "</SERVICE-INSTANCE-COLLECTION-SET>" "</ELEMENTS>" "</ROOT>".format(ns=NS)
    )
    package = AUTOSAR.getInstance().createARPackage("Pkg")
    parser.readARPackageElements(root, package)

    collection_set = package.getReferrableElement("EmptySet", ServiceInstanceCollectionSet)
    assert isinstance(collection_set, ServiceInstanceCollectionSet)
    assert collection_set.getServiceInstances() == []
