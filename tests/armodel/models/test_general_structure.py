import pytest
from armodel.models.ar_package import AUTOSAR
from armodel.models.general_structure import ARElement, ARObject, AtpFeature, CollectableElement, Identifiable, Limit, MultilanguageReferrable, PackageableElement, Referrable

class TestGeneralStructure:
    def test_ar_object(self):
        with pytest.raises(NotImplementedError) as err:
            ARObject()
        assert(str(err.value) == "ARObject is an abstract class.")

    def test_Referrable(self):
        with pytest.raises(NotImplementedError) as err:
            Referrable(AUTOSAR.getInstance(), "ar_referrable")
        assert(str(err.value) == "Referrable is an abstract class.")

    def test_MultilanguageReferrable(self):
        with pytest.raises(NotImplementedError) as err:
            MultilanguageReferrable(AUTOSAR.getInstance(), "MultilanguageReferrable")
        assert(str(err.value) == "MultilanguageReferrable is an abstract class.")

    def test_CollectableElement(self):
        with pytest.raises(NotImplementedError) as err:
            CollectableElement()
        assert(str(err.value) == "CollectableElement is an abstract class.")

    def test_Identifiable(self):
        with pytest.raises(NotImplementedError) as err:
            Identifiable(AUTOSAR.getInstance(), "ar_identifiable")
        assert(str(err.value) == "Identifiable is an abstract class.")

    def test_AtpFeature(self):
        with pytest.raises(NotImplementedError) as err:
            AtpFeature(AUTOSAR.getInstance(), "AtpFeature")
        assert(str(err.value) == "AtpFeature is an abstract class.")

    def test_packageable_element(self):
        with pytest.raises(NotImplementedError) as err:
            PackageableElement(AUTOSAR.getInstance(), "ar_packageable_element")
        assert(str(err.value) == "PackageableElement is an abstract class.")

    def test_ar_element(self):
        with pytest.raises(NotImplementedError) as err:
            ARElement(AUTOSAR.getInstance(), "ar_element")
        assert(str(err.value) == "ARElement is an abstract class.")

    def test_limit(self):
        limit = Limit()
        assert(limit.value == None)
        assert(limit.interval_type == None)