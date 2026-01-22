import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior


from armodel.parser.arxml_parser import ARXMLParser


class TestRteEVent:

    def test_data_send_completed_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <DATA-TYPE-MAPPING-REFS>
                    <DATA-TYPE-MAPPING-REF DEST="DATA-TYPE-MAPPING-SET">/DataType/MappingSet/Array_mapping_set</DATA-TYPE-MAPPING-REF>
                    <DATA-TYPE-MAPPING-REF DEST="DATA-TYPE-MAPPING-SET">/DataType/MappingSet/uint8_mapping_set</DATA-TYPE-MAPPING-REF>
                  </DATA-TYPE-MAPPING-REFS>
                  <EVENTS>
                    <DATA-SEND-COMPLETED-EVENT >
                      <SHORT-NAME>data_send_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_data_send_completed_1</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="VARIABLE-ACCESS">/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_data_send_completed_1</EVENT-SOURCE-REF>
                    </DATA-SEND-COMPLETED-EVENT>
                    <DATA-SEND-COMPLETED-EVENT>
                      <SHORT-NAME>data_send_event2</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_data_send_completed_2</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="VARIABLE-ACCESS">/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_data_send_completed_2</EVENT-SOURCE-REF>
                    </DATA-SEND-COMPLETED-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """ # noqa E501
        
        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = AtomicSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        assert isinstance(internal_behavior, SwcInternalBehavior) is True
        assert internal_behavior.getShortName() == "MyInternalBehavior"
        assert len(internal_behavior.getDataSendCompletedEvents()) == 2

        event1 = internal_behavior.getDataSendCompletedEvents()[0]
        assert event1.getShortName() == "data_send_event1"
        assert event1.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event1.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_data_send_completed_1"
        assert event1.getEventSourceRef().getDest() == "VARIABLE-ACCESS"
        assert event1.getEventSourceRef().getValue() == "/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_data_send_completed_1"

        event2 = internal_behavior.getDataSendCompletedEvents()[1]
        assert event2.getShortName() == "data_send_event2"
        assert event2.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event2.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_data_send_completed_2"
        assert event2.getEventSourceRef().getDest() == "VARIABLE-ACCESS"
        assert event2.getEventSourceRef().getValue() == "/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_data_send_completed_2"

    def test_operation_invoked_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <DATA-TYPE-MAPPING-REFS>
                    <DATA-TYPE-MAPPING-REF DEST="DATA-TYPE-MAPPING-SET">/DataType/MappingSet/Array_mapping_set</DATA-TYPE-MAPPING-REF>
                    <DATA-TYPE-MAPPING-REF DEST="DATA-TYPE-MAPPING-SET">/DataType/MappingSet/uint8_mapping_set</DATA-TYPE-MAPPING-REF>
                  </DATA-TYPE-MAPPING-REFS>
                  <EVENTS>
                    <DATA-SEND-COMPLETED-EVENT >
                      <SHORT-NAME>data_send_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_data_send_completed_1</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="VARIABLE-ACCESS">/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_data_send_completed_1</EVENT-SOURCE-REF>
                    </DATA-SEND-COMPLETED-EVENT>
                    <OPERATION-INVOKED-EVENT>
                      <SHORT-NAME>oie_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_event1</START-ON-EVENT-REF>
                      <OPERATION-IREF>
                        <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/MyComponents/pp_oie_port</CONTEXT-P-PORT-REF>
                        <TARGET-PROVIDED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/MyComponents/Interfaces/ClientServerInterfaces/IfCs_event/operation1</TARGET-PROVIDED-OPERATION-REF>
                      </OPERATION-IREF>
                    </OPERATION-INVOKED-EVENT>
                    <OPERATION-INVOKED-EVENT >
                      <SHORT-NAME>oie_event2</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_event2</START-ON-EVENT-REF>
                      <OPERATION-IREF T="2021-07-21T17:39:44+03:00">
                        <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/MyComponents//pp_oie_port</CONTEXT-P-PORT-REF>
                        <TARGET-PROVIDED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/MyComponents/Interfaces/ClientServerInterfaces/IfCs_event/operation2</TARGET-PROVIDED-OPERATION-REF>
                      </OPERATION-IREF>
                    </OPERATION-INVOKED-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """ # noqa E501
        
        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = AtomicSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        assert isinstance(internal_behavior, SwcInternalBehavior) is True
        assert internal_behavior.getShortName() == "MyInternalBehavior"
        assert len(internal_behavior.getOperationInvokedEvents()) == 2

        event1 = internal_behavior.getOperationInvokedEvents()[0]
        assert event1.getShortName() == "oie_event1"
        assert event1.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event1.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_event1"
        assert event1.getOperationIRef().getContextPPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert event1.getOperationIRef().getContextPPortRef().getValue() == "/MyComponents/pp_oie_port"
        assert event1.getOperationIRef().getTargetProvidedOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert event1.getOperationIRef().getTargetProvidedOperationRef().getValue() == "/MyComponents/Interfaces/ClientServerInterfaces/IfCs_event/operation1"

        event2 = internal_behavior.getOperationInvokedEvents()[1]
        assert event2.getShortName() == "oie_event2"
        assert event2.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event2.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_event2"
        assert event2.getOperationIRef().getContextPPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert event2.getOperationIRef().getContextPPortRef().getValue() == "/MyComponents//pp_oie_port"
        assert event2.getOperationIRef().getTargetProvidedOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert event2.getOperationIRef().getTargetProvidedOperationRef().getValue() == "/MyComponents/Interfaces/ClientServerInterfaces/IfCs_event/operation2"
