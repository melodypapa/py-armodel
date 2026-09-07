import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity, BuildActionInvocator
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import VerbatimString
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg


class TestBuildActionEntity:
    def test_is_abstract_and_has_spec_shape(self):
        with pytest.raises(TypeError, match="BuildActionEntity is an abstract class"):
            BuildActionEntity(AUTOSAR.getInstance(), "Entity")

        assert BuildActionEntity.__doc__.strip() == (
            "This meta-class represents the ability to describe a build action entity which might be specialized " "to environments as well as to individual build actions."
        )

    def test_initialization_and_accessors(self):
        class ConcreteBuildActionEntity(BuildActionEntity):
            pass

        entity = ConcreteBuildActionEntity(AUTOSAR.getInstance(), "Entity")
        assert entity.getDeliveryArtifacts() == []
        assert entity.getInvocation() is None
        artifact = AutosarEngineeringObject()
        assert entity.addDeliveryArtifact(artifact) is entity
        assert entity.setInvocation(None) is entity
        assert entity.getDeliveryArtifacts() == [artifact]

        invocator = BuildActionInvocator()
        assert entity.setInvocation(invocator) is entity
        assert entity.getInvocation() is invocator

    def test_base_reader_writer_helpers_exist(self):
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        assert hasattr(ARXMLParser, "readBuildActionEntity")
        assert hasattr(ARXMLWriter, "writeBuildActionEntity")


class TestBuildActionInvocator:
    def test_docstring_matches_spec_note(self):
        assert BuildActionInvocator.__doc__.strip() == ("This meta-class represents the ability to specify the invocation of a task in a build action.")

    def test_initialization_and_accessors(self):
        invocator = BuildActionInvocator()
        assert invocator.getCommand() is None
        assert invocator.getSdgs() == []

        assert invocator.setCommand(None) is invocator
        assert invocator.getCommand() is None
        command = VerbatimString()
        command.setValue("make all")
        assert invocator.setCommand(command) is invocator
        assert invocator.getCommand() is command

        sdg = Sdg()
        assert invocator.addSdg(None) is invocator
        assert invocator.getSdgs() == []
        assert invocator.addSdg(sdg) is invocator
        assert invocator.getSdgs() == [sdg]
