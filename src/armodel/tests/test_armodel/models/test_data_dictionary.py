import pytest

from ....models.M2.MSR.DataDictionary.DataDefProperties import SwDataDefProps, SwPointerTargetProps
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

class Test_M2_MSR_DataDictionary_DataDefProperties:
    def test_SwDataDefProps(self):
        props = SwDataDefProps()

        assert(isinstance(props, ARObject))
        assert(isinstance(props, SwDataDefProps))

        assert(props.baseTypeRef == None)
        assert(props.compuMethodRef == None)
        assert(props.dataConstrRef == None)                 
        assert(props.implementationDataTypeRef == None)
        assert(props.swImplPolicy == None)
        assert(props.swCalibrationAccess == None)
        assert(props.swPointerTargetProps == None)

    def test_SwPointerTargetProps(self):
        props = SwPointerTargetProps()

        assert(isinstance(props, ARObject))
        assert(isinstance(props, SwPointerTargetProps))

        assert(props.getFunctionPointerSignatureRef() == None)
        assert(props.getSwDataDefProps() == None)
        assert(props.getTargetCategory() == None)