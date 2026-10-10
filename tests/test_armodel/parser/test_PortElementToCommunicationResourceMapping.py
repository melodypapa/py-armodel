"""Reader tests for the PortElementToCommunicationResourceMapping class (Table 11.15, p.905)."""

import xml.etree.ElementTree as ET

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PortElementToCommunicationResourceMapping
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    return ARXMLParser()


class TestReadPortElementToCommunicationResourceMapping:
    def test_read_all_elements(self, parser):
        """
        The six Table 11.15 rows are read; the base Identifiable level (SHORT-NAME,
        UUID) is populated by the base helper. Each iref row is read into its
        InstanceRef implementation named by the spec row.
        """
        element = ET.fromstring(
            "<PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING xmlns='%(ns)s' UUID='1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d'>"
            "<SHORT-NAME>mapping1</SHORT-NAME>"
            "<CLIENT-SERVER-OPERATION-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/SwcA</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-PORT-REF DEST='R-PORT-PROTOTYPE'>/Root/SwcA/rp1</CONTEXT-PORT-REF>"
            "<TARGET-OPERATION-REF DEST='CLIENT-SERVER-OPERATION'>/Root/SwcA/rp1/op1</TARGET-OPERATION-REF>"
            "</CLIENT-SERVER-OPERATION-IREF>"
            "<COMMUNICATION-RESOURCE-REF DEST='CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE'>/Resources/MyResource</COMMUNICATION-RESOURCE-REF>"
            "<MODE-DECLARATION-GROUP-PROTOTYPE-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/SwcB</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-PORT-REF DEST='P-PORT-PROTOTYPE'>/Root/SwcB/pp1</CONTEXT-PORT-REF>"
            "<TARGET-MODE-DECLARATION-GROUP-PROTOTYPE-REF DEST='MODE-DECLARATION-GROUP-PROTOTYPE'>/Root/SwcB/pp1/mg1</TARGET-MODE-DECLARATION-GROUP-PROTOTYPE-REF>"
            "</MODE-DECLARATION-GROUP-PROTOTYPE-IREF>"
            "<PARAMETER-DATA-PROTOTYPE-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/SwcC</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-PORT-REF DEST='R-PORT-PROTOTYPE'>/Root/SwcC/rp2</CONTEXT-PORT-REF>"
            "<TARGET-PARAMETER-DATA-PROTOTYPE-REF DEST='PARAMETER-DATA-PROTOTYPE'>/Root/SwcC/rp2/prm1</TARGET-PARAMETER-DATA-PROTOTYPE-REF>"
            "</PARAMETER-DATA-PROTOTYPE-IREF>"
            "<TRIGGER-IREF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/SwcD</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-PORT-REF DEST='P-PORT-PROTOTYPE'>/Root/SwcD/pp2</CONTEXT-PORT-REF>"
            "<TARGET-TRIGGER-REF DEST='TRIGGER'>/Root/SwcD/pp2/trg1</TARGET-TRIGGER-REF>"
            "</TRIGGER-IREF>"
            "<VARIABLE-DATA-PROTOTYPE-IREF>"
            "<CONTEXT-COMPONENT-REF DEST='SW-COMPONENT-PROTOTYPE'>/Root/SwcE</CONTEXT-COMPONENT-REF>"
            "<CONTEXT-COMPOSITION-REF DEST='ROOT-SW-COMPOSITION-PROTOTYPE'>/Root</CONTEXT-COMPOSITION-REF>"
            "<CONTEXT-PORT-REF DEST='P-PORT-PROTOTYPE'>/Root/SwcE/pp3</CONTEXT-PORT-REF>"
            "<TARGET-DATA-PROTOTYPE-REF DEST='VARIABLE-DATA-PROTOTYPE'>/Root/SwcE/pp3/var1</TARGET-DATA-PROTOTYPE-REF>"
            "</VARIABLE-DATA-PROTOTYPE-IREF>"
            "</PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING>" % {"ns": NS}
        )

        mapping = parser.readPortElementToCommunicationResourceMapping(element, PortElementToCommunicationResourceMapping(None, "mapping1"))

        assert mapping.getShortName() == "mapping1"
        assert mapping.getUuid().getValue() == "1a2b3c4d-5e6f-4aaa-bbbc-2e3f4a5b6c7d"

        op_iref = mapping.getClientServerOperationIRef()
        assert op_iref is not None
        assert op_iref.getContextCompositionRef().getValue() == "/Root"
        assert [ref.getValue() for ref in op_iref.getContextComponentRefs()] == ["/Root/SwcA"]
        assert op_iref.getContextPortRef().getValue() == "/Root/SwcA/rp1"
        assert op_iref.getTargetOperationRef().getValue() == "/Root/SwcA/rp1/op1"

        assert mapping.getCommunicationResourceRef().getValue() == "/Resources/MyResource"
        assert mapping.getCommunicationResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"

        mode_iref = mapping.getModeDeclarationGroupPrototypeIRef()
        assert mode_iref is not None
        assert mode_iref.getContextCompositionRef().getValue() == "/Root"
        assert [ref.getValue() for ref in mode_iref.getContextComponentRefs()] == ["/Root/SwcB"]
        assert mode_iref.getContextPortRef().getValue() == "/Root/SwcB/pp1"
        assert mode_iref.getTargetModeDeclarationGroupPrototypeRef().getValue() == "/Root/SwcB/pp1/mg1"

        prm_iref = mapping.getParameterDataPrototypeIRef()
        assert prm_iref is not None
        assert [ref.getValue() for ref in prm_iref.getContextComponentRefs()] == ["/Root/SwcC"]
        assert prm_iref.getContextCompositionRef().getValue() == "/Root"
        assert prm_iref.getContextPortRef().getValue() == "/Root/SwcC/rp2"
        assert prm_iref.getTargetParameterDataPrototypeRef().getValue() == "/Root/SwcC/rp2/prm1"

        trg_iref = mapping.getTriggerIRef()
        assert trg_iref is not None
        assert trg_iref.getContextCompositionRef().getValue() == "/Root"
        assert [ref.getValue() for ref in trg_iref.getContextComponentRefs()] == ["/Root/SwcD"]
        assert trg_iref.getContextPortRef().getValue() == "/Root/SwcD/pp2"
        assert trg_iref.getTargetTriggerRef().getValue() == "/Root/SwcD/pp2/trg1"

        var_iref = mapping.getVariableDataPrototypeIRef()
        assert var_iref is not None
        assert [ref.getValue() for ref in var_iref.getContextComponentRefs()] == ["/Root/SwcE"]
        assert var_iref.getContextCompositionRef().getValue() == "/Root"
        assert var_iref.getContextPortRef().getValue() == "/Root/SwcE/pp3"
        assert var_iref.getTargetDataPrototypeRef().getValue() == "/Root/SwcE/pp3/var1"

    def test_read_empty_element(self, parser):
        """
        A mapping without group content leaves all fields unset.
        """
        element = ET.fromstring("<PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING xmlns='%s'><SHORT-NAME>mapping2</SHORT-NAME></PORT-ELEMENT-TO-COMMUNICATION-RESOURCE-MAPPING>" % NS)

        mapping = parser.readPortElementToCommunicationResourceMapping(element, PortElementToCommunicationResourceMapping(None, "mapping2"))

        assert mapping.getClientServerOperationIRef() is None
        assert mapping.getCommunicationResourceRef() is None
        assert mapping.getModeDeclarationGroupPrototypeIRef() is None
        assert mapping.getParameterDataPrototypeIRef() is None
        assert mapping.getTriggerIRef() is None
        assert mapping.getVariableDataPrototypeIRef() is None
