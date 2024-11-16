from ..models.M2.autosar_templates.generic_structure.ar_package import ARPackage
from .excel_report import ExcelReporter
from ..models import AUTOSAR, CompositionSwComponentType
from ..models import PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from typing import List

class ConnectorXlsReport(ExcelReporter):
    def __init__(self) -> None:
        super().__init__()
        self.swcs = []              # type: List[CompositionSwComponentType]

    def _parse_pkg(self, parent: ARPackage):
        for pkg in parent.getARPackages():
            self._parse_pkg(pkg)
        for swc in parent.getSwComponentTypes():
            self.swcs.append(swc)

    def import_data(self, document: AUTOSAR):
        for pkg in document.getARPackages():
            self._parse_pkg(pkg)

    def _write_assembly_sw_connection(self, swc: CompositionSwComponentType, index = 0):
        sheet = self.wb.create_sheet("%s - AC" % swc.short_name, index)
        title_row = ["Short Name", "Provide SW-C", "PPort", "Request SW-C", "RPort"]
        self.write_title_row(sheet, title_row)

        row = 2
        for connector in swc.getAssemblySwConnectors():
            self._logger.debug("Write AssemblySwConnection %s" % connector.short_name)
            self.write_cell(sheet, row, 1, connector.short_name)
            self.write_cell(sheet, row, 2, connector.provider_iref.context_component_ref.value)
            self.write_cell(sheet, row, 3, connector.provider_iref.target_p_port_ref.value)
            self.write_cell(sheet, row, 4, connector.requester_iref.context_component_ref.value)
            self.write_cell(sheet, row, 5, connector.requester_iref.target_r_port_ref.value)
            row += 1

        self.auto_width(sheet)

    def _write_delegation_sw_connection(self, swc: CompositionSwComponentType, index = 0):
        sheet = self.wb.create_sheet("%s - DC" % swc.short_name, index)
        title_row = ["Short Name", "Inner SW-C", "Inner PPort", "Outer PPort", "Inner RPort", "Outer RPort"]
        self.write_title_row(sheet, title_row)

        row = 2
        for connector in swc.getDelegationSwConnectors():
            self._logger.debug("Write DelegationSwConnection %s" % connector.short_name)
            self.write_cell(sheet, row, 1, connector.short_name)

            if connector.inner_port_iref:
                if isinstance(connector.inner_port_iref, PPortInCompositionInstanceRef):
                    self.write_cell(sheet, row, 2, connector.inner_port_iref.context_component_ref.value)
                    self.write_cell(sheet, row, 3, connector.inner_port_iref.target_p_port_ref.value)
                elif isinstance(connector.inner_port_iref, RPortInCompositionInstanceRef):
                    self.write_cell(sheet, row, 2, connector.inner_port_iref.context_component_ref.value)
                    self.write_cell(sheet, row, 5, connector.inner_port_iref.target_r_port_ref.value)

            if connector.outer_port_ref.dest == "P-PORT-PROTOTYPE":
                self.write_cell(sheet, row, 4, connector.outer_port_ref.value)
            elif connector.outer_port_ref.dest == "R-PORT-PROTOTYPE":
                self.write_cell(sheet, row, 6, connector.outer_port_ref.value)
            else:
                raise ValueError("Invalid OUTER-PORT-REF of SwConnector <%s>" % connector.short_name)
            row += 1

        self.auto_width(sheet)

    def write(self, filename: str):
        swc_list = filter(lambda o: isinstance(o, CompositionSwComponentType), self.swcs)
        
        idx = 1
        for swc in sorted(swc_list, key = lambda o: o.short_name):
            self._logger.info("CompositionSwComponentType %s" % swc.short_name)
            self._write_assembly_sw_connection(swc, idx)
            self._write_delegation_sw_connection(swc, idx + 1)
            idx += 2

        self.wb.save(filename)