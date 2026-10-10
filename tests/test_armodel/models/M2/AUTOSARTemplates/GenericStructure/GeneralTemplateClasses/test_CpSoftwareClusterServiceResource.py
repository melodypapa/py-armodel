"""
This module contains tests for the CpSoftwareClusterServiceResource class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.Identifiable module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.14, p.904
"""

import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    CpSoftwareClusterResource,
    CpSoftwareClusterServiceResource,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


class TestCpSoftwareClusterServiceResource:
    """
    Test class for CpSoftwareClusterServiceResource functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.14, p.904
    """

    CLASS_NOTE = "Represents a single resource required or provided by a CP Software Cluster which relates to the BSW."
    RESOURCE_NEEDS_NOTE = "Refernce(s) to one or multiple EcucContainerValue(s) qualifying the characteristics of the resource."

    def _create_resource(self) -> CpSoftwareClusterServiceResource:
        return CpSoftwareClusterServiceResource(None, "ServiceResource1")

    def test_is_cp_software_cluster_resource_subclass(self):
        """
        Test that CpSoftwareClusterServiceResource derives from CpSoftwareClusterResource per the Table 11.14 Base row.
        """
        assert issubclass(CpSoftwareClusterServiceResource, CpSoftwareClusterResource)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(CpSoftwareClusterServiceResource.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert CpSoftwareClusterServiceResource.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.14 displayed row order
        (the adder first on the multi row, getter last).
        """
        methods = [name for name, value in CpSoftwareClusterServiceResource.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "addResourceNeedsRef",
            "getResourceNeedsRefs",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_resource()

        assert obj.getShortName() == "ServiceResource1"
        assert obj.getResourceNeedsRefs() == []

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types.
        """
        hints = typing.get_type_hints(CpSoftwareClusterServiceResource.addResourceNeedsRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is CpSoftwareClusterServiceResource
        hints = typing.get_type_hints(CpSoftwareClusterServiceResource.getResourceNeedsRefs)
        assert hints.get("return") == typing.List[RefType]

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (the adder carries the None no-op tail).
        """
        assert inspect.cleandoc(CpSoftwareClusterServiceResource.addResourceNeedsRef.__doc__) == (self.RESOURCE_NEEDS_NOTE + "\n\nA None value is a no-op and does not append to resourceNeedsRefs.")
        assert inspect.cleandoc(CpSoftwareClusterServiceResource.getResourceNeedsRefs.__doc__) == self.RESOURCE_NEEDS_NOTE

    def test_add_resource_needs_ref(self):
        """
        Test addResourceNeedsRef appends, returns self and ignores None.
        """
        obj = self._create_resource()

        ref = RefType().setValue("/Config/Container1").setDest("ECUC-CONTAINER-VALUE")
        result = obj.addResourceNeedsRef(ref)
        assert result is obj
        assert obj.getResourceNeedsRefs() == [ref]
        assert obj.getResourceNeedsRefs()[0].getValue() == "/Config/Container1"
        assert obj.getResourceNeedsRefs()[0].getDest() == "ECUC-CONTAINER-VALUE"

        result = obj.addResourceNeedsRef(None)
        assert result is obj
        assert obj.getResourceNeedsRefs() == [ref]

        second = RefType().setValue("/Config/Container2").setDest("ECUC-CONTAINER-VALUE")
        obj.addResourceNeedsRef(second)
        assert obj.getResourceNeedsRefs() == [ref, second]
