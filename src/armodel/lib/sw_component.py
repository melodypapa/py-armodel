import logging

from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType
from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

class SwComponentAnalyzer:
    def __init__(self) -> None:
        self.swcs = []      # type: List[AtomicSwComponentType]

    def parse_pkg(self, parent: ARPackage):
        for pkg in parent.getARPackages():
            self.parse_pkg(pkg)
        for swc in parent.getSwComponentTypes():
            self.swcs.append(swc)

    def import_data(self, document: AUTOSAR):
        for pkg in document.getARPackages():
            self.parse_pkg(pkg)

    def print_out(self, option = {}):
        logger = logging.getLogger()

        logger.info("== SW-C LIST ==")

        if option['filter'] == 'CompositionSwComponent':
            swc_list = filter(lambda o: isinstance(o, CompositionSwComponentType), self.swcs)
        else:
            swc_list = self.swcs

        for swc in sorted(swc_list, key = lambda o: o.short_name):
            if option['format'] == 'long':
                logger.info("%s" % swc.full_name)
            else:
                logger.info("%s" % swc.short_name)