import pytest

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptEnablerImplTypeEnum, RptExecutionControlEnum, RptPreparationEnum
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.AnyInstanceRef import AnyInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import DiagnosticParameterElement, Identifiable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CIdentifier, NameToken, PositiveInteger, RefType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario import (
    DiagnosticParameterIdent,
    ExternalTriggeringPointIdent,
    IdentCaption,
    ModeAccessPointIdent,
    RptContainer,
    RptExecutableEntityProperties,
    RptHook,
    RptImplPolicy,
    RptProfile,
    RptServicePointEnum,
)
from armodel.models.M2.MSR.AsamHdo.SpecialData import Sdg


class TestIdentCaption:
    """Test class for IdentCaption class (Table 14.4, p.851)."""

    SPEC_NOTE = "This meta-class represents the caption. This allows having some meta-classes optionally identifiable."

    def test_ident_caption_abstract(self):
        """IdentCaption is abstract (Table 14.4 header) — direct instantiation must fail."""
        with pytest.raises(TypeError):
            IdentCaption(None, "caption")

    def test_ident_caption_heritage(self):
        """Most-derived direct base is AtpStructureElement (Table 14.4 Base chain), verified via concrete subclass."""
        ident = ExternalTriggeringPointIdent(None, "ident")

        assert type(ident).__bases__ == (IdentCaption,)
        for ancestor in (IdentCaption, AtpStructureElement, Identifiable, Referrable, ARObject):
            assert isinstance(ident, ancestor)

    def test_ident_caption_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 14.4)."""
        assert IdentCaption.__doc__.strip() == self.SPEC_NOTE

    def test_ident_caption_base_accessors_via_subclass(self):
        """Base accessors (short_name/parent from Referrable) work through a concrete subclass."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ExternalTriggeringPointIdent(ar_root, "ident")

        assert ident.parent == ar_root
        assert ident.getShortName() == "ident"


class TestModeAccessPointIdent:
    """Test class for ModeAccessPointIdent class (Table 14.5, p.852)."""

    SPEC_NOTE = "This meta-class has been created to introduce the ability to become referenced into the meta-class Mode AccessPoint without breaking backwards compatibility."

    def test_mode_access_point_ident_concrete(self):
        """ModeAccessPointIdent is concrete (Table 14.5 header) — instantiable."""
        ident = ModeAccessPointIdent(None, "ident")

        assert isinstance(ident, ModeAccessPointIdent)

    def test_mode_access_point_ident_heritage(self):
        """Most-derived direct base is IdentCaption (Table 14.5 Base chain)."""
        ident = ModeAccessPointIdent(None, "ident")

        assert type(ident).__bases__ == (IdentCaption,)
        for ancestor in (IdentCaption, AtpStructureElement, Identifiable, Referrable, ARObject):
            assert isinstance(ident, ancestor)

    def test_mode_access_point_ident_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 14.5)."""
        assert ModeAccessPointIdent.__doc__.strip() == self.SPEC_NOTE

    def test_mode_access_point_ident_base_accessors(self):
        """Base accessors (short_name/parent from Referrable) work through the concrete class."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ModeAccessPointIdent(ar_root, "ident")

        assert ident.parent == ar_root
        assert ident.getShortName() == "ident"


