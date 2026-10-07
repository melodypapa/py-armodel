"""
Tests for the DdsCpConfig model class (Fibex4Ethernet::Dds) — DdsCpConfig, Table 6.175 (p.526, R23-11).
"""

import inspect
import typing

import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DdsCpDomain, DdsCpQosProfile
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.Dds import DdsCpConfig


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    AUTOSAR.getInstance().setARRelease("R23-11")
    yield
    AUTOSAR.getInstance().new()


class TestDdsCpConfig:
    """
    Test class for DdsCpConfig functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 6.175, p.526
    """

    CLASS_NOTE = "Collection of DDS definitions. Tags: atp.Status=candidate atp.recommendedPackage=DdsCpConfigs"
    DDS_DOMAIN_NOTE = "Collection of DDS Domain definitions. Tags: atp.Status=candidate"
    DDS_QOS_PROFILE_NOTE = "Collection of DDS QOS Profiles. Tags: atp.Status=candidate"

    def _create_config(self) -> DdsCpConfig:
        return DdsCpConfig(AUTOSAR.getInstance(), "DdsCpConfig1")

    def test_initialization(self):
        """
        Test that a new DdsCpConfig initializes all attributes to their defaults.
        """
        obj = self._create_config()

        assert obj.getShortName() == "DdsCpConfig1"
        assert obj.getDdsDomains() == []
        assert obj.getDdsQosProfiles() == []

    def test_is_arelement_subclass(self):
        """
        Test that DdsCpConfig derives from ARElement (Base column most-derived class).
        """
        assert issubclass(DdsCpConfig, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpConfig.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert DdsCpConfig.__init__.__doc__ is None

    def test_create_dds_domain(self):
        """
        Test createDdsDomain appends a DdsCpDomain and returns the existing one for a duplicate short name.
        """
        obj = self._create_config()

        domain = obj.createDdsDomain("Domain1")
        assert isinstance(domain, DdsCpDomain)
        assert domain.getShortName() == "Domain1"
        assert obj.getDdsDomains() == [domain]

        duplicate = obj.createDdsDomain("Domain1")
        assert duplicate is domain
        assert len(obj.getDdsDomains()) == 1

    def test_create_dds_domain_aggregates_partitions_and_topics(self):
        """
        Test that a created DdsCpDomain aggregates DdsCpPartition/DdsCpTopic children (one level down).
        """
        obj = self._create_config()

        domain = obj.createDdsDomain("Domain1")
        partition = domain.createDdsPartition("Partition1")
        topic = domain.createDdsTopic("Topic1")
        assert domain.getDdsPartitions() == [partition]
        assert domain.getDdsTopics() == [topic]

    def test_create_dds_qos_profile(self):
        """
        Test createDdsQosProfile appends a DdsCpQosProfile and returns the existing one for a duplicate short name.
        """
        obj = self._create_config()

        profile = obj.createDdsQosProfile("QosProfile1")
        assert isinstance(profile, DdsCpQosProfile)
        assert profile.getShortName() == "QosProfile1"
        assert obj.getDdsQosProfiles() == [profile]

        duplicate = obj.createDdsQosProfile("QosProfile1")
        assert duplicate is profile
        assert len(obj.getDdsQosProfiles()) == 1

    def test_arpackage_creates_dds_cp_config(self):
        """
        Test the ARPackage.element polymorphic dispatch factory (Aggregated by: ARPackage.element).
        """
        package = ARPackage(AUTOSAR.getInstance(), "DdsCpConfigs")
        config = package.createDdsConfig("DdsCpConfig1")
        assert isinstance(config, DdsCpConfig)
        assert package.createDdsConfig("DdsCpConfig1") is config

    def test_type_annotations(self):
        """
        Getter returns match the spec multiplicity (`*` → List) and factories take str.
        """
        assert typing.get_type_hints(DdsCpConfig.createDdsDomain)["short_name"] is str
        assert typing.get_type_hints(DdsCpConfig.getDdsDomains)["return"] == typing.List[DdsCpDomain]
        assert typing.get_type_hints(DdsCpConfig.createDdsQosProfile)["short_name"] is str
        assert typing.get_type_hints(DdsCpConfig.getDdsQosProfiles)["return"] == typing.List[DdsCpQosProfile]

    def test_accessor_docstrings_are_spec_notes_verbatim(self):
        """
        Accessor docstrings carry the spec Note verbatim.
        """
        assert inspect.cleandoc(DdsCpConfig.createDdsDomain.__doc__) == self.DDS_DOMAIN_NOTE
        assert inspect.cleandoc(DdsCpConfig.getDdsDomains.__doc__) == self.DDS_DOMAIN_NOTE
        assert inspect.cleandoc(DdsCpConfig.createDdsQosProfile.__doc__) == self.DDS_QOS_PROFILE_NOTE
        assert inspect.cleandoc(DdsCpConfig.getDdsQosProfiles.__doc__) == self.DDS_QOS_PROFILE_NOTE
