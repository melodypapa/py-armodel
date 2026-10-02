"""Model tests for PModeInSystemInstanceRef (XSD-only; AUTOSAR_00052.xsd line 87429).

PModeInSystemInstanceRef (AtpInstanceRef; DiagnosticExtract::InstanceRefs) is the
InstanceRef implemented by DiagnosticEnvSwcModeElement.mode — XSD group
P-MODE-IN-SYSTEM-INSTANCE-REF (AUTOSAR_00052.xsd l.87359): CONTEXT-COMPOSITION-REF
(seq 20), CONTEXT-COMPONENT-REF (seq 30, 0..*), CONTEXT-P-PORT-REF (seq 40),
CONTEXT-MODE-DECLARATION-GROUP-REF (seq 50), TARGET-MODE-REF (seq 60); BASE-REF via
the ATP-INSTANCE-REF group (atpDerived).
"""

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.InstanceRefs import PModeInSystemInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType


def _ref(dest, value):
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestPModeInSystemInstanceRef:
    def test_initialization(self):
        iref = PModeInSystemInstanceRef()
        assert iref is not None
        assert iref.getBaseRef() is None
        assert iref.getContextCompositionRef() is None
        assert iref.getContextComponentRefs() == []
        assert iref.getContextPPortRef() is None
        assert iref.getContextModeDeclarationGroupRef() is None
        assert iref.getTargetModeRef() is None

    def test_get_set_base_ref(self):
        iref = PModeInSystemInstanceRef()
        ref = _ref("ROOT-SW-COMPOSITION-PROTOTYPE", "/AUTOSAR/Base")
        assert iref.setBaseRef(ref) is iref
        assert iref.getBaseRef() is ref
        iref.setBaseRef(None)
        assert iref.getBaseRef() is ref

    def test_get_set_context_composition_ref(self):
        iref = PModeInSystemInstanceRef()
        ref = _ref("ROOT-SW-COMPOSITION-PROTOTYPE", "/AUTOSAR/System/RootSwComposition")
        assert iref.setContextCompositionRef(ref) is iref
        assert iref.getContextCompositionRef() is ref
        iref.setContextCompositionRef(None)
        assert iref.getContextCompositionRef() is ref

    def test_add_context_component_ref(self):
        iref = PModeInSystemInstanceRef()
        ref1 = _ref("SW-COMPONENT-PROTOTYPE", "/AUTOSAR/System/Comp1")
        ref2 = _ref("SW-COMPONENT-PROTOTYPE", "/AUTOSAR/System/Comp1/Sw1/InnerComp")
        assert iref.addContextComponentRef(ref1) is iref
        iref.addContextComponentRef(ref2)
        assert iref.getContextComponentRefs() == [ref1, ref2]
        iref.addContextComponentRef(None)
        assert iref.getContextComponentRefs() == [ref1, ref2]

    def test_get_set_context_p_port_ref(self):
        iref = PModeInSystemInstanceRef()
        ref = _ref("ABSTRACT-PROVIDED-PORT-PROTOTYPE", "/AUTOSAR/Sw1/modePort")
        assert iref.setContextPPortRef(ref) is iref
        assert iref.getContextPPortRef() is ref
        iref.setContextPPortRef(None)
        assert iref.getContextPPortRef() is ref

    def test_get_set_context_mode_declaration_group_ref(self):
        iref = PModeInSystemInstanceRef()
        ref = _ref("MODE-DECLARATION-GROUP-PROTOTYPE", "/AUTOSAR/Port/MDG1")
        assert iref.setContextModeDeclarationGroupRef(ref) is iref
        assert iref.getContextModeDeclarationGroupRef() is ref
        iref.setContextModeDeclarationGroupRef(None)
        assert iref.getContextModeDeclarationGroupRef() is ref

    def test_get_set_target_mode_ref(self):
        iref = PModeInSystemInstanceRef()
        ref = _ref("MODE-DECLARATION", "/AUTOSAR/ModeDcls/MDG1/Normal")
        assert iref.setTargetModeRef(ref) is iref
        assert iref.getTargetModeRef() is ref
        iref.setTargetModeRef(None)
        assert iref.getTargetModeRef() is ref
