import pytest

from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable

from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject

from .... import AUTOSAR
from ....models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from ....models.M2.AUTOSARTemplates.SWComponentTemplate.data_type.data_prototypes import ApplicationArrayElement, ApplicationCompositeElementDataPrototype, ApplicationRecordElement, AtpPrototype, AutosarDataPrototype, DataPrototype, VariableDataPrototype
from ....models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpFeature

class Test_M2_AUTOSARTemplates_SWComponentTemplate_Datatype_DataPrototypes:

    def test_AtpPrototype(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            AtpPrototype(ar_root, "prototype")
        assert(str(err.value) == "AtpPrototype is an abstract class.")

    def test_DataPrototype(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            DataPrototype(ar_root, "prototype")
        assert(str(err.value) == "DataPrototype is an abstract class.")

    def test_AutosarDataPrototype(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            AutosarDataPrototype(ar_root, "prototype")
        assert(str(err.value) == "AutosarDataPrototype is an abstract class.")

    def test_VariableDataPrototype(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = VariableDataPrototype(ar_root, "prototype")

        assert(isinstance(prototype, ARObject))
        assert(isinstance(prototype, AtpFeature))
        assert(isinstance(prototype, AtpPrototype))
        assert(isinstance(prototype, AutosarDataPrototype))
        assert(isinstance(prototype, DataPrototype))
        assert(isinstance(prototype, Identifiable))
        assert(isinstance(prototype, MultilanguageReferrable))
        assert(isinstance(prototype, Referrable))

        assert(prototype._parent == ar_root)
        assert(prototype.short_name == "prototype")
        assert(prototype.typeTRef is None)

    def test_ApplicationCompositeElementDataPrototype(self):
        with pytest.raises(NotImplementedError) as err:
            document = AUTOSAR.getInstance()
            ar_root = document.createARPackage("AUTOSAR")
            ApplicationCompositeElementDataPrototype(ar_root, "application_composition_element_data_prototype")
        assert(str(err.value) == "ApplicationCompositeElementDataPrototype is an abstract class.")

    def test_ApplicationArrayElement(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = ApplicationArrayElement(ar_root, "prototype")

        assert(isinstance(prototype, ARObject))
        assert(isinstance(prototype, ApplicationCompositeElementDataPrototype))
        assert(isinstance(prototype, AtpFeature))
        assert(isinstance(prototype, AtpPrototype))
        assert(isinstance(prototype, DataPrototype))
        assert(isinstance(prototype, Identifiable))
        assert(isinstance(prototype, MultilanguageReferrable))
        assert(isinstance(prototype, Referrable))
        assert(isinstance(prototype, ApplicationArrayElement))

    def test_ApplicationRecordElement(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = ApplicationRecordElement(ar_root, "prototype")

        assert(isinstance(prototype, ARObject))
        assert(isinstance(prototype, ApplicationCompositeElementDataPrototype))
        assert(isinstance(prototype, AtpFeature))
        assert(isinstance(prototype, AtpPrototype))
        assert(isinstance(prototype, DataPrototype))
        assert(isinstance(prototype, Identifiable))
        assert(isinstance(prototype, MultilanguageReferrable))
        assert(isinstance(prototype, Referrable))
        assert(isinstance(prototype, ApplicationRecordElement))

        assert(prototype.isOptional == None)