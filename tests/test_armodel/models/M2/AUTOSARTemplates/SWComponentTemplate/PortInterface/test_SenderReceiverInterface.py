"""Unit tests for SenderReceiverInterface (AUTOSAR CP TPS SWCT Table 4.1)."""

from armodel.models import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import (
    VariableDataPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
    InvalidationPolicy,
    MetaDataItemSet,
    SenderReceiverInterface,
)


class TestSenderReceiverInterface:
    def setup_method(self):
        document = AUTOSAR.getInstance()
        document.clear()
        self.pkg = document.createARPackage("Pkg")
        self.sr = self.pkg.createSenderReceiverInterface("SR")

    def test_class_docstring_matches_spec_note(self):
        assert SenderReceiverInterface.__doc__ == "A sender/receiver interface declares a number of data elements to be sent and received."

    def test_heritage(self):
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import (
            ARObject,
        )
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import (
            DataInterface,
            PortInterface,
        )

        assert isinstance(self.sr, ARObject)
        assert isinstance(self.sr, DataInterface)
        assert isinstance(self.sr, PortInterface)
        assert isinstance(self.sr, SenderReceiverInterface)

    def test_init_defaults(self):
        assert self.sr.getShortName() == "SR"
        assert self.sr.getDataElements() == []
        assert self.sr.getInvalidationPolicies() == []
        assert self.sr.getMetaDataItemSets() == []

    def test_create_data_element_round_trip(self):
        element = self.sr.createDataElement("Elem")
        assert isinstance(element, VariableDataPrototype)
        assert element.getShortName() == "Elem"
        assert self.sr.getDataElements() == [element]
        assert self.sr.getDataElement("Elem") is element

    def test_create_data_element_is_idempotent(self):
        element1 = self.sr.createDataElement("Elem")
        element2 = self.sr.createDataElement("Elem")
        assert element1 is element2
        assert len(self.sr.getDataElements()) == 1

    def test_add_invalidation_policy_none_is_noop(self):
        result = self.sr.addInvalidationPolicy(None)
        assert result is self.sr
        assert self.sr.getInvalidationPolicies() == []

    def test_add_invalidation_policy_round_trip(self):
        policy = InvalidationPolicy()
        result = self.sr.addInvalidationPolicy(policy)
        assert result is self.sr
        assert self.sr.getInvalidationPolicies() == [policy]

    def test_create_invalidation_policy_round_trip(self):
        policy = self.sr.createInvalidationPolicy()
        assert isinstance(policy, InvalidationPolicy)
        assert self.sr.getInvalidationPolicies() == [policy]

    def test_add_meta_data_item_set_none_is_noop(self):
        result = self.sr.addMetaDataItemSet(None)
        assert result is self.sr
        assert self.sr.getMetaDataItemSets() == []

    def test_add_meta_data_item_set_round_trip(self):
        mapping_set = MetaDataItemSet()
        result = self.sr.addMetaDataItemSet(mapping_set)
        assert result is self.sr
        assert self.sr.getMetaDataItemSets() == [mapping_set]
