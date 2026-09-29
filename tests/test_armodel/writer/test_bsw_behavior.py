"""Writer tests for BswBehavior classes (BswVariableAccess, BSW events, BSW policies).

Builds the model via the model API, saves with ARXMLWriter, reloads with ARXMLParser
and asserts field values round-trip.

Round-trip counterpart: tests/test_armodel/parser/test_bsw_behavior.py
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    RefType,
    TimeValue,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest is not None:
        ref.setDest(dest)
    return ref


def _new_document():
    document = AUTOSAR.getInstance()
    document.clear()
    document.setARRelease("R23-11")
    return document


def _make_behavior():
    document = _new_document()
    pkg = document.createARPackage("Pkg")
    desc = pkg.createBswModuleDescription("BswMd")
    return document, desc.createBswInternalBehavior("Beh")


def _reload(tmp_path, document, filename: str):
    out_file = tmp_path / filename
    ARXMLWriter().save(str(out_file), document)
    reloaded = AUTOSAR.getInstance()
    reloaded.clear()
    reloaded.setARRelease("R23-11")
    ARXMLParser().load(str(out_file), reloaded)
    behavior = reloaded.getARPackages()[0].getBswModuleDescriptions()[0].getInternalBehaviors()[0]
    return out_file.read_text(), behavior


class TestBswVariableAccess:
    def test_round_trip_data_send_point_full(self, tmp_path):
        document, behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("Ent")
        entity.setImplementedEntryRef(_ref("/Pkg/Entry", "BSW-MODULE-ENTRY"))
        point = entity.createDataSendPoint("Dsp")
        point.setAccessedVariableRef(_ref("/Pkg/Vdp", "VARIABLE-DATA-PROTOTYPE"))
        point.addContextLimitationRef(_ref("/Pkg/Part1", "BSW-DISTINGUISHED-PARTITION"))
        point.addContextLimitationRef(_ref("/Pkg/Part2", "BSW-DISTINGUISHED-PARTITION"))

        raw, behavior_2 = _reload(tmp_path, document, "dsp.arxml")
        entity_2 = behavior_2.getBswSchedulableEntities()[0]
        points = entity_2.getDataSendPoints()
        assert len(points) == 1
        assert points[0].getShortName() == "Dsp"
        assert points[0].getAccessedVariableRef().getValue() == "/Pkg/Vdp"
        assert points[0].getAccessedVariableRef().getDest() == "VARIABLE-DATA-PROTOTYPE"
        limitations = points[0].getContextLimitationRefs()
        assert len(limitations) == 2
        assert limitations[0].getValue() == "/Pkg/Part1"
        assert limitations[0].getDest() == "BSW-DISTINGUISHED-PARTITION"
        assert limitations[1].getValue() == "/Pkg/Part2"
        assert "CONTEXT-LIMITATION-REFS" in raw

    def test_round_trip_data_receive_point_full(self, tmp_path):
        document, behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("Ent")
        entity.setImplementedEntryRef(_ref("/Pkg/Entry", "BSW-MODULE-ENTRY"))
        point = entity.createDataReceivePoint("Drp")
        point.setAccessedVariableRef(_ref("/Pkg/RVdp", "VARIABLE-DATA-PROTOTYPE"))
        point.addContextLimitationRef(_ref("/Pkg/Part1", "BSW-DISTINGUISHED-PARTITION"))

        _, behavior_2 = _reload(tmp_path, document, "drp.arxml")
        entity_2 = behavior_2.getBswSchedulableEntities()[0]
        points = entity_2.getDataReceivePoints()
        assert len(points) == 1
        assert points[0].getShortName() == "Drp"
        assert points[0].getAccessedVariableRef().getValue() == "/Pkg/RVdp"
        limitations = points[0].getContextLimitationRefs()
        assert len(limitations) == 1
        assert limitations[0].getValue() == "/Pkg/Part1"

    def test_round_trip_empty_wrapper(self, tmp_path):
        document, behavior = _make_behavior()
        entity = behavior.createBswSchedulableEntity("Ent")
        entity.setImplementedEntryRef(_ref("/Pkg/Entry", "BSW-MODULE-ENTRY"))
        point = entity.createDataSendPoint("Dsp")
        point.setAccessedVariableRef(_ref("/Pkg/Vdp", "VARIABLE-DATA-PROTOTYPE"))

        raw, behavior_2 = _reload(tmp_path, document, "dsp_empty.arxml")
        assert "CONTEXT-LIMITATION-REFS" not in raw
        entity_2 = behavior_2.getBswSchedulableEntities()[0]
        assert len(entity_2.getDataSendPoints()) == 1
        assert entity_2.getDataSendPoints()[0].getContextLimitationRefs() == []

    def test_no_wrapper_when_no_points(self, tmp_path):
        document, behavior = _make_behavior()
        behavior.createBswSchedulableEntity("Ent").setImplementedEntryRef(_ref("/Pkg/Entry", "BSW-MODULE-ENTRY"))

        raw, behavior_2 = _reload(tmp_path, document, "no_points.arxml")
        assert "DATA-SEND-POINTS" not in raw
        assert "DATA-RECEIVE-POINTS" not in raw
        assert behavior_2.getBswSchedulableEntities()[0].getDataSendPoints() == []


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


def _posint(value):
    p = PositiveInteger()
    p.setValue(str(value))
    return p


def _time(value):
    t = TimeValue()
    t.setValue(value)
    return t
