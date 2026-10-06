import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ApplicationSwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import SwcInternalBehavior
from armodel.parser.arxml_parser import ARXMLParser


class TestRteEVent:

    def test_swc_mode_switch_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <SWC-MODE-SWITCH-EVENT>
                      <SHORT-NAME>mse_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_mse_1</START-ON-EVENT-REF>
                      <ACTIVATION>ON-ENTRY</ACTIVATION>
                      <MODE-IREFS>
                        <MODE-IREF>
                          <CONTEXT-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_mode</CONTEXT-PORT-REF>
                          <TARGET-MODE-DECLARATION-REF DEST="MODE-DECLARATION">/MyComponents/ModeDclGroup/On</TARGET-MODE-DECLARATION-REF>
                        </MODE-IREF>
                        <MODE-IREF>
                          <CONTEXT-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_mode</CONTEXT-PORT-REF>
                          <TARGET-MODE-DECLARATION-REF DEST="MODE-DECLARATION">/MyComponents/ModeDclGroup/Off</TARGET-MODE-DECLARATION-REF>
                        </MODE-IREF>
                      </MODE-IREFS>
                    </SWC-MODE-SWITCH-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        events = internal_behavior.getSwcModeSwitchEvents()
        assert len(events) == 1

        event = events[0]
        assert event.getShortName() == "mse_event1"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_mse_1"
        assert event.getActivation() is not None
        assert event.getActivation().getValue() == "onEntry"
        irefs = event.getModeIRefs()
        assert len(irefs) == 2
        assert irefs[0].getContextPortRef().getDest() == "R-PORT-PROTOTYPE"
        assert irefs[0].getContextPortRef().getValue() == "/MyComponents/rp_mode"
        assert irefs[0].getTargetModeDeclarationRef().getValue() == "/MyComponents/ModeDclGroup/On"
        assert irefs[1].getTargetModeDeclarationRef().getValue() == "/MyComponents/ModeDclGroup/Off"

    def test_mode_switched_ack_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <MODE-SWITCHED-ACK-EVENT>
                      <SHORT-NAME>msa_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_msa_1</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="MODE-SWITCH-POINT">/MyComponents/MySwc_IB/msp_1</EVENT-SOURCE-REF>
                    </MODE-SWITCHED-ACK-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        events = internal_behavior.getModeSwitchedAckEvents()
        assert len(events) == 1

        event = events[0]
        assert event.getShortName() == "msa_event1"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_msa_1"
        assert event.getEventSourceRef() is not None
        assert event.getEventSourceRef().getDest() == "MODE-SWITCH-POINT"
        assert event.getEventSourceRef().getValue() == "/MyComponents/MySwc_IB/msp_1"

    def test_external_trigger_occurred_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <EXTERNAL-TRIGGER-OCCURRED-EVENT>
                      <SHORT-NAME>eto_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_eto_1</START-ON-EVENT-REF>
                      <TRIGGER-IREF>
                        <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_trigger</CONTEXT-R-PORT-REF>
                        <TARGET-TRIGGER-REF DEST="TRIGGER">/MyComponents/trigger_1</TARGET-TRIGGER-REF>
                      </TRIGGER-IREF>
                    </EXTERNAL-TRIGGER-OCCURRED-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        events = internal_behavior.getExternalTriggerOccurredEvents()
        assert len(events) == 1

        event = events[0]
        assert event.getShortName() == "eto_event1"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_eto_1"
        iref = event.getTriggerIRef()
        assert iref is not None
        assert iref.getContextRPortRef().getDest() == "R-PORT-PROTOTYPE"
        assert iref.getContextRPortRef().getValue() == "/MyComponents/rp_trigger"
        assert iref.getTargetTriggerRef().getDest() == "TRIGGER"
        assert iref.getTargetTriggerRef().getValue() == "/MyComponents/trigger_1"

    def test_transformer_hard_error_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <TRANSFORMER-HARD-ERROR-EVENT>
                      <SHORT-NAME>the_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_the_1</START-ON-EVENT-REF>
                      <OPERATION-IREF>
                        <CONTEXT-P-PORT-REF DEST="P-PORT-PROTOTYPE">/MyComponents/pp_cs</CONTEXT-P-PORT-REF>
                        <TARGET-PROVIDED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/MyComponents/If/op1</TARGET-PROVIDED-OPERATION-REF>
                      </OPERATION-IREF>
                      <REQUIRED-TRIGGER-IREF>
                        <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_trig</CONTEXT-R-PORT-REF>
                        <TARGET-TRIGGER-REF DEST="TRIGGER">/MyComponents/trigger_1</TARGET-TRIGGER-REF>
                      </REQUIRED-TRIGGER-IREF>
                    </TRANSFORMER-HARD-ERROR-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        events = internal_behavior.getTransformerHardErrorEvents()
        assert len(events) == 1

        event = events[0]
        assert event.getShortName() == "the_event1"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_the_1"
        op_iref = event.getOperationIRef()
        assert op_iref is not None
        assert op_iref.getContextPPortRef().getDest() == "P-PORT-PROTOTYPE"
        assert op_iref.getContextPPortRef().getValue() == "/MyComponents/pp_cs"
        assert op_iref.getTargetProvidedOperationRef().getValue() == "/MyComponents/If/op1"
        trig_iref = event.getRequiredTriggerIRef()
        assert trig_iref is not None
        assert trig_iref.getContextRPortRef().getValue() == "/MyComponents/rp_trig"
        assert trig_iref.getTargetTriggerRef().getValue() == "/MyComponents/trigger_1"

    def test_os_task_execution_events(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <OS-TASK-EXECUTION-EVENT>
                      <SHORT-NAME>ote_event1</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_ote_1</START-ON-EVENT-REF>
                    </OS-TASK-EXECUTION-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None
        events = internal_behavior.getOsTaskExecutionEvents()
        assert len(events) == 1

        event = events[0]
        assert event.getShortName() == "ote_event1"
        assert event.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_ote_1"

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
        """  # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
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
        """  # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
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

    def test_disabled_mode_irefs(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <DATA-SEND-COMPLETED-EVENT>
                      <SHORT-NAME>dse_disabled</SHORT-NAME>
                      <DISABLED-MODE-IREFS>
                        <DISABLED-MODE-IREF>
                          <CONTEXT-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_mode_port</CONTEXT-PORT-REF>
                          <CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF DEST="MODE-DECLARATION-GROUP-PROTOTYPE">/MyComponents/mdg_prototype</CONTEXT-MODE-DECLARATION-GROUP-PROTOTYPE-REF>
                          <TARGET-MODE-DECLARATION-REF DEST="MODE-DECLARATION">/Mdgs/MyModeGroup/MyMode</TARGET-MODE-DECLARATION-REF>
                        </DISABLED-MODE-IREF>
                        <DISABLED-MODE-IREF>
                          <TARGET-MODE-DECLARATION-REF DEST="MODE-DECLARATION">/Mdgs/MyModeGroup/MyOtherMode</TARGET-MODE-DECLARATION-REF>
                        </DISABLED-MODE-IREF>
                      </DISABLED-MODE-IREFS>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_disabled</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="VARIABLE-ACCESS">/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_disabled</EVENT-SOURCE-REF>
                    </DATA-SEND-COMPLETED-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None

        events = internal_behavior.getDataSendCompletedEvents()
        assert len(events) == 1
        event = events[0]

        irefs = event.getDisabledModeIRefs()
        assert len(irefs) == 2

        iref1 = irefs[0]
        assert iref1.getContextPortRef().getDest() == "R-PORT-PROTOTYPE"
        assert iref1.getContextPortRef().getValue() == "/MyComponents/rp_mode_port"
        assert iref1.getContextModeDeclarationGroupPrototypeRef().getDest() == "MODE-DECLARATION-GROUP-PROTOTYPE"
        assert iref1.getContextModeDeclarationGroupPrototypeRef().getValue() == "/MyComponents/mdg_prototype"
        assert iref1.getTargetModeDeclarationRef().getDest() == "MODE-DECLARATION"
        assert iref1.getTargetModeDeclarationRef().getValue() == "/Mdgs/MyModeGroup/MyMode"

        iref2 = irefs[1]
        assert iref2.getContextPortRef() is None
        assert iref2.getTargetModeDeclarationRef().getValue() == "/Mdgs/MyModeGroup/MyOtherMode"

        assert event.getStartOnEventRef().getDest() == "RUNNABLE-ENTITY"
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_disabled"

    def test_no_disabled_mode_irefs(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <EVENTS>
                    <DATA-SEND-COMPLETED-EVENT>
                      <SHORT-NAME>dse_plain</SHORT-NAME>
                      <START-ON-EVENT-REF DEST="RUNNABLE-ENTITY">/MyComponents/MySwc_IB/re_plain</START-ON-EVENT-REF>
                      <EVENT-SOURCE-REF DEST="VARIABLE-ACCESS">/MyComponents/MySwc_IB/re_CyclicJob_20ms/dsp_plain</EVENT-SOURCE-REF>
                    </DATA-SEND-COMPLETED-EVENT>
                  </EVENTS>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        # prepare the XML content
        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = ApplicationSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None

        events = internal_behavior.getDataSendCompletedEvents()
        assert len(events) == 1
        event = events[0]
        assert event.getDisabledModeIRefs() == []
        assert event.getStartOnEventRef().getValue() == "/MyComponents/MySwc_IB/re_plain"
