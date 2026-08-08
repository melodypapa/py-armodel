"""Reader (parser) tests for the Implementation module SWC-IMPLEMENTATION elements.

The fragment used here must validate against the AUTOSAR XSD (see
:mod:`tests.test_armodel.xsd_validation`), so enum literals use the serialized
UPPERCASE form expected by the schema (e.g. ``BUILD``, ``C``) rather than the
camelCase ``mmt.qualifiedName`` constant form.
"""

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation import (
    Code,
    Compiler,
    DependencyOnArtifact,
    Linker,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcImplementation import (
    SwcImplementation,
)
from tests.test_armodel import xsd_validation

FRAGMENT = """<?xml version="1.0" encoding="UTF-8"?>
<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xml="http://www.w3.org/XML/1998/namespace" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_00046.xsd">
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Pkg</SHORT-NAME>
      <ELEMENTS><SWC-IMPLEMENTATION>
      <SHORT-NAME>Impl1</SHORT-NAME>
      <BUILD-ACTION-MANIFESTS>
        <BUILD-ACTION-MANIFEST-REF-CONDITIONAL>
          <BUILD-ACTION-MANIFEST-REF DEST="BUILD-ACTION-MANIFEST">/Pkg/Bam</BUILD-ACTION-MANIFEST-REF>
        </BUILD-ACTION-MANIFEST-REF-CONDITIONAL>
      </BUILD-ACTION-MANIFESTS>
      <CODE-DESCRIPTORS>
        <CODE>
          <SHORT-NAME>Code1</SHORT-NAME>
          <CALLBACK-HEADER-REFS>
            <CALLBACK-HEADER-REF DEST="SERVICE-NEEDS">/Pkg/Cb_h</CALLBACK-HEADER-REF>
          </CALLBACK-HEADER-REFS>
        </CODE>
      </CODE-DESCRIPTORS>
      <COMPILERS>
        <COMPILER>
          <SHORT-NAME>Gcc</SHORT-NAME>
          <NAME>gcc</NAME>
          <OPTIONS>-O2</OPTIONS>
          <VENDOR>GNU</VENDOR>
          <VERSION>11</VERSION>
        </COMPILER>
      </COMPILERS>
      <GENERATED-ARTIFACTS>
        <DEPENDENCY-ON-ARTIFACT>
          <SHORT-NAME>GenA</SHORT-NAME>
          <USAGES>
            <USAGE>BUILD</USAGE>
          </USAGES>
        </DEPENDENCY-ON-ARTIFACT>
      </GENERATED-ARTIFACTS>
      <HW-ELEMENT-REFS>
        <HW-ELEMENT-REF DEST="HW-ELEMENT">/Pkg/Cpu</HW-ELEMENT-REF>
      </HW-ELEMENT-REFS>
      <LINKERS>
        <LINKER>
          <SHORT-NAME>Ld</SHORT-NAME>
          <NAME>ld</NAME>
          <OPTIONS>-Map</OPTIONS>
          <VENDOR>GNU</VENDOR>
          <VERSION>2.40</VERSION>
        </LINKER>
      </LINKERS>
      <PROGRAMMING-LANGUAGE>C</PROGRAMMING-LANGUAGE>
      <REQUIRED-ARTIFACTS>
        <DEPENDENCY-ON-ARTIFACT>
          <SHORT-NAME>ReqA</SHORT-NAME>
          <USAGES>
            <USAGE>LINK</USAGE>
          </USAGES>
        </DEPENDENCY-ON-ARTIFACT>
      </REQUIRED-ARTIFACTS>
      <REQUIRED-GENERATOR-TOOLS>
        <DEPENDENCY-ON-ARTIFACT>
          <SHORT-NAME>GenT</SHORT-NAME>
          <USAGES>
            <USAGE>CODEGENERATION</USAGE>
          </USAGES>
        </DEPENDENCY-ON-ARTIFACT>
      </REQUIRED-GENERATOR-TOOLS>
      <SW-VERSION>1.0.0</SW-VERSION>
      <SWC-BSW-MAPPING-REF DEST="SWC-BSW-MAPPING">/Pkg/Mapping</SWC-BSW-MAPPING-REF>
      <USED-CODE-GENERATOR>gen</USED-CODE-GENERATOR>
      <VENDOR-ID>42</VENDOR-ID>
    </SWC-IMPLEMENTATION>      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
"""


def _load(parser):
    document = parser.getAUTOSARDocHostingDocument() if hasattr(parser, "getAUTOSARDocHostingDocument") else None
    return document


class TestImplementationFragmentIsXSDValid:
    def test_fragment_validates(self):
        xsd_validation.assert_valid(FRAGMENT)


class TestReadSwcImplementation:
    def test_swc_implementation_parse(self, parser):
        xml = FRAGMENT
        document = __import__(
            "armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure",
            fromlist=["AUTOSARDoc"],
        ).AUTOSARDoc()
        parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
        element = __import__("xml.etree.ElementTree", fromlist=["fromstring"]).fromstring(xml)
        parser.readARPackages(element, document)
        pkg = document.getARPackages()[0]
        impl = pkg.getElement("Impl1", SwcImplementation)
        assert impl is not None
        self._assert_fields(impl)

    def _assert_fields(self, impl):
        assert impl.getShortName() == "Impl1"
        assert impl.getSwVersion() is not None
        assert impl.getSwVersion().getText() == "1.0.0"
        assert impl.getVendorId() is not None
        assert isinstance(impl.getVendorId(), PositiveInteger)
        assert impl.getVendorId().getValue() == 42.0

        langs = impl.getProgrammingLanguage()
        assert langs is not None
        assert langs.getText() == "C"

        assert impl.getUsedCodeGenerator().getText() == "gen"
        assert impl.getBuildActionManifestRef() is not None
        assert impl.getBuildActionManifestRef().getValue() == "/Pkg/Bam"
        assert impl.getSwcBswMappingRef() is not None
        assert impl.getSwcBswMappingRef().getValue() == "/Pkg/Mapping"


class TestImplementationCompilers:
    def test_compiler_fields(self, parser):
        impl = _parse_impl(parser)
        comps = impl.getCompilers()
        assert len(comps) == 1
        comp = comps[0]
        assert isinstance(comp, Compiler)
        assert comp.getShortName() == "Gcc"
        assert comp.getName().getText() == "gcc"
        assert comp.getOptions().getText() == "-O2"
        assert comp.getVendor().getText() == "GNU"
        assert comp.getVersion().getText() == "11"


class TestImplementationLinkers:
    def test_linker_fields(self, parser):
        impl = _parse_impl(parser)
        linkers = impl.getLinkers()
        assert len(linkers) == 1
        linker = linkers[0]
        assert isinstance(linker, Linker)
        assert linker.getShortName() == "Ld"
        assert linker.getVersion().getText() == "2.40"


class TestImplementationArtifacts:
    def test_generated_artifacts(self, parser):
        impl = _parse_impl(parser)
        generated = impl.getGeneratedArtifacts()
        assert len(generated) == 1
        ga = generated[0]
        assert isinstance(ga, DependencyOnArtifact)
        assert ga.getShortName() == "GenA"
        assert [u.getText() for u in ga.getUsages()] == ["BUILD"]

    def test_required_artifacts(self, parser):
        impl = _parse_impl(parser)
        required = impl.getRequiredArtifacts()
        assert len(required) == 1
        ra = required[0]
        assert isinstance(ra, DependencyOnArtifact)
        assert ra.getShortName() == "ReqA"
        assert [u.getText() for u in ra.getUsages()] == ["LINK"]

    def test_required_generator_tools(self, parser):
        impl = _parse_impl(parser)
        tools = impl.getRequiredGeneratorTools()
        assert len(tools) == 1
        tool = tools[0]
        assert isinstance(tool, DependencyOnArtifact)
        assert tool.getShortName() == "GenT"
        assert [u.getText() for u in tool.getUsages()] == ["CODEGENERATION"]


class TestImplementationHwAndCode:
    def test_hw_element_refs(self, parser):
        impl = _parse_impl(parser)
        refs = impl.getHwElementRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Pkg/Cpu"

    def test_code_callback_header_refs(self, parser):
        impl = _parse_impl(parser)
        codes = impl.getCodeDescriptors()
        assert len(codes) == 1
        code = codes[0]
        assert isinstance(code, Code)
        assert code.getShortName() == "Code1"
        refs = code.getCallbackHeaderRefs()
        assert len(refs) == 1
        assert refs[0].getValue() == "/Pkg/Cb_h"


def _parse_impl(parser):
    from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSARDoc

    parser.nsmap = {"xmlns": "http://autosar.org/schema/r4.0"}
    element = __import__("xml.etree.ElementTree", fromlist=["fromstring"]).fromstring(FRAGMENT)
    document = AUTOSARDoc()
    parser.readARPackages(element, document)
    pkg = document.getARPackages()[0]
    return pkg.getElement("Impl1", SwcImplementation)
