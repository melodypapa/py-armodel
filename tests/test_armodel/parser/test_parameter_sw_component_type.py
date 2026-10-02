"""Parser/writer round-trip tests for ParameterSwComponentType (Table 2.1, p.41).

XSD group PARAMETER-SW-COMPONENT-TYPE element order: CONSTANT-MAPPING-REFS,
DATA-TYPE-MAPPING-REFS, INSTANTIATION-DATA-DEF-PROPSS (base SwComponentType
content via readSwComponentType/writeSwComponentType).
"""

import os
import tempfile

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import ParameterSwComponentType
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestParameterSwComponentType:
    def test_model_members(self):
        obj = ParameterSwComponentType(AUTOSAR.getInstance().createARPackage("Pkg"), "Psc")

        assert obj.getConstantMappingRefs() == []
        assert obj.getDataTypeMappingRefs() == []
        assert obj.getInstantiationDataDefProps() == []

        ref = RefType()
        ref.setDest("CONSTANT-SPECIFICATION-MAPPING-SET")
        ref.setValue("/Mappings/Csm1")
        assert obj.addConstantMappingRef(ref) is obj  # method chaining
        assert obj.getConstantMappingRefs() == [ref]

        ref2 = RefType()
        ref2.setDest("DATA-TYPE-MAPPING-SET")
        ref2.setValue("/Mappings/Dtm1")
        obj.addDataTypeMappingRef(ref2)
        assert obj.getDataTypeMappingRefs() == [ref2]

        obj.addConstantMappingRef(None)
        assert len(obj.getConstantMappingRefs()) == 1  # None is a no-op

    def test_full_round_trip(self):
        package = AUTOSAR.getInstance().createARPackage("Pkg")
        psc = package.createParameterSwComponentType("Psc1")
        ref = RefType()
        ref.setDest("CONSTANT-SPECIFICATION-MAPPING-SET")
        ref.setValue("/Mappings/Csm1")
        psc.addConstantMappingRef(ref)

        path = tempfile.mktemp(suffix=".arxml")
        ARXMLWriter().save(path, AUTOSAR.getInstance())
        try:
            AUTOSAR.getInstance().new()
            AUTOSAR.getInstance().setARRelease("R23-11")
            ARXMLParser(options={"warning": True}).load(path, AUTOSAR.getInstance())
            psc2 = AUTOSAR.getInstance().find("/Pkg/Psc1")
            assert isinstance(psc2, ParameterSwComponentType)
            assert len(psc2.getConstantMappingRefs()) == 1
            assert psc2.getConstantMappingRefs()[0].getValue() == "/Mappings/Csm1"
        finally:
            os.unlink(path)
