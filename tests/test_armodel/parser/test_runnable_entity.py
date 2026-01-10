import xml.etree.ElementTree as ET

from src.armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior import RunnableEntity, SwcInternalBehavior
from src.armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from src.armodel.parser.arxml_parser import ARXMLParser


class TestRunnableEntity:
    def setup_method(self):
        self.xml_content = """
            <SWC-INTERNAL-BEHAVIOR>
                <RUNNABLES>
                    <RUNNABLE-ENTITY>
                      <SHORT-NAME>Cyclic</SHORT-NAME>
                      <MINIMUM-START-INTERVAL>0.0</MINIMUM-START-INTERVAL>
                      <CAN-BE-INVOKED-CONCURRENTLY>false</CAN-BE-INVOKED-CONCURRENTLY>
                      <DATA-RECEIVE-POINT-BY-ARGUMENTS>
                        <VARIABLE-ACCESS>
                          <SHORT-NAME>DRP_P_Special_EventMessage</SHORT-NAME>
                          <ACCESSED-VARIABLE>
                            <AUTOSAR-VARIABLE-IREF>
                              <PORT-PROTOTYPE-REF DEST="R-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/R_SpecialHandling</PORT-PROTOTYPE-REF>
                              <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/PortInterfaces/If_Internal/EventMessage</TARGET-DATA-PROTOTYPE-REF>
                            </AUTOSAR-VARIABLE-IREF>
                          </ACCESSED-VARIABLE>
                        </VARIABLE-ACCESS>
                      </DATA-RECEIVE-POINT-BY-ARGUMENTS>
                      <DATA-SEND-POINTS>
                        <VARIABLE-ACCESS>
                          <SHORT-NAME>DWA_P_CounterOut_CounterValue</SHORT-NAME>
                          <ACCESSED-VARIABLE>
                            <AUTOSAR-VARIABLE-IREF>
                              <PORT-PROTOTYPE-REF DEST="P-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/P_CounterOut</PORT-PROTOTYPE-REF>
                              <TARGET-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/PortInterfaces/If_Counter/CounterValue</TARGET-DATA-PROTOTYPE-REF>
                            </AUTOSAR-VARIABLE-IREF>
                          </ACCESSED-VARIABLE>
                        </VARIABLE-ACCESS>
                      </DATA-SEND-POINTS>
                      <READ-LOCAL-VARIABLES>
                        <VARIABLE-ACCESS>
                          <SHORT-NAME>CurrentCounterValue3</SHORT-NAME>
                          <ACCESSED-VARIABLE>
                            <LOCAL-VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter/CurrentCounterValue</LOCAL-VARIABLE-REF>
                          </ACCESSED-VARIABLE>
                        </VARIABLE-ACCESS>
                      </READ-LOCAL-VARIABLES>
                      <SERVER-CALL-POINTS>
                        <SYNCHRONOUS-SERVER-CALL-POINT>
                          <SHORT-NAME>CS_DETService_ReportError</SHORT-NAME>
                          <OPERATION-IREF>
                            <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/R_CyclicCounterDet</CONTEXT-R-PORT-REF>
                            <TARGET-REQUIRED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/DemoApplication/PortInterfaces/DETService/ReportError</TARGET-REQUIRED-OPERATION-REF>
                          </OPERATION-IREF>
                          <TIMEOUT>0.0</TIMEOUT>
                        </SYNCHRONOUS-SERVER-CALL-POINT>
                        <SYNCHRONOUS-SERVER-CALL-POINT>
                          <SHORT-NAME>CS_EchoResult_SetCounterAndAdd</SHORT-NAME>
                          <OPERATION-IREF>
                            <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/R_MyLED</CONTEXT-R-PORT-REF>
                            <TARGET-REQUIRED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/DemoApplication/PortInterfaces/If_DiscreteValueOutput/SetDiscreteValue</TARGET-REQUIRED-OPERATION-REF>
                          </OPERATION-IREF>
                          <TIMEOUT>0.0</TIMEOUT>
                        </SYNCHRONOUS-SERVER-CALL-POINT>
                        <SYNCHRONOUS-SERVER-CALL-POINT>
                          <SHORT-NAME>CS_UR_ComMUser_0_ComM_UserRequest</SHORT-NAME>
                          <OPERATION-IREF>
                            <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/UR_ComMUser_0</CONTEXT-R-PORT-REF>
                            <TARGET-REQUIRED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/DemoApplication/PortInterfaces/ComM_UserRequest/RequestComMode</TARGET-REQUIRED-OPERATION-REF>
                          </OPERATION-IREF>
                          <TIMEOUT>0.0</TIMEOUT>
                        </SYNCHRONOUS-SERVER-CALL-POINT>
                      </SERVER-CALL-POINTS>
                      <SYMBOL>SWC_CyclicCounter_Cyclic</SYMBOL>
                      <WRITTEN-LOCAL-VARIABLES>
                        <VARIABLE-ACCESS>
                          <SHORT-NAME>CurrentCounterValue4</SHORT-NAME>
                          <ACCESSED-VARIABLE T="2020-08-03T07:59:25+02:00">
                            <LOCAL-VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter/CurrentCounterValue</LOCAL-VARIABLE-REF>
                          </ACCESSED-VARIABLE>
                        </VARIABLE-ACCESS>
                      </WRITTEN-LOCAL-VARIABLES>
                    </RUNNABLE-ENTITY>
                </RUNNABLES>
            </SWC-INTERNAL-BEHAVIOR>
        """

    def test_data_receive_point_by_argument(self):
        # prepare the XML content
        element = ET.fromstring(self.xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        behavior = SwcInternalBehavior(document, "Behavior")
        parser.readSwcInternalBehaviorRunnables(element, behavior)

        assert len(behavior.getRunnableEntities()) == 1
        assert isinstance(behavior.getRunnableEntities()[0], RunnableEntity) is True

        runnable_entity = behavior.getRunnableEntities()[0]
        assert runnable_entity.getShortName() == "Cyclic"
        assert runnable_entity.getMinimumStartInterval().getValue() == 0.0
        assert runnable_entity.getCanBeInvokedConcurrently().getValue() is False
        assert len(runnable_entity.getDataReceivePointByArguments()) == 1

        drp_arg = runnable_entity.getDataReceivePointByArguments()[0]
        assert drp_arg.getShortName() == "DRP_P_Special_EventMessage"
        assert drp_arg.getAccessedVariableRef().getAutosarVariableIRef().getPortPrototypeRef().getDest() == "R-PORT-PROTOTYPE"
        assert drp_arg.getAccessedVariableRef().getAutosarVariableIRef().getPortPrototypeRef().getValue() == "/DemoApplication/SwComponentTypes/SWC_CyclicCounter/R_SpecialHandling"
        assert drp_arg.getAccessedVariableRef().getAutosarVariableIRef().getTargetDataPrototypeRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert drp_arg.getAccessedVariableRef().getAutosarVariableIRef().getTargetDataPrototypeRef().getValue() == "/DemoApplication/PortInterfaces/If_Internal/EventMessage"

    def test_written_local_variables(self):
        # prepare the XML content
        element = ET.fromstring(self.xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        behavior = SwcInternalBehavior(document, "Behavior")
        parser.readSwcInternalBehaviorRunnables(element, behavior)

        assert len(behavior.getRunnableEntities()) == 1
        assert isinstance(behavior.getRunnableEntities()[0], RunnableEntity) is True

        runnable_entity = behavior.getRunnableEntities()[0]
        assert len(runnable_entity.getWrittenLocalVariables()) == 1

        written_var = runnable_entity.getWrittenLocalVariables()[0]
        assert written_var.getShortName() == "CurrentCounterValue4"
        assert written_var.getAccessedVariableRef().timestamp == "2020-08-03T07:59:25+02:00"
        assert written_var.getAccessedVariableRef().getLocalVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        assert written_var.getAccessedVariableRef().getLocalVariableRef().getValue() == "/DemoApplication/SwComponentTypes/SWC_CyclicCounter/IB_SWC_CyclicCounter/CurrentCounterValue"