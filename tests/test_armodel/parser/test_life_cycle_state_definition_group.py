"""
Tests for parsing LIFE-CYCLE-STATE-DEFINITION-GROUP elements (LifeCycleStateDefinitionGroup, Table 12.1).

Round-trip counterpart: tests/test_armodel/writer/test_life_cycle_state_definition_group.py
"""

import os
import tempfile
import xml.etree.ElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    LifeCycleStateDefinitionGroup,
)
from armodel.parser.arxml_parser import ARXMLParser

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    """Reset AUTOSAR singleton before each test."""
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    """Create ARXML parser instance."""
    AUTOSAR.getInstance().new()
    return ARXMLParser()


def _make_group() -> LifeCycleStateDefinitionGroup:
    AUTOSAR.getInstance().new()
    ar_root = AUTOSAR.getInstance().createARPackage("AUTOSAR")
    return ar_root.createLifeCycleStateDefinitionGroup("MyLifeCycleStateDefinitionGroup")


class TestReadLifeCycleStateDefinitionGroup:
    """
    Test readLifeCycleStateDefinitionGroup (LifeCycleStateDefinitionGroup, Table 12.1).
    """

    def test_read_lc_states(self, parser):
        """Test that the LC-STATES wrapper populates lcStates with LIFE-CYCLE-STATE children."""
        group = _make_group()
        element = ET.fromstring(
            f"""<LIFE-CYCLE-STATE-DEFINITION-GROUP xmlns='{NS}'>
                <SHORT-NAME>MyLifeCycleStateDefinitionGroup</SHORT-NAME>
                <LC-STATES>
                    <LIFE-CYCLE-STATE>
                        <SHORT-NAME>STATE-1</SHORT-NAME>
                        <CATEGORY>STATE</CATEGORY>
                    </LIFE-CYCLE-STATE>
                    <LIFE-CYCLE-STATE>
                        <SHORT-NAME>STATE-2</SHORT-NAME>
                    </LIFE-CYCLE-STATE>
                </LC-STATES>
            </LIFE-CYCLE-STATE-DEFINITION-GROUP>"""
        )

        parser.readLifeCycleStateDefinitionGroup(element, group)

        lc_states = group.getLcStates()
        assert len(lc_states) == 2
        assert lc_states[0].getShortName() == "STATE-1"
        assert lc_states[0].getCategory().getValue() == "STATE"
        assert lc_states[1].getShortName() == "STATE-2"

    def test_read_empty_lc_states(self, parser):
        """Test that an absent LC-STATES wrapper leaves lcStates empty (empty-wrapper case)."""
        group = _make_group()
        element = ET.fromstring(
            f"""<LIFE-CYCLE-STATE-DEFINITION-GROUP xmlns='{NS}'>
                <SHORT-NAME>MyLifeCycleStateDefinitionGroup</SHORT-NAME>
            </LIFE-CYCLE-STATE-DEFINITION-GROUP>"""
        )

        parser.readLifeCycleStateDefinitionGroup(element, group)

        assert group.getLcStates() == []

    def test_load_via_ar_package(self, parser):
        """Test that the ARPackage ELEMENTS dispatch reads a LIFE-CYCLE-STATE-DEFINITION-GROUP into getLifeCycleStateDefinitionGroups()."""
        AUTOSAR.getInstance().setARRelease("R23-11")
        content = f"""<?xml version="1.0" encoding="utf-8"?>
<AUTOSAR xmlns="{NS}" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="{NS} AUTOSAR_00052.xsd">
    <AR-PACKAGES>
        <AR-PACKAGE>
            <SHORT-NAME>AUTOSAR</SHORT-NAME>
            <ELEMENTS>
                <LIFE-CYCLE-STATE-DEFINITION-GROUP>
                    <SHORT-NAME>MyLifeCycleStateDefinitionGroup</SHORT-NAME>
                    <LC-STATES>
                        <LIFE-CYCLE-STATE>
                            <SHORT-NAME>STATE-1</SHORT-NAME>
                        </LIFE-CYCLE-STATE>
                    </LC-STATES>
                </LIFE-CYCLE-STATE-DEFINITION-GROUP>
            </ELEMENTS>
        </AR-PACKAGE>
    </AR-PACKAGES>
</AUTOSAR>"""
        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

            document = AUTOSAR.getInstance()
            document.clear()
            parser.load(file_path, document)

            groups = document.getARPackages()[0].getLifeCycleStateDefinitionGroups()
            assert len(groups) == 1
            assert groups[0].getShortName() == "MyLifeCycleStateDefinitionGroup"
            assert groups[0].getLcStates()[0].getShortName() == "STATE-1"
        finally:
            os.remove(file_path)
