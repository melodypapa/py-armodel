import pytest

from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement, PackageableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpFeature
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from ....models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import Limit


class TestGeneralStructure:
    def test_ar_object(self):
        with pytest.raises(TypeError) as err:
            ARObject()
        assert (str(err.value) == "ARObject is an abstract class.")

    def test_Referrable(self):
        with pytest.raises(TypeError) as err:
            Referrable(AUTOSAR.getInstance(), "ar_referrable")
        assert (str(err.value) == "Referrable is an abstract class.")

    def test_MultilanguageReferrable(self):
        with pytest.raises(TypeError) as err:
            MultilanguageReferrable(AUTOSAR.getInstance(), "MultilanguageReferrable")
        assert (str(err.value) == "MultilanguageReferrable is an abstract class.")

    def test_CollectableElement(self):
        with pytest.raises(TypeError) as err:
            CollectableElement()
        assert (str(err.value) == "CollectableElement is an abstract class.")

    def test_Identifiable(self):
        with pytest.raises(TypeError) as err:
            Identifiable(AUTOSAR.getInstance(), "ar_identifiable")
        assert (str(err.value) == "Identifiable is an abstract class.")

    def test_AtpFeature(self):
        with pytest.raises(TypeError) as err:
            AtpFeature(AUTOSAR.getInstance(), "AtpFeature")
        assert (str(err.value) == "AtpFeature is an abstract class.")

    def test_packageable_element(self):
        with pytest.raises(TypeError) as err:
            PackageableElement(AUTOSAR.getInstance(), "ar_packageable_element")
        assert (str(err.value) == "PackageableElement is an abstract class.")

    def test_ar_element(self):
        with pytest.raises(TypeError) as err:
            ARElement(AUTOSAR.getInstance(), "ar_element")
        assert (str(err.value) == "ARElement is an abstract class.")

    def test_limit(self):
        limit = Limit()
        assert (limit.value is None)
        assert (limit.intervalType is None)
