import pytest

from armodel import AUTOSAR
from armodel.models.general_structure import ARObject
from armodel.models.m2_msr import Compu, CompuConst, CompuConstContent, CompuConstNumericContent, CompuConstTextContent, CompuContent, CompuScale, CompuScales

class Test_M2_MSR_AsamHdo_ComputationMethod:
    def test_CompuContent(self):
        with pytest.raises(NotImplementedError) as err:
            CompuContent()
        assert(str(err.value) == "CompuContent is an abstract class.")

    def test_Compu(self):
        compu = Compu()

        assert(isinstance(compu, ARObject))
        assert(isinstance(compu, Compu))

        assert(compu.compu_content == None)
        assert(compu.compu_default_value == None)

    def test_CompuConstContent(self):
        content = CompuConstContent()

        assert(isinstance(content, ARObject))
        assert(isinstance(content, CompuConstContent))

    def test_CompuConstTextContent(self):
        content = CompuConstTextContent()

        assert(isinstance(content, ARObject))
        assert(isinstance(content, CompuConstContent))
        assert(isinstance(content, CompuConstTextContent))

        assert(content.vt == None)

    def test_CompuConstNumericContent(self):
        content = CompuConstNumericContent()

        assert(isinstance(content, ARObject))
        assert(isinstance(content, CompuConstContent))
        assert(isinstance(content, CompuConstNumericContent))

        assert(content.v == None)

    def test_CompuConst(self):
        compu_const = CompuConst()

        assert(isinstance(compu_const, ARObject))
        assert(isinstance(compu_const, CompuConst))

        assert(compu_const.compu_const_content_type == None)

    def test_CompuScale(self):
        compu_scale = CompuScale()

        assert(isinstance(compu_scale, ARObject))
        assert(isinstance(compu_scale, CompuScale))

        assert(compu_scale.compu_content == None)
        assert(compu_scale.lower_limit == None)
        assert(compu_scale.upper_limit == None)
        assert(compu_scale.compu_inverse_value == None)
        assert(compu_scale.compu_scale_contents == None)

    def test_CompuScales(self):
        compu_scales = CompuScales()

        assert(isinstance(compu_scales, ARObject))
        assert(isinstance(compu_scales, CompuScales))

        assert(len(compu_scales.compu_scales) == 0)

        compu_scale = CompuScale()
        compu_scales.addCompuScale(compu_scale)

        assert(len(compu_scales.getCompuScales()) == 1)
        assert(compu_scales.getCompuScales()[0] == compu_scale)