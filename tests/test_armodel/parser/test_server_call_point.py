import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import TimeValue
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import AtomicSwComponentType
from armodel.parser.arxml_parser import ARXMLParser


class TestServerCallPoint:

    def test_server_call_points_field_values(self):
        xml_content = """
            <APPLICATION-SW-COMPONENT-TYPE>
              <SHORT-NAME>MyComponents</SHORT-NAME>
              <INTERNAL-BEHAVIORS>
                <SWC-INTERNAL-BEHAVIOR T="2024-11-01T09:39:52+02:00" UUID="0c573b8e-57a1-4bc5-b815-07b6e0094060">
                  <SHORT-NAME>MyInternalBehavior</SHORT-NAME>
                  <RUNNABLES>
                    <RUNNABLE-ENTITY>
                      <SHORT-NAME>re_main</SHORT-NAME>
                      <SERVER-CALL-POINTS>
                        <SYNCHRONOUS-SERVER-CALL-POINT>
                          <SHORT-NAME>scp_sync</SHORT-NAME>
                          <OPERATION-IREF>
                            <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_cs</CONTEXT-R-PORT-REF>
                            <TARGET-REQUIRED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/MyComponents/IfCs/op1</TARGET-REQUIRED-OPERATION-REF>
                          </OPERATION-IREF>
                          <TIMEOUT>0.005</TIMEOUT>
                        </SYNCHRONOUS-SERVER-CALL-POINT>
                        <ASYNCHRONOUS-SERVER-CALL-POINT>
                          <SHORT-NAME>scp_async</SHORT-NAME>
                          <OPERATION-IREF>
                            <CONTEXT-R-PORT-REF DEST="R-PORT-PROTOTYPE">/MyComponents/rp_cs</CONTEXT-R-PORT-REF>
                            <TARGET-REQUIRED-OPERATION-REF DEST="CLIENT-SERVER-OPERATION">/MyComponents/IfCs/op2</TARGET-REQUIRED-OPERATION-REF>
                          </OPERATION-IREF>
                        </ASYNCHRONOUS-SERVER-CALL-POINT>
                      </SERVER-CALL-POINTS>
                    </RUNNABLE-ENTITY>
                  </RUNNABLES>
                </SWC-INTERNAL-BEHAVIOR>
              </INTERNAL-BEHAVIORS>
            </APPLICATION-SW-COMPONENT-TYPE>
        """  # noqa E501

        element = ET.fromstring(xml_content)
        document = AUTOSARDoc()

        parser = ARXMLParser()
        parser.nsmap = {"xmlns": ""}

        sw_component = AtomicSwComponentType(document, "MyComponents")
        parser.readAtomicSwComponentType(element, sw_component)

        internal_behavior = sw_component.getInternalBehavior()
        assert internal_behavior is not None

        runnables = internal_behavior.getRunnableEntities()
        assert len(runnables) == 1
        runnable = runnables[0]

        sync_points = runnable.getSynchronousServerCallPoint()
        assert len(sync_points) == 1
        sync_point = sync_points[0]
        assert sync_point.getShortName() == "scp_sync"

        operation_iref = sync_point.getOperationIRef()
        assert operation_iref is not None
        assert operation_iref.getContextRPortRef().getDest() == "R-PORT-PROTOTYPE"
        assert operation_iref.getContextRPortRef().getValue() == "/MyComponents/rp_cs"
        assert operation_iref.getTargetRequiredOperationRef().getDest() == "CLIENT-SERVER-OPERATION"
        assert operation_iref.getTargetRequiredOperationRef().getValue() == "/MyComponents/IfCs/op1"

        timeout = sync_point.getTimeout()
        assert timeout is not None
        assert isinstance(timeout, TimeValue)
        assert timeout.getValue() == 0.005

        async_points = runnable.getAsynchronousServerCallPoint()
        assert len(async_points) == 1
        async_point = async_points[0]
        assert async_point.getShortName() == "scp_async"
        assert async_point.getOperationIRef().getTargetRequiredOperationRef().getValue() == "/MyComponents/IfCs/op2"
        assert async_point.getTimeout() is None
