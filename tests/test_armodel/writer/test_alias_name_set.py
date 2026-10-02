"""Writer/reader round-trip tests for AliasNameSet / AliasNameAssignment (ALIAS-NAME-SET)."""

import os
import tempfile

import pytest

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import AliasNameAssignment, AliasNameSet
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType, String
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


def _ref(value, dest):
    ref = RefType()
    ref.setValue(value)
    ref.setDest(dest)
    return ref


class TestAliasNameSetRoundTrip:
    def test_alias_name_set_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        alias_set = ar_root.createAliasNameSet("AliasSet1")
        assignment = AliasNameAssignment()
        short_label = String()
        short_label.setValue("aliasName1")
        assignment.setShortLabel(short_label)
        assignment.setIdentifiableRef(_ref("/AUTOSAR/SomeElement", "IDENTIFIABLE"))
        assignment.setFlatInstanceRef(_ref("/AUTOSAR/FlatInstance", "FLAT-INSTANCE-REF"))
        alias_set.addAliasName(assignment)

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            parsed_pkg = document_2.getARPackages()[0]
            parsed_sets = [el for el in parsed_pkg.getReferrableElements() if isinstance(el, AliasNameSet)]
            assert len(parsed_sets) == 1
            parsed_set = parsed_sets[0]
            assert parsed_set.getShortName() == "AliasSet1"
            assignments = parsed_set.getAliasNames()
            assert len(assignments) == 1
            parsed_assignment = assignments[0]
            assert isinstance(parsed_assignment, AliasNameAssignment)
            assert parsed_assignment.getShortLabel().getValue() == "aliasName1"
            assert parsed_assignment.getIdentifiableRef().getValue() == "/AUTOSAR/SomeElement"
            assert parsed_assignment.getIdentifiableRef().getDest() == "IDENTIFIABLE"
            assert parsed_assignment.getFlatInstanceRef().getValue() == "/AUTOSAR/FlatInstance"
            assert parsed_assignment.getFlatInstanceRef().getDest() == "FLAT-INSTANCE-REF"
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_alias_name_set_empty_round_trip(self):
        AUTOSAR.getInstance().setARRelease("R23-11")
        document = AUTOSAR.getInstance()
        document.clear()
        ar_root = document.createARPackage("AUTOSAR")
        ar_root.createAliasNameSet("EmptySet")

        file_path = tempfile.mktemp(suffix=".arxml")
        try:
            ARXMLWriter().save(file_path, document)

            document_2 = AUTOSAR.getInstance()
            document_2.clear()
            ARXMLParser().load(file_path, document_2)

            parsed_pkg = document_2.getARPackages()[0]
            parsed_sets = [el for el in parsed_pkg.getReferrableElements() if isinstance(el, AliasNameSet)]
            assert len(parsed_sets) == 1
            assert parsed_sets[0].getShortName() == "EmptySet"
            assert parsed_sets[0].getAliasNames() == []
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
