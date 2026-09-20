import filecmp
from pathlib import Path

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SystemTemplate import ComManagementMapping, J1939SharedAddressCluster, RootSwCompositionPrototype, System, SystemMapping
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import PortGroupInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuPartition
from armodel.models.M2.MSR.Documentation.Chapters import Chapter
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

FULL_SYSTEM_ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Systems</SHORT-NAME>
      <ELEMENTS>
        <SYSTEM>
          <SHORT-NAME>FullSystem</SHORT-NAME>
          <SYSTEM-DOCUMENTATIONS>
            <CHAPTER HELP-ENTRY="help-topic-1">
              <SHORT-NAME>Doc1</SHORT-NAME>
            </CHAPTER>
          </SYSTEM-DOCUMENTATIONS>
          <CLIENT-ID-DEFINITION-SET-REFS>
            <CLIENT-ID-DEFINITION-SET-REF DEST="CLIENT-ID-DEFINITION-SET">/Systems/ClientIds</CLIENT-ID-DEFINITION-SET-REF>
          </CLIENT-ID-DEFINITION-SET-REFS>
          <CONTAINER-I-PDU-HEADER-BYTE-ORDER>MOST-SIGNIFICANT-BYTE-FIRST</CONTAINER-I-PDU-HEADER-BYTE-ORDER>
          <ECU-EXTRACT-VERSION>1.0.0</ECU-EXTRACT-VERSION>
          <FIBEX-ELEMENTS>
            <FIBEX-ELEMENT-REF-CONDITIONAL>
              <FIBEX-ELEMENT-REF DEST="CAN-CLUSTER">/CanSystem/CLUSTERS/CanNetwork</FIBEX-ELEMENT-REF>
            </FIBEX-ELEMENT-REF-CONDITIONAL>
          </FIBEX-ELEMENTS>
          <INTERPOLATION-ROUTINE-MAPPING-SET-REFS>
            <INTERPOLATION-ROUTINE-MAPPING-SET-REF DEST="INTERPOLATION-ROUTINE-MAPPING-SET">/Systems/InterpMapping</INTERPOLATION-ROUTINE-MAPPING-SET-REF>
          </INTERPOLATION-ROUTINE-MAPPING-SET-REFS>
          <J-1939-SHARED-ADDRESS-CLUSTERS>
            <J-1939-SHARED-ADDRESS-CLUSTER>
              <SHORT-NAME>Cluster1</SHORT-NAME>
            </J-1939-SHARED-ADDRESS-CLUSTER>
          </J-1939-SHARED-ADDRESS-CLUSTERS>
          <MAPPINGS>
            <SYSTEM-MAPPING>
              <SHORT-NAME>Mapping1</SHORT-NAME>
            </SYSTEM-MAPPING>
          </MAPPINGS>
          <PNC-VECTOR-LENGTH>8</PNC-VECTOR-LENGTH>
          <PNC-VECTOR-OFFSET>4</PNC-VECTOR-OFFSET>
          <ROOT-SOFTWARE-COMPOSITIONS>
            <ROOT-SW-COMPOSITION-PROTOTYPE>
              <SHORT-NAME>RootComp</SHORT-NAME>
            </ROOT-SW-COMPOSITION-PROTOTYPE>
          </ROOT-SOFTWARE-COMPOSITIONS>
          <SW-CLUSTERS>
            <CP-SOFTWARE-CLUSTER-REF-CONDITIONAL>
              <CP-SOFTWARE-CLUSTER-REF DEST="CP-SOFTWARE-CLUSTER">/Systems/Cluster</CP-SOFTWARE-CLUSTER-REF>
            </CP-SOFTWARE-CLUSTER-REF-CONDITIONAL>
          </SW-CLUSTERS>
          <SYSTEM-VERSION>2.0.0</SYSTEM-VERSION>
        </SYSTEM>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""

