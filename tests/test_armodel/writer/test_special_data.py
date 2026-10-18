"""
Round-trip coverage for the VerbatimStringPlain value carried by the SD element.

VerbatimStringPlain (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 4.68, p.115) is a
``Primitive`` table with **zero Attribute rows**, so the class itself owns no XML element
(Rule 0001.7). It also has **no** ``getChildElementOptionalVerbatimStringPlain`` /
``setChildElementOptionalVerbatimStringPlain`` leaf pair, and none can be added: XSD
``complexType VERBATIM-STRING-PLAIN`` (AUTOSAR_00052.xsd l.145304) is ``xsd:simpleContent``
over ``VERBATIM-STRING-PLAIN--SIMPLE`` with only the ``AR:AR-OBJECT`` attributeGroup, and
no element or attribute anywhere declares ``type="AR:VERBATIM-STRING-PLAIN"``
(``grep -c`` = 0). The ``--SIMPLE`` type is referenced exactly once, at l.101712, as the
``simpleContent`` extension base of ``complexType SD`` -- i.e. the value *is* the ``SD``
element's own text.

That is exactly the situation the Table 4.68 Note describes: "This primitive is applied in
cases where xml:space attribute cannot be provided by the primitive type but needs to be
provided by the container class." The container class here is ``Sd``, whose spec row types
``value`` as ``VerbatimStringPlain`` (Table 4.21, Mult ``1``, Kind ``attr``).

Consequently this consumer round-trip is the **only** place the Rule 0013.2
typed-preservation property can be pinned for this type: a regression that degraded the
value to a bare ``ARLiteral``/plain ``str`` would pass every other test in the repo.
``readSd`` constructs the concrete type directly, so the property is asserted here rather
than inferred.

Leaf-helper coverage does not apply (no leaf pair exists); see the ``BASE`` warn on
``audit_class.py VerbatimStringPlain``, an accepted deviation recorded on the Group21
``VerbatimStringPlain`` row.
"""

import os
import tempfile

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Enumerations import XmlSpaceEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ARLiteral,
    NameToken,
    VerbatimStringPlain,
)
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sd, Sdg, SdgContents
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


def _build_document(value, xml_space=False, set_value=True):
    """Build a minimal R23-11 document whose ADMIN-DATA/SDGS/SDG carries one SD."""
    AUTOSAR.getInstance().setARRelease("R23-11")
    document = AUTOSAR.getInstance()
    document.clear()
    document.createARPackage("AUTOSAR")

    sdg = Sdg()
    sdg.setGID(NameToken().setValue("demo"))
    sd = Sd()
    sd.setGID(NameToken().setValue("key1"))
    if set_value:
        sd.setValue(VerbatimStringPlain().setValue(value))
    if xml_space:
        sd.setXmlSpace(XmlSpaceEnum().setValue(XmlSpaceEnum.PRESERVE))
    contents = SdgContents()
    contents.addSd(sd)
    sdg.setSdgContentsType(contents)
    document.setAdminData(AdminData().addSdg(sdg))

    return document


def _first_sd(document):
    return document.getAdminData().getSdgs()[0].getSdgContentsType().getSds()[0]


def _save_and_reload(document):
    """Save then re-load with the bundled XSD validation gates left ON (Rule 0027)."""
    file_path = tempfile.mktemp(suffix=".arxml")
    try:
        ARXMLWriter().save(file_path, document)
        written = open(file_path, encoding="utf-8").read()

        document_2 = AUTOSAR.getInstance()
        document_2.clear()
        ARXMLParser().load(file_path, document_2)
        return written, document_2
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


class TestVerbatimStringPlainSdRoundTrip:
    """
    Rule 0013.2 typed preservation for the VerbatimStringPlain value on the SD path.
    """

    def test_round_trip_preserves_value_and_type(self):
        """Write then re-read an SD; the value survives AND re-parses as a real VerbatimStringPlain."""
        document = _build_document("special   data")

        written, document_2 = _save_and_reload(document)

        assert '<SD GID="key1">special   data</SD>' in written
        reparsed = _first_sd(document_2).getValue()
        assert isinstance(reparsed, VerbatimStringPlain)
        assert reparsed.getValue() == "special   data"

    def test_round_trip_preserves_internal_whitespace_run(self):
        """
        The whole point of the type: an internal run of spaces survives verbatim.

        ``VERBATIM-STRING-PLAIN--SIMPLE`` declares ``whiteSpace=preserve`` (l.145320), and
        the Note calls this primitive "a string in which white-space needs to be
        preserved". An internal run needs no xml:space to survive XML line-end handling.
        """
        document = _build_document("special   data")

        _, document_2 = _save_and_reload(document)

        assert _first_sd(document_2).getValue().getValue() == "special   data"

    def test_round_trip_preserves_leading_and_trailing_whitespace(self):
        """
        Leading/trailing padding survives when the container class supplies xml:space.

        This is the container-class responsibility the Table 4.68 Note describes
        ("xml:space attribute cannot be provided by the primitive type but needs to be
        provided by the container class"), carried on ``Sd.xmlSpace`` (Table 4.21).
        """
        document = _build_document("  padded value  ", xml_space=True)

        written, document_2 = _save_and_reload(document)

        assert 'xml:space="preserve"' in written
        reparsed = _first_sd(document_2).getValue()
        assert isinstance(reparsed, VerbatimStringPlain)
        assert reparsed.getValue() == "  padded value  "

    def test_round_trip_preserves_embedded_newline(self):
        """An embedded newline survives when xml:space is set on the container."""
        document = _build_document("line one\nline two", xml_space=True)

        _, document_2 = _save_and_reload(document)

        reparsed = _first_sd(document_2).getValue()
        assert isinstance(reparsed, VerbatimStringPlain)
        assert reparsed.getValue() == "line one\nline two"

    def test_value_is_not_degraded_to_a_bare_arliteral(self):
        """
        The explicit Rule 0013.2 guard, stated as a negative.

        A reader that fell back to the generic literal helper would hand back an
        ``ARLiteral`` that still satisfies every value assertion above; this pins the
        concrete type so that failure mode cannot pass unnoticed.
        """
        document = _build_document("special   data")

        _, document_2 = _save_and_reload(document)

        reparsed = _first_sd(document_2).getValue()
        assert not isinstance(reparsed, ARLiteral) or isinstance(reparsed, VerbatimStringPlain)
        assert type(reparsed) is VerbatimStringPlain


class TestVerbatimStringPlainSdEmptyCases:
    """
    The empty cases: an unset value emits no text and re-parses as None.
    """

    def test_unset_value_emits_empty_sd_and_reparses_as_none(self):
        """No value set -> the SD element carries no text and getValue() is None on re-parse."""
        document = _build_document(None, set_value=False)

        written, document_2 = _save_and_reload(document)

        assert '<SD GID="key1"/>' in written
        assert _first_sd(document_2).getValue() is None

    def test_empty_string_value_emits_empty_sd_and_reparses_as_none(self):
        """
        An empty string is legal for xsd:string, but is indistinguishable from "absent"
        once it is carried as SD element text (readSd skips blank text).

        Documented rather than asserted as a defect: the blank-text mapping belongs to
        ``Sd``'s reader, not to VerbatimStringPlain, which is value-carried and never
        inspects its own text.
        """
        document = _build_document("")

        written, document_2 = _save_and_reload(document)

        assert '<SD GID="key1"/>' in written
        assert _first_sd(document_2).getValue() is None
