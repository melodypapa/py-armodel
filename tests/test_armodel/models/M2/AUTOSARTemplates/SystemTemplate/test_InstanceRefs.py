from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.InstanceRefs import (
    ComponentInSystemInstanceRef,
    OperationInSystemInstanceRef,
    PortGroupInSystemInstanceRef,
    VariableDataPrototypeInSystemInstanceRef,
)

# Post-table paragraph of Table B.1 (AUTOSAR_CP_TPS_SystemTemplate, p.1000), verbatim;
# markdown word-split "PortPrototype s" corrected against the sibling Table B.2 wording.
CISIR_NOTE = (
    "If the referenced SwComponentPrototype is located within the RootSwCompositionPrototype of a System then the "
    "contextComposition to the RootSwCompositionPrototype shall be provided. In this scenario we have a System "
    "Extract where the RootSwComposition may contain other compositions. If the referenced SwComponentPrototype is "
    "the RootSwCompositionPrototype itself then contextComposition reference to the RootSwCompositionPrototype shall "
    "be skipped and only the targetComponent to the RootSwCompositionPrototype shall be used. In this scenario we "
    "have an Ecu Extract where the RootSwComposition contains PortPrototypes that describe the external communication."
)

# Post-table paragraph of Table B.3 (AUTOSAR_CP_TPS_SystemTemplate, p.1004), verbatim;
# markdown word-splits ("PortPrototype s", "contextComponent .") corrected against the
# sibling Table B.2 wording.
VDPIR_NOTE = (
    "If the referenced VariableDataPrototype is part of a PortInterface of a SwComponentPrototype that is located "
    "within the RootSwCompositionPrototype then the contextComposition reference to the RootSwCompositionPrototype "
    "shall be provided. In this scenario we have a System Extract where the RootSwComposition may contain other "
    "compositions. If the referenced VariableDataPrototype is part of a PortInterface of the RootSwCompositionPrototype "
    "itself then the contextComposition reference to the RootSwCompositionPrototype shall be skipped and the "
    "RootSwCompositionPrototype shall be referenced as contextComponent. In this scenario we have an Ecu Extract where "
    "the RootSwComposition contains PortPrototypes that describe the external communication.\n"
    "\n"
    "Please note that the xml.sequenceOffset is not set for this InstanceRef and therefore the properties are "
    "serialized in an alphabetical order."
)


def _norm(doc):
    return " ".join(doc.split())


