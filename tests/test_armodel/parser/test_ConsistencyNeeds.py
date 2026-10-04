"""Reader tests for ConsistencyNeeds (Swc TPS Table 4.99, p.222).

readConsistencyNeeds populates the model via createDpgDoesNotRequireCoherency /
createDpgRequiresCoherency / createRegDoesNotRequireStability /
createRegRequiresStability, with VARIATION-POINT last per the XSD group
CONSISTENCY-NEEDS (AUTOSAR_00052.xsd, sequenceOffset 10000).
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    DataPrototypeGroup,
    RunnableEntityGroup,
)
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_consistency_needs(short_name: str = "Needs"):
    document = _autosar_root()
    package = document.createARPackage("Pkg")
    return package.createConsistencyNeeds(short_name)


class TestConsistencyNeedsReader:
    def test_read_full_field_values(self, parser):
        consistency_needs = _make_consistency_needs("FullNeeds")
        element = _snip(
            """
            <SHORT-NAME>FullNeeds</SHORT-NAME>
            <DPG-DOES-NOT-REQUIRE-COHERENCYS>
                <DATA-PROTOTYPE-GROUP>
                    <SHORT-NAME>DpgNotCoherent</SHORT-NAME>
                    <IMPLICIT-DATA-ACCESS-IREFS>
                        <IMPLICIT-DATA-ACCESS-IREF>
                            <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                            <TARGET-VARIABLE-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/vdp/Var1</TARGET-VARIABLE-DATA-PROTOTYPE-REF>
                        </IMPLICIT-DATA-ACCESS-IREF>
                    </IMPLICIT-DATA-ACCESS-IREFS>
                </DATA-PROTOTYPE-GROUP>
            </DPG-DOES-NOT-REQUIRE-COHERENCYS>
            <DPG-REQUIRES-COHERENCYS>
                <DATA-PROTOTYPE-GROUP>
                    <SHORT-NAME>DpgCoherent</SHORT-NAME>
                </DATA-PROTOTYPE-GROUP>
            </DPG-REQUIRES-COHERENCYS>
            <REG-DOES-NOT-REQUIRE-STABILITYS>
                <RUNNABLE-ENTITY-GROUP>
                    <SHORT-NAME>RegNotStable</SHORT-NAME>
                    <RUNNABLE-ENTITY-IREFS>
                        <RUNNABLE-ENTITY-IREF>
                            <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                            <TARGET-RUNNABLE-ENTITY-REF DEST="RUNNABLE-ENTITY">/comp/Root/Swc1/Runnable1</TARGET-RUNNABLE-ENTITY-REF>
                        </RUNNABLE-ENTITY-IREF>
                    </RUNNABLE-ENTITY-IREFS>
                </RUNNABLE-ENTITY-GROUP>
            </REG-DOES-NOT-REQUIRE-STABILITYS>
            <REG-REQUIRES-STABILITYS>
                <RUNNABLE-ENTITY-GROUP>
                    <SHORT-NAME>RegStable</SHORT-NAME>
                </RUNNABLE-ENTITY-GROUP>
            </REG-REQUIRES-STABILITYS>
            <VARIATION-POINT>
                <SHORT-LABEL>VP1</SHORT-LABEL>
            </VARIATION-POINT>
            """,
            root_tag="CONSISTENCY-NEEDS",
        )
        parser.readConsistencyNeeds(element, consistency_needs)
        assert consistency_needs.getShortName() == "FullNeeds"

        dpg_not_coherent = consistency_needs.getDpgDoesNotRequireCoherencys()
        assert len(dpg_not_coherent) == 1
        assert isinstance(dpg_not_coherent[0], DataPrototypeGroup)
        assert dpg_not_coherent[0].getShortName() == "DpgNotCoherent"
        implicit_refs = dpg_not_coherent[0].getImplicitDataAccessIRefs()
        assert len(implicit_refs) == 1
        assert implicit_refs[0].getTargetVariableDataPrototypeRef().getValue() == "/vdp/Var1"
        assert implicit_refs[0].getContextSwComponentPrototypeRefs()[0].getValue() == "/comp/Root/Swc1"

        dpg_coherent = consistency_needs.getDpgRequiresCoherencys()
        assert len(dpg_coherent) == 1
        assert isinstance(dpg_coherent[0], DataPrototypeGroup)
        assert dpg_coherent[0].getShortName() == "DpgCoherent"

        reg_not_stable = consistency_needs.getRegDoesNotRequireStabilitys()
        assert len(reg_not_stable) == 1
        assert isinstance(reg_not_stable[0], RunnableEntityGroup)
        assert reg_not_stable[0].getShortName() == "RegNotStable"
        runnable_refs = reg_not_stable[0].getRunnableEntityIRefs()
        assert len(runnable_refs) == 1
        assert runnable_refs[0].getTargetRunnableEntityRef().getValue() == "/comp/Root/Swc1/Runnable1"
        assert runnable_refs[0].getContextSwComponentPrototypeRefs()[0].getValue() == "/comp/Root/Swc1"

        reg_stable = consistency_needs.getRegRequiresStabilitys()
        assert len(reg_stable) == 1
        assert isinstance(reg_stable[0], RunnableEntityGroup)
        assert reg_stable[0].getShortName() == "RegStable"

        assert consistency_needs.getVariationPoint() is not None
        assert consistency_needs.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_empty_wrappers(self, parser):
        consistency_needs = _make_consistency_needs()
        element = _snip(
            """
            <SHORT-NAME>EmptyNeeds</SHORT-NAME>
            <DPG-DOES-NOT-REQUIRE-COHERENCYS/>
            <DPG-REQUIRES-COHERENCYS/>
            <REG-DOES-NOT-REQUIRE-STABILITYS/>
            <REG-REQUIRES-STABILITYS/>
            """,
            root_tag="CONSISTENCY-NEEDS",
        )
        parser.readConsistencyNeeds(element, consistency_needs)
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == []
        assert consistency_needs.getDpgRequiresCoherencys() == []
        assert consistency_needs.getRegDoesNotRequireStabilitys() == []
        assert consistency_needs.getRegRequiresStabilitys() == []
        assert consistency_needs.getVariationPoint() is None

    def test_read_absent_wrappers(self, parser):
        consistency_needs = _make_consistency_needs()
        element = _snip(
            """
            <SHORT-NAME>BareNeeds</SHORT-NAME>
            """,
            root_tag="CONSISTENCY-NEEDS",
        )
        parser.readConsistencyNeeds(element, consistency_needs)
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == []
        assert consistency_needs.getDpgRequiresCoherencys() == []
        assert consistency_needs.getRegDoesNotRequireStabilitys() == []
        assert consistency_needs.getRegRequiresStabilitys() == []
        assert consistency_needs.getVariationPoint() is None
