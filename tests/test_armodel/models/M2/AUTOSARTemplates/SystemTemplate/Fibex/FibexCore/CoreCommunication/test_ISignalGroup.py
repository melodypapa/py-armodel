import inspect

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore import FibexElement
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication import ISignalGroup
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationISignalProps

CLASS_NOTE = (
    'SignalGroup of the Interaction Layer. The RTE supports a "signal fan-out" where the same System Signal Group '
    "is sent in different SignalIPdus to multiple receivers. An ISignalGroup refers to a set of ISignals that shall "
    "always be kept together. A ISignalGroup represents a COM Signal Group. Therefore it is recommended to put the "
    "ISignalGroup in the same Package as ISignals (see atp.recommendedPackage) Tags: atp.recommendedPackage=ISignalGroup"
)
CLASS_CONSTRAINTS = (
    "[constr_9225] Existence of ISignalGroup.systemSignalGroup: For each ISignalGroup, the reference to "
    "SystemSignalGroup in the role systemSignalGroup shall exist at the time when the System Description is complete."
)
NOTES = {
    "comBasedSignalGroupTransformationRef": (
        "Optional reference to a DataTransformation which represents the transformer chain that is used to transform "
        "the data that shall be placed inside this ISignalGroup based on the COMBasedTransformer approach. "
        "Stereotypes: atpSplitable; atpVariation Tags: atp.Splitkey=comBasedSignalGroupTransformation.data "
        "Transformation, comBasedSignalGroup Transformation.variationPoint.shortLabel "
        "vh.latestBindingTime=codeGenerationTime"
    ),
    "iSignalRefs": "Reference to a set of ISignals that shall always be kept together.",
    "systemSignalGroupRef": "Reference to the SystemSignalGroup that is defined on VFB level and that is supposed to be transmitted in the ISignalGroup.",
    "transformationISignalProps": (
        "A transformer chain consists of an ordered list of transformers. The ISignalGroup specific configuration "
        "properties for each transformer are defined in the TransformationISignalProps class. The transformer "
        "configuration properties that are common for all ISignal Groups are described in the TransformationTechnology "
        "class. Stereotypes: atpSplitable Tags: atp.Splitkey=transformationISignalProps"
    ),
}


class TestISignalGroup:
    """Test cases for ISignalGroup (Table 6.12, p.324)."""

    def test_inheritance(self):
        assert issubclass(ISignalGroup, FibexElement)

    def test_initialization_defaults(self):
        group = ISignalGroup(None, "Group")
        assert group.getComBasedSignalGroupTransformationRef() is None
        assert group.getISignalRefs() == []
        assert group.getSystemSignalGroupRef() is None
        assert group.getTransformationISignalProps() == []

    def test_get_set_com_based_signal_group_transformation_ref(self):
        group = ISignalGroup(None, "Group")

        ref = RefType()
        ref.value = "/transformations/data_transformation"
        assert group.setComBasedSignalGroupTransformationRef(ref) is group
        assert group.getComBasedSignalGroupTransformationRef() is ref
        group.setComBasedSignalGroupTransformationRef(None)
        assert group.getComBasedSignalGroupTransformationRef() is ref

    def test_get_set_system_signal_group_ref(self):
        group = ISignalGroup(None, "Group")

        ref = RefType()
        ref.value = "/system_signal_groups/ssg"
        assert group.setSystemSignalGroupRef(ref) is group
        assert group.getSystemSignalGroupRef() is ref
        group.setSystemSignalGroupRef(None)
        assert group.getSystemSignalGroupRef() is ref

    def test_add_refs_append_and_none_noop(self):
        group = ISignalGroup(None, "Group")

        ref = RefType()
        ref.value = "/isignals/signal1"
        assert group.addISignalRef(ref) is group
        assert group.getISignalRefs() == [ref]
        group.addISignalRef(None)
        assert group.getISignalRefs() == [ref]

    def test_add_transformation_isignal_props_append_and_none_noop(self):
        group = ISignalGroup(None, "Group")

        props = EndToEndTransformationISignalProps()
        assert group.addTransformationISignalProps(props) is group
        assert group.getTransformationISignalProps() == [props]
        group.addTransformationISignalProps(None)
        assert group.getTransformationISignalProps() == [props]

    def test_class_docstring_note(self):
        assert inspect.cleandoc(ISignalGroup.__doc__) == CLASS_NOTE + "\n\n" + CLASS_CONSTRAINTS

    def test_accessor_docstrings_verbatim(self):
        group = ISignalGroup(None, "Group")
        pairs = (
            ("getComBasedSignalGroupTransformationRef", "setComBasedSignalGroupTransformationRef", "comBasedSignalGroupTransformationRef"),
            ("getISignalRefs", "addISignalRef", "iSignalRefs"),
            ("getSystemSignalGroupRef", "setSystemSignalGroupRef", "systemSignalGroupRef"),
            ("getTransformationISignalProps", "addTransformationISignalProps", "transformationISignalProps"),
        )
        for getter_name, mutator_name, key in pairs:
            getter = getattr(group, getter_name)
            mutator = getattr(group, mutator_name)
            assert inspect.cleandoc(getter.__doc__) == NOTES[key], key
            assert inspect.cleandoc(mutator.__doc__).split("\n")[0] == NOTES[key], key

    def test_init_has_no_docstring(self):
        assert ISignalGroup.__init__.__doc__ is None