J1939_SHARED_ADDRESS_CLUSTER_ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Systems</SHORT-NAME>
      <ELEMENTS>
        <SYSTEM>
          <SHORT-NAME>J1939System</SHORT-NAME>
          <J-1939-SHARED-ADDRESS-CLUSTERS>
            <J-1939-SHARED-ADDRESS-CLUSTER>
              <SHORT-NAME>Cluster1</SHORT-NAME>
              <PARTICIPATING-J-1939-CLUSTER-REFS>
                <PARTICIPATING-J-1939-CLUSTER-REF DEST="J-1939-CLUSTER">/Systems/J1939ClusterA</PARTICIPATING-J-1939-CLUSTER-REF>
                <PARTICIPATING-J-1939-CLUSTER-REF DEST="J-1939-CLUSTER">/Systems/J1939ClusterB</PARTICIPATING-J-1939-CLUSTER-REF>
              </PARTICIPATING-J-1939-CLUSTER-REFS>
              <VARIATION-POINT>
                <SHORT-LABEL>VP_CLUSTER</SHORT-LABEL>
              </VARIATION-POINT>
            </J-1939-SHARED-ADDRESS-CLUSTER>
          </J-1939-SHARED-ADDRESS-CLUSTERS>
        </SYSTEM>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""

COM_MANAGEMENT_MAPPING_ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Systems</SHORT-NAME>
      <ELEMENTS>
        <SYSTEM>
          <SHORT-NAME>ComMapSystem</SHORT-NAME>
          <MAPPINGS>
            <SYSTEM-MAPPING>
              <SHORT-NAME>Mapping1</SHORT-NAME>
              <COM-MANAGEMENT-MAPPINGS>
                <COM-MANAGEMENT-MAPPING>
                  <SHORT-NAME>ComMapping1</SHORT-NAME>
                  <COM-MANAGEMENT-GROUP-REFS>
                    <COM-MANAGEMENT-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/Systems/IPduGroupA</COM-MANAGEMENT-GROUP-REF>
                    <COM-MANAGEMENT-GROUP-REF DEST="I-SIGNAL-I-PDU-GROUP">/Systems/IPduGroupB</COM-MANAGEMENT-GROUP-REF>
                  </COM-MANAGEMENT-GROUP-REFS>
                  <COM-MANAGEMENT-PORT-GROUP-IREFS>
                    <COM-MANAGEMENT-PORT-GROUP-IREF>
                      <CONTEXT-COMPOSITION-REF DEST="ROOT-SW-COMPOSITION-PROTOTYPE">/Systems/RootSwCompositionPrototype</CONTEXT-COMPOSITION-REF>
                      <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Systems/RootSwCompositionPrototype/Comp1</CONTEXT-COMPONENT-REF>
                      <CONTEXT-COMPONENT-REF DEST="SW-COMPONENT-PROTOTYPE">/Systems/RootSwCompositionPrototype/Comp1/NestedComp</CONTEXT-COMPONENT-REF>
                      <TARGET-REF DEST="PORT-GROUP">/Systems/RootSwCompositionPrototype/Comp1/PG</TARGET-REF>
                    </COM-MANAGEMENT-PORT-GROUP-IREF>
                    <COM-MANAGEMENT-PORT-GROUP-IREF>
                      <TARGET-REF DEST="PORT-GROUP">/Systems/RootSwCompositionPrototype/Comp2/PG2</TARGET-REF>
                    </COM-MANAGEMENT-PORT-GROUP-IREF>
                  </COM-MANAGEMENT-PORT-GROUP-IREFS>
                  <PHYSICAL-CHANNEL-REFS>
                    <PHYSICAL-CHANNEL-REF DEST="CAN-COMMUNICATION-CONNECTOR">/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel</PHYSICAL-CHANNEL-REF>
                    <PHYSICAL-CHANNEL-REF DEST="CAN-COMMUNICATION-CONNECTOR">/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel2</PHYSICAL-CHANNEL-REF>
                  </PHYSICAL-CHANNEL-REFS>
                  <VARIATION-POINT>
                    <SHORT-LABEL>VP_COMMAP</SHORT-LABEL>
                  </VARIATION-POINT>
                </COM-MANAGEMENT-MAPPING>
              </COM-MANAGEMENT-MAPPINGS>
            </SYSTEM-MAPPING>
          </MAPPINGS>
        </SYSTEM>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""


