"""
This module contains tests for the PortElementToCommunicationResourceMapping class in the
AUTOSAR GenericStructure.GeneralTemplateClasses.Identifiable module.

Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.15, p.905
"""

import inspect
import typing

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ModeDeclarationGroupPrototypeInSystemInstanceRef,
    OperationInSystemInstanceRef,
    ParameterDataPrototypeInSystemInstanceRef,
    TriggerInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)


class TestPortElementToCommunicationResourceMapping:
    """
    Test class for PortElementToCommunicationResourceMapping functionality.

    Spec: AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 11.15, p.905
    """

    CLASS_NOTE = "This meta class maps a communication resource to CP Software Clusters. In this case the kind of Port Prototype specified whether the Software Cluster has to provide or to require the resource."
    CLIENT_SERVER_OPERATION_NOTE = "ClientServerOperation instance qualifying the communication resource InstanceRef implemented by: OperationInSystemInstanceRef"
    COMMUNICATION_RESOURCE_NOTE = "Communication resource for which the mapping applies."
    MODE_DECLARATION_GROUP_PROTOTYPE_NOTE = "ModeDeclarationGroupPrototype instance qualifying the communication resource InstanceRef implemented by: ModeDeclarationGroupPrototypeInSystemInstanceRef"
    PARAMETER_DATA_PROTOTYPE_NOTE = "ParameterDataPrototype instance qualifying the communication resource. InstanceRef implemented by: ParameterDataPrototypeInSystemInstanceRef"
    TRIGGER_NOTE = "Trigger instance qualifying the communication resource. InstanceRef implemented by: TriggerInSystemInstanceRef"
    VARIABLE_DATA_PROTOTYPE_NOTE = "VariableDataPrototype instance qualifying the communication resource InstanceRef implemented by: VariableDataPrototypeInSystemInstanceRef"

    def _create_mapping(self) -> PortElementToCommunicationResourceMapping:
        return PortElementToCommunicationResourceMapping(None, "mapping1")

    def test_is_identifiable_subclass(self):
        """
        Test that PortElementToCommunicationResourceMapping derives from Identifiable per the Table 11.15 Base row.
        """
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable

        assert issubclass(PortElementToCommunicationResourceMapping, Identifiable)

    def test_class_docstring_is_spec_note_verbatim(self):
        """
        Test that the class docstring is the spec Note verbatim.
        """
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.__doc__) == self.CLASS_NOTE

    def test_init_has_no_docstring(self):
        """
        Test that __init__ carries no docstring.
        """
        assert PortElementToCommunicationResourceMapping.__init__.__doc__ is None

    def test_member_order_follows_spec_rows(self):
        """
        Test that the accessors follow the Table 11.15 displayed row order
        (getter then setter per row).
        """
        methods = [name for name, value in PortElementToCommunicationResourceMapping.__dict__.items() if callable(value) and not name.startswith("_")]
        assert methods == [
            "getClientServerOperationIRef",
            "setClientServerOperationIRef",
            "getCommunicationResourceRef",
            "setCommunicationResourceRef",
            "getModeDeclarationGroupPrototypeIRef",
            "setModeDeclarationGroupPrototypeIRef",
            "getParameterDataPrototypeIRef",
            "setParameterDataPrototypeIRef",
            "getTriggerIRef",
            "setTriggerIRef",
            "getVariableDataPrototypeIRef",
            "setVariableDataPrototypeIRef",
        ]

    def test_initialization_defaults(self):
        """
        Test that the instance initializes all attributes to their defaults.
        """
        obj = self._create_mapping()

        assert obj.getShortName() == "mapping1"
        assert obj.getClientServerOperationIRef() is None
        assert obj.getCommunicationResourceRef() is None
        assert obj.getModeDeclarationGroupPrototypeIRef() is None
        assert obj.getParameterDataPrototypeIRef() is None
        assert obj.getTriggerIRef() is None
        assert obj.getVariableDataPrototypeIRef() is None

    def test_annotations_are_optional_typed(self):
        """
        Test that the accessors carry the spec types. communicationResourceRef resolves
        at runtime (RefType is a same-package name); the InstanceRef member types are
        cross-package TYPE_CHECKING names in Identifiable.py (nothing pins them at
        runtime — DiagnosticDataElement.swDataDefProps precedent), so those annotations
        are pinned in raw string form.
        """
        hints = typing.get_type_hints(PortElementToCommunicationResourceMapping.getCommunicationResourceRef)
        assert hints.get("return") == typing.Optional[RefType]
        hints = typing.get_type_hints(PortElementToCommunicationResourceMapping.setCommunicationResourceRef)
        assert hints.get("value") == typing.Optional[RefType]
        assert hints.get("return") is PortElementToCommunicationResourceMapping

        assert PortElementToCommunicationResourceMapping.getClientServerOperationIRef.__annotations__["return"] == "Optional[OperationInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setClientServerOperationIRef.__annotations__["value"] == "Optional[OperationInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setClientServerOperationIRef.__annotations__["return"] == "PortElementToCommunicationResourceMapping"
        assert PortElementToCommunicationResourceMapping.getModeDeclarationGroupPrototypeIRef.__annotations__["return"] == "Optional[ModeDeclarationGroupPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setModeDeclarationGroupPrototypeIRef.__annotations__["value"] == "Optional[ModeDeclarationGroupPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setModeDeclarationGroupPrototypeIRef.__annotations__["return"] == "PortElementToCommunicationResourceMapping"
        assert PortElementToCommunicationResourceMapping.getParameterDataPrototypeIRef.__annotations__["return"] == "Optional[ParameterDataPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setParameterDataPrototypeIRef.__annotations__["value"] == "Optional[ParameterDataPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setParameterDataPrototypeIRef.__annotations__["return"] == "PortElementToCommunicationResourceMapping"
        assert PortElementToCommunicationResourceMapping.getTriggerIRef.__annotations__["return"] == "Optional[TriggerInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setTriggerIRef.__annotations__["value"] == "Optional[TriggerInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setTriggerIRef.__annotations__["return"] == "PortElementToCommunicationResourceMapping"
        assert PortElementToCommunicationResourceMapping.getVariableDataPrototypeIRef.__annotations__["return"] == "Optional[VariableDataPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setVariableDataPrototypeIRef.__annotations__["value"] == "Optional[VariableDataPrototypeInSystemInstanceRef]"
        assert PortElementToCommunicationResourceMapping.setVariableDataPrototypeIRef.__annotations__["return"] == "PortElementToCommunicationResourceMapping"

    def test_method_docstrings_are_spec_notes_verbatim(self):
        """
        Test that the accessor docstrings are the spec Notes verbatim
        (the setters carry the None no-op tail).
        """
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getClientServerOperationIRef.__doc__) == self.CLIENT_SERVER_OPERATION_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setClientServerOperationIRef.__doc__) == (
            self.CLIENT_SERVER_OPERATION_NOTE + "\n\nA None value is a no-op and does not overwrite an existing clientServerOperationIRef."
        )
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getCommunicationResourceRef.__doc__) == self.COMMUNICATION_RESOURCE_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setCommunicationResourceRef.__doc__) == (
            self.COMMUNICATION_RESOURCE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing communicationResourceRef."
        )
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getModeDeclarationGroupPrototypeIRef.__doc__) == self.MODE_DECLARATION_GROUP_PROTOTYPE_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setModeDeclarationGroupPrototypeIRef.__doc__) == (
            self.MODE_DECLARATION_GROUP_PROTOTYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing modeDeclarationGroupPrototypeIRef."
        )
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getParameterDataPrototypeIRef.__doc__) == self.PARAMETER_DATA_PROTOTYPE_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setParameterDataPrototypeIRef.__doc__) == (
            self.PARAMETER_DATA_PROTOTYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing parameterDataPrototypeIRef."
        )
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getTriggerIRef.__doc__) == self.TRIGGER_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setTriggerIRef.__doc__) == (self.TRIGGER_NOTE + "\n\nA None value is a no-op and does not overwrite an existing triggerIRef.")
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.getVariableDataPrototypeIRef.__doc__) == self.VARIABLE_DATA_PROTOTYPE_NOTE
        assert inspect.cleandoc(PortElementToCommunicationResourceMapping.setVariableDataPrototypeIRef.__doc__) == (
            self.VARIABLE_DATA_PROTOTYPE_NOTE + "\n\nA None value is a no-op and does not overwrite an existing variableDataPrototypeIRef."
        )

    def test_get_set_client_server_operation_i_ref(self):
        """
        Test setClientServerOperationIRef stores the instance reference and ignores None.
        """
        obj = self._create_mapping()

        instance_ref = OperationInSystemInstanceRef()
        result = obj.setClientServerOperationIRef(instance_ref)
        assert result is obj
        assert obj.getClientServerOperationIRef() is instance_ref

        obj.setClientServerOperationIRef(None)
        assert obj.getClientServerOperationIRef() is instance_ref

    def test_get_set_communication_resource_ref(self):
        """
        Test setCommunicationResourceRef stores the reference and ignores None.
        """
        obj = self._create_mapping()

        ref = RefType().setValue("/Resources/MyResource").setDest("CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE")
        result = obj.setCommunicationResourceRef(ref)
        assert result is obj
        assert obj.getCommunicationResourceRef() is ref
        assert obj.getCommunicationResourceRef().getValue() == "/Resources/MyResource"
        assert obj.getCommunicationResourceRef().getDest() == "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"

        obj.setCommunicationResourceRef(None)
        assert obj.getCommunicationResourceRef() is ref

    def test_get_set_mode_declaration_group_prototype_i_ref(self):
        """
        Test setModeDeclarationGroupPrototypeIRef stores the instance reference and ignores None.
        """
        obj = self._create_mapping()

        instance_ref = ModeDeclarationGroupPrototypeInSystemInstanceRef()
        result = obj.setModeDeclarationGroupPrototypeIRef(instance_ref)
        assert result is obj
        assert obj.getModeDeclarationGroupPrototypeIRef() is instance_ref

        obj.setModeDeclarationGroupPrototypeIRef(None)
        assert obj.getModeDeclarationGroupPrototypeIRef() is instance_ref

    def test_get_set_parameter_data_prototype_i_ref(self):
        """
        Test setParameterDataPrototypeIRef stores the instance reference and ignores None.
        """
        obj = self._create_mapping()

        instance_ref = ParameterDataPrototypeInSystemInstanceRef()
        result = obj.setParameterDataPrototypeIRef(instance_ref)
        assert result is obj
        assert obj.getParameterDataPrototypeIRef() is instance_ref

        obj.setParameterDataPrototypeIRef(None)
        assert obj.getParameterDataPrototypeIRef() is instance_ref

    def test_get_set_trigger_i_ref(self):
        """
        Test setTriggerIRef stores the instance reference and ignores None.
        """
        obj = self._create_mapping()

        instance_ref = TriggerInSystemInstanceRef()
        result = obj.setTriggerIRef(instance_ref)
        assert result is obj
        assert obj.getTriggerIRef() is instance_ref

        obj.setTriggerIRef(None)
        assert obj.getTriggerIRef() is instance_ref

    def test_get_set_variable_data_prototype_i_ref(self):
        """
        Test setVariableDataPrototypeIRef stores the instance reference and ignores None.
        """
        obj = self._create_mapping()

        instance_ref = VariableDataPrototypeInSystemInstanceRef()
        result = obj.setVariableDataPrototypeIRef(instance_ref)
        assert result is obj
        assert obj.getVariableDataPrototypeIRef() is instance_ref

        obj.setVariableDataPrototypeIRef(None)
        assert obj.getVariableDataPrototypeIRef() is instance_ref

    def test_created_via_parent_factories(self):
        """
        Test that both aggregators (CpSoftwareClusterMappingSet, SystemMapping) create
        PortElementToCommunicationResourceMapping instances (Table 11.15 Aggregated by row).
        """
        document = AUTOSAR.getInstance()
        document.setARRelease("R23-11")
        pkg = document.createARPackage("pkg")
        mapping_set = pkg.createCpSoftwareClusterMappingSet("mapping_set")

        mapping = mapping_set.createPortElementToComResourceMapping("port_mapping")
        assert isinstance(mapping, PortElementToCommunicationResourceMapping)
        assert mapping.getShortName() == "port_mapping"
        assert mapping_set.createPortElementToComResourceMapping("port_mapping") is mapping
