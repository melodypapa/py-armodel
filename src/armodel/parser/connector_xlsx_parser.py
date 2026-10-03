import re
from typing import Dict, List

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet

from armodel.data_models.sw_connector import AssemblySwConnectorData, DelegationSwConnectorData, SwConnectorData
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage import ARPackage
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import RefType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition import CompositionSwComponentType
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Composition.InstanceRefs import PPortInCompositionInstanceRef, RPortInCompositionInstanceRef
from armodel.parser.excel_parser import AbstractExcelParser


class ConnectorXls:
    """
    Constants class defining column names for connector Excel worksheets.
    """

    COL_SHORT_NAME = "Short Name"
    COL_INNER_SW_C = "Inner SW-C"
    COL_INNER_PPORT = "Inner PPort"
    COL_OUTER_PPORT = "Outer PPort"
    COL_INNER_RPORT = "Inner RPort"
    COL_OUTER_RPORT = "Outer RPort"

    COL_PROVIDER_SW_C = "Provide SW-C"
    COL_PPORT = "PPort"
    COL_REQUESTER_SW_C = "Request SW-C"
    COL_RPORT = "RPort"


class ConnectorXlsReader(AbstractExcelParser):
    """
    Reads connector definitions from Excel worksheets and maps them to
    AssemblySwConnectorData and DelegationSwConnectorData.
    """

    def __init__(self) -> None:
        super().__init__()

        self.column_delegation_sw_connectors = {
            ConnectorXls.COL_SHORT_NAME: -1,
            ConnectorXls.COL_INNER_SW_C: -1,
            ConnectorXls.COL_INNER_PPORT: -1,
            ConnectorXls.COL_OUTER_PPORT: -1,
            ConnectorXls.COL_INNER_RPORT: -1,
            ConnectorXls.COL_OUTER_RPORT: -1,
        }

        self.column_assembly_sw_connectors = {
            ConnectorXls.COL_SHORT_NAME: -1,
            ConnectorXls.COL_PROVIDER_SW_C: -1,
            ConnectorXls.COL_PPORT: -1,
            ConnectorXls.COL_REQUESTER_SW_C: -1,
            ConnectorXls.COL_RPORT: -1,
        }

        self.sw_connectors: Dict[str, List[SwConnectorData]] = {}

    def getCompositionSwComponentList(self) -> List[str]:
        return list(self.sw_connectors.keys())

    def getSwConnectorList(self, swc: str) -> List[SwConnectorData]:
        if swc not in self.sw_connectors:
            self.sw_connectors[swc] = []
        return self.sw_connectors[swc]
        # return sorted(self.sw_connectors[swc], key = lambda o: o.short_name)

    def readDelegationSwConnectors(self, sheet: Worksheet, swc: str, start_row: int, column_list: Dict[str, int]):
        connectors = self.getSwConnectorList(swc)
        for row in sheet.iter_rows(min_row=start_row, values_only=True):
            connector = DelegationSwConnectorData()
            connector.short_name = row[column_list[ConnectorXls.COL_SHORT_NAME]]
            connector.inner_swc = row[column_list[ConnectorXls.COL_INNER_SW_C]]
            connector.inner_pport = row[column_list[ConnectorXls.COL_INNER_PPORT]]
            connector.inner_rport = row[column_list[ConnectorXls.COL_INNER_RPORT]]
            connector.outer_pport = row[column_list[ConnectorXls.COL_OUTER_PPORT]]
            connector.outer_rport = row[column_list[ConnectorXls.COL_OUTER_RPORT]]
            connectors.append(connector)
            self._logger.debug("ShortName: %s" % connector.short_name)

    def readAssemblySwConnectors(self, sheet: Worksheet, swc: str, start_row: int, column_list: Dict[str, int]):
        connectors = self.getSwConnectorList(swc)
        for row in sheet.iter_rows(min_row=start_row, values_only=True):
            connector = AssemblySwConnectorData()
            connector.short_name = row[column_list[ConnectorXls.COL_SHORT_NAME]]
            connector.provider_swc = row[column_list[ConnectorXls.COL_PROVIDER_SW_C]]
            connector.p_port = row[column_list[ConnectorXls.COL_PPORT]]
            connector.r_swc = row[column_list[ConnectorXls.COL_REQUESTER_SW_C]]
            connector.r_port = row[column_list[ConnectorXls.COL_RPORT]]
            connectors.append(connector)
            self._logger.debug("ShortName: %s" % connector.short_name)

    def parseDelegationSWConnectors(self, sheet: Worksheet, swc: str):
        self._logger.debug("Parse all DelegationSwConnector of %s" % swc)

        self.getColumnTitles(sheet, 1, self.column_delegation_sw_connectors)
        self.checkColumnTitles(self.column_delegation_sw_connectors, "Invalid DelegationSwConnectors Excel and column <%s> cannot be located.")
        self.readDelegationSwConnectors(sheet, swc, 2, self.column_delegation_sw_connectors)

    def parseAssemblySWConnectors(self, sheet: Worksheet, swc: str):
        self._logger.debug("Parse all AssemblySwConnector of %s" % swc)

        self.getColumnTitles(sheet, 1, self.column_assembly_sw_connectors)
        self.checkColumnTitles(self.column_assembly_sw_connectors, "Invalid AssemblySwConnectors Excel and column <%s> cannot be located.")
        self.readAssemblySwConnectors(sheet, swc, 2, self.column_assembly_sw_connectors)

    def read(self, excel_file: str):
        self._logger.info("Parse excel file <%s>" % excel_file)

        wb = openpyxl.load_workbook(excel_file, data_only=True)

        for name in wb.sheetnames:
            m = re.match(r"(\w+)\s+-\s+(AC|DC)", name)
            if m:
                if m.group(2) == "DC":
                    self.parseDelegationSWConnectors(wb[name], m.group(1))
                elif m.group(2) == "AC":
                    self.parseAssemblySWConnectors(wb[name], m.group(1))
                else:
                    raise ValueError("Invalid sheet")

    def _addAssemblySwConnector(self, swc: CompositionSwComponentType, connector: AssemblySwConnectorData):
        sw_connector = swc.createAssemblySwConnector(connector.short_name)

        sw_connector.providerIRef = PPortInCompositionInstanceRef()
        sw_connector.providerIRef.contextComponentRef = RefType()
        sw_connector.providerIRef.targetPPortRef = RefType()
        sw_connector.providerIRef.contextComponentRef.dest = "SW-COMPONENT-PROTOTYPE"
        sw_connector.providerIRef.contextComponentRef.value = connector.provider_swc
        sw_connector.providerIRef.targetPPortRef.dest = "P-PORT-PROTOTYPE"
        sw_connector.providerIRef.targetPPortRef.value = connector.p_port

        sw_connector.requesterIRef = RPortInCompositionInstanceRef()
        sw_connector.requesterIRef.contextComponentRef = RefType()
        sw_connector.requesterIRef.targetRPortRef = RefType()
        sw_connector.requesterIRef.contextComponentRef.dest = "SW-COMPONENT-PROTOTYPE"
        sw_connector.requesterIRef.contextComponentRef.value = connector.r_swc
        sw_connector.requesterIRef.targetRPortRef.dest = "R-PORT-PROTOTYPE"
        sw_connector.requesterIRef.targetRPortRef.value = connector.r_port

    def _addDelegationSwConnector(self, swc: CompositionSwComponentType, connector: DelegationSwConnectorData):
        sw_connector = swc.createDelegationSwConnector(connector.short_name)
        if connector.inner_pport is not None and connector.outer_pport is not None:
            sw_connector.innerPortIRef = PPortInCompositionInstanceRef()
            sw_connector.innerPortIRef.contextComponentRef = RefType()
            sw_connector.innerPortIRef.targetPPortRef = RefType()
            sw_connector.outerPortRef = RefType()
            sw_connector.innerPortIRef.contextComponentRef.dest = "SW-COMPONENT-PROTOTYPE"
            sw_connector.innerPortIRef.contextComponentRef.value = connector.inner_swc
            sw_connector.innerPortIRef.targetPPortRef.dest = "P-PORT-PROTOTYPE"
            sw_connector.innerPortIRef.targetPPortRef.value = connector.inner_pport
            sw_connector.outerPortRef.dest = "P-PORT-PROTOTYPE"
            sw_connector.outerPortRef.value = connector.outer_pport
        elif connector.inner_rport is not None and connector.outer_rport is not None:
            sw_connector.innerPortIRef = RPortInCompositionInstanceRef()
            sw_connector.innerPortIRef.contextComponentRef = RefType()
            sw_connector.innerPortIRef.targetRPortRef = RefType()
            sw_connector.outerPortRef = RefType()
            sw_connector.innerPortIRef.contextComponentRef.dest = "SW-COMPONENT-PROTOTYPE"
            sw_connector.innerPortIRef.contextComponentRef.value = connector.inner_swc
            sw_connector.innerPortIRef.targetRPortRef.dest = "R-PORT-PROTOTYPE"
            sw_connector.innerPortIRef.targetRPortRef.value = connector.inner_rport
            sw_connector.outerPortRef.dest = "R-PORT-PROTOTYPE"
            sw_connector.outerPortRef.value = connector.outer_rport
        else:
            raise ValueError("Invalid DelegationSwConnector Configuration")

    def _updateCompositionSwComponent(self, swc: CompositionSwComponentType):
        # remove all the sw connector first
        swc.removeAllAssemblySwConnector()
        swc.removeAllDelegationSwConnector()

        connectors = self.getSwConnectorList(swc.short_name)

        for connector in connectors:
            # self._logger.info("Update %s" % connector.short_name)
            if isinstance(connector, AssemblySwConnectorData):
                self._addAssemblySwConnector(swc, connector)
            elif isinstance(connector, DelegationSwConnectorData):
                self._addDelegationSwConnector(swc, connector)
            else:
                raise ValueError("Invalid connector information")

    def _locateCompositionSwComponent(self, swc_name: str, parent: ARPackage):
        for swc in parent.getSwComponentTypes():
            if isinstance(swc, CompositionSwComponentType) and swc.short_name == swc_name:
                self._updateCompositionSwComponent(swc)
        for pkg in parent.getARPackages():
            self._locateCompositionSwComponent(swc_name, pkg)

    def update(self, document: AUTOSAR):
        for name in self.getCompositionSwComponentList():
            for pkg in document.getARPackages():
                self._locateCompositionSwComponent(name, pkg)
