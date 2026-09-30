"""
Tests for writing LIFE-CYCLE-STATE-DEFINITION-GROUP elements (LifeCycleStateDefinitionGroup, Table 12.1).

Round-trip counterpart: tests/test_armodel/parser/test_life_cycle_state_definition_group.py
"""

import logging
import os
import tempfile
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    LifeCycleStateDefinitionGroup,
)
from armodel.writer.arxml_writer import ARXMLWriter


def _make_writer() -> ARXMLWriter:
    writer = ARXMLWriter.__new__(ARXMLWriter)
    writer.logger = logging.getLogger("test.writer")
    return writer


class TestWriteLifeCycleStateDefinitionGroup:
    """
    Test writeLifeCycleStateDefinitionGroup (LifeCycleStateDefinitionGroup, Table 12.1).
    """

    def test_write_lc_states(self):
        """Test that lcStates are written as an LC-STATES wrapper with LIFE-CYCLE-STATE children."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        group = LifeCycleStateDefinitionGroup(None, "MyLifeCycleStateDefinitionGroup")
        group.createLcState("STATE-1")
        group.createLcState("STATE-2")

        writer.writeLifeCycleStateDefinitionGroup(element, group)

        group_tag = element.find("LIFE-CYCLE-STATE-DEFINITION-GROUP")
        assert group_tag is not None
        states_tag = group_tag.find("LC-STATES")
        assert states_tag is not None
        state_tags = states_tag.findall("LIFE-CYCLE-STATE")
        assert len(state_tags) == 2
        assert state_tags[0].find("SHORT-NAME").text == "STATE-1"
        assert state_tags[1].find("SHORT-NAME").text == "STATE-2"

    def test_write_empty_wrappers(self):
        """Test that a LifeCycleStateDefinitionGroup with no lcStates writes no LC-STATES wrapper (empty-wrapper case)."""
        writer = _make_writer()
        element = ET.Element("AR-PACKAGE")

        group = LifeCycleStateDefinitionGroup(None, "MyLifeCycleStateDefinitionGroup")
        writer.writeLifeCycleStateDefinitionGroup(element, group)

        group_tag = element.find("LIFE-CYCLE-STATE-DEFINITION-GROUP")
        assert group_tag is not None
        assert group_tag.find("LC-STATES") is None

    def test_round_trip(self):
        """Write a LifeCycleStateDefinitionGroup with lcStates, reparse, and assert all fields survive."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        group = ar_root.createLifeCycleStateDefinitionGroup("MyLifeCycleStateDefinitionGroup")

        group.createLcState("STATE-1")
        group.createLcState("STATE-2")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            from armodel.parser.arxml_parser import ARXMLParser

            ARXMLParser().load(file_path, document_2)

            group_2 = document_2.getARPackages()[0].getLifeCycleStateDefinitionGroups()[0]
            assert group_2.getShortName() == "MyLifeCycleStateDefinitionGroup"
            lc_states = group_2.getLcStates()
            assert len(lc_states) == 2
            assert lc_states[0].getShortName() == "STATE-1"
            assert lc_states[1].getShortName() == "STATE-2"
        finally:
            os.remove(file_path)
