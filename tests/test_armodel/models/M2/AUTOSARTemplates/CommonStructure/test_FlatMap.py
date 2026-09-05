from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap import AliasNameAssignment, AliasNameSet, FlatInstanceDescriptor, FlatMap, RtePluginProps
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARElement, PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Identifier, RefType, String
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.VariationPointCapable import VariationPointCapable
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultilanguageLongName


class TestFlatInstanceDescriptor:
    CLASS_NOTE = (
        "Represents exactly one node (e.g. a component instance or data element) of the instance tree of a software system. "
        "The purpose of this element is to map the various nested representations of this instance to a flat representation and assign a unique name (shortName) to it. "
        "Use cases: • Specify unique names of measurable data to be used by MCD tools • Specify unique names of calibration data to be used by MCD tool • "
        "Specify a unique name for an instance of a component prototype in the ECU extract of the system description Note that in addition it is possible to assign alias names via AliasNameAssignment."
    )

    def test_initialization(self):
        """Test FlatInstanceDescriptor initialization"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        assert flat_instance is not None
        assert flat_instance.getShortName() == "TestInstance"
        assert flat_instance.ecuExtractReferenceIRef is None
        assert flat_instance.role is None
        assert flat_instance.rtePluginProps is None
        assert flat_instance.swDataDefProps is None
        assert flat_instance.upstreamReferenceIRef is None

    def test_heritage(self):
        """Test FlatInstanceDescriptor heritage: direct bases Identifiable + VariationPointCapable (Table 14.2 Base chain, Rule 0020 VP-capable)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        assert FlatInstanceDescriptor.__bases__ == (Identifiable, VariationPointCapable)
        assert isinstance(flat_instance, Identifiable)
        assert isinstance(flat_instance, VariationPointCapable)

    def test_verbatim_class_docstring(self):
        """Test the class docstring is the spec Note verbatim (Table 14.2, wrap-normalised)"""
        assert FlatInstanceDescriptor.__doc__.strip() == TestFlatInstanceDescriptor.CLASS_NOTE

    def test_get_set_ecu_extract_reference_iref(self):
        """Test getEcuExtractReferenceIRef/setEcuExtractReferenceIRef (chaining, round-trip, None no-op)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        test_value = AnyInstanceRef()
        result = flat_instance.setEcuExtractReferenceIRef(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getEcuExtractReferenceIRef() == test_value

        flat_instance.setEcuExtractReferenceIRef(None)  # No-op
        assert flat_instance.getEcuExtractReferenceIRef() == test_value

    def test_get_set_role(self):
        """Test getRole/setRole (chaining, round-trip, None no-op)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        test_value = Identifier().setValue("TestRole")
        result = flat_instance.setRole(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getRole() == test_value

        flat_instance.setRole(None)  # No-op
        assert flat_instance.getRole() == test_value

    def test_get_set_rte_plugin_props(self):
        """Test getRtePluginProps/setRtePluginProps (chaining, round-trip, None no-op)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        test_value = RtePluginProps()
        result = flat_instance.setRtePluginProps(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getRtePluginProps() == test_value

        flat_instance.setRtePluginProps(None)  # No-op
        assert flat_instance.getRtePluginProps() == test_value

    def test_get_set_sw_data_def_props(self):
        """Test getSwDataDefProps/setSwDataDefProps (chaining, round-trip, None no-op)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        test_value = SwDataDefProps()
        result = flat_instance.setSwDataDefProps(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getSwDataDefProps() == test_value

        flat_instance.setSwDataDefProps(None)  # No-op
        assert flat_instance.getSwDataDefProps() == test_value

    def test_get_set_upstream_reference_iref(self):
        """Test getUpstreamReferenceIRef/setUpstreamReferenceIRef (chaining, round-trip, None no-op)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_instance = FlatInstanceDescriptor(ar_root, "TestInstance")

        test_value = AnyInstanceRef()
        result = flat_instance.setUpstreamReferenceIRef(test_value)
        assert result is flat_instance  # Method chaining
        assert flat_instance.getUpstreamReferenceIRef() == test_value

        flat_instance.setUpstreamReferenceIRef(None)  # No-op
        assert flat_instance.getUpstreamReferenceIRef() == test_value


class TestAliasNameAssignment:
    def test_initialization(self):
        """Test AliasNameAssignment initialization"""
        assignment = AliasNameAssignment()

        assert assignment.shortLabel is None
        assert assignment.label is None
        assert assignment.identifiableRef is None
        assert assignment.flatInstanceRef is None

    def test_get_set_short_label(self):
        """Test getShortLabel/setShortLabel (chaining, round-trip, None no-op)"""
        assignment = AliasNameAssignment()

        value = String().setValue("aliasName")
        result = assignment.setShortLabel(value)
        assert result is assignment  # Method chaining
        assert assignment.getShortLabel() == value

        assignment.setShortLabel(None)  # No-op
        assert assignment.getShortLabel() == value

    def test_get_set_label(self):
        """Test getLabel/setLabel (chaining, round-trip, None no-op)"""
        assignment = AliasNameAssignment()

        value = MultilanguageLongName()
        result = assignment.setLabel(value)
        assert result is assignment  # Method chaining
        assert assignment.getLabel() == value

        assignment.setLabel(None)  # No-op
        assert assignment.getLabel() == value

    def test_get_set_identifiable_ref(self):
        """Test getIdentifiableRef/setIdentifiableRef (chaining, round-trip, None no-op)"""
        assignment = AliasNameAssignment()

        value = RefType().setValue("/IdentifiableRef")
        result = assignment.setIdentifiableRef(value)
        assert result is assignment  # Method chaining
        assert assignment.getIdentifiableRef() == value

        assignment.setIdentifiableRef(None)  # No-op
        assert assignment.getIdentifiableRef() == value

    def test_get_set_flat_instance_ref(self):
        """Test getFlatInstanceRef/setFlatInstanceRef (chaining, round-trip, None no-op)"""
        assignment = AliasNameAssignment()

        value = RefType().setValue("/FlatInstanceRef")
        result = assignment.setFlatInstanceRef(value)
        assert result is assignment  # Method chaining
        assert assignment.getFlatInstanceRef() == value

        assignment.setFlatInstanceRef(None)  # No-op
        assert assignment.getFlatInstanceRef() == value


class TestAliasNameSet:
    def test_initialization(self):
        """Test AliasNameSet initialization"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        alias_set = AliasNameSet(ar_root, "TestAliasNameSet")

        assert alias_set is not None
        assert alias_set.getShortName() == "TestAliasNameSet"
        assert alias_set.getAliasNames() == []

    def test_add_alias_name(self):
        """Test addAliasName method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        alias_set = AliasNameSet(ar_root, "TestAliasNameSet")

        assignment = AliasNameAssignment()
        result = alias_set.addAliasName(assignment)
        assert result is alias_set  # Method chaining
        assert len(alias_set.getAliasNames()) == 1
        assert alias_set.getAliasNames()[0] == assignment

    def test_add_alias_name_none_noop(self):
        """Test that addAliasName(None) is a no-op"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        alias_set = AliasNameSet(ar_root, "TestAliasNameSet")

        alias_set.addAliasName(AliasNameAssignment())
        alias_set.addAliasName(None)  # Should not append
        assert len(alias_set.getAliasNames()) == 1

    def test_get_alias_names_empty(self):
        """Test getAliasNames returns empty list by default"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        alias_set = AliasNameSet(ar_root, "TestAliasNameSet")

        assert alias_set.getAliasNames() == []


class TestFlatMap:
    CLASS_NOTE = (
        "Contains a flat list of references to software objects. This list is used to identify instances and to resolve name conflicts. "
        "The scope is given by the RootSwCompositionPrototype for which it is used, i.e. it can be applied to a system, system extract or ECU-extract. "
        "An instance of FlatMap may also be used in a preliminary context, e.g. in the scope of a software component before integration into a system. "
        "In this case it is not referred by a RootSwCompositionPrototype."
    )

    def test_initialization(self):
        """Test FlatMap initialization"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        assert flat_map is not None
        assert flat_map.getShortName() == "TestFlatMap"
        assert flat_map.instances == []

    def test_heritage(self):
        """Test FlatMap heritage: direct base ARElement (Table 14.1 Base chain, most-derived; VP-capable via PackageableElement, Rule 0020)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        assert FlatMap.__bases__ == (ARElement,)
        assert isinstance(flat_map, ARElement)
        assert isinstance(flat_map, PackageableElement)
        assert isinstance(flat_map, CollectableElement)
        assert isinstance(flat_map, Identifiable)
        assert isinstance(flat_map, VariationPointCapable)

    def test_verbatim_class_docstring(self):
        """Test the class docstring is the spec Note verbatim (Table 14.1, wrap-normalised)"""
        assert FlatMap.__doc__.strip() == TestFlatMap.CLASS_NOTE

    def test_create_flat_instance_descriptor(self):
        """Test createFlatInstanceDescriptor method"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        instance = flat_map.createFlatInstanceDescriptor("TestInstance")
        assert instance is not None
        assert instance.getShortName() == "TestInstance"
        assert len(flat_map.instances) == 1
        assert flat_map.instances[0] == instance

    def test_create_flat_instance_descriptor_duplicate(self):
        """Test createFlatInstanceDescriptor with duplicate name"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        instance1 = flat_map.createFlatInstanceDescriptor("TestInstance")
        instance2 = flat_map.createFlatInstanceDescriptor("TestInstance")  # Should return the same instance
        assert instance1 is instance2

    def test_get_instances_empty(self):
        """Test getInstances method with empty list"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        instances = flat_map.getInstances()
        assert instances == []

    def test_get_instances(self):
        """Test getInstances returns the dedicated field in insertion order (Rule 0004)"""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        flat_map = FlatMap(ar_root, "TestFlatMap")

        # Create in non-alphabetical order to prove insertion order, not sorting
        instance2 = flat_map.createFlatInstanceDescriptor("Instance2")
        instance1 = flat_map.createFlatInstanceDescriptor("Instance1")

        instances = flat_map.getInstances()
        assert instances == [instance2, instance1]
        assert [i.getShortName() for i in instances] == ["Instance2", "Instance1"]
