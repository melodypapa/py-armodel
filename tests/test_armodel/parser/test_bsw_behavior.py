"""Parser tests for BswBehavior classes (BswVariableAccess, BSW events, BSW policies).

Exercises the readers wired into readBswModuleDescription -> readBswInternalBehavior /
readBswModuleEntity dispatch paths via full-document loads.

Round-trip counterpart: tests/test_armodel/writer/test_bsw_behavior.py
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _behavior_doc(inner: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>Pkg</SHORT-NAME>
            <ELEMENTS>
                <BSW-MODULE-DESCRIPTION>
                    <SHORT-NAME>BswMd</SHORT-NAME>
                    <INTERNAL-BEHAVIORS>
                        <BSW-INTERNAL-BEHAVIOR>
                            <SHORT-NAME>Beh</SHORT-NAME>
                            {inner}
                        </BSW-INTERNAL-BEHAVIOR>
                    </INTERNAL-BEHAVIORS>
                </BSW-MODULE-DESCRIPTION>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""


def _load_behavior(tmp_path, inner: str, filename: str = "doc.arxml"):
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    arxml_file = tmp_path / filename
    arxml_file.write_text(_behavior_doc(inner), encoding="utf-8")
    ARXMLParser().load(str(arxml_file), document)
    behavior = document.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
    return document, behavior


_ENTITY_TMPL = """<ENTITYS>
    {points}
    <BSW-SCHEDULABLE-ENTITY>
        <SHORT-NAME>Ent</SHORT-NAME>
        <IMPLEMENTED-ENTRY-REF DEST="BSW-MODULE-ENTRY">/Pkg/Entry</IMPLEMENTED-ENTRY-REF>
        {accesses}
    </BSW-SCHEDULABLE-ENTITY>
</ENTITYS>"""


class TestBswVariableAccess:
    def test_read_data_send_point_full(self, tmp_path):
        accesses = """<DATA-SEND-POINTS>
            <BSW-VARIABLE-ACCESS>
                <SHORT-NAME>Dsp</SHORT-NAME>
                <ACCESSED-VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Pkg/Vdp</ACCESSED-VARIABLE-REF>
                <CONTEXT-LIMITATION-REFS>
                    <CONTEXT-LIMITATION-REF DEST="BSW-DISTINGUISHED-PARTITION">/Pkg/Part1</CONTEXT-LIMITATION-REF>
                    <CONTEXT-LIMITATION-REF DEST="BSW-DISTINGUISHED-PARTITION">/Pkg/Part2</CONTEXT-LIMITATION-REF>
                </CONTEXT-LIMITATION-REFS>
            </BSW-VARIABLE-ACCESS>
        </DATA-SEND-POINTS>"""
        _, behavior = _load_behavior(tmp_path, _ENTITY_TMPL.format(points="", accesses=accesses))
        entity = behavior.getBswSchedulableEntities()[0]
        points = entity.getDataSendPoints()
        assert len(points) == 1
        assert points[0].getShortName() == "Dsp"
        assert points[0].getAccessedVariableRef().getValue() == "/Pkg/Vdp"
        assert points[0].getAccessedVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        limitations = points[0].getContextLimitationRefs()
        assert len(limitations) == 2
        assert limitations[0].getValue() == "/Pkg/Part1"
        assert limitations[0].getDest() == "BSW-DISTINGUISHED-PARTITION"
        assert limitations[1].getValue() == "/Pkg/Part2"

    def test_read_data_receive_point_full(self, tmp_path):
        accesses = """<DATA-RECEIVE-POINTS>
            <BSW-VARIABLE-ACCESS>
                <SHORT-NAME>Drp</SHORT-NAME>
                <ACCESSED-VARIABLE-REF DEST="VARIABLE-DATA-PROTOTYPE">/Pkg/RVdp</ACCESSED-VARIABLE-REF>
                <CONTEXT-LIMITATION-REFS>
                    <CONTEXT-LIMITATION-REF DEST="BSW-DISTINGUISHED-PARTITION">/Pkg/Part1</CONTEXT-LIMITATION-REF>
                </CONTEXT-LIMITATION-REFS>
            </BSW-VARIABLE-ACCESS>
        </DATA-RECEIVE-POINTS>"""
        _, behavior = _load_behavior(tmp_path, _ENTITY_TMPL.format(points="", accesses=accesses))
        entity = behavior.getBswSchedulableEntities()[0]
        points = entity.getDataReceivePoints()
        assert len(points) == 1
        assert points[0].getShortName() == "Drp"
        assert points[0].getAccessedVariableRef().getValue() == "/Pkg/RVdp"
        limitations = points[0].getContextLimitationRefs()
        assert len(limitations) == 1
        assert limitations[0].getValue() == "/Pkg/Part1"

    def test_read_empty_wrapper(self, tmp_path):
        accesses = """<DATA-SEND-POINTS></DATA-SEND-POINTS>
        <DATA-RECEIVE-POINTS></DATA-RECEIVE-POINTS>"""
        _, behavior = _load_behavior(tmp_path, _ENTITY_TMPL.format(points="", accesses=accesses))
        entity = behavior.getBswSchedulableEntities()[0]
        assert entity.getDataSendPoints() == []
        assert entity.getDataReceivePoints() == []
