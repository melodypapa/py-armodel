"""Reader tests for DataPrototypeGroup (Swc TPS Table 4.101, p.223).

readDataPrototypeGroup populates the model via addDataPrototypeGroupIRef /
addImplicitDataAccessIRef, with VARIATION-POINT last per the XSD group
DATA-PROTOTYPE-GROUP (AUTOSAR_00052.xsd, sequenceOffset 10000).
"""

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior.InstanceRef import (
    InnerDataPrototypeGroupInCompositionInstanceRef,
    VariableDataPrototypeInCompositionInstanceRef,
)
from tests.test_armodel.parser._helpers import _autosar_root, _snip


def _make_data_prototype_group(short_name: str = "Group"):
    document = _autosar_root()
    package = document.createARPackage("Pkg")
    return package.createDataPrototypeGroup(short_name)


class TestDataPrototypeGroupReader:
    def test_read_full_field_values(self, parser):
        data_group = _make_data_prototype_group("FullGroup")
        element = _snip(
            """
            <SHORT-NAME>FullGroup</SHORT-NAME>
            <DATA-PROTOTYPE-GROUP-IREFS>
                <DATA-PROTOTYPE-GROUP-IREF>
                    <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                    <TARGET-DATA-PROTOTYPE-GROUP-REF DEST="DATA-PROTOTYPE-GROUP">/comp/Root/Swc1/NestedGroup</TARGET-DATA-PROTOTYPE-GROUP-REF>
                </DATA-PROTOTYPE-GROUP-IREF>
            </DATA-PROTOTYPE-GROUP-IREFS>
            <IMPLICIT-DATA-ACCESS-IREFS>
                <IMPLICIT-DATA-ACCESS-IREF>
                    <CONTEXT-SW-COMPONENT-PROTOTYPE-REF DEST="SW-COMPONENT-PROTOTYPE">/comp/Root/Swc1</CONTEXT-SW-COMPONENT-PROTOTYPE-REF>
                    <CONTEXT-PORT-PROTOTYPE-REF DEST="PORT-PROTOTYPE">/comp/Root/Swc1/Port1</CONTEXT-PORT-PROTOTYPE-REF>
                    <TARGET-VARIABLE-DATA-PROTOTYPE-REF DEST="VARIABLE-DATA-PROTOTYPE">/comp/Root/Swc1/Data1</TARGET-VARIABLE-DATA-PROTOTYPE-REF>
                </IMPLICIT-DATA-ACCESS-IREF>
            </IMPLICIT-DATA-ACCESS-IREFS>
            <VARIATION-POINT>
                <SHORT-LABEL>VP1</SHORT-LABEL>
            </VARIATION-POINT>
            """,
            root_tag="DATA-PROTOTYPE-GROUP",
        )
        parser.readDataPrototypeGroup(element, data_group)
        assert data_group.getShortName() == "FullGroup"

        inner_refs = data_group.getDataPrototypeGroupIRefs()
        assert len(inner_refs) == 1
        assert isinstance(inner_refs[0], InnerDataPrototypeGroupInCompositionInstanceRef)
        assert [ref.getValue() for ref in inner_refs[0].getContextSwComponentPrototypeRefs()] == ["/comp/Root/Swc1"]
        assert inner_refs[0].getTargetDataPrototypeGroupRef().getValue() == "/comp/Root/Swc1/NestedGroup"

        access_refs = data_group.getImplicitDataAccessIRefs()
        assert len(access_refs) == 1
        assert isinstance(access_refs[0], VariableDataPrototypeInCompositionInstanceRef)
        assert [ref.getValue() for ref in access_refs[0].getContextSwComponentPrototypeRefs()] == ["/comp/Root/Swc1"]
        assert access_refs[0].getContextPortPrototypeRef().getValue() == "/comp/Root/Swc1/Port1"
        assert access_refs[0].getTargetVariableDataPrototypeRef().getValue() == "/comp/Root/Swc1/Data1"

        assert data_group.getVariationPoint() is not None
        assert data_group.getVariationPoint().getShortLabel().getValue() == "VP1"

    def test_read_empty_wrappers(self, parser):
        data_group = _make_data_prototype_group()
        element = _snip(
            """
            <SHORT-NAME>EmptyGroup</SHORT-NAME>
            <DATA-PROTOTYPE-GROUP-IREFS/>
            <IMPLICIT-DATA-ACCESS-IREFS/>
            """,
            root_tag="DATA-PROTOTYPE-GROUP",
        )
        parser.readDataPrototypeGroup(element, data_group)
        assert data_group.getDataPrototypeGroupIRefs() == []
        assert data_group.getImplicitDataAccessIRefs() == []
        assert data_group.getVariationPoint() is None

    def test_read_absent_wrappers(self, parser):
        data_group = _make_data_prototype_group()
        element = _snip(
            """
            <SHORT-NAME>BareGroup</SHORT-NAME>
            """,
            root_tag="DATA-PROTOTYPE-GROUP",
        )
        parser.readDataPrototypeGroup(element, data_group)
        assert data_group.getDataPrototypeGroupIRefs() == []
        assert data_group.getImplicitDataAccessIRefs() == []
        assert data_group.getVariationPoint() is None