class TestSystemTemplate:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        test_file = Path(__file__).parent.parent.parent / "integration_tests" / "test_files" / "CanSystem.arxml"
        parser.load(str(test_file), document)

    def test_can_system_arxml_loading_and_saving(self):
        document = AUTOSAR.getInstance()
        document.clear()
        parser = ARXMLParser()
        test_file = Path(__file__).parent.parent.parent / "integration_tests" / "test_files" / "CanSystem.arxml"
        parser.load(str(test_file), document)

        writer = ARXMLWriter()
        output_file = Path(__file__).parent.parent.parent / "test_armodel" / "parser" / "data" / "generated_CanSystem.arxml"
        output_file.parent.mkdir(parents=True, exist_ok=True)
        writer.save(str(output_file), document)

        assert filecmp.cmp(str(test_file), str(output_file), shallow=False) is True

    def test_system_full_attribute_round_trip(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        arxml_file = tmp_path / "full_system.arxml"
        arxml_file.write_text(FULL_SYSTEM_ARXML, encoding="utf-8")
        ARXMLParser().load(str(arxml_file), document)

        system = document.getARPackages()[0].getElement("FullSystem")
        assert isinstance(system, System)

        documentations = system.getSystemDocumentations()
        assert len(documentations) == 1
        assert isinstance(documentations[0], Chapter)
        assert documentations[0].getShortName() == "Doc1"
        assert documentations[0].getHelpEntry().getValue() == "help-topic-1"

        client_id_refs = system.getClientIdDefinitionSetRefs()
        assert len(client_id_refs) == 1
        assert client_id_refs[0].getValue() == "/Systems/ClientIds"
        assert client_id_refs[0].getDest() == "CLIENT-ID-DEFINITION-SET"

        assert system.getContainerIPduHeaderByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"

        assert system.getEcuExtractVersion().getValue() == "1.0.0"

        fibex_refs = system.getFibexElementRefs()
        assert len(fibex_refs) == 1
        assert fibex_refs[0].getValue() == "/CanSystem/CLUSTERS/CanNetwork"
        assert fibex_refs[0].getDest() == "CAN-CLUSTER"

        interp_refs = system.getInterpolationRoutineMappingSetRefs()
        assert len(interp_refs) == 1
        assert interp_refs[0].getValue() == "/Systems/InterpMapping"
        assert interp_refs[0].getDest() == "INTERPOLATION-ROUTINE-MAPPING-SET"

        clusters = system.getJ1939SharedAddressClusters()
        assert len(clusters) == 1
        assert isinstance(clusters[0], J1939SharedAddressCluster)
        assert clusters[0].getShortName() == "Cluster1"

        mappings = system.getMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SystemMapping)
        assert mappings[0].getShortName() == "Mapping1"

        assert system.getPncVectorLength().getValue() == 8
        assert system.getPncVectorOffset().getValue() == 4

        root = system.getRootSoftwareComposition()
        assert isinstance(root, RootSwCompositionPrototype)
        assert root.getShortName() == "RootComp"

        sw_cluster_refs = system.getSwClusterRefs()
        assert len(sw_cluster_refs) == 1
        assert sw_cluster_refs[0].getValue() == "/Systems/Cluster"
        assert sw_cluster_refs[0].getDest() == "CP-SOFTWARE-CLUSTER"

        assert system.getSystemVersion().getValue() == "2.0.0"

        saved_file = tmp_path / "full_system_saved.arxml"
        ARXMLWriter().save(str(saved_file), document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(str(saved_file), document_2)

        system_2 = document_2.getARPackages()[0].getElement("FullSystem")
        assert system_2 is not None
        assert len(system_2.getSystemDocumentations()) == 1
        assert system_2.getSystemDocumentations()[0].getShortName() == "Doc1"
        assert system_2.getClientIdDefinitionSetRefs()[0].getValue() == "/Systems/ClientIds"
        assert system_2.getContainerIPduHeaderByteOrder().getValue() == "MOST-SIGNIFICANT-BYTE-FIRST"
        assert system_2.getEcuExtractVersion().getValue() == "1.0.0"
        assert system_2.getFibexElementRefs()[0].getValue() == "/CanSystem/CLUSTERS/CanNetwork"
        assert system_2.getInterpolationRoutineMappingSetRefs()[0].getValue() == "/Systems/InterpMapping"
        assert [c.getShortName() for c in system_2.getJ1939SharedAddressClusters()] == ["Cluster1"]
        assert [m.getShortName() for m in system_2.getMappings()] == ["Mapping1"]
        assert system_2.getPncVectorLength().getValue() == 8
        assert system_2.getPncVectorOffset().getValue() == 4
        assert system_2.getRootSoftwareComposition().getShortName() == "RootComp"
        assert system_2.getSwClusterRefs()[0].getValue() == "/Systems/Cluster"
        assert system_2.getSystemVersion().getValue() == "2.0.0"

    def test_j1939_shared_address_cluster_content(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        arxml_file = tmp_path / "j1939_shared_address_cluster.arxml"
        arxml_file.write_text(J1939_SHARED_ADDRESS_CLUSTER_ARXML, encoding="utf-8")
        ARXMLParser().load(str(arxml_file), document)

        system = document.getARPackages()[0].getElement("J1939System")
        assert isinstance(system, System)

        clusters = system.getJ1939SharedAddressClusters()
        assert len(clusters) == 1
        cluster = clusters[0]
        assert isinstance(cluster, J1939SharedAddressCluster)
        assert cluster.getShortName() == "Cluster1"

        refs = cluster.getParticipatingJ1939ClusterRefs()
        assert len(refs) == 2
        assert refs[0].getValue() == "/Systems/J1939ClusterA"
        assert refs[0].getDest() == "J-1939-CLUSTER"
        assert refs[1].getValue() == "/Systems/J1939ClusterB"
        assert refs[1].getDest() == "J-1939-CLUSTER"

        variation_point = cluster.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "VP_CLUSTER"

    def test_com_management_mapping_content(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        arxml_file = tmp_path / "com_management_mapping.arxml"
        arxml_file.write_text(COM_MANAGEMENT_MAPPING_ARXML, encoding="utf-8")
        ARXMLParser().load(str(arxml_file), document)

        system = document.getARPackages()[0].getElement("ComMapSystem")
        assert isinstance(system, System)

        mappings = system.getMappings()
        assert len(mappings) == 1
        assert isinstance(mappings[0], SystemMapping)
        assert mappings[0].getShortName() == "Mapping1"

        com_mappings = mappings[0].getComManagementMappings()
        assert len(com_mappings) == 1
        com_mapping = com_mappings[0]
        assert isinstance(com_mapping, ComManagementMapping)
        assert com_mapping.getShortName() == "ComMapping1"

        group_refs = com_mapping.getComManagementGroupRefs()
        assert len(group_refs) == 2
        assert group_refs[0].getValue() == "/Systems/IPduGroupA"
        assert group_refs[0].getDest() == "I-SIGNAL-I-PDU-GROUP"
        assert group_refs[1].getValue() == "/Systems/IPduGroupB"
        assert group_refs[1].getDest() == "I-SIGNAL-I-PDU-GROUP"

        irefs = com_mapping.getComManagementPortGroupIRefs()
        assert len(irefs) == 2
        assert isinstance(irefs[0], PortGroupInSystemInstanceRef)
        assert irefs[0].getContextCompositionRef().getValue() == "/Systems/RootSwCompositionPrototype"
        assert irefs[0].getContextCompositionRef().getDest() == "ROOT-SW-COMPOSITION-PROTOTYPE"
        comp_refs = irefs[0].getContextComponentRefs()
        assert len(comp_refs) == 2
        assert comp_refs[0].getValue() == "/Systems/RootSwCompositionPrototype/Comp1"
        assert comp_refs[0].getDest() == "SW-COMPONENT-PROTOTYPE"
        assert comp_refs[1].getValue() == "/Systems/RootSwCompositionPrototype/Comp1/NestedComp"
        assert irefs[0].getTargetRef().getValue() == "/Systems/RootSwCompositionPrototype/Comp1/PG"
        assert irefs[0].getTargetRef().getDest() == "PORT-GROUP"
        assert irefs[1].getContextCompositionRef() is None
        assert irefs[1].getContextComponentRefs() == []
        assert irefs[1].getTargetRef().getValue() == "/Systems/RootSwCompositionPrototype/Comp2/PG2"
        assert irefs[1].getTargetRef().getDest() == "PORT-GROUP"

        channel_refs = com_mapping.getPhysicalChannelRefs()
        assert len(channel_refs) == 2
        assert channel_refs[0].getValue() == "/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel"
        assert channel_refs[0].getDest() == "CAN-COMMUNICATION-CONNECTOR"
        assert channel_refs[1].getValue() == "/CanSystem/CLUSTERS/CanNetwork/CHANNELS/CanChannel2"
        assert channel_refs[1].getDest() == "CAN-COMMUNICATION-CONNECTOR"

        variation_point = com_mapping.getVariationPoint()
        assert variation_point is not None
        assert variation_point.getShortLabel().getValue() == "VP_COMMAP"


ECU_INSTANCE_PARTITIONS_ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TopLevelDecorations</SHORT-NAME>
      <ELEMENTS>
        <ECU-INSTANCE>
          <SHORT-NAME>EcuInst</SHORT-NAME>
          <PARTITIONS>
            <ECU-PARTITION>
              <SHORT-NAME>PartA</SHORT-NAME>
              <EXEC-IN-USER-MODE>true</EXEC-IN-USER-MODE>
            </ECU-PARTITION>
            <ECU-PARTITION>
              <SHORT-NAME>PartB</SHORT-NAME>
              <EXEC-IN-USER-MODE>false</EXEC-IN-USER-MODE>
            </ECU-PARTITION>
          </PARTITIONS>
          <PN-RESET-TIME>2.0</PN-RESET-TIME>
        </ECU-INSTANCE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""

ECU_INSTANCE_NO_PARTITIONS_ARXML = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-0-3.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>TopLevelDecorations</SHORT-NAME>
      <ELEMENTS>
        <ECU-INSTANCE>
          <SHORT-NAME>EcuInst</SHORT-NAME>
        </ECU-INSTANCE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""


class TestEcuInstancePartitions:
    def test_partitions_round_trip(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        arxml_file = tmp_path / "ecu_instance_partitions.arxml"
        arxml_file.write_text(ECU_INSTANCE_PARTITIONS_ARXML, encoding="utf-8")
        ARXMLParser().load(str(arxml_file), document)

        ecu = document.getARPackages()[0].getElement("EcuInst")
        assert ecu is not None

        partitions = ecu.getPartitions()
        assert [p.getShortName() for p in partitions] == ["PartA", "PartB"]
        assert all(isinstance(p, EcuPartition) for p in partitions)
        assert partitions[0].getExecInUserMode().getValue() is True
        assert partitions[1].getExecInUserMode().getValue() is False
        assert ecu.getPnResetTime() is not None

        saved_file = tmp_path / "ecu_instance_partitions_saved.arxml"
        ARXMLWriter().save(str(saved_file), document)

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(str(saved_file), document_2)

        ecu_2 = document_2.getARPackages()[0].getElement("EcuInst")
        partitions_2 = ecu_2.getPartitions()
        assert [p.getShortName() for p in partitions_2] == ["PartA", "PartB"]
        assert partitions_2[0].getExecInUserMode().getValue() is True
        assert partitions_2[1].getExecInUserMode().getValue() is False
        assert ecu_2.getPnResetTime() is not None

    def test_ecu_instance_without_partitions(self, tmp_path):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        arxml_file = tmp_path / "ecu_instance_no_partitions.arxml"
        arxml_file.write_text(ECU_INSTANCE_NO_PARTITIONS_ARXML, encoding="utf-8")
        ARXMLParser().load(str(arxml_file), document)

        ecu = document.getARPackages()[0].getElement("EcuInst")
        assert ecu is not None
        assert ecu.getPartitions() == []
