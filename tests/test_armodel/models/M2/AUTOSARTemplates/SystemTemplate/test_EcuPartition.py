"""Tests for the EcuPartition class (R23-11 SystemTemplate Table 5.7)."""

import inspect

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Boolean
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping import EcuPartition


def _bool(value):
    b = Boolean()
    b.setValue(value)
    return b


class TestEcuPartition:
    """
    Test class for EcuPartition functionality.

    Spec: R23-11/AUTOSAR_CP_TPS_SystemTemplate.pdf, Table 5.7, p.201 (R23-11)
    """

    MEMBERS = [
        "execInUserMode",
    ]

    def test_inheritance(self):
        assert issubclass(EcuPartition, Identifiable)

    def test_class_docstring_note(self):
        expected = (
            "Partitions are used as error containment regions. They permit the grouping of SWCs and resources "
            "and allow to describe recovery policies individually for each partition. Partitions can be terminated "
            "or restarted during run-time as a result of a detected error."
        )
        assert inspect.cleandoc(EcuPartition.__doc__) == expected

    def test_initialization_defaults(self):
        pkg = AUTOSAR.getInstance().createARPackage("EcuPartitionPkg")
        obj = EcuPartition(pkg, "Partition1")
        assert obj.getExecInUserMode() is None

    def test_member_order(self):
        pkg = AUTOSAR.getInstance().createARPackage("EcuPartitionPkg")
        obj = EcuPartition(pkg, "Partition1")
        members = [k for k in vars(obj) if k in set(self.MEMBERS)]
        assert members == self.MEMBERS

    def test_get_set_exec_in_user_mode(self):
        pkg = AUTOSAR.getInstance().createARPackage("EcuPartitionPkg")
        obj = EcuPartition(pkg, "Partition1")
        value = _bool(True)
        result = obj.setExecInUserMode(value)
        assert result is obj
        assert obj.getExecInUserMode() is value
        obj.setExecInUserMode(None)
        assert obj.getExecInUserMode() is value

    def test_ecuinstance_create_ecu_partition(self):
        pkg = AUTOSAR.getInstance().createARPackage("EcuPartitionPkg")
        ecu = pkg.createEcuInstance("EcuInst")
        partition = ecu.createEcuPartition("Partition1")
        assert isinstance(partition, EcuPartition)
        assert ecu.getPartitions() == [partition]
        again = ecu.createEcuPartition("Partition1")
        assert again is partition
        assert ecu.getPartitions() == [partition]
