"""Reader tests for SwcServiceDependency (Swc TPS Table 7.56, p.609).

readSwcServiceDependency populates the model via the SwcInternalBehavior
factory and the own-group readers, with the inherited SERVICE-DEPENDENCY
group (assignedDataType / diagnosticRelevance / symbolicNameProps) read
through readServiceDependency (Rule 0025: base helper called exactly once).
Element set per the XSD group SWC-SERVICE-DEPENDENCY (AUTOSAR_00052.xsd
line 117470): ASSIGNED-DATAS, ASSIGNED-PORTS, REPRESENTED-PORT-GROUP-REF,
SERVICE-NEEDS.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.ServiceNeeds import NvBlockNeeds
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_behavior():
    document = _autosar_root()
    package = document.createARPackage("Pkg")
    swc = package.createApplicationSwComponentType("Swc")
    return swc.createSwcInternalBehavior("IB")


class TestSwcServiceDependencyReader:
    def test_read_own_group_field_values(self, parser):
        behavior = _make_behavior()
        element = _snip(
            """
            <SHORT-NAME>Dep</SHORT-NAME>
            <ASSIGNED-DATAS>
                <ROLE-BASED-DATA-ASSIGNMENT>
                    <SHORT-NAME>Assignment1</SHORT-NAME>
                    <ROLE>ramMirror</ROLE>
                    <USED-PIM-REF DEST="PER-INSTANCE-MEMORY">/Pkg/Swc/IB/Pim</USED-PIM-REF>
                </ROLE-BASED-DATA-ASSIGNMENT>
            </ASSIGNED-DATAS>
            <ASSIGNED-PORTS>
                <ROLE-BASED-PORT-ASSIGNMENT>
                    <SHORT-NAME>Assignment2</SHORT-NAME>
                    <PORT-PROTOTYPE-REF DEST="R-PORT-PROTOTYPE">/Pkg/Swc/Port</PORT-PROTOTYPE-REF>
                    <ROLE>NvMService</ROLE>
                </ROLE-BASED-PORT-ASSIGNMENT>
            </ASSIGNED-PORTS>
            <REPRESENTED-PORT-GROUP-REF DEST="PORT-GROUP">/Pkg/PortGroup</REPRESENTED-PORT-GROUP-REF>
            <SERVICE-NEEDS>
                <NV-BLOCK-NEEDS>
                    <SHORT-NAME>NvNeeds</SHORT-NAME>
                    <READONLY>true</READONLY>
                    <RELIABILITY>NO-PROTECTION</RELIABILITY>
                </NV-BLOCK-NEEDS>
            </SERVICE-NEEDS>
            """,
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        parser.readSwcServiceDependency(element, behavior)

        dependencies = behavior.getSwcServiceDependencies()
        assert len(dependencies) == 1
        dependency = dependencies[0]
        assert dependency.short_name == "Dep"

        assert len(dependency.getAssignedData()) == 1
        assert dependency.getAssignedData()[0].getRole().getValue() == "ramMirror"
        assert dependency.getAssignedData()[0].getUsedPimRef().getValue() == "/Pkg/Swc/IB/Pim"

        assert len(dependency.getAssignedPorts()) == 1
        assert dependency.getAssignedPorts()[0].getPortPrototypeRef().getValue() == "/Pkg/Swc/Port"
        assert dependency.getAssignedPorts()[0].getRole().getValue() == "NvMService"

        assert dependency.getRepresentedPortGroupRef().getValue() == "/Pkg/PortGroup"

        needs = dependency.getServiceNeeds()
        assert isinstance(needs, NvBlockNeeds)
        assert needs.short_name == "NvNeeds"
        assert needs.getReadonly().getValue() is True
        assert needs.getReliability().getValue() == "NO-PROTECTION"

    def test_read_inherited_service_dependency_group(self, parser):
        """The inherited SERVICE-DEPENDENCY group (diagnosticRelevance, symbolicNameProps) is read once."""
        behavior = _make_behavior()
        element = _snip(
            """
            <SHORT-NAME>Dep</SHORT-NAME>
            <DIAGNOSTIC-RELEVANCE>IS-RELEVANT</DIAGNOSTIC-RELEVANCE>
            <SYMBOLIC-NAME-PROPS>
                <SHORT-NAME>SNP</SHORT-NAME>
            </SYMBOLIC-NAME-PROPS>
            <SERVICE-NEEDS>
                <DLT-USER-NEEDS>
                    <SHORT-NAME>DltNeeds</SHORT-NAME>
                </DLT-USER-NEEDS>
            </SERVICE-NEEDS>
            """,
            root_tag="SWC-SERVICE-DEPENDENCY",
        )
        parser.readSwcServiceDependency(element, behavior)

        dependency = behavior.getSwcServiceDependencies()[0]
        assert dependency.getDiagnosticRelevance().getValue() == "IS-RELEVANT"
        assert dependency.getSymbolicNameProps().getShortName() == "SNP"
        assert dependency.getServiceNeeds().short_name == "DltNeeds"
