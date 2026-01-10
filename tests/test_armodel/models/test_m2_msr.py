import pytest

from src.armodel import AUTOSAR
from src.armodel.models.M2.MSR.AsamHdo.ComputationMethod import Compu, CompuConst, CompuConstContent, CompuConstNumericContent, CompuConstTextContent
from src.armodel.models.M2.MSR.AsamHdo.ComputationMethod import CompuContent, CompuScale, CompuScales
from src.armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject


class Test_M2_MSR_AsamHdo_ComputationMethod:
    def test_CompuContent(self):
        with pytest.raises(NotImplementedError) as err:
            CompuContent()
        assert (str(err.value) == "CompuContent is an abstract class.")

    def test_Compu(self):
        compu = Compu()

        assert (isinstance(compu, ARObject))
        assert (isinstance(compu, Compu))

        assert (compu.compuContent is None)
        assert (compu.compuDefaultValue is None)

    def test_CompuConstContent(self):
        with pytest.raises(NotImplementedError) as err:
            CompuConstContent()
        assert (str(err.value) == "CompuConstContent is an abstract class.")

    def test_CompuConstTextContent(self):
        content = CompuConstTextContent()

        assert (isinstance(content, ARObject))
        assert (isinstance(content, CompuConstContent))
        assert (isinstance(content, CompuConstTextContent))

        assert (content.vt is None)

    def test_CompuConstNumericContent(self):
        content = CompuConstNumericContent()

        assert (isinstance(content, ARObject))
        assert (isinstance(content, CompuConstContent))
        assert (isinstance(content, CompuConstNumericContent))

        assert (content.v is None)

    def test_CompuConst(self):
        compu_const = CompuConst()

        assert (isinstance(compu_const, ARObject))
        assert (isinstance(compu_const, CompuConst))

        assert (compu_const.compuConstContentType is None)

    def test_CompuScale(self):
        compu_scale = CompuScale()

        assert (isinstance(compu_scale, ARObject))
        assert (isinstance(compu_scale, CompuScale))

        assert (compu_scale.compuContent is None)
        assert (compu_scale.lowerLimit is None)
        assert (compu_scale.upperLimit is None)
        assert (compu_scale.compuInverseValue is None)
        assert (compu_scale.compuScaleContents is None)

    def test_CompuScales(self):
        compu_scales = CompuScales()

        assert (isinstance(compu_scales, ARObject))
        assert (isinstance(compu_scales, CompuScales))

        assert (len(compu_scales.compuScales) == 0)

        compu_scale = CompuScale()
        compu_scales.addCompuScale(compu_scale)

        assert (len(compu_scales.getCompuScales()) == 1)
        assert (compu_scales.getCompuScales()[0] == compu_scale)
