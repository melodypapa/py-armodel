import pytest

from ....models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwPointerTargetProps
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class Test_M2_MSR_DataDictionary_DataDefProperties:
    def test_SwDataDefProps(self):
        props = SwDataDefProps()

        assert (isinstance(props, ARObject))
        assert (isinstance(props, SwDataDefProps))

        assert (props.baseTypeRef is None)
        assert (props.compuMethodRef is None)
        assert (props.dataConstrRef is None)
        assert (props.implementationDataTypeRef is None)
        assert (props.swImplPolicy is None)
        assert (props.swCalibrationAccess is None)
        assert (props.swPointerTargetProps is None)

    def test_SwPointerTargetProps(self):
        props = SwPointerTargetProps()

        assert (isinstance(props, ARObject))
        assert (isinstance(props, SwPointerTargetProps))

        assert (props.getFunctionPointerSignatureRef() is None)
        assert (props.getSwDataDefProps() is None)
        assert (props.getTargetCategory() is None)
