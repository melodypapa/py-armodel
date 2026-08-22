import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInClientServerInterfaceInstanceRef,
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInSenderReceiverInterfaceInstanceRef,
    DataPrototypeReference,
    DataPrototypeTransformationProps,
    ImplementationDataTypeElementInPortInterfaceRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps


class TestDataPrototypeTransformationProps:
    """
    Model tests for DataPrototypeTransformationProps (Table 7.17) and its
    DataPrototypeReference closure (Tables 7.18-7.22).
    """

    def test_initialization(self):
        props = DataPrototypeTransformationProps()

        assert isinstance(props, ARObject)
        assert props.getDataPrototypeInPortInterfaceRef() is None
        assert props.getNetworkRepresentationProps() is None
        assert props.getTransformationProps() is None

    def test_get_set_data_prototype_in_port_interface_ref(self):
        props = DataPrototypeTransformationProps()
        ref = DataPrototypeInPortInterfaceRef()

        assert props == props.setDataPrototypeInPortInterfaceRef(None)
        assert props.getDataPrototypeInPortInterfaceRef() is None

        assert props == props.setDataPrototypeInPortInterfaceRef(ref)
        assert props.getDataPrototypeInPortInterfaceRef() == ref

        assert props == props.setDataPrototypeInPortInterfaceRef(None)  # None no-op
        assert props.getDataPrototypeInPortInterfaceRef() == ref

    def test_get_set_network_representation_props(self):

        props = DataPrototypeTransformationProps()
        net = SwDataDefProps()

        assert props == props.setNetworkRepresentationProps(None)
        assert props.getNetworkRepresentationProps() is None

        assert props == props.setNetworkRepresentationProps(net)
        assert props.getNetworkRepresentationProps() == net

        assert props == props.setNetworkRepresentationProps(None)  # None no-op
        assert props.getNetworkRepresentationProps() == net

    def test_get_set_transformation_props(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        props = DataPrototypeTransformationProps()
        tp = RefType()
        tp.setValue("/TransformationProps")

        assert props == props.setTransformationProps(None)
        assert props.getTransformationProps() is None

        assert props == props.setTransformationProps(tp)
        assert props.getTransformationProps() == tp

        assert props == props.setTransformationProps(None)  # None no-op
        assert props.getTransformationProps() == tp

    def test_no_fabricated_members(self):
        props = DataPrototypeTransformationProps()

        assert not hasattr(props, "sizeOfArrayLengthField")
        assert not hasattr(props, "sizeOfStructLengthField")


class TestDataPrototypeReference:
    """
    Model tests for the abstract DataPrototypeReference (Table 7.18).
    """

    def test_abstract_not_instantiable(self):
        with pytest.raises(TypeError):
            DataPrototypeReference()

    def test_tag_id_round_trip(self):
        ref = DataPrototypeInPortInterfaceRef()
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import PositiveInteger

        tag = PositiveInteger().setValue(5)

        assert ref == ref.setTagId(None)
        assert ref.getTagId() is None

        assert ref == ref.setTagId(tag)
        assert ref.getTagId() == tag
        assert ref.getTagId().getValue() == 5

        assert ref == ref.setTagId(None)  # None no-op
        assert ref.getTagId() == tag

    def test_concrete_subclass_is_data_prototype_reference(self):
        ref = DataPrototypeInPortInterfaceRef()

        assert isinstance(ref, DataPrototypeReference)


class TestDataPrototypeInPortInterfaceRef:
    """
    Model tests for DataPrototypeInPortInterfaceRef (Table 7.19).
    """

    def test_initialization(self):
        ref = DataPrototypeInPortInterfaceRef()

        assert isinstance(ref, DataPrototypeReference)
        assert ref.getDataPrototypeInClientServerInterface() is None

    def test_get_set_data_prototype_in_client_server_interface(self):
        ref = DataPrototypeInPortInterfaceRef()
        cs = DataPrototypeInClientServerInterfaceInstanceRef()
        cs.setTargetDataPrototypeInCsRef(RefType().setValue("/Cs/MyArg"))

        assert ref == ref.setDataPrototypeInClientServerInterface(None)
        assert ref.getDataPrototypeInClientServerInterface() is None

        assert ref == ref.setDataPrototypeInClientServerInterface(cs)
        assert ref.getDataPrototypeInClientServerInterface() == cs

        assert ref == ref.setDataPrototypeInClientServerInterface(None)  # None no-op
        assert ref.getDataPrototypeInClientServerInterface() == cs


class TestDataPrototypeInSenderReceiverInterfaceInstanceRef:
    """
    Model tests for DataPrototypeInSenderReceiverInterfaceInstanceRef (Table 7.20).
    """

    def test_initialization(self):
        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()

        assert iref.getBaseRef() is None
        assert iref.getContextDataPrototypeInSrRefs() == []
        assert iref.getRootDataPrototypeInSrRef() is None
        assert iref.getTargetDataPrototypeInSrRef() is None

    def test_base_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        base = RefType()
        base.setValue("/SenderReceiverInterface")

        assert iref == iref.setBaseRef(None)
        assert iref.getBaseRef() is None

        assert iref == iref.setBaseRef(base)
        assert iref.getBaseRef() == base

        assert iref == iref.setBaseRef(None)  # None no-op
        assert iref.getBaseRef() == base

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetDataPrototype")

        iref.setRootDataPrototypeInSrRef(root)
        iref.setTargetDataPrototypeInSrRef(target)
        assert iref.getRootDataPrototypeInSrRef() == root
        assert iref.getTargetDataPrototypeInSrRef() == target

    def test_add_context_data_prototype_in_sr(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")
        ctx2 = RefType()
        ctx2.setValue("/Ctx2")

        iref.addContextDataPrototypeInSrRefs(ctx1)
        assert ctx1 in iref.getContextDataPrototypeInSrRefs()
        assert len(iref.getContextDataPrototypeInSrRefs()) == 1

        assert iref == iref.addContextDataPrototypeInSrRefs(None)  # None no-op
        assert len(iref.getContextDataPrototypeInSrRefs()) == 1

        assert iref == iref.addContextDataPrototypeInSrRefs(ctx2)
        assert len(iref.getContextDataPrototypeInSrRefs()) == 2


class TestDataPrototypeInClientServerInterfaceInstanceRef:
    """
    Model tests for DataPrototypeInClientServerInterfaceInstanceRef (Table 7.21).
    """

    def test_initialization(self):
        iref = DataPrototypeInClientServerInterfaceInstanceRef()

        assert iref.getBaseRef() is None
        assert iref.getContextDataPrototypeInCsRefs() == []
        assert iref.getRootDataPrototypeInCsRef() is None
        assert iref.getTargetDataPrototypeInCsRef() is None

    def test_base_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        base = RefType()
        base.setValue("/ClientServerInterface")

        assert iref == iref.setBaseRef(None)
        assert iref.getBaseRef() is None

        assert iref == iref.setBaseRef(base)
        assert iref.getBaseRef() == base

        assert iref == iref.setBaseRef(None)  # None no-op
        assert iref.getBaseRef() == base

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetDataPrototype")

        iref.setRootDataPrototypeInCsRef(root)
        iref.setTargetDataPrototypeInCsRef(target)
        assert iref.getRootDataPrototypeInCsRef() == root
        assert iref.getTargetDataPrototypeInCsRef() == target

    def test_add_context_data_prototype_in_cs(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")

        iref.addContextDataPrototypeInCsRefs(ctx1)
        assert ctx1 in iref.getContextDataPrototypeInCsRefs()
        assert len(iref.getContextDataPrototypeInCsRefs()) == 1

        assert iref == iref.addContextDataPrototypeInCsRefs(None)  # None no-op
        assert len(iref.getContextDataPrototypeInCsRefs()) == 1


class TestImplementationDataTypeElementInPortInterfaceRef:
    """
    Model tests for ImplementationDataTypeElementInPortInterfaceRef (Table 7.22).
    """

    def test_initialization(self):
        ref = ImplementationDataTypeElementInPortInterfaceRef()

        assert isinstance(ref, DataPrototypeReference)
        assert ref.getContextImplementationDataElementRefs() == []
        assert ref.getRootDataPrototypeRef() is None
        assert ref.getTargetImplementationDataTypeElementRef() is None

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = ImplementationDataTypeElementInPortInterfaceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetImplDataTypeElement")

        ref.setRootDataPrototypeRef(root)
        ref.setTargetImplementationDataTypeElementRef(target)
        assert ref.getRootDataPrototypeRef() == root
        assert ref.getTargetImplementationDataTypeElementRef() == target

    def test_add_context_implementation_data_element(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = ImplementationDataTypeElementInPortInterfaceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")

        ref.addContextImplementationDataElementRefs(ctx1)
        assert ctx1 in ref.getContextImplementationDataElementRefs()
        assert len(ref.getContextImplementationDataElementRefs()) == 1

        assert ref == ref.addContextImplementationDataElementRefs(None)  # None no-op
        assert len(ref.getContextImplementationDataElementRefs()) == 1
