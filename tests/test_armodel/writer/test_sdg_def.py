"""
Tests for writing SDG-DEF elements (SdgDef family, Tables 4.24-4.35).

Round-trip counterpart: tests/test_armodel/parser/test_sdg_def.py
"""

import os
import tempfile

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ModelRestrictionTypes import (
    FullBindingTimeEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Limit,
    NameToken,
    PositiveInteger,
    RefType,
    RegularExpression,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef import (
    SdgAggregationWithVariation,
    SdgClass,
    SdgForeignReference,
    SdgForeignReferenceWithVariation,
    SdgPrimitiveAttribute,
    SdgPrimitiveAttributeWithVariation,
    SdgReference,
)
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


class TestSdgDefRoundTrip:
    """
    Build a full SdgDef family, write it, re-parse it and compare field values.
    """

    def test_round_trip(self):
        document = AUTOSAR.getInstance()
        document.clear()
        document.setARRelease("R23-11")
        root = document.createARPackage("AUTOSAR")
        sdg_def = root.createSdgDef("MySdgDef")

        sdg_class = SdgClass(sdg_def, "MySdgClass")
        sdg_class.setGid(NameToken().setValue("MY-CLASS-GID"))
        sdg_class.setExtendsMetaClass("ArPackage")
        sdg_class.setCaption(Boolean().setValue(True))
        sdg_def.addSdgClass(sdg_class)

        prim = SdgPrimitiveAttribute(sdg_class, "Severity")
        prim.setGid(NameToken().setValue("SEVERITY"))
        prim.setMax(Limit().setValue("3"))
        prim.setMaxLength(PositiveInteger().setValue(16))
        prim.setPattern(RegularExpression().setValue("critical|significant|minor|low"))
        sdg_class.addAttribute(prim)

        prim_wv = SdgPrimitiveAttributeWithVariation(sdg_class, "VarAttr")
        prim_wv.setVariation(Boolean().setValue(False))
        prim_wv.addValidBindingTime(FullBindingTimeEnum().setValue(FullBindingTimeEnum.POST_BUILD))
        sdg_class.addAttribute(prim_wv)

        sdg_ref = SdgReference(sdg_class, "ClassRef")
        sdg_ref.setDestSdgRef(RefType().setValue("/AUTOSAR/SdgDefs/MySdgDef/MySdgClass").setDest("SDG-CLASS"))
        sdg_class.addAttribute(sdg_ref)

        agg = SdgAggregationWithVariation(sdg_class, "SubSdg")
        agg.setGid(NameToken().setValue("SUB-SDG"))
        agg.setSubSdgRef(RefType().setValue("/AUTOSAR/SdgDefs/MySdgDef/MySdgClass").setDest("SDG-CLASS"))
        sdg_class.addAttribute(agg)

        fref = SdgForeignReference(sdg_class, "PackageRef")
        fref.setDestMetaClass("ARPackage")
        sdg_class.addAttribute(fref)

        fref_wv = SdgForeignReferenceWithVariation(sdg_class, "PackageRefWV")
        fref_wv.setDestMetaClass("ARPackage")
        sdg_class.addAttribute(fref_wv)

        sdg_class.addSdgConstraintRef(RefType().setValue("/AUTOSAR/MyConstraint").setDest("TRACEABLE-TEXT"))

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            writer = ARXMLWriter()
            writer.save(file_path, document)

            reload_doc = AUTOSAR.getInstance()
            reload_doc.new()
            reload_doc.setARRelease("R23-11")
            parser = ARXMLParser()
            parser.load(file_path, reload_doc)

            reloaded_def = reload_doc.getARPackages()[0].getReferrableElement("MySdgDef")
            assert reloaded_def is not None
            reloaded_classes = reloaded_def.getSdgClasses()
            assert len(reloaded_classes) == 1
            reloaded = reloaded_classes[0]

            assert reloaded.getShortName() == "MySdgClass"
            assert reloaded.getGid().getValue() == "MY-CLASS-GID"
            assert reloaded.getExtendsMetaClass() == "ArPackage"
            assert reloaded.getCaption().getValue() is True

            attributes = reloaded.getAttributes()
            assert len(attributes) == 6
            by_name = {a.getShortName(): a for a in attributes}

            prim_r = by_name["Severity"]
            assert prim_r.getGid().getValue() == "SEVERITY"
            assert prim_r.getMax().getValue() == "3"
            assert prim_r.getMaxLength().getValue() == 16
            assert prim_r.getPattern().getValue() == "critical|significant|minor|low"

            prim_wv_r = by_name["VarAttr"]
            assert prim_wv_r.getVariation().getValue() is False
            assert prim_wv_r.getValidBindingTimes()[0].getValue() == "POST-BUILD"

            sdg_ref_r = by_name["ClassRef"]
            assert sdg_ref_r.getDestSdgRef().getValue() == "/AUTOSAR/SdgDefs/MySdgDef/MySdgClass"
            assert sdg_ref_r.getDestSdgRef().getDest() == "SDG-CLASS"

            agg_r = by_name["SubSdg"]
            assert agg_r.getGid().getValue() == "SUB-SDG"
            assert agg_r.getSubSdgRef().getDest() == "SDG-CLASS"

            fref_r = by_name["PackageRef"]
            assert fref_r.getDestMetaClass() == "ARPackage"
            fref_wv_r = by_name["PackageRefWV"]
            assert fref_wv_r.getDestMetaClass() == "ARPackage"

            refs = reloaded.getSdgConstraintRefs()
            assert len(refs) == 1
            assert refs[0].getValue() == "/AUTOSAR/MyConstraint"
            assert refs[0].getDest() == "TRACEABLE-TEXT"
        finally:
            os.remove(file_path)
