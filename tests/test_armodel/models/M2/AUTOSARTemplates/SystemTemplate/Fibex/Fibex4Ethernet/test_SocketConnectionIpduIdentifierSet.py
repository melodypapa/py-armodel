"""Spec-sync tests for SocketConnectionIpduIdentifierSet (R23-11 CP_TPS_SystemTemplate, Table 6.164, p.490)."""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    SocketConnectionIpduIdentifierSet,
    SoConIPduIdentifier,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement


class MockParent(ARObject):
    def __init__(self):
        super().__init__()


class TestSocketConnectionIpduIdentifierSet:
    MEMBERS = [
        "iPduIdentifiers",
    ]

    IPDU_IDENTIFIER_NOTE = "Collection of IPduIdentifiers that are transmitted over Socket Connections. Stereotypes: atpSplitable Tags: atp.Splitkey=iPduIdentifier.shortName"

    def _set(self):
        return SocketConnectionIpduIdentifierSet(MockParent(), "ipdu_set")

    def test_rehoused_to_spec_package(self):
        """Spec Package row = Fibex4Ethernet::ServiceInstances (Rule 0007) - rehoused from the ARPackage.py stub."""
        module = inspect.getmodule(SocketConnectionIpduIdentifierSet).__name__

        assert module == "armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances"

    def test_inheritance(self):
        identifier_set = self._set()

        assert isinstance(identifier_set, FibexElement)

    def test_top_level_export(self):
        import armodel

        assert armodel.SocketConnectionIpduIdentifierSet is SocketConnectionIpduIdentifierSet

    def test_init_parameter_annotations(self):
        annotations = typing.get_type_hints(SocketConnectionIpduIdentifierSet.__init__)

        assert annotations["parent"] is ARObject
        assert annotations["short_name"] is str

    def test_member_annotations_match_getter_returns(self):
        assert typing.get_type_hints(SocketConnectionIpduIdentifierSet.getIPduIdentifiers)["return"] == typing.List[SoConIPduIdentifier]

    def test_initialization_defaults(self):
        identifier_set = self._set()

        assert identifier_set.getIPduIdentifiers() == []

    def test_member_order(self):
        identifier_set = self._set()

        members = [k for k in vars(identifier_set) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_ipdu_identifier(self):
        identifier_set = self._set()

        identifier = identifier_set.createIPduIdentifier("ipdu_id1")
        assert isinstance(identifier, SoConIPduIdentifier)
        assert identifier.getShortName() == "ipdu_id1"
        assert identifier_set.getIPduIdentifiers() == [identifier]

        again = identifier_set.createIPduIdentifier("ipdu_id1")
        assert again is identifier
        assert len(identifier_set.getIPduIdentifiers()) == 1

    def test_class_docstring_note(self):
        expected = "Collection of PduIdentifiers used for transmission over a Socket Connection with the header option. " "Tags: atp.recommendedPackage=SocketConnectionIpduIdentiferSets"
        assert inspect.cleandoc(SocketConnectionIpduIdentifierSet.__doc__) == expected

    def test_notes_verbatim(self):
        assert inspect.cleandoc(SocketConnectionIpduIdentifierSet.createIPduIdentifier.__doc__) == self.IPDU_IDENTIFIER_NOTE
        assert inspect.cleandoc(SocketConnectionIpduIdentifierSet.getIPduIdentifiers.__doc__) == self.IPDU_IDENTIFIER_NOTE
        assert self.IPDU_IDENTIFIER_NOTE in inspect.getsource(SocketConnectionIpduIdentifierSet.__init__)
