import logging
from typing import List

from ..models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage

from ..models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from ..models.fibex.fibex_core.core_communication import SystemSignal

class SystemSignalAnalyzer:
    def __init__(self) -> None:
        self.system_signals = []      # type: List[SystemSignal]

    def add_system_signal(self, signal: SystemSignal):
        self.system_signals.append(signal)

    def get_system_signals(self) -> List[SystemSignal]:
        return self.system_signals
    
    def parse_pkg(self, parent: ARPackage):
        for pkg in parent.getARPackages():
            self.parse_pkg(pkg)
        for signal in parent.getSystemSignals():
            
            self.add_system_signal(signal)

    def import_data(self, document: AUTOSAR):
        for pkg in document.getARPackages():
            self.parse_pkg(pkg)

    def print_out(self, option = {}):
        logger = logging.getLogger()

        logger.info("== SYSTEM SIGNAL LIST ==")

        for signal in sorted(self.system_signals, key = lambda o: o.short_name):
            if option['format'] == 'full':
                logger.info("%s" % signal.full_name)
            else:
                logger.info("%s" % signal.short_name)