class TestExternalTriggeringPointIdent:
    """Test class for ExternalTriggeringPointIdent class."""

    def test_external_triggering_point_ident_spec_contract(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ExternalTriggeringPointIdent(ar_root, "ident")

        assert ident.__class__.__doc__.strip() == (
            "This meta-class has been created to introduce the ability to become referenced into the meta-class ExternalTriggeringPoint without breaking backwards compatibility."
        )
        assert isinstance(ident, IdentCaption)

    def test_external_triggering_point_ident_initialization(self):
        """Test ExternalTriggeringPointIdent initialization."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = ExternalTriggeringPointIdent(ar_root, "TestExternalTriggeringPointIdent")

        assert ident.parent == ar_root
        assert ident.short_name == "TestExternalTriggeringPointIdent"
        # ExternalTriggeringPointIdent inherits from IdentCaption, which doesn't have returnValueProvision
        # That attribute is only on InternalTriggeringPoint (which inherits from AbstractAccessPoint)
        assert isinstance(ident, IdentCaption)


class TestRptImplPolicy:
    def test_initialization(self):
        """Test RptImplPolicy initialization defaults"""
        policy = RptImplPolicy()
        assert policy is not None
        assert policy.rptEnablerImplType is None
        assert policy.rptPreparationLevel is None

    def test_rpt_enabler_impl_type_setter_getter(self):
        """Test rptEnablerImplType setter and getter"""
        policy = RptImplPolicy()
        test_value = RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM)
        result = policy.setRptEnablerImplType(test_value)
        assert result is policy
        assert policy.getRptEnablerImplType() == test_value

    def test_rpt_enabler_impl_type_none_is_noop(self):
        """Test setting None rptEnablerImplType is a no-op"""
        policy = RptImplPolicy()
        test_value = RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_ROM)
        policy.setRptEnablerImplType(test_value)
        policy.setRptEnablerImplType(None)
        assert policy.getRptEnablerImplType() == test_value

    def test_rpt_preparation_level_setter_getter(self):
        """Test rptPreparationLevel setter and getter"""
        policy = RptImplPolicy()
        test_value = RptPreparationEnum().setValue(RptPreparationEnum.RPT_LEVEL_2)
        result = policy.setRptPreparationLevel(test_value)
        assert result is policy
        assert policy.getRptPreparationLevel() == test_value


class TestRptExecutableEntityProperties:
    def test_initialization(self):
        """Test RptExecutableEntityProperties initialization defaults"""
        properties = RptExecutableEntityProperties()
        assert properties is not None
        assert properties.maxRptEventId is None
        assert properties.minRptEventId is None
        assert properties.rptExecutionControl is None
        assert properties.rptServicePoint is None

    def test_max_min_rpt_event_id_setter_getter(self):
        """Test maxRptEventId and minRptEventId setters and getters"""
        properties = RptExecutableEntityProperties()
        max_id = PositiveInteger().setValue("100")
        min_id = PositiveInteger().setValue("1")
        result = properties.setMaxRptEventId(max_id)
        assert result is properties
        assert properties.getMaxRptEventId() == max_id
        assert properties.setMinRptEventId(min_id) is properties
        assert properties.getMinRptEventId() == min_id

    def test_rpt_execution_control_setter_getter(self):
        """Test rptExecutionControl setter and getter"""
        properties = RptExecutableEntityProperties()
        test_value = RptExecutionControlEnum().setValue(RptExecutionControlEnum.CONDITIONAL)
        result = properties.setRptExecutionControl(test_value)
        assert result is properties
        assert properties.getRptExecutionControl() == test_value

    def test_rpt_service_point_setter_getter(self):
        """Test rptServicePoint setter and getter"""
        properties = RptExecutableEntityProperties()
        test_value = RptServicePointEnum().setValue(RptServicePointEnum.ENABLED)
        result = properties.setRptServicePoint(test_value)
        assert result is properties
        assert properties.getRptServicePoint() == test_value


class TestRptServicePointEnum:
    def test_members(self):
        """Test RptServicePointEnum members match the spec literals"""
        assert RptServicePointEnum.ENABLED == "ENABLED"
        assert RptServicePointEnum.NONE == "NONE"


class TestDiagnosticParameterIdent:
    """Test class for DiagnosticParameterIdent class (Table 4.7, p.37, R23-11)."""

    SPEC_NOTE = "This meta-class has been created to introduce the ability to become referenced into the meta-class AbstractDiagnosticParameter without breaking backwards compatibility."

    def test_diagnostic_parameter_ident_concrete(self):
        """DiagnosticParameterIdent is concrete (Table 4.7 header) — instantiable."""
        ident = DiagnosticParameterIdent(None, "ident")

        assert isinstance(ident, DiagnosticParameterIdent)

    def test_diagnostic_parameter_ident_heritage(self):
        """Most-derived direct base is IdentCaption (Table 4.7 Base chain)."""
        ident = DiagnosticParameterIdent(None, "ident")

        assert type(ident).__bases__ == (IdentCaption,)
        for ancestor in (IdentCaption, AtpStructureElement, Identifiable, Referrable, ARObject):
            assert isinstance(ident, ancestor)

    def test_diagnostic_parameter_ident_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 4.7)."""
        assert DiagnosticParameterIdent.__doc__.strip() == self.SPEC_NOTE

    def test_initialization_defaults(self):
        """Test that DiagnosticParameterIdent is initialized with the spec defaults."""
        ident = DiagnosticParameterIdent(None, "ident")

        assert ident.getShortName() == "ident"
        assert ident.getSubElements() == []

    def test_create_sub_element(self):
        """Test createSubElement creates, appends and returns the existing one for a duplicate short name."""
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        ident = DiagnosticParameterIdent(ar_root, "ident")

        sub_element = ident.createSubElement("Sub1")
        assert sub_element is not None
        assert sub_element.getShortName() == "Sub1"
        assert sub_element.getParent() is ident
        assert isinstance(sub_element, DiagnosticParameterElement)
        assert ident.getSubElements() == [sub_element]

        duplicate = ident.createSubElement("Sub1")
        assert duplicate is sub_element  # duplicate short name returns the existing element
        assert len(ident.getSubElements()) == 1

        second = ident.createSubElement("Sub2")
        assert ident.getSubElements() == [sub_element, second]

    def test_get_sub_elements_type_hints(self):
        """Pin the subElement aggregation annotations to the spec types (Rule 0003)."""
        import typing

        getter_hints = typing.get_type_hints(DiagnosticParameterIdent.getSubElements)
        assert getter_hints.get("return") == typing.List[DiagnosticParameterElement]

        factory_hints = typing.get_type_hints(DiagnosticParameterIdent.createSubElement)
        assert factory_hints.get("short_name") is str
        assert factory_hints.get("return") is DiagnosticParameterElement


class TestRptHook:
    """Test class for RptHook class (Table 14.3, p.848)."""

    SPEC_NOTE = (
        "This meta-class provide the ability to describe a rapid prototyping hook. This can either be described by an other AUTOSAR system with the category RPT_SYSTEM or as a non AUTOSAR software."
    )

    def test_rpt_hook_concrete(self):
        """RptHook is concrete (Table 14.3 header) — instantiable without parent/short_name (Base = ARObject)."""
        hook = RptHook()

        assert isinstance(hook, RptHook)

    def test_rpt_hook_heritage(self):
        """Most-derived base is ARObject (Table 14.3 Base); VP capability via the VariationPointCapable mixin (Rule 0020)."""
        hook = RptHook()

        assert type(hook).__bases__ == (ARObject, VariationPointCapable)
        for ancestor in (ARObject, VariationPointCapable):
            assert isinstance(hook, ancestor)

    def test_rpt_hook_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 14.3)."""
        assert RptHook.__doc__.strip() == self.SPEC_NOTE

    def test_initialization(self):
        """Test RptHook initialization defaults (all Table 14.3 attributes unset)."""
        hook = RptHook()

        assert hook is not None
        assert hook.getCodeLabel() is None
        assert hook.getMcdIdentifier() is None
        assert hook.getRptArHookIRef() is None
        assert hook.getSdgs() == []

    def test_get_set_code_label(self):
        """Test codeLabel setter and getter (CIdentifier, 0..1)."""
        hook = RptHook()
        test_value = CIdentifier().setValue("RptHookFunc")
        result = hook.setCodeLabel(test_value)

        assert result is hook
        assert hook.getCodeLabel() == test_value

        hook.setCodeLabel(None)
        assert hook.getCodeLabel() == test_value

    def test_get_set_mcd_identifier(self):
        """Test mcdIdentifier setter and getter (NameToken, 0..1)."""
        hook = RptHook()
        test_value = NameToken().setValue("McdHook")
        result = hook.setMcdIdentifier(test_value)

        assert result is hook
        assert hook.getMcdIdentifier() == test_value

        hook.setMcdIdentifier(None)
        assert hook.getMcdIdentifier() == test_value

    def test_get_set_rpt_ar_hook_iref(self):
        """Test rptArHook iref setter and getter (AnyInstanceRef, 0..1, Rule 0001.5 IRef suffix)."""
        hook = RptHook()
        iref = AnyInstanceRef()
        iref.setTargetRef(RefType().setValue("/RptAlgorithm"))
        result = hook.setRptArHookIRef(iref)

        assert result is hook
        assert hook.getRptArHookIRef() == iref

        hook.setRptArHookIRef(None)
        assert hook.getRptArHookIRef() == iref

    def test_add_get_sdgs(self):
        """Test sdg aggregation (Sdg, *, Base = ARObject → add, not create)."""
        hook = RptHook()
        sdg = Sdg()
        sdg.setGID(NameToken().setValue("toolData"))
        result = hook.addSdg(sdg)

        assert result is hook
        assert hook.getSdgs() == [sdg]

        hook.addSdg(None)
        assert hook.getSdgs() == [sdg]

        second = Sdg()
        hook.addSdg(second)
        assert hook.getSdgs() == [sdg, second]

    def test_get_set_variation_point(self):
        """VP capability inherited from VariationPointCapable (Rule 0020)."""
        hook = RptHook()
        vp = VariationPoint()

        assert hook == hook.setVariationPoint(vp)
        assert hook.getVariationPoint() == vp

        assert hook == hook.setVariationPoint(None)
        assert hook.getVariationPoint() == vp

    def test_type_hints(self):
        """Pin the member annotations to the spec types (Rule 0003)."""
        import typing

        assert typing.get_type_hints(RptHook.getCodeLabel).get("return") == typing.Optional[CIdentifier]
        assert typing.get_type_hints(RptHook.setCodeLabel).get("value") == typing.Optional[CIdentifier]
        assert typing.get_type_hints(RptHook.setCodeLabel).get("return") is RptHook

        assert typing.get_type_hints(RptHook.getMcdIdentifier).get("return") == typing.Optional[NameToken]
        assert typing.get_type_hints(RptHook.setMcdIdentifier).get("value") == typing.Optional[NameToken]

        assert typing.get_type_hints(RptHook.getRptArHookIRef).get("return") == typing.Optional[AnyInstanceRef]
        assert typing.get_type_hints(RptHook.setRptArHookIRef).get("value") == typing.Optional[AnyInstanceRef]

        assert typing.get_type_hints(RptHook.getSdgs).get("return") == typing.List[Sdg]
        assert typing.get_type_hints(RptHook.addSdg).get("sdg") == typing.Optional[Sdg]
        assert typing.get_type_hints(RptHook.addSdg).get("return") is RptHook


class TestRptProfile:
    """Test class for RptProfile class (Table 14.7, p.854)."""

    SPEC_NOTE = "The RptProfile describes the common properties of a Rapid Prototyping method."

    def test_rpt_profile_concrete(self):
        """RptProfile is concrete (Table 14.7 header, XSD RPT-PROFILE abstract="false") — instantiable with parent/short_name (Base chain reaches Identifiable)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")

        assert isinstance(profile, RptProfile)
        assert profile.getShortName() == "RptProfile1"

    def test_rpt_profile_heritage(self):
        """Most-derived base is Identifiable (Table 14.7 Base: ARObject, Identifiable, MultilanguageReferrable, Referrable — Rule 0001.2)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")

        assert type(profile).__bases__ == (Identifiable,)
        for ancestor in (ARObject, Identifiable):
            assert isinstance(profile, ancestor)

    def test_rpt_profile_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 14.7)."""
        assert RptProfile.__doc__.strip() == self.SPEC_NOTE

    def test_initialization(self):
        """Test RptProfile initialization defaults (all Table 14.7 attributes unset)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")

        assert profile is not None
        assert profile.getMaxServicePointId() is None
        assert profile.getMinServicePointId() is None
        assert profile.getServicePointSymbolPost() is None
        assert profile.getServicePointSymbolPre() is None
        assert profile.getStimEnabler() is None

    def test_get_set_max_service_point_id(self):
        """Test maxServicePointId setter and getter (PositiveInteger, 0..1)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
        test_value = PositiveInteger().setValue("4")
        result = profile.setMaxServicePointId(test_value)

        assert result is profile
        assert profile.getMaxServicePointId() == test_value

        profile.setMaxServicePointId(None)
        assert profile.getMaxServicePointId() == test_value

    def test_get_set_min_service_point_id(self):
        """Test minServicePointId setter and getter (PositiveInteger, 0..1)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
        test_value = PositiveInteger().setValue("2")
        result = profile.setMinServicePointId(test_value)

        assert result is profile
        assert profile.getMinServicePointId() == test_value

        profile.setMinServicePointId(None)
        assert profile.getMinServicePointId() == test_value

    def test_get_set_service_point_symbol_post(self):
        """Test servicePointSymbolPost setter and getter (CIdentifier, 0..1)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
        test_value = CIdentifier().setValue("Rpt_PostServicePoint")
        result = profile.setServicePointSymbolPost(test_value)

        assert result is profile
        assert profile.getServicePointSymbolPost() == test_value

        profile.setServicePointSymbolPost(None)
        assert profile.getServicePointSymbolPost() == test_value

    def test_get_set_service_point_symbol_pre(self):
        """Test servicePointSymbolPre setter and getter (CIdentifier, 0..1)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
        test_value = CIdentifier().setValue("Rpt_PreServicePoint")
        result = profile.setServicePointSymbolPre(test_value)

        assert result is profile
        assert profile.getServicePointSymbolPre() == test_value

        profile.setServicePointSymbolPre(None)
        assert profile.getServicePointSymbolPre() == test_value

    def test_get_set_stim_enabler(self):
        """Test stimEnabler setter and getter (RptEnablerImplTypeEnum, 0..1)."""
        profile = RptProfile(AUTOSAR.getInstance(), "RptProfile1")
        test_value = RptEnablerImplTypeEnum().setValue(RptEnablerImplTypeEnum.RPT_ENABLER_RAM)
        result = profile.setStimEnabler(test_value)

        assert result is profile
        assert profile.getStimEnabler() == test_value

        profile.setStimEnabler(None)
        assert profile.getStimEnabler() == test_value

    def test_type_hints(self):
        """Pin the member annotations to the spec types (Rule 0003)."""
        import typing

        assert typing.get_type_hints(RptProfile.getMaxServicePointId).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(RptProfile.setMaxServicePointId).get("value") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(RptProfile.setMaxServicePointId).get("return") is RptProfile

        assert typing.get_type_hints(RptProfile.getMinServicePointId).get("return") == typing.Optional[PositiveInteger]
        assert typing.get_type_hints(RptProfile.setMinServicePointId).get("value") == typing.Optional[PositiveInteger]

        assert typing.get_type_hints(RptProfile.getServicePointSymbolPost).get("return") == typing.Optional[CIdentifier]
        assert typing.get_type_hints(RptProfile.setServicePointSymbolPost).get("value") == typing.Optional[CIdentifier]

        assert typing.get_type_hints(RptProfile.getServicePointSymbolPre).get("return") == typing.Optional[CIdentifier]
        assert typing.get_type_hints(RptProfile.setServicePointSymbolPre).get("value") == typing.Optional[CIdentifier]

        assert typing.get_type_hints(RptProfile.getStimEnabler).get("return") == typing.Optional[RptEnablerImplTypeEnum]
        assert typing.get_type_hints(RptProfile.setStimEnabler).get("value") == typing.Optional[RptEnablerImplTypeEnum]


class TestRptContainer:
    """Test class for RptContainer class (Table 14.2, p.847)."""

    SPEC_NOTE = (
        "This meta-class defines a byPassPoint and the relation to a rptHook. Additionally it may contain further rptContainers if the byPassPoint is not atomic. "
        "For example a byPass Point referencing to a RunnableEntity may contain rptContainers referring to the data access points of the RunnableEntity. "
        "The RptContainer structure on M1 shall follow the M1 structure of the Software Component Descriptions. "
        "The category attribute denotes which level of the Software Component Description is annotated."
    )

    def test_rpt_container_concrete(self):
        """RptContainer is concrete (Table 14.2 header, XSD RPT-CONTAINER abstract="false") — instantiable with parent/short_name (Base chain reaches Identifiable)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")

        assert isinstance(container, RptContainer)
        assert container.getShortName() == "RptContainer1"

    def test_rpt_container_heritage(self):
        """Most-derived base is Identifiable (Table 14.2 Base: ARObject, Identifiable, MultilanguageReferrable, Referrable — Rule 0001.2); VP capability via the VariationPointCapable mixin (Rule 0020)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")

        assert type(container).__bases__ == (Identifiable, VariationPointCapable)
        for ancestor in (ARObject, Identifiable, VariationPointCapable):
            assert isinstance(container, ancestor)

    def test_rpt_container_class_docstring_verbatim(self):
        """Class docstring must be the spec Note verbatim (Table 14.2)."""
        assert RptContainer.__doc__.strip() == self.SPEC_NOTE

    def test_initialization(self):
        """Test RptContainer initialization defaults (all Table 14.2 attributes unset)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")

        assert container is not None
        assert container.getByPassPointIRefs() == []
        assert container.getExplicitRptProfileSelectionRefs() == []
        assert container.getRptContainers() == []
        assert container.getRptExecutableEntityProperties() is None
        assert container.getRptHook() is None
        assert container.getRptImplPolicy() is None
        assert container.getRptSwPrototypingAccess() is None

    def test_add_get_by_pass_point_irefs(self):
        """Test byPassPoint iref aggregation (AnyInstanceRef, *, Rule 0001.5 IRef suffix + plural)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        iref = AnyInstanceRef()
        iref.setTargetRef(RefType().setValue("/comp/Swc1/Data1"))
        result = container.addByPassPointIRef(iref)

        assert result is container
        assert container.getByPassPointIRefs() == [iref]

        container.addByPassPointIRef(None)
        assert container.getByPassPointIRefs() == [iref]

        second = AnyInstanceRef()
        second.setTargetRef(RefType().setValue("/comp/Swc1/Data2"))
        container.addByPassPointIRef(second)
        assert container.getByPassPointIRefs() == [iref, second]

    def test_add_get_explicit_rpt_profile_selection_refs(self):
        """Test explicitRptProfileSelection ref aggregation (RefType, *)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        ref = RefType().setValue("/RptScenario/RptProfile1")
        result = container.addExplicitRptProfileSelectionRef(ref)

        assert result is container
        assert container.getExplicitRptProfileSelectionRefs() == [ref]

        container.addExplicitRptProfileSelectionRef(None)
        assert container.getExplicitRptProfileSelectionRefs() == [ref]

        second = RefType().setValue("/RptScenario/RptProfile2")
        container.addExplicitRptProfileSelectionRef(second)
        assert container.getExplicitRptProfileSelectionRefs() == [ref, second]

    def test_create_get_rpt_containers(self):
        """Test rptContainer recursive aggregation (RptContainer, *, Identifiable child -> create)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")

        sub_container = container.createRptContainer("SubContainer")
        assert sub_container is not None
        assert sub_container.getShortName() == "SubContainer"
        assert sub_container.getParent() is container
        assert isinstance(sub_container, RptContainer)
        assert container.getRptContainers() == [sub_container]

        duplicate = container.createRptContainer("SubContainer")
        assert duplicate is sub_container  # duplicate short name returns the existing element
        assert len(container.getRptContainers()) == 1

        second = container.createRptContainer("SubContainer2")
        assert container.getRptContainers() == [sub_container, second]

    def test_get_set_rpt_hook(self):
        """Test rptHook aggregation (RptHook, 0..1, ARObject child -> set)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        hook = RptHook()
        result = container.setRptHook(hook)

        assert result is container
        assert container.getRptHook() == hook

        container.setRptHook(None)
        assert container.getRptHook() == hook

    def test_get_set_rpt_executable_entity_properties(self):
        """Test rptExecutableEntityProperties aggregation (0..1, ARObject child -> set)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        properties = RptExecutableEntityProperties()
        result = container.setRptExecutableEntityProperties(properties)

        assert result is container
        assert container.getRptExecutableEntityProperties() == properties

        container.setRptExecutableEntityProperties(None)
        assert container.getRptExecutableEntityProperties() == properties

    def test_get_set_rpt_impl_policy(self):
        """Test rptImplPolicy aggregation (0..1, ARObject child -> set)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        policy = RptImplPolicy()
        result = container.setRptImplPolicy(policy)

        assert result is container
        assert container.getRptImplPolicy() == policy

        container.setRptImplPolicy(None)
        assert container.getRptImplPolicy() == policy

    def test_get_set_rpt_sw_prototyping_access(self):
        """Test rptSwPrototypingAccess aggregation (0..1, ARObject child -> set)."""
        from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptSwPrototypingAccess

        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        access = RptSwPrototypingAccess()
        result = container.setRptSwPrototypingAccess(access)

        assert result is container
        assert container.getRptSwPrototypingAccess() == access

        container.setRptSwPrototypingAccess(None)
        assert container.getRptSwPrototypingAccess() == access

    def test_get_set_variation_point(self):
        """VP capability inherited from VariationPointCapable (Rule 0020)."""
        container = RptContainer(AUTOSAR.getInstance(), "RptContainer1")
        vp = VariationPoint()

        assert container == container.setVariationPoint(vp)
        assert container.getVariationPoint() == vp

        assert container == container.setVariationPoint(None)
        assert container.getVariationPoint() == vp

    def test_type_hints(self):
        """Pin the member annotations to the spec types (Rule 0003)."""
        import typing

        assert typing.get_type_hints(RptContainer.getByPassPointIRefs).get("return") == typing.List[AnyInstanceRef]
        assert typing.get_type_hints(RptContainer.addByPassPointIRef).get("iref") == typing.Optional[AnyInstanceRef]
        assert typing.get_type_hints(RptContainer.addByPassPointIRef).get("return") is RptContainer

        assert typing.get_type_hints(RptContainer.getExplicitRptProfileSelectionRefs).get("return") == typing.List[RefType]
        assert typing.get_type_hints(RptContainer.addExplicitRptProfileSelectionRef).get("ref") == typing.Optional[RefType]

        assert typing.get_type_hints(RptContainer.getRptContainers).get("return") == typing.List[RptContainer]
        assert typing.get_type_hints(RptContainer.createRptContainer).get("short_name") is str
        assert typing.get_type_hints(RptContainer.createRptContainer).get("return") is RptContainer

        assert typing.get_type_hints(RptContainer.getRptExecutableEntityProperties).get("return") == typing.Optional[RptExecutableEntityProperties]
        assert typing.get_type_hints(RptContainer.setRptExecutableEntityProperties).get("value") == typing.Optional[RptExecutableEntityProperties]

        assert typing.get_type_hints(RptContainer.getRptHook).get("return") == typing.Optional[RptHook]
        assert typing.get_type_hints(RptContainer.setRptHook).get("value") == typing.Optional[RptHook]

        assert typing.get_type_hints(RptContainer.getRptImplPolicy).get("return") == typing.Optional[RptImplPolicy]
        assert typing.get_type_hints(RptContainer.setRptImplPolicy).get("value") == typing.Optional[RptImplPolicy]

        from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport import RptSwPrototypingAccess

        assert typing.get_type_hints(RptContainer.getRptSwPrototypingAccess).get("return") == typing.Optional[RptSwPrototypingAccess]
        assert typing.get_type_hints(RptContainer.setRptSwPrototypingAccess).get("value") == typing.Optional[RptSwPrototypingAccess]