class Test_InstanceRefs:
    """Test cases for InstanceRefs-related classes."""

    def test_VariableDataPrototypeInSystemInstanceRef_initialization(self):
        """Test VariableDataPrototypeInSystemInstanceRef default values (Table B.3)."""
        ref = VariableDataPrototypeInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)

        assert ref.getBaseRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextCompositionRef() is None
        assert ref.getContextPortRef() is None
        assert ref.getTargetDataPrototypeRef() is None

    def test_VariableDataPrototypeInSystemInstanceRef_get_set(self):
        """Test VariableDataPrototypeInSystemInstanceRef setter/getter round-trips and chaining."""
        ref = VariableDataPrototypeInSystemInstanceRef()

        assert ref.setBaseRef("mock_base_ref") is ref
        assert ref.getBaseRef() == "mock_base_ref"

        assert ref.setContextCompositionRef("mock_context_comp_ref") is ref
        assert ref.getContextCompositionRef() == "mock_context_comp_ref"

        assert ref.setContextPortRef("mock_context_port_ref") is ref
        assert ref.getContextPortRef() == "mock_context_port_ref"

        assert ref.setTargetDataPrototypeRef("mock_target_ref") is ref
        assert ref.getTargetDataPrototypeRef() == "mock_target_ref"

    def test_VariableDataPrototypeInSystemInstanceRef_add_context_component_refs(self):
        """Test VariableDataPrototypeInSystemInstanceRef context component ref aggregation."""
        ref = VariableDataPrototypeInSystemInstanceRef()

        assert ref.addContextComponentRef("comp1") is ref
        assert ref.addContextComponentRef("comp2") is ref
        assert ref.getContextComponentRefs() == ["comp1", "comp2"]

    def test_VariableDataPrototypeInSystemInstanceRef_none_noop(self):
        """None is a no-op for all mutators of VariableDataPrototypeInSystemInstanceRef."""
        ref = VariableDataPrototypeInSystemInstanceRef()
        ref.setBaseRef("keep")
        ref.setContextCompositionRef("keep")
        ref.setContextPortRef("keep")
        ref.setTargetDataPrototypeRef("keep")

        ref.setBaseRef(None)
        ref.setContextCompositionRef(None)
        ref.setContextPortRef(None)
        ref.setTargetDataPrototypeRef(None)
        ref.addContextComponentRef(None)

        assert ref.getBaseRef() == "keep"
        assert ref.getContextCompositionRef() == "keep"
        assert ref.getContextPortRef() == "keep"
        assert ref.getTargetDataPrototypeRef() == "keep"
        assert ref.getContextComponentRefs() == []

    def test_VariableDataPrototypeInSystemInstanceRef_docstring(self):
        """Class docstring is the Table B.3 post-table text verbatim; base Note on accessors."""
        doc_lines = [line.strip() for line in VariableDataPrototypeInSystemInstanceRef.__doc__.strip().splitlines()]
        assert "\n".join(doc_lines) == VDPIR_NOTE
        assert VariableDataPrototypeInSystemInstanceRef.__init__.__doc__ is None

        assert _norm(VariableDataPrototypeInSystemInstanceRef.getBaseRef.__doc__) == "Stereotypes: atpDerived"
        assert _norm(VariableDataPrototypeInSystemInstanceRef.setBaseRef.__doc__) == ("Stereotypes: atpDerived A None value is a no-op and does not overwrite an existing baseRef.")
        # Table B.3 leaves the contextComponent/contextComposition/contextPort/targetDataPrototype
        # Note cells empty - the accessors stay docstring-free.
        assert VariableDataPrototypeInSystemInstanceRef.getContextPortRef.__doc__ is None
        assert VariableDataPrototypeInSystemInstanceRef.setTargetDataPrototypeRef.__doc__ is None

    def test_ComponentInSystemInstanceRef_initialization(self):
        """Test ComponentInSystemInstanceRef default values (Table B.1)."""
        ref = ComponentInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)

        assert ref.getBaseRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextCompositionRef() is None
        assert ref.getTargetComponentRef() is None

    def test_ComponentInSystemInstanceRef_get_set(self):
        """Test ComponentInSystemInstanceRef setter/getter round-trips and chaining."""
        ref = ComponentInSystemInstanceRef()

        assert ref.setBaseRef("mock_base_ref") is ref
        assert ref.getBaseRef() == "mock_base_ref"

        assert ref.setContextCompositionRef("mock_context_comp_ref") is ref
        assert ref.getContextCompositionRef() == "mock_context_comp_ref"

        assert ref.setTargetComponentRef("mock_target_comp_ref") is ref
        assert ref.getTargetComponentRef() == "mock_target_comp_ref"

    def test_ComponentInSystemInstanceRef_add_context_component_refs(self):
        """Test ComponentInSystemInstanceRef context component ref aggregation."""
        ref = ComponentInSystemInstanceRef()

        assert ref.addContextComponentRef("comp1") is ref
        assert ref.addContextComponentRef("comp2") is ref
        assert ref.getContextComponentRefs() == ["comp1", "comp2"]

    def test_ComponentInSystemInstanceRef_none_noop(self):
        """None is a no-op for all mutators of ComponentInSystemInstanceRef."""
        ref = ComponentInSystemInstanceRef()
        ref.setBaseRef("keep")
        ref.setContextCompositionRef("keep")
        ref.setTargetComponentRef("keep")

        ref.setBaseRef(None)
        ref.setContextCompositionRef(None)
        ref.setTargetComponentRef(None)
        ref.addContextComponentRef(None)

        assert ref.getBaseRef() == "keep"
        assert ref.getContextCompositionRef() == "keep"
        assert ref.getTargetComponentRef() == "keep"
        assert ref.getContextComponentRefs() == []

    def test_ComponentInSystemInstanceRef_docstring(self):
        """Class docstring is the Table B.1 post-table paragraph verbatim; member Notes on accessors."""
        assert ComponentInSystemInstanceRef.__doc__.strip() == CISIR_NOTE
        assert ComponentInSystemInstanceRef.__init__.__doc__ is None

        assert _norm(ComponentInSystemInstanceRef.getBaseRef.__doc__) == "Stereotypes: atpDerived Tags: xml.sequenceOffset=10"
        assert _norm(ComponentInSystemInstanceRef.setBaseRef.__doc__) == ("Stereotypes: atpDerived Tags: xml.sequenceOffset=10 A None value is a no-op and does not overwrite an existing baseRef.")
        assert _norm(ComponentInSystemInstanceRef.getContextComponentRefs.__doc__) == "Tags: xml.sequenceOffset=30"
        assert _norm(ComponentInSystemInstanceRef.addContextComponentRef.__doc__) == ("Tags: xml.sequenceOffset=30 A None value is a no-op and does not append anything.")
        assert _norm(ComponentInSystemInstanceRef.getContextCompositionRef.__doc__) == "Tags: xml.sequenceOffset=20"
        assert _norm(ComponentInSystemInstanceRef.setContextCompositionRef.__doc__) == ("Tags: xml.sequenceOffset=20 A None value is a no-op and does not overwrite an existing contextCompositionRef.")
        assert _norm(ComponentInSystemInstanceRef.getTargetComponentRef.__doc__) == "Tags: xml.sequenceOffset=40"
        assert _norm(ComponentInSystemInstanceRef.setTargetComponentRef.__doc__) == ("Tags: xml.sequenceOffset=40 A None value is a no-op and does not overwrite an existing targetComponentRef.")

    def test_OperationInSystemInstanceRef_initialization(self):
        """Test OperationInSystemInstanceRef default values."""
        ref = OperationInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)

        assert ref.getBaseRef() is None
        assert ref.getContextCompositionRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextPortRef() is None
        assert ref.getTargetOperationRef() is None

    def test_OperationInSystemInstanceRef_get_set(self):
        """Test OperationInSystemInstanceRef setter/getter methods."""
        ref = OperationInSystemInstanceRef()

        mock_base_ref = "mock_base_ref"
        ref.setBaseRef(mock_base_ref)
        assert ref.getBaseRef() == mock_base_ref

        mock_context_composition_ref = "mock_context_composition_ref"
        ref.setContextCompositionRef(mock_context_composition_ref)
        assert ref.getContextCompositionRef() == mock_context_composition_ref

        mock_context_port_ref = "mock_context_port_ref"
        ref.setContextPortRef(mock_context_port_ref)
        assert ref.getContextPortRef() == mock_context_port_ref

        mock_target_operation_ref = "mock_target_operation_ref"
        ref.setTargetOperationRef(mock_target_operation_ref)
        assert ref.getTargetOperationRef() == mock_target_operation_ref

    def test_OperationInSystemInstanceRef_add_context_component_refs(self):
        """Test OperationInSystemInstanceRef context component ref aggregation."""
        ref = OperationInSystemInstanceRef()

        mock_comp_ref1 = "comp1"
        mock_comp_ref2 = "comp2"
        ref.addContextComponentRef(mock_comp_ref1)
        ref.addContextComponentRef(mock_comp_ref2)
        assert ref.getContextComponentRefs() == [mock_comp_ref1, mock_comp_ref2]

    def test_OperationInSystemInstanceRef_none_noop(self):
        """None is a no-op for all mutators of OperationInSystemInstanceRef."""
        ref = OperationInSystemInstanceRef()

        ref.setBaseRef(None)
        ref.setContextCompositionRef(None)
        ref.setContextPortRef(None)
        ref.setTargetOperationRef(None)
        ref.addContextComponentRef(None)

        assert ref.getBaseRef() is None
        assert ref.getContextCompositionRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getContextPortRef() is None
        assert ref.getTargetOperationRef() is None

    def test_PortGroupInSystemInstanceRef_initialization(self):
        """Test PortGroupInSystemInstanceRef default values."""
        ref = PortGroupInSystemInstanceRef()

        assert isinstance(ref, AtpInstanceRef)

        assert ref.getBaseRef() is None
        assert ref.getContextCompositionRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getTargetRef() is None

    def test_PortGroupInSystemInstanceRef_get_set(self):
        """Test PortGroupInSystemInstanceRef setter/getter methods."""
        ref = PortGroupInSystemInstanceRef()

        mock_base_ref = "mock_base_ref"
        ref.setBaseRef(mock_base_ref)
        assert ref.getBaseRef() == mock_base_ref

        mock_context_composition_ref = "mock_context_composition_ref"
        ref.setContextCompositionRef(mock_context_composition_ref)
        assert ref.getContextCompositionRef() == mock_context_composition_ref

        mock_target_ref = "mock_target_ref"
        ref.setTargetRef(mock_target_ref)
        assert ref.getTargetRef() == mock_target_ref

    def test_PortGroupInSystemInstanceRef_add_context_component_refs(self):
        """Test PortGroupInSystemInstanceRef context component ref aggregation."""
        ref = PortGroupInSystemInstanceRef()

        mock_comp_ref1 = "comp1"
        mock_comp_ref2 = "comp2"
        ref.addContextComponentRef(mock_comp_ref1)
        ref.addContextComponentRef(mock_comp_ref2)
        assert ref.getContextComponentRefs() == [mock_comp_ref1, mock_comp_ref2]

    def test_PortGroupInSystemInstanceRef_none_noop(self):
        """None is a no-op for all mutators of PortGroupInSystemInstanceRef."""
        ref = PortGroupInSystemInstanceRef()

        ref.setBaseRef(None)
        ref.setContextCompositionRef(None)
        ref.setTargetRef(None)
        ref.addContextComponentRef(None)

        assert ref.getBaseRef() is None
        assert ref.getContextCompositionRef() is None
        assert ref.getContextComponentRefs() == []
        assert ref.getTargetRef() is None
