"""Writer gate: VARIATION-POINT is emitted only for VariationPointCapable classes.

The XSD declares VARIATION-POINT once per anchor class (e.g. the PORT-PROTOTYPE
group); concrete subclasses inherit the slot via group refs. The writer must
mirror this: writeIdentifiable emits VARIATION-POINT only when the object is
VariationPointCapable ([TPS_GST_00200], constr_2638).
"""

import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import PostBuildVariantCriterion, VariationPoint
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _make_identifiable():
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    pkg = document.createARPackage("Pkg")
    return pkg


class TestVariationPointWriterGate:
    def test_capable_class_writes_variation_point(self):
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components import PRPortPrototype

        pkg = _make_identifiable()
        port = PRPortPrototype(pkg, "Port")
        port.setVariationPoint(VariationPoint().setShortLabel(Identifier().setValue("VP_Port")))

        writer = ARXMLWriter()
        element = ET.Element("PR-PORT-PROTOTYPE")
        writer.writeIdentifiable(element, port)

        vp_element = element.find("VARIATION-POINT")
        assert vp_element is not None
        assert vp_element.find("SHORT-LABEL").text == "VP_Port"

    def test_non_capable_class_never_writes_variation_point(self):
        # PostBuildVariantCriterion is an Identifiable but NOT an XSD VARIATION-POINT
        # anchor. Until the Identifiable deviation is removed it can still *hold* a
        # VP; the writer gate must suppress the emission regardless.
        pkg = _make_identifiable()
        criterion = PostBuildVariantCriterion(pkg, "Criterion")
        criterion.setVariationPoint(VariationPoint().setShortLabel(Identifier().setValue("VP_Should_Not_Write")))

        writer = ARXMLWriter()
        element = ET.Element("POST-BUILD-VARIANT-CRITERION")
        writer.writeIdentifiable(element, criterion)

        assert element.find("VARIATION-POINT") is None

    def test_capable_class_round_trips_variation_point(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        pkg = document.createARPackage("Pkg")
        component = pkg.createApplicationSwComponentType("Component")
        port = component.createPRPortPrototype("Port")
        port.setVariationPoint(VariationPoint().setShortLabel(Identifier().setValue("VP_Port")))

        import os
        import tempfile

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            component_2 = document_2.getARPackages()[0].getAtomicSwComponentTypes()[0]
            ports = component_2.getPortPrototypes()
            assert len(ports) == 1
            vp = ports[0].getVariationPoint()
            assert vp is not None
            assert vp.getShortLabel().getValue() == "VP_Port"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
