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


class TestBswExclusiveAreaPolicy:
    def test_read_full(self, tmp_path):
        policies = """<EXCLUSIVE-AREA-POLICYS>
            <BSW-EXCLUSIVE-AREA-POLICY>
                <ENABLE-TAKE-ADDRESS>true</ENABLE-TAKE-ADDRESS>
                <API-PRINCIPLE>common</API-PRINCIPLE>
                <EXCLUSIVE-AREA-REF DEST="EXCLUSIVE-AREA">/Pkg/Ea</EXCLUSIVE-AREA-REF>
            </BSW-EXCLUSIVE-AREA-POLICY>
        </EXCLUSIVE-AREA-POLICYS>"""
        _, behavior = _load_behavior(tmp_path, policies)
        policies_2 = behavior.getExclusiveAreaPolicies()
        assert len(policies_2) == 1
        assert policies_2[0].getEnableTakeAddress().getValue() is True
        assert policies_2[0].getApiPrinciple().getValue() == "common"
        assert policies_2[0].getExclusiveAreaRef().getValue() == "/Pkg/Ea"
        assert policies_2[0].getExclusiveAreaRef().getDest() == "EXCLUSIVE-AREA"

    def test_read_empty_wrapper(self, tmp_path):
        _, behavior = _load_behavior(tmp_path, "<EXCLUSIVE-AREA-POLICYS></EXCLUSIVE-AREA-POLICYS>")
        assert behavior.getExclusiveAreaPolicies() == []


class TestBswExternalTriggerOccurredEvent:
    def test_read_full(self, tmp_path):
        events = """<EVENTS>
            <BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT>
                <SHORT-NAME>Evt</SHORT-NAME>
                <CONTEXT-LIMITATION-REFS>
                    <CONTEXT-LIMITATION-REF DEST="BSW-DISTINGUISHED-PARTITION">/Pkg/Part1</CONTEXT-LIMITATION-REF>
                </CONTEXT-LIMITATION-REFS>
                <STARTS-ON-EVENT-REF DEST="BSW-SCHEDULABLE-ENTITY">/Pkg/Ent</STARTS-ON-EVENT-REF>
                <TRIGGER-REF DEST="TRIGGER">/Pkg/Trig</TRIGGER-REF>
            </BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT>
        </EVENTS>"""
        _, behavior = _load_behavior(tmp_path, events)
        events_2 = behavior.getBswExternalTriggerOccurredEvents()
        assert len(events_2) == 1
        assert events_2[0].getShortName() == "Evt"
        assert events_2[0].getTriggerRef().getValue() == "/Pkg/Trig"
        assert events_2[0].getTriggerRef().getDest() == "TRIGGER"
        assert events_2[0].getStartsOnEventRef().getValue() == "/Pkg/Ent"
        limitations = events_2[0].getContextLimitationRefs()
        assert len(limitations) == 1
        assert limitations[0].getValue() == "/Pkg/Part1"

    def test_read_empty_context_limitation_wrapper(self, tmp_path):
        events = """<EVENTS>
            <BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT>
                <SHORT-NAME>Evt</SHORT-NAME>
                <CONTEXT-LIMITATION-REFS></CONTEXT-LIMITATION-REFS>
                <TRIGGER-REF DEST="TRIGGER">/Pkg/Trig</TRIGGER-REF>
            </BSW-EXTERNAL-TRIGGER-OCCURRED-EVENT>
        </EVENTS>"""
        _, behavior = _load_behavior(tmp_path, events)
        events_2 = behavior.getBswExternalTriggerOccurredEvents()
        assert len(events_2) == 1
        assert events_2[0].getTriggerRef().getValue() == "/Pkg/Trig"
        assert events_2[0].getContextLimitationRefs() == []


class TestBswOperationInvokedEvent:
    def test_read_full(self, tmp_path):
        events = """<EVENTS>
            <BSW-OPERATION-INVOKED-EVENT>
                <SHORT-NAME>Evt</SHORT-NAME>
                <CONTEXT-LIMITATION-REFS>
                    <CONTEXT-LIMITATION-REF DEST="BSW-DISTINGUISHED-PARTITION">/Pkg/Part1</CONTEXT-LIMITATION-REF>
                </CONTEXT-LIMITATION-REFS>
                <STARTS-ON-EVENT-REF DEST="BSW-SCHEDULABLE-ENTITY">/Pkg/Ent</STARTS-ON-EVENT-REF>
                <ENTRY-REF DEST="BSW-MODULE-CLIENT-SERVER-ENTRY">/Pkg/CsEntry</ENTRY-REF>
            </BSW-OPERATION-INVOKED-EVENT>
        </EVENTS>"""
        _, behavior = _load_behavior(tmp_path, events)
        events_2 = behavior.getBswOperationInvokedEvents()
        assert len(events_2) == 1
        assert events_2[0].getShortName() == "Evt"
        assert events_2[0].getEntryRef().getValue() == "/Pkg/CsEntry"
        assert events_2[0].getEntryRef().getDest() == "BSW-MODULE-CLIENT-SERVER-ENTRY"
        assert events_2[0].getStartsOnEventRef().getValue() == "/Pkg/Ent"
        limitations = events_2[0].getContextLimitationRefs()
        assert len(limitations) == 1
        assert limitations[0].getValue() == "/Pkg/Part1"

    def test_read_minimal(self, tmp_path):
        events = """<EVENTS>
            <BSW-OPERATION-INVOKED-EVENT>
                <SHORT-NAME>Evt</SHORT-NAME>
                <CONTEXT-LIMITATION-REFS></CONTEXT-LIMITATION-REFS>
                <ENTRY-REF DEST="BSW-MODULE-CLIENT-SERVER-ENTRY">/Pkg/CsEntry</ENTRY-REF>
            </BSW-OPERATION-INVOKED-EVENT>
        </EVENTS>"""
        _, behavior = _load_behavior(tmp_path, events)
        events_2 = behavior.getBswOperationInvokedEvents()
        assert len(events_2) == 1
        assert events_2[0].getEntryRef().getValue() == "/Pkg/CsEntry"
        assert events_2[0].getStartsOnEventRef() is None
        assert events_2[0].getContextLimitationRefs() == []
