"""
This module contains tests for the DataExchangePointKind enumeration.
"""

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import DataExchangePointKind


class TestDataExchangePointKind:
    def test_member_presence_and_values(self):
        assert DataExchangePointKind.AGREED == "AGREED"
        assert DataExchangePointKind.CONSUMER == "CONSUMER"
        assert DataExchangePointKind.PRODUCER == "PRODUCER"
        assert DataExchangePointKind.ALWAYS == "ALWAYS"
        assert DataExchangePointKind.MASKED_NEW_DIFFERS_MASKED_OLD == "MASKED-NEW-DIFFERS-MASKED-OLD"

    def test_instantiability(self):
        obj = DataExchangePointKind()
        assert isinstance(obj, DataExchangePointKind)
        obj.setValue(DataExchangePointKind.AGREED)
        assert obj.getValue() == "AGREED"
