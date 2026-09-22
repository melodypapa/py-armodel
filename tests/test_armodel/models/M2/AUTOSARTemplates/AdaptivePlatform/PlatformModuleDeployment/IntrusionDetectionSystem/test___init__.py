import pytest

from armodel import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.AdaptivePlatform.PlatformModuleDeployment.IntrusionDetectionSystem import (
    IdsmModuleInstantiation,
    IdsPlatformInstantiation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpStructureElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType

IDS_PLATFORM_NOTE = "This meta-class acts as an abstract base class for platform modules " "that implement the intrusion detection system. Tags: atp.Status=candidate"
IDSM_MODULE_NOTE = "This meta-class defines the attributes for the IdsM configuration on a " "specific machine. Tags: atp.Status=candidate"
NETWORK_INTERFACE_NOTE = "This association contains the network configuration that shall be applied " "to an instance of an IDS entity. Tags: atp.Status=candidate"
TIME_BASE_NOTE = (
    "This reference identifies the applicable time base resource. "
    "Stereotypes: atpSplitable; atpVariation Tags: "
    "atp.Splitkey=timeBase.timeBaseResource, timeBase.variationPoint.shortLabel "
    "atp.Status=candidate vh.latestBindingTime=systemDesignTime"
)


def _new_instance(short_name: str) -> IdsmModuleInstantiation:
    document = AUTOSAR.getInstance()
    ar_root = document.createARPackage("AUTOSAR")
    return IdsmModuleInstantiation(ar_root, short_name)


def _new_ref(value: str, dest: str) -> RefType:
    ref = RefType()
    ref.setDest(dest)
    ref.setValue(value)
    return ref


class TestIdsPlatformInstantiation:
    def test_abstract_class_cannot_be_instantiated(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")

        with pytest.raises(TypeError) as err:
            _obj = IdsPlatformInstantiation(ar_root, "test_idsplatforminstantiation")
        assert str(err.value) == "IdsPlatformInstantiation is an abstract class."

    def test_subclass_relationships(self):
        assert issubclass(IdsPlatformInstantiation, AtpStructureElement)
        assert issubclass(IdsmModuleInstantiation, IdsPlatformInstantiation)

    def test_class_docstring_is_spec_note(self):
        assert IdsPlatformInstantiation.__doc__.strip() == IDS_PLATFORM_NOTE

    def test_init_has_no_docstring(self):
        assert IdsPlatformInstantiation.__init__.__doc__ is None

    def test_add_network_interface_ref(self):
        inst = _new_instance("test_idsplatforminstantiation")
        ref = _new_ref("/AUTOSAR/config", "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION")

        assert inst.getNetworkInterfaceRefs() == []
        assert inst.addNetworkInterfaceRef(ref) is inst
        assert inst.getNetworkInterfaceRefs() == [ref]
        assert inst.addNetworkInterfaceRef(None) is inst
        assert inst.getNetworkInterfaceRefs() == [ref]

    def test_network_interface_accessor_docstrings(self):
        inst = _new_instance("test_idsplatforminstantiation")
        assert inst.addNetworkInterfaceRef.__doc__.strip().splitlines()[0] == NETWORK_INTERFACE_NOTE
        assert inst.getNetworkInterfaceRefs.__doc__.strip().splitlines()[0] == NETWORK_INTERFACE_NOTE

    def test_time_base_ref_round_trip(self):
        inst = _new_instance("test_idsplatforminstantiation")
        ref = _new_ref("/AUTOSAR/time_base", "TIME-BASE-RESOURCE")

        assert inst.getTimeBaseRef() is None
        assert inst.setTimeBaseRef(ref) is inst
        assert inst.getTimeBaseRef() is ref
        assert inst.setTimeBaseRef(None) is inst
        assert inst.getTimeBaseRef() is ref

    def test_time_base_accessor_docstrings(self):
        inst = _new_instance("test_idsplatforminstantiation")
        assert inst.getTimeBaseRef.__doc__.strip().splitlines()[0] == TIME_BASE_NOTE
        assert inst.setTimeBaseRef.__doc__.strip().splitlines()[0] == TIME_BASE_NOTE


class TestIdsmModuleInstantiation:
    def test_initialization(self):
        inst = _new_instance("test_idsmmoduleinstantiation")

        assert inst.short_name == "test_idsmmoduleinstantiation"
        assert inst.getNetworkInterfaceRefs() == []
        assert inst.getTimeBaseRef() is None

    def test_class_docstring_is_spec_note(self):
        assert IdsmModuleInstantiation.__doc__.strip() == IDSM_MODULE_NOTE

    def test_init_has_no_docstring(self):
        assert IdsmModuleInstantiation.__init__.__doc__ is None

    def test_no_spec_attributes(self):
        inst = _new_instance("test_idsmmoduleinstantiation")
        assert not hasattr(inst, "reportableSecurityEventRefs")
