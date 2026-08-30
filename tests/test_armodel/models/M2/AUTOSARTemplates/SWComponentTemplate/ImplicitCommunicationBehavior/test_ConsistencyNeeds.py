from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.AbstractBlueprintStructure import AtpBlueprintable
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.ImplicitCommunicationBehavior import (
    ConsistencyNeeds,
    DataPrototypeGroup,
    RunnableEntityGroup,
)


class TestConsistencyNeedsInitialization:
    def test_initialization(self):
        """Test ConsistencyNeeds __init__ defaults"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        assert consistency_needs is not None
        assert isinstance(consistency_needs, ConsistencyNeeds)
        assert isinstance(consistency_needs, AtpBlueprintable)
        assert consistency_needs.getShortName() == "Needs"
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == []
        assert consistency_needs.getDpgRequiresCoherencys() == []
        assert consistency_needs.getRegDoesNotRequireStabilitys() == []
        assert consistency_needs.getRegRequiresStabilitys() == []


class TestConsistencyNeedsDpgDoesNotRequireCoherency:
    def test_create_get(self):
        """Test createDpgDoesNotRequireCoherency and getDpgDoesNotRequireCoherencys"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        data_group = consistency_needs.createDpgDoesNotRequireCoherency("Group")
        assert isinstance(data_group, DataPrototypeGroup)
        assert consistency_needs.getDpgDoesNotRequireCoherencys() == [data_group]

    def test_create_existing_returns_same(self):
        """Test creating a dpgDoesNotRequireCoherency with the same short name returns the existing one"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        data_group = consistency_needs.createDpgDoesNotRequireCoherency("Group")
        data_group_2 = consistency_needs.createDpgDoesNotRequireCoherency("Group")
        assert data_group is data_group_2


class TestConsistencyNeedsDpgRequiresCoherency:
    def test_create_get(self):
        """Test createDpgRequiresCoherency and getDpgRequiresCoherencys"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        data_group = consistency_needs.createDpgRequiresCoherency("Group")
        assert isinstance(data_group, DataPrototypeGroup)
        assert consistency_needs.getDpgRequiresCoherencys() == [data_group]


class TestConsistencyNeedsRegDoesNotRequireStability:
    def test_create_get(self):
        """Test createRegDoesNotRequireStability and getRegDoesNotRequireStabilitys"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        runnable_group = consistency_needs.createRegDoesNotRequireStability("Group")
        assert isinstance(runnable_group, RunnableEntityGroup)
        assert consistency_needs.getRegDoesNotRequireStabilitys() == [runnable_group]


class TestConsistencyNeedsRegRequiresStability:
    def test_create_get(self):
        """Test createRegRequiresStability and getRegRequiresStabilitys"""
        parent = AUTOSAR.getInstance()
        ar_root = parent.createARPackage("AUTOSAR")
        consistency_needs = ConsistencyNeeds(ar_root, "Needs")

        runnable_group = consistency_needs.createRegRequiresStability("Group")
        assert isinstance(runnable_group, RunnableEntityGroup)
        assert consistency_needs.getRegRequiresStabilitys() == [runnable_group]
