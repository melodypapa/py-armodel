"""
This module contains tests for the CpSoftwareClusterBinaryManifestDescriptor class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.ARPackage module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.17, p.913
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARElement,
    ARPackage,
    CpSoftwareClusterBinaryManifestDescriptor,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    BinaryManifestMetaDataField,
    BinaryManifestProvideResource,
    BinaryManifestRequireResource,
    BinaryManifestResourceDefinition,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    RefType,
)


class TestCpSoftwareClusterBinaryManifestDescriptor:
    """
    Test class for CpSoftwareClusterBinaryManifestDescriptor functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.17, p.913
    """

    CLASS_NOTE = "This meta-class has the ability to act as a hub for all information related to the binary manifest of a given CP software cluster. The manifest is subject to integrator work and therefore not a part of the definition of the CP software cluster itself. Tags: atp.recommendedPackage=CpSoftwareClusterBinaryManifestDescriptors"
    CP_SOFTWARE_CLUSTER_NOTE = "This reference identifies the CpSoftwareCluster to which the enclosing CpSoftwareClusterBinaryManifestDescriptor belongs, The CpSoftwareClusterBinaryManifestDescriptor is defined in an integration phase while the referenced CpSoftwareCluster represents a design element. Therefore, it makes sense to use a reference rather than an aggregation in the relation of the two meta-classes."
    META_DATA_FIELD_NOTE = "This aggregation identifies the collection of meta-data contained in the enclosing binary manifest."
    PROVIDE_RESOURCE_NOTE = "This aggregation represents the collection of provided resources in the enclosing binary manifest."
    REQUIRE_RESOURCE_NOTE = "This aggregation represents the collection of required resources in the enclosing binary manifest."
    RESOURCE_DEFINITION_NOTE = "This aggregation represents the collection of binary manifest resource definitions that belong to the enclosing CpSoftwareClusterBinaryManifestDescriptor."
    SOFTWARE_CLUSTER_ID_NOTE = "This attribute represents the value of the id of the corresponding CP software cluster. This id is assigned by an integrator, but may also be copied from CpSoftwareCluster.softwareClusterId if available."

    def _create_descriptor(self) -> CpSoftwareClusterBinaryManifestDescriptor:
        return CpSoftwareClusterBinaryManifestDescriptor(None, "Manifest1")

    def test_is_arelement_subclass(self):
        """
        Test that CpSoftwareClusterBinaryManifestDescriptor derives from ARElement per the Table 11.17 Base row.
        """
        assert issubclass(CpSoftwareClusterBinaryManifestDescriptor, ARElement)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterBinaryManifestDescriptor.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.17 displayed row order
        (getter first on the scalar rows, creates first on the multi rows).
        """
        methods = [name for name, value in CpSoftwareClusterBinaryManifestDescriptor.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getCpSoftwareClusterRef",
            "setCpSoftwareClusterRef",
            "createMetaDataField",
            "getMetaDataFields",
            "createProvideResource",
            "getProvideResources",
            "createRequireResource",
            "getRequireResources",
            "createResourceDefinition",
            "getResourceDefinitions",
            "getSoftwareClusterId",
            "setSoftwareClusterId",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_descriptor()

        assert obj.getShortName() == "Manifest1"
        assert obj.getCpSoftwareClusterRef() is None
        assert obj.getMetaDataFields() == []
        assert obj.getProvideResources() == []
        assert obj.getRequireResources() == []
        assert obj.getResourceDefinitions() == []
        assert obj.getSoftwareClusterId() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types.
        """
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getCpSoftwareClusterRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.setCpSoftwareClusterRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterBinaryManifestDescriptor

        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.createMetaDataField)
        assert hints.get("short_name") is str
        assert hints.get("return") is BinaryManifestMetaDataField
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getMetaDataFields)
        assert hints.get("return") == typing.List[BinaryManifestMetaDataField]

        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.createProvideResource)
        assert hints.get("short_name") is str
        assert hints.get("return") is BinaryManifestProvideResource
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getProvideResources)
        assert hints.get("return") == typing.List[BinaryManifestProvideResource]

        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.createRequireResource)
        assert hints.get("short_name") is str
        assert hints.get("return") is BinaryManifestRequireResource
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getRequireResources)
        assert hints.get("return") == typing.List[BinaryManifestRequireResource]

        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.createResourceDefinition)
        assert hints.get("short_name") is str
        assert hints.get("return") is BinaryManifestResourceDefinition
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getResourceDefinitions)
        assert hints.get("return") == typing.List[BinaryManifestResourceDefinition]

        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.getSoftwareClusterId)
        assert hints.get("return") == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(CpSoftwareClusterBinaryManifestDescriptor.setSoftwareClusterId)
        assert hints.get("value") == typing.Optional[PositiveInteger]
        assert hints.get("return") is CpSoftwareClusterBinaryManifestDescriptor

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (setters carry the None no-op tail).
        """
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getCpSoftwareClusterRef.__doc__) == self.CP_SOFTWARE_CLUSTER_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.setCpSoftwareClusterRef.__doc__) == (
            self.CP_SOFTWARE_CLUSTER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing cpSoftwareClusterRef."
        )
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.createMetaDataField.__doc__) == self.META_DATA_FIELD_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getMetaDataFields.__doc__) == self.META_DATA_FIELD_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.createProvideResource.__doc__) == self.PROVIDE_RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getProvideResources.__doc__) == self.PROVIDE_RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.createRequireResource.__doc__) == self.REQUIRE_RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getRequireResources.__doc__) == self.REQUIRE_RESOURCE_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.createResourceDefinition.__doc__) == self.RESOURCE_DEFINITION_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getResourceDefinitions.__doc__) == self.RESOURCE_DEFINITION_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.getSoftwareClusterId.__doc__) == self.SOFTWARE_CLUSTER_ID_NOTE
        assert inspect.cleandoc(CpSoftwareClusterBinaryManifestDescriptor.setSoftwareClusterId.__doc__) == (
            self.SOFTWARE_CLUSTER_ID_NOTE + "\n\nA None value is a no-op and does not overwrite an existing softwareClusterId."
        )

    def test_get_set_cp_software_cluster_ref(self):
        """
        Test setCpSoftwareClusterRef round-trips and ignores None.
        """
        obj = self._create_descriptor()

        ref = RefType().setValue("/Cluster/Cluster1").setDest("CP-SOFTWARE-CLUSTER")
        result = obj.setCpSoftwareClusterRef(ref)
        assert result is obj
        assert obj.getCpSoftwareClusterRef() is ref
        assert obj.getCpSoftwareClusterRef().getValue() == "/Cluster/Cluster1"
        assert obj.getCpSoftwareClusterRef().getDest() == "CP-SOFTWARE-CLUSTER"

        result = obj.setCpSoftwareClusterRef(None)
        assert result is obj
        assert obj.getCpSoftwareClusterRef() is ref

    def test_create_meta_data_field(self):
        """
        Test createMetaDataField registers the child and duplicate-protects by type.
        """
        obj = self._create_descriptor()
        field = obj.createMetaDataField("Field1")
        assert isinstance(field, BinaryManifestMetaDataField)
        assert field.getParent() is obj
        assert obj.getMetaDataFields() == [field]

        same = obj.createMetaDataField("Field1")
        assert same is field
        assert obj.getMetaDataFields() == [field]

    def test_create_provide_resource(self):
        """
        Test createProvideResource registers the child and duplicate-protects by type.
        """
        obj = self._create_descriptor()
        resource = obj.createProvideResource("Provide1")
        assert isinstance(resource, BinaryManifestProvideResource)
        assert resource.getParent() is obj
        assert obj.getProvideResources() == [resource]

        same = obj.createProvideResource("Provide1")
        assert same is resource
        assert obj.getProvideResources() == [resource]

    def test_create_require_resource(self):
        """
        Test createRequireResource registers the child and duplicate-protects by type.
        """
        obj = self._create_descriptor()
        resource = obj.createRequireResource("Require1")
        assert isinstance(resource, BinaryManifestRequireResource)
        assert resource.getParent() is obj
        assert obj.getRequireResources() == [resource]

        same = obj.createRequireResource("Require1")
        assert same is resource
        assert obj.getRequireResources() == [resource]

    def test_create_resource_definition(self):
        """
        Test createResourceDefinition registers the child and duplicate-protects by type.
        """
        obj = self._create_descriptor()
        definition = obj.createResourceDefinition("Definition1")
        assert isinstance(definition, BinaryManifestResourceDefinition)
        assert definition.getParent() is obj
        assert obj.getResourceDefinitions() == [definition]

        same = obj.createResourceDefinition("Definition1")
        assert same is definition
        assert obj.getResourceDefinitions() == [definition]

    def test_get_set_software_cluster_id(self):
        """
        Test setSoftwareClusterId round-trips and ignores None.
        """
        obj = self._create_descriptor()

        value = PositiveInteger().setValue(5)
        result = obj.setSoftwareClusterId(value)
        assert result is obj
        assert obj.getSoftwareClusterId() is value
        assert obj.getSoftwareClusterId().getValue() == 5

        result = obj.setSoftwareClusterId(None)
        assert result is obj
        assert obj.getSoftwareClusterId() is value

    def test_arpackage_create_factory(self):
        """
        Test the ARPackage.createCpSoftwareClusterBinaryManifestDescriptor factory
        registers the element and duplicate-protects by type.
        """
        package = ARPackage(None, "Package1")
        descriptor = package.createCpSoftwareClusterBinaryManifestDescriptor("Manifest1")
        assert isinstance(descriptor, CpSoftwareClusterBinaryManifestDescriptor)
        assert descriptor.getParent() is package

        same = package.createCpSoftwareClusterBinaryManifestDescriptor("Manifest1")
        assert same is descriptor
