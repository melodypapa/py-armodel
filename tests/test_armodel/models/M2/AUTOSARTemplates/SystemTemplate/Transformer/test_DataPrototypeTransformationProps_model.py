import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import (
    DataPrototypeInPortInterfaceRef,
    DataPrototypeInClientServerInterfaceInstanceRef,
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
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

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
        cs.setTargetDataPrototypeInCs(RefType().setValue("/Cs/MyArg"))

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

        assert iref.getBase() is None
        assert iref.getContextDataPrototypeInSr() == []
        assert iref.getRootDataPrototypeInSr() is None
        assert iref.getTargetDataPrototypeInSr() is None

    def test_base_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        base = RefType()
        base.setValue("/SenderReceiverInterface")

        assert iref == iref.setBase(None)
        assert iref.getBase() is None

        assert iref == iref.setBase(base)
        assert iref.getBase() == base

        assert iref == iref.setBase(None)  # None no-op
        assert iref.getBase() == base

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetDataPrototype")

        iref.setRootDataPrototypeInSr(root)
        iref.setTargetDataPrototypeInSr(target)
        assert iref.getRootDataPrototypeInSr() == root
        assert iref.getTargetDataPrototypeInSr() == target

    def test_add_context_data_prototype_in_sr(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInSenderReceiverInterfaceInstanceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")
        ctx2 = RefType()
        ctx2.setValue("/Ctx2")

        iref.addContextDataPrototypeInSr(ctx1)
        assert ctx1 in iref.getContextDataPrototypeInSr()
        assert len(iref.getContextDataPrototypeInSr()) == 1

        assert iref == iref.addContextDataPrototypeInSr(None)  # None no-op
        assert len(iref.getContextDataPrototypeInSr()) == 1

        assert iref == iref.addContextDataPrototypeInSr(ctx2)
        assert len(iref.getContextDataPrototypeInSr()) == 2


class TestDataPrototypeInClientServerInterfaceInstanceRef:
    """
    Model tests for DataPrototypeInClientServerInterfaceInstanceRef (Table 7.21).
    """

    def test_initialization(self):
        iref = DataPrototypeInClientServerInterfaceInstanceRef()

        assert iref.getBase() is None
        assert iref.getContextDataPrototypeInCs() == []
        assert iref.getRootDataPrototypeInCs() is None
        assert iref.getTargetDataPrototypeInCs() is None

    def test_base_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        base = RefType()
        base.setValue("/ClientServerInterface")

        assert iref == iref.setBase(None)
        assert iref.getBase() is None

        assert iref == iref.setBase(base)
        assert iref.getBase() == base

        assert iref == iref.setBase(None)  # None no-op
        assert iref.getBase() == base

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetDataPrototype")

        iref.setRootDataPrototypeInCs(root)
        iref.setTargetDataPrototypeInCs(target)
        assert iref.getRootDataPrototypeInCs() == root
        assert iref.getTargetDataPrototypeInCs() == target

    def test_add_context_data_prototype_in_cs(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        iref = DataPrototypeInClientServerInterfaceInstanceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")

        iref.addContextDataPrototypeInCs(ctx1)
        assert ctx1 in iref.getContextDataPrototypeInCs()
        assert len(iref.getContextDataPrototypeInCs()) == 1

        assert iref == iref.addContextDataPrototypeInCs(None)  # None no-op
        assert len(iref.getContextDataPrototypeInCs()) == 1


class TestImplementationDataTypeElementInPortInterfaceRef:
    """
    Model tests for ImplementationDataTypeElementInPortInterfaceRef (Table 7.22).
    """

    def test_initialization(self):
        ref = ImplementationDataTypeElementInPortInterfaceRef()

        assert isinstance(ref, DataPrototypeReference)
        assert ref.getContextImplementationDataElement() == []
        assert ref.getRootDataPrototype() is None
        assert ref.getTargetImplementationDataTypeElement() is None

    def test_root_and_target_round_trip(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = ImplementationDataTypeElementInPortInterfaceRef()
        root = RefType()
        root.setValue("/RootDataPrototype")
        target = RefType()
        target.setValue("/TargetImplDataTypeElement")

        ref.setRootDataPrototype(root)
        ref.setTargetImplementationDataTypeElement(target)
        assert ref.getRootDataPrototype() == root
        assert ref.getTargetImplementationDataTypeElement() == target

    def test_add_context_implementation_data_element(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

        ref = ImplementationDataTypeElementInPortInterfaceRef()
        ctx1 = RefType()
        ctx1.setValue("/Ctx1")

        ref.addContextImplementationDataElement(ctx1)
        assert ctx1 in ref.getContextImplementationDataElement()
        assert len(ref.getContextImplementationDataElement()) == 1

        assert ref == ref.addContextImplementationDataElement(None)  # None no-op
        assert len(ref.getContextImplementationDataElement()) == 1
