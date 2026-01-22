import pytest

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import PackageableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpFeature
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import CollectableElement
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Identifiable, MultilanguageReferrable, Referrable
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject import ARObject
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import AtpPrototype, AutosarDataPrototype, DataPrototype
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes import VariableDataPrototype
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure import AtpType
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import ARElement
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ApplicationError, ArgumentDataPrototype, ClientServerInterface
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ClientServerOperation, DataInterface, NvDataInterface
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import ParameterInterface, PortInterface, SenderReceiverInterface


class Test_M2_AUTOSARTemplates_SWComponentTemplate_PortInterface:

    def test_PortInterface(self):
        with pytest.raises(TypeError) as err:
            PortInterface(AUTOSAR.getInstance(), "PortInterface")
        assert (str(err.value) == "PortInterface is an abstract class.")

    def test_DataInterface(self):
        with pytest.raises(TypeError) as err:
            DataInterface(AUTOSAR.getInstance(), "DataInterface")
        assert (str(err.value) == "DataInterface is an abstract class.")

    def test_NvDataInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = NvDataInterface(ar_root, "NvDataInterface")

        assert (isinstance(data_if, ARElement))
        assert (isinstance(data_if, ARObject))
        # assert (isinstance(sr, AtpBlueprint))
        # assert (isinstance(sr, AtpBlueprintable))
        # assert (isinstance(sr, AtpClassifier))
        assert (isinstance(data_if, AtpType))
        assert (isinstance(data_if, CollectableElement))
        assert (isinstance(data_if, DataInterface))
        assert (isinstance(data_if, Identifiable))
        assert (isinstance(data_if, MultilanguageReferrable))
        assert (isinstance(data_if, PackageableElement))
        assert (isinstance(data_if, PortInterface))
        assert (isinstance(data_if, Referrable))
        assert (isinstance(data_if, NvDataInterface))

        assert (data_if.parent == ar_root)
        assert (data_if.short_name == "NvDataInterface")

    def test_ParameterInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        data_if = ParameterInterface(ar_root, "ParameterInterface")

        assert (isinstance(data_if, ARElement))
        assert (isinstance(data_if, ARObject))
        # assert (isinstance(sr, AtpBlueprint))
        # assert (isinstance(sr, AtpBlueprintable))
        # assert (isinstance(sr, AtpClassifier))
        assert (isinstance(data_if, AtpType))
        assert (isinstance(data_if, CollectableElement))
        assert (isinstance(data_if, DataInterface))
        assert (isinstance(data_if, Identifiable))
        assert (isinstance(data_if, MultilanguageReferrable))
        assert (isinstance(data_if, PackageableElement))
        assert (isinstance(data_if, PortInterface))
        assert (isinstance(data_if, Referrable))
        assert (isinstance(data_if, ParameterInterface))

        assert (data_if.parent == ar_root)
        assert (data_if.short_name == "ParameterInterface")

    def test_SenderReceiverInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        sr_if = SenderReceiverInterface(ar_root, "sr_if")

        assert (isinstance(sr_if, ARElement))
        assert (isinstance(sr_if, ARObject))
        # assert (isinstance(sr, AtpBlueprint))
        # assert (isinstance(sr, AtpBlueprintable))
        # assert (isinstance(sr, AtpClassifier))
        assert (isinstance(sr_if, AtpType))
        assert (isinstance(sr_if, CollectableElement))
        assert (isinstance(sr_if, DataInterface))
        assert (isinstance(sr_if, Identifiable))
        assert (isinstance(sr_if, MultilanguageReferrable))
        assert (isinstance(sr_if, PackageableElement))
        assert (isinstance(sr_if, PortInterface))
        assert (isinstance(sr_if, Referrable))
        assert (isinstance(sr_if, SenderReceiverInterface))

        assert (sr_if.getShortName() == "sr_if")
        assert (sr_if.parent == ar_root)
        assert (len(sr_if.getDataElements()) == 0)

        element = sr_if.createDataElement("element")
        assert (isinstance(element, VariableDataPrototype))
        assert (element.getShortName() == "element")
        assert (len(sr_if.getDataElements()) == 1)

        element2 = sr_if.getDataElement("element")
        assert (element == element2)

    def test_ArgumentDataPrototype(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        prototype = ArgumentDataPrototype(ar_root, "ArgumentDataPrototype")

        assert (isinstance(prototype, ARObject))
        assert (isinstance(prototype, AtpFeature))
        assert (isinstance(prototype, AtpPrototype))
        assert (isinstance(prototype, AutosarDataPrototype))
        assert (isinstance(prototype, DataPrototype))
        assert (isinstance(prototype, Identifiable))
        assert (isinstance(prototype, MultilanguageReferrable))
        assert (isinstance(prototype, Referrable))
        assert (isinstance(prototype, ArgumentDataPrototype))

        assert (prototype.getParent() == ar_root)
        assert (prototype.getShortName() == "ArgumentDataPrototype")
        assert (prototype.getDirection() is None)
        assert (prototype.getServerArgumentImplPolicy() is None)

    def test_ApplicationError(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        app_error = ApplicationError(ar_root, "ApplicationError")

        assert (isinstance(app_error, ARObject))
        assert (isinstance(app_error, Identifiable))
        assert (isinstance(app_error, MultilanguageReferrable))
        assert (isinstance(app_error, Referrable))
        assert (isinstance(app_error, ApplicationError))

        assert (app_error.parent == ar_root)
        assert (app_error.short_name == "ApplicationError")

    def test_ClientServerOperation(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        operation = ClientServerOperation(ar_root, "client_server_operation")
        assert (isinstance(operation, ARObject))
        # assert (isinstance(operation, AtpClassifier))
        assert (isinstance(operation, AtpFeature))
        assert (isinstance(operation, Identifiable))
        assert (isinstance(operation, MultilanguageReferrable))
        assert (isinstance(operation, Referrable))
        assert (isinstance(operation, ClientServerOperation))
        assert (operation.short_name == "client_server_operation")

        prototype = operation.createArgumentDataPrototype(
            "argument_data_prototype1")
        assert (prototype.short_name == "argument_data_prototype1")

        assert (len(operation.getArguments()) == 1)
        assert (operation.getArguments()[0] == prototype)

        refType = RefType()
        refType.dest = "APPLICATION-ERROR"
        refType.value = "/AUTOSAR_NvM/PortInterfaces/NvMService/E_NOT_OK"
        operation.addPossibleErrorRef(refType)

        assert (len(operation.getPossibleErrorRefs()) == 1)
        assert (operation.getPossibleErrorRefs()[0] == refType)

    def test_ClientServerInterface(self):
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        cs_if = ClientServerInterface(ar_root, "client_server_interface")
        assert (isinstance(cs_if, ARObject))
        assert (isinstance(cs_if, ARElement))
        # assert (isinstance(operation, AtpBlueprint))
        # assert (isinstance(operation, AtpBlueprintable))
        # assert (isinstance(operation, AtpClassifier))
        assert (isinstance(cs_if, AtpType))
        assert (isinstance(cs_if, CollectableElement))
        assert (isinstance(cs_if, Identifiable))
        assert (isinstance(cs_if, MultilanguageReferrable))
        assert (isinstance(cs_if, PackageableElement))
        assert (isinstance(cs_if, PortInterface))
        assert (isinstance(cs_if, Referrable))

        element = cs_if.createOperation("operation")
        assert (isinstance(element, ClientServerOperation))
        assert (element.short_name == "operation")
        assert (len(cs_if.getOperations()) == 1)

        element2 = cs_if.getOperations()[0]
        assert (element == element2)

        element = cs_if.createApplicationError("error")
        assert (isinstance(element, ApplicationError))
        assert (element.short_name == "error")
        assert (len(cs_if.getPossibleErrors()) == 1)

        element2 = cs_if.getPossibleErrors()[0]
        assert (element == element2)
    
    def test_NvDataInterface_serviceKind(self):
        """Test NvDataInterface getServiceKind method to cover line 42 in PortInterface/__init__.py"""
        from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface import NvDataInterface
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARLiteral
        document = AUTOSAR.getInstance()
        ar_root = document.createARPackage("AUTOSAR")
        nv_data_if = NvDataInterface(ar_root, "NvDataInterface")

        # Test getServiceKind - this should return self.serviceKind
        service_kind = nv_data_if.getServiceKind()
        # NvDataInterface inherits from PortInterface, so it should have serviceKind attribute
        # This test covers line 42 in PortInterface/__init__.py

        # Test setServiceKind to cover lines 45-46
        ar_literal = ARLiteral()
        nv_data_if.setServiceKind(ar_literal)
        assert nv_data_if.getServiceKind() == ar_literal
        assert nv_data_if == nv_data_if.setServiceKind(ar_literal)  # Test method chaining

        # Test setIsService and getIsService to cover lines 35, 38-39
        from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import ARBoolean
        ar_bool = ARBoolean()
        nv_data_if.setIsService(ar_bool)
        assert nv_data_if.getIsService() == ar_bool
        assert nv_data_if == nv_data_if.setIsService(ar_bool)  # Test method chaining

