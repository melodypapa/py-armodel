import inspect
import typing

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean, Identifier, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import PortGroupInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping import PncMapping, PncMappingIdent


class TestPncMapping:
    """Test cases for PncMapping (Table 5.45, p.266)."""

    MEMBERS = [
        "dynamicPncMappingPduGroupRefs",
        "ident",
        "physicalChannelRefs",
        "pncConsumedProvidedServiceInstanceGroupRefs",
        "pncGroupRefs",
        "pncIdentifier",
        "pncPdurGroupRefs",
        "pncWakeupEnable",
        "relevantForDynamicPncMappingRefs",
        "shortLabel",
        "vfcIRefs",
        "wakeupFrameRefs",
    ]

    def test_inheritance(self):
        assert issubclass(PncMapping, Describable)

    def test_instantiable(self):
        PncMapping()

    def test_class_docstring_note(self):
        expected = "Describes a mapping between one or several Virtual Function Clusters onto Partial Network Clusters. A Virtual Function Cluster is realized by a PortGroup. A Partial Network Cluster is realized by one or more IPduGroups."
        assert inspect.cleandoc(PncMapping.__doc__) == expected

    def test_init_has_no_docstring(self):
        assert PncMapping.__init__.__doc__ is None

    def test_initialization_defaults(self):
        mapping = PncMapping()
        assert mapping.getDynamicPncMappingPduGroupRefs() == []
        assert mapping.getIdent() is None
        assert mapping.getPhysicalChannelRefs() == []
        assert mapping.getPncConsumedProvidedServiceInstanceGroupRefs() == []
        assert mapping.getPncGroupRefs() == []
        assert mapping.getPncIdentifier() is None
        assert mapping.getPncPdurGroupRefs() == []
        assert mapping.getPncWakeupEnable() is None
        assert mapping.getRelevantForDynamicPncMappingRefs() == []
        assert mapping.getShortLabel() is None
        assert mapping.getVfcIRefs() == []
        assert mapping.getWakeupFrameRefs() == []

    def test_member_order(self):
        mapping = PncMapping()
        members = [k for k in vars(mapping) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_create_ident(self):
        mapping = PncMapping()
        ident = mapping.createIdent("PncIdent")
        assert isinstance(ident, PncMappingIdent)
        assert ident.getShortName() == "PncIdent"
        assert mapping.getIdent() is ident
        duplicate = mapping.createIdent("PncIdent")
        assert duplicate is ident

    def test_add_dynamic_pnc_mapping_pdu_group_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Groups/Group1")
        result = mapping.addDynamicPncMappingPduGroupRef(ref1)
        assert result is mapping
        mapping.addDynamicPncMappingPduGroupRef(None)
        assert mapping.getDynamicPncMappingPduGroupRefs() == [ref1]

    def test_add_physical_channel_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Topology/Can1")
        mapping.addPhysicalChannelRef(ref1)
        assert mapping.getPhysicalChannelRefs() == [ref1]

    def test_add_pnc_consumed_provided_service_instance_group_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/ServiceInstances/Group1")
        mapping.addPncConsumedProvidedServiceInstanceGroupRef(ref1)
        assert mapping.getPncConsumedProvidedServiceInstanceGroupRefs() == [ref1]

    def test_add_pnc_group_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Groups/PncGroup1")
        mapping.addPncGroupRef(ref1)
        assert mapping.getPncGroupRefs() == [ref1]

    def test_get_set_pnc_identifier(self):
        mapping = PncMapping()
        value = PositiveInteger()
        value.setValue("8")
        result = mapping.setPncIdentifier(value)
        assert result is mapping
        assert mapping.getPncIdentifier() is value
        mapping.setPncIdentifier(None)
        assert mapping.getPncIdentifier() is value

    def test_add_pnc_pdur_group_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Groups/PdurGroup1")
        mapping.addPncPdurGroupRef(ref1)
        assert mapping.getPncPdurGroupRefs() == [ref1]

    def test_get_set_pnc_wakeup_enable(self):
        mapping = PncMapping()
        value = Boolean()
        value.setValue(True)
        result = mapping.setPncWakeupEnable(value)
        assert result is mapping
        assert mapping.getPncWakeupEnable() is value
        mapping.setPncWakeupEnable(None)
        assert mapping.getPncWakeupEnable() is value

    def test_add_relevant_for_dynamic_pnc_mapping_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Ecu/Gateway1")
        mapping.addRelevantForDynamicPncMappingRef(ref1)
        assert mapping.getRelevantForDynamicPncMappingRefs() == [ref1]

    def test_get_set_short_label(self):
        mapping = PncMapping()
        value = Identifier()
        value.setValue("PNC_1")
        result = mapping.setShortLabel(value)
        assert result is mapping
        assert mapping.getShortLabel() is value
        mapping.setShortLabel(None)
        assert mapping.getShortLabel() is value

    def test_add_vfc_iref(self):
        mapping = PncMapping()
        iref1 = PortGroupInSystemInstanceRef()
        result = mapping.addVfcIRef(iref1)
        assert result is mapping
        mapping.addVfcIRef(None)
        assert mapping.getVfcIRefs() == [iref1]

    def test_add_wakeup_frame_ref(self):
        mapping = PncMapping()
        ref1 = RefType()
        ref1.setValue("/Frames/Frame1")
        mapping.addWakeupFrameRef(ref1)
        assert mapping.getWakeupFrameRefs() == [ref1]

    def test_type_hints(self):
        hints = typing.get_type_hints(PncMapping.getDynamicPncMappingPduGroupRefs)
        assert hints["return"] == typing.List[RefType]
        hints = typing.get_type_hints(PncMapping.getIdent)
        assert hints["return"] == typing.Optional[PncMappingIdent]
        hints = typing.get_type_hints(PncMapping.createIdent)
        assert hints["return"] is PncMappingIdent
        hints = typing.get_type_hints(PncMapping.getPncIdentifier)
        assert hints["return"] == typing.Optional[PositiveInteger]
        hints = typing.get_type_hints(PncMapping.getPncWakeupEnable)
        assert hints["return"] == typing.Optional[Boolean]
        hints = typing.get_type_hints(PncMapping.getShortLabel)
        assert hints["return"] == typing.Optional[Identifier]
        hints = typing.get_type_hints(PncMapping.getVfcIRefs)
        assert hints["return"] == typing.List[PortGroupInSystemInstanceRef]
        hints = typing.get_type_hints(PncMapping.getWakeupFrameRefs)
        assert hints["return"] == typing.List[RefType]
