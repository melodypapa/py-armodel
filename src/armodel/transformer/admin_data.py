import logging

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import (
    ARPackage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Describable,
    Identifiable,
)
from armodel.transformer.abstract import AbstractTransformer


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
            if isinstance(element, Describable) or isinstance(element, Identifiable):
                self.logger.debug("Remove AdminData of <%s>", element.getShortName())
                element.removeAdminData()

    def remove(self, root: AUTOSAR):
        root.removeAdminData()
        for pkg in root.getARPackages():
            self.process_pkg(pkg)
