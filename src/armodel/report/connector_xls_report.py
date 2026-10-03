from typing import List, Optional

from armodel.models import AUTOSAR, PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType
from armodel.report.excel_report import ExcelReporter


class ConnectorXlsReport(ExcelReporter):
    """
    Generates Excel reports for assembly and delegation SW connectors
    from CompositionSwComponentType instances.
    """

    def __init__(self) -> None:
        super().__init__()
        self.swcs: List[CompositionSwComponentType] = []

    def _ref_value(self, ref: Optional[RefType]) -> Optional[str]:
        return ref.value if ref is not None else None

    def _parse_pkg(self, parent: ARPackage):
        for pkg in parent.getARPackages():
            self._parse_pkg(pkg)
        for swc in parent.getSwComponentTypes():
            if isinstance(swc, CompositionSwComponentType):
                self.swcs.append(swc)

    def import_data(self, document: AUTOSAR):
        for pkg in document.getARPackages():
            self._parse_pkg(pkg)

    def _write_assembly_sw_connection(self, swc: CompositionSwComponentType, index=0):
        sheet = self.wb.create_sheet("%s - AC" % swc.short_name, index)
        title_row = ["Short Name", "Provide SW-C", "PPort", "Request SW-C", "RPort"]
        self.write_title_row(sheet, title_row)

        row = 2
        for connector in swc.getAssemblySwConnectors():
            self._logger.debug("Write AssemblySwConnection %s" % connector.short_name)
            self.write_cell(sheet, row, 1, connector.short_name)
            provider_iref = connector.providerIRef
            if provider_iref is not None:
                self.write_cell(sheet, row, 2, self._ref_value(provider_iref.contextComponentRef))
                self.write_cell(sheet, row, 3, self._ref_value(provider_iref.targetPPortRef))
            requester_iref = connector.requesterIRef
            if requester_iref is not None:
                self.write_cell(sheet, row, 4, self._ref_value(requester_iref.contextComponentRef))
                self.write_cell(sheet, row, 5, self._ref_value(requester_iref.targetRPortRef))
            row += 1

        self.auto_width(sheet)

    def _write_delegation_sw_connection(self, swc: CompositionSwComponentType, index=0):
        sheet = self.wb.create_sheet("%s - DC" % swc.short_name, index)
        title_row = ["Short Name", "Inner SW-C", "Inner PPort", "Outer PPort", "Inner RPort", "Outer RPort"]
        self.write_title_row(sheet, title_row)

        row = 2
        for connector in swc.getDelegationSwConnectors():
            self._logger.debug("Write DelegationSwConnection %s" % connector.short_name)
            self.write_cell(sheet, row, 1, connector.short_name)

            inner_port_iref = connector.innerPortIRef
            if inner_port_iref is not None and isinstance(inner_port_iref, PPortInCompositionInstanceRef):
                self.write_cell(sheet, row, 2, self._ref_value(inner_port_iref.contextComponentRef))
                self.write_cell(sheet, row, 3, self._ref_value(inner_port_iref.targetPPortRef))
            elif inner_port_iref is not None and isinstance(inner_port_iref, RPortInCompositionInstanceRef):
                self.write_cell(sheet, row, 2, self._ref_value(inner_port_iref.contextComponentRef))
                self.write_cell(sheet, row, 5, self._ref_value(inner_port_iref.targetRPortRef))

            outer_port_ref = connector.outerPortRef
            if outer_port_ref is not None:
                if outer_port_ref.dest == "P-PORT-PROTOTYPE":
                    self.write_cell(sheet, row, 4, self._ref_value(outer_port_ref))
                elif outer_port_ref.dest == "R-PORT-PROTOTYPE":
                    self.write_cell(sheet, row, 6, self._ref_value(outer_port_ref))
                else:
                    raise ValueError("Invalid OUTER-PORT-REF of SwConnector <%s>" % connector.short_name)
            row += 1

        self.auto_width(sheet)

    def write(self, filename: str):
        swc_list = filter(lambda o: isinstance(o, CompositionSwComponentType), self.swcs)

        idx = 1
        for swc in sorted(swc_list, key=lambda o: o.short_name):
            self._logger.info("CompositionSwComponentType %s" % swc.short_name)
            self._write_assembly_sw_connection(swc, idx)
            self._write_delegation_sw_connection(swc, idx + 1)
            idx += 2

        self.wb.save(filename)
