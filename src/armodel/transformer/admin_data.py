import logging
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import Describable, Identifiable
from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..transformer.abstract import AbstractTransformer


class AdminDataTransformer(AbstractTransformer):
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger()

    def process_pkg(self, pkg: ARPackage):
        for sub_package in pkg.getARPackages():
            self.process_pkg(sub_package)

        self.logger.debug("Remove AdminData of <%s>", pkg.getShortName())
        pkg.removeAdminData()

        for element in pkg.getElements():
            if isinstance(element, Describable):
                self.logger.debug("Remove AdminData of <%s>", element.getShortName())
                element.removeAdminData()
            elif isinstance(element, Identifiable):
                self.logger.debug("Remove AdminData of <%s>", element.getShortName())
                element.removeAdminData()

    def remove(self, root: AUTOSAR):
        root.removeAdminData()
        for pkg in root.getARPackages():
            self.process_pkg(pkg)
