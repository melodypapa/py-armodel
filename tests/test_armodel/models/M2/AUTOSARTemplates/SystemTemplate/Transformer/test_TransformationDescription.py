import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import CategoryString
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.StereotypeMixins import VariationPointCapable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling import VariationPoint
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer import EndToEndTransformationDescription, TransformationDescription
from armodel.models.M2.MSR.AsamHdo.AdminData import AdminData
from armodel.models.M2.MSR.Documentation.TextModel.BlockElements import DocumentationBlock
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData import MultiLanguageOverviewParagraph


class TestTransformationDescription:
    """
    Model tests for TransformationDescription (Table 4.89).

    Abstract class (Base = ARObject, Describable) with no own attributes —
    exercised through its concrete subclass EndToEndTransformationDescription.
    """

    def test_initialization(self):
        with pytest.raises(TypeError):
            TransformationDescription()

        desc = EndToEndTransformationDescription()

        assert isinstance(desc, TransformationDescription)
        assert isinstance(desc, Describable)
        assert isinstance(desc, ARObject)
        assert isinstance(desc, VariationPointCapable)

        assert desc.getAdminData() is None
        assert desc.getCategory() is None
        assert desc.getDesc() is None
        assert desc.getIntroduction() is None
        assert desc.getVariationPoint() is None

    def test_get_set_admin_data(self):
        desc = EndToEndTransformationDescription()
        admin_data = AdminData()

        assert desc == desc.setAdminData(None)
        assert desc.getAdminData() is None

        assert desc == desc.setAdminData(admin_data)
        assert desc.getAdminData() == admin_data

        assert desc == desc.setAdminData(None)  # None no-op
        assert desc.getAdminData() == admin_data

    def test_get_set_category(self):
        desc = EndToEndTransformationDescription()
        category = CategoryString().setValue("myCategory")

        assert desc == desc.setCategory(None)
        assert desc.getCategory() is None

        assert desc == desc.setCategory(category)
        assert desc.getCategory() == category
        assert desc.getCategory().getValue() == "myCategory"

        assert desc == desc.setCategory(None)  # None no-op
        assert desc.getCategory() == category
        assert desc.getCategory().getValue() == "myCategory"

    def test_get_set_desc(self):
        desc = EndToEndTransformationDescription()
        paragraph = MultiLanguageOverviewParagraph()

        assert desc == desc.setDesc(None)
        assert desc.getDesc() is None

        assert desc == desc.setDesc(paragraph)
        assert desc.getDesc() == paragraph

        assert desc == desc.setDesc(None)  # None no-op
        assert desc.getDesc() == paragraph

    def test_get_set_introduction(self):
        desc = EndToEndTransformationDescription()
        block = DocumentationBlock()

        assert desc == desc.setIntroduction(None)
        assert desc.getIntroduction() is None

        assert desc == desc.setIntroduction(block)
        assert desc.getIntroduction() == block

        assert desc == desc.setIntroduction(None)  # None no-op
        assert desc.getIntroduction() == block

    def test_get_set_variation_point(self):
        desc = EndToEndTransformationDescription()
        variation_point = VariationPoint()

        assert desc == desc.setVariationPoint(None)
        assert desc.getVariationPoint() is None

        assert desc == desc.setVariationPoint(variation_point)
        assert desc.getVariationPoint() == variation_point

        assert desc == desc.setVariationPoint(None)  # None no-op
        assert desc.getVariationPoint() == variation_point
