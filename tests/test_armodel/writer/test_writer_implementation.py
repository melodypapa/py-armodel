"""Writer tests for the Implementation module SWC-IMPLEMENTATION elements.

The written XML conforms to the AUTOSAR XSD, so enum values must use the
serialized UPPERCASE form (``BUILD``, ``C``) that the schema expects.
"""

import os
import tempfile
import xml.etree.cElementTree as ET

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    DependencyUsageEnum,
    ProgramminglanguageEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    PositiveInteger,
    RefType,
    RevisionLabelString,
    String,
)
from armodel.writer.arxml_writer import ARXMLWriter
from tests.test_armodel import xsd_validation


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def writer():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    return ARXMLWriter()


def _ref(value, dest=None):
    ref = RefType()
    ref.setValue(value)
    if dest:
        ref.setDest(dest)
    return ref


def _lit(value):
    lit = ARLiteral()
    lit.setValue(value)
    return lit


def _build_impl():
    pkg = AUTOSAR.getInstance().createARPackage("Pkg")
    impl = pkg.createSwcImplementation("Impl1")
    impl.setSwVersion(RevisionLabelString().setValue("1.0.0"))
    impl.setVendorId(PositiveInteger().setValue("42"))
    impl.setProgrammingLanguage(ProgramminglanguageEnum().setValue("C"))
    impl.setUsedCodeGenerator(String().setValue("gen"))
    impl.setBuildActionManifestRef(_ref("/Pkg/Bam", "BUILD-ACTION-MANIFEST"))
    impl.setSwcBswMappingRef(_ref("/Pkg/Mapping", "SWC-BSW-MAPPING"))

    comp = impl.createCompiler("Gcc")
    comp.setName(_lit("gcc"))
    comp.setOptions(_lit("-O2"))
    comp.setVendor(_lit("GNU"))
    comp.setVersion(_lit("11"))

    linker = impl.createLinker("Ld")
    linker.setVersion(_lit("2.40"))

    ga = impl.createGeneratedArtifact("GenA")
    ga.addUsage(DependencyUsageEnum().setValue("BUILD"))

    ra = impl.createRequiredArtifact("ReqA")
    ra.addUsage(DependencyUsageEnum().setValue("LINK"))

    tool = impl.createRequiredGeneratorTool("GenT")
    tool.addUsage(DependencyUsageEnum().setValue("CODEGENERATION"))

    code = impl.createCodeDescriptor("Code1")
    code.addCallbackHeaderRef(_ref("/Pkg/Cb_h", "SERVICE-NEEDS"))

    impl.addHwElementRef(_ref("/Pkg/Cpu", "HW-ELEMENT"))
    return impl


def _saved_xml():
    with tempfile.NamedTemporaryFile(suffix=".arxml", delete=False) as tmp:
        tmp_path = tmp.name
    try:
        ARXMLWriter().save(tmp_path, AUTOSAR.getInstance())
        with open(tmp_path, encoding="utf-8") as fh:
            return fh.read()
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)


def _write_impl(writer):
    parent = ET.Element("ROOT")
    writer.writeARPackageElement(parent, _build_impl())
    return parent


class TestWriteSwcImplementationXSDValid:
    def test_full_implementation_xml_is_xsd_valid(self):
        _build_impl()
        xml = _saved_xml()
        xsd_validation.assert_valid(xml)

    def test_written_fragment_is_xsd_valid(self):
        _build_impl()
        xml = _saved_xml()
        import xml.etree.ElementTree as XET

        root = XET.fromstring(xml)
        assert root.tag.endswith("AUTOSAR")
        swc = root.find(".//{http://autosar.org/schema/r4.0}SWC-IMPLEMENTATION")
        assert swc is not None
        assert swc.find("{http://autosar.org/schema/r4.0}SW-VERSION").text == "1.0.0"
        assert swc.find("{http://autosar.org/schema/r4.0}VENDOR-ID").text == "42"
