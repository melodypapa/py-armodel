import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest import BuildActionEntity
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject import AutosarEngineeringObject


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

    def test_base_reader_writer_helpers_exist(self):
        from armodel.parser.arxml_parser import ARXMLParser
        from armodel.writer.arxml_writer import ARXMLWriter

        assert hasattr(ARXMLParser, "readBuildActionEntity")
        assert hasattr(ARXMLWriter, "writeBuildActionEntity")
