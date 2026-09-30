"""
Tests for the ARObject class (AUTOSAR_FO_TPS_GenericStructureTemplate, Table 6.1).
"""

import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
    ARObject,
    DiagnosticParameter,
    DiagnosticParameterSupportInfo,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class ConcreteARObject(ARObject):
    pass


class TestARObject:
    def test_abstract_initialization(self):
        """
        ARObject is abstract and cannot be instantiated directly.
        """
        with pytest.raises(TypeError):
            ARObject()

    def test_initialization(self):
        """
        A concrete ARObject initializes all members to None.
        """
        obj = ConcreteARObject()

        assert obj.getChecksum() is None
        assert obj.getTimestamp() is None
        assert obj.parent is None

    def test_get_set_checksum(self):
        """
        Round-trips the checksum member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = String()
        value.setValue("abc123")
        obj.setChecksum(value)
        assert obj.getChecksum() is value

        obj.setChecksum(None)
        assert obj.getChecksum() is value

    def test_get_set_timestamp(self):
        """
        Round-trips the timestamp member; None is a no-op.
        """
        obj = ConcreteARObject()

        value = DateTime()
        value.setValue("2009-07-23T13:38:00Z")
        obj.setTimestamp(value)
        assert obj.getTimestamp() is value

        obj.setTimestamp(None)
        assert obj.getTimestamp() is value

    def test_get_tag_name(self):
        """
        getTagName strips the namespace prefix from a tag name.
        """
        obj = ConcreteARObject()

        nsmap = {"xmlns": "http://www.example.com/ns"}
        assert obj.getTagName("{http://www.example.com/ns}elementName", nsmap) == "elementName"
        assert obj.getTagName("simpleTag", nsmap) == "simpleTag"


class TestDiagnosticParameter:
    """
    Test class for DiagnosticParameter functionality.

    Spec: AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf, Table 4.5, p.36
    (Base DiagnosticAbstractParameter is an un-synced stub queued for a later
    batch — only DiagnosticParameter's own Table 4.5 rows are exercised here.)
    """

    def _create_parameter(self) -> DiagnosticParameter:
        return DiagnosticParameter()

    def test_initialization(self):
        """
        Test that DiagnosticParameter is initialized with the spec defaults.
        """
        obj = self._create_parameter()

        assert obj.getIdent() is None
        assert obj.getSupportInfo() is None

    def test_create_ident(self):
        """
        Test createIdent creates, returns self-contained ident and returns the existing one for a duplicate short name.
        """
        obj = self._create_parameter()

        ident = obj.createIdent("Pid1")
        assert ident is not None
        assert ident.getShortName() == "Pid1"
        assert obj.getIdent() is ident

        duplicate = obj.createIdent("Pid1")
        assert duplicate is ident  # duplicate short name returns the existing ident

    def test_get_set_support_info(self):
        """
        Test getSupportInfo and setSupportInfo round-trip and None no-op.
        """
        obj = self._create_parameter()

        support_info = DiagnosticParameterSupportInfo()
        result = obj.setSupportInfo(support_info)
        assert result is obj  # method chaining
        assert obj.getSupportInfo() is support_info

        result = obj.setSupportInfo(None)
        assert result is obj  # method chaining with None
        assert obj.getSupportInfo() is support_info  # None is a no-op

    def test_variation_point_mixin(self):
        """
        Test the VariationPointCapable mixin accessors (VP-capable per Rule 0020: XSD group DIAGNOSTIC-PARAMETER carries VARIATION-POINT).
        """
        obj = self._create_parameter()

        assert obj.getVariationPoint() is None
