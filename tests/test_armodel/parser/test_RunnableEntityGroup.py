"""Reader tests for RunnableEntityGroup (Swc TPS Table 4.100, p.223).

readRunnableEntityGroup populates the model via addRunnableEntityGroupIRef /
addRunnableEntityIRef, with VARIATION-POINT last per the XSD group
RUNNABLE-ENTITY-GROUP (AUTOSAR_00052.xsd, sequenceOffset 10000).
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerRunnableEntityGroupInCompositionInstanceRef,
    RunnableEntityInCompositionInstanceRef,
)
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_runnable_entity_group(short_name: str = "Group"):
    document = _autosar_root()
    package = document.createARPackage("Pkg")
    return package.createRunnableEntityGroup(short_name)


class TestRunnableEntityGroupReader:
    def test_read_full_field_values(self, parser):
        runnable_group = _make_runnable_entity_group("FullGroup")
        element = _snip(
            """
            <SHORT-NAME>FullGroup</SHORT-NAME>
            <RUNNABLE-ENTITY-GROUP-IREFS>
                <RUNNABLE-ENTITY-GROUP-IREF>
                    <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                    <TARGET-RUNNABLE-ENTITY-GROUP-REF DEST="RUNNABLE-ENTITY-GROUP">/comp/Root/Swc1/NestedGroup</TARGET-RUNNABLE-ENTITY-GROUP-REF>
                </RUNNABLE-ENTITY-GROUP-IREF>
            </RUNNABLE-ENTITY-GROUP-IREFS>
            <RUNNABLE-ENTITY-IREFS>
                <RUNNABLE-ENTITY-IREF>
                    <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                    <TARGET-RUNNABLE-ENTITY-REF DEST="RUNNABLE-ENTITY">/comp/Root/Swc1/Runnable1</TARGET-RUNNABLE-ENTITY-REF>
                </RUNNABLE-ENTITY-IREF>
            </RUNNABLE-ENTITY-IREFS>
            <VARIATION-POINT>
                <SHORT-LABEL>VP1</SHORT-LABEL>
            </VARIATION-POINT>
            """,
            root_tag="RUNNABLE-ENTITY-GROUP",
        )
        parser.readRunnableEntityGroup(element, runnable_group)
        assert runnable_group.getShortName() == "FullGroup"

        inner_refs = runnable_group.getRunnableEntityGroupIRefs()
        assert len(inner_refs) == 1
        assert isinstance(inner_refs[0], InnerRunnableEntityGroupInCompositionInstanceRef)
        assert [ref.getValue() for ref in inner_refs[0].getContextSwComponentPrototypeRefs()] == ["/comp/Root/Swc1"]
        assert inner_refs[0].getTargetRunnableEntityGroupRef().getValue() == "/comp/Root/Swc1/NestedGroup"

        runnable_refs = runnable_group.getRunnableEntityIRefs()
        assert len(runnable_refs) == 1
        assert isinstance(runnable_refs[0], RunnableEntityInCompositionInstanceRef)
        assert [ref.getValue() for ref in runnable_refs[0].getContextSwComponentPrototypeRefs()] == ["/comp/Root/Swc1"]
        assert runnable_refs[0].getTargetRunnableEntityRef().getValue() == "/comp/Root/Swc1/Runnable1"

        assert runnable_group.getVariationPoint() is not None
        assert runnable_group.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_empty_wrappers(self, parser):
        runnable_group = _make_runnable_entity_group()
        element = _snip(
            """
            <SHORT-NAME>EmptyGroup</SHORT-NAME>
            <RUNNABLE-ENTITY-GROUP-IREFS/>
            <RUNNABLE-ENTITY-IREFS/>
            """,
            root_tag="RUNNABLE-ENTITY-GROUP",
        )
        parser.readRunnableEntityGroup(element, runnable_group)
        assert runnable_group.getRunnableEntityGroupIRefs() == []
        assert runnable_group.getRunnableEntityIRefs() == []
        assert runnable_group.getVariationPoint() is None

    def test_read_absent_wrappers(self, parser):
        runnable_group = _make_runnable_entity_group()
        element = _snip(
            """
            <SHORT-NAME>BareGroup</SHORT-NAME>
            """,
            root_tag="RUNNABLE-ENTITY-GROUP",
        )
        parser.readRunnableEntityGroup(element, runnable_group)
        assert runnable_group.getRunnableEntityGroupIRefs() == []
        assert runnable_group.getRunnableEntityIRefs() == []
        assert runnable_group.getVariationPoint() is None
