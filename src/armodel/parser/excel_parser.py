from typing import Dict
from openpyxl.worksheet.worksheet import Worksheet

import logging
class AbstractExcelParser:
    def __init__(self) -> None:
        self._logger = logging.getLogger()

    def getColumnTitles(self, sheet: Worksheet, title_row:int, column_list: Dict[str, int]):
        for column in range(1, sheet.max_column + 1):
            value = sheet.cell(title_row, column).value
            if value in column_list:
                column_list[value] = column - 1

    def checkColumnTitles(self, column_list: Dict[str, int], message: str):
        for key, value in column_list.items():
            if value == -1:
                raise ValueError(message % key)