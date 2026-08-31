"""
Tests for ApplicationCompositeElementInPortInterfaceInstanceRef — Table D.17 (p.953, R23-11).

Base chain: ARObject → AtpInstanceRef (most-derived AtpInstanceRef).
base is a 0..1 ref with NO XML element (XSD: "Association <<atpDerived>>base skipped");
contextDataPrototype is an ordered `*` ref → typed list; root/target are 0..1 refs.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.InstanceRefs import ApplicationCompositeElementInPortInterfaceInstanceRef


class TestApplicationCompositeElementInPortInterfaceInstanceRef:
    """
    Spec: AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf, Table D.17, p.953 (R23-11)
    """

    def test_initialization(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()

        assert obj.getBaseRef() is None
        assert obj.getContextDataPrototypeRefs() == []
        assert obj.getRootDataPrototypeRef() is None
        assert obj.getTargetDataPrototypeRef() is None

        # Base chain (Table D.17): most-derived model base = AtpInstanceRef
        assert isinstance(obj, AtpInstanceRef)

    def test_base_ref_round_trip(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()

        base_ref = RefType().setValue("/Base/Iface")
        assert obj.setBaseRef(base_ref) is obj
        assert obj.getBaseRef() is base_ref

    def test_base_ref_none_no_op(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()
        obj.setBaseRef(RefType().setValue("/Base/Iface"))

        obj.setBaseRef(None)

        assert obj.getBaseRef() is not None
        assert obj.getBaseRef().getValue() == "/Base/Iface"

    def test_context_data_prototype_refs_add(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()

        ref1 = RefType().setValue("/Ctx/First")
        ref1.setDest("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE")
        ref2 = RefType().setValue("/Ctx/Second")
        ref2.setDest("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE")

        assert obj.addContextDataPrototypeRef(ref1) is obj
        obj.addContextDataPrototypeRef(ref2)

        refs = obj.getContextDataPrototypeRefs()
        assert refs == [ref1, ref2]
        assert refs[0].getValue() == "/Ctx/First"
        assert refs[1].getDest() == "APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE"

    def test_context_data_prototype_refs_add_none_no_op(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()
        obj.addContextDataPrototypeRef(RefType().setValue("/Ctx/First"))

        obj.addContextDataPrototypeRef(None)

        assert len(obj.getContextDataPrototypeRefs()) == 1

    def test_root_data_prototype_ref_round_trip(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()

        root_ref = RefType().setValue("/Root/Proto")
        root_ref.setDest("AUTOSAR-DATA-PROTOTYPE")
        assert obj.setRootDataPrototypeRef(root_ref) is obj
        assert obj.getRootDataPrototypeRef() is root_ref

    def test_root_data_prototype_ref_none_no_op(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()
        obj.setRootDataPrototypeRef(RefType().setValue("/Root/Proto"))

        obj.setRootDataPrototypeRef(None)

        assert obj.getRootDataPrototypeRef() is not None

    def test_target_data_prototype_ref_round_trip(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()

        target_ref = RefType().setValue("/Target/Proto")
        target_ref.setDest("APPLICATION-COMPOSITE-ELEMENT-DATA-PROTOTYPE")
        assert obj.setTargetDataPrototypeRef(target_ref) is obj
        assert obj.getTargetDataPrototypeRef() is target_ref

    def test_target_data_prototype_ref_none_no_op(self):
        obj = ApplicationCompositeElementInPortInterfaceInstanceRef()
        obj.setTargetDataPrototypeRef(RefType().setValue("/Target/Proto"))

        obj.setTargetDataPrototypeRef(None)

        assert obj.getTargetDataPrototypeRef() is not None
