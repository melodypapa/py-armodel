import os
from typing import Any, Dict, Generic, List, Optional, TypeVar, Union

from openpyxl.styles import Alignment

from armodel.report.excel_report import ExcelReporter

ModelType = TypeVar("ModelType")
Sections = Dict[str, List[Dict[str, Any]]]


def format_list_item(item: Any) -> str:
    if isinstance(item, dict):
        return ",".join("%s=%s" % (key, item[key]) for key in item)
    return str(item)


class EcucConfigModelMapper(Generic[ModelType]):
    """Maps a semantic ECUC model to ordered sections of flat rows.

    Every section becomes one worksheet (XLSX) or one top-level key (YAML).
    """

    def to_dict(self, model: ModelType) -> Sections:
        raise NotImplementedError

    def headers(self, section: str) -> List[str]:
        """Columns that every row of ``section`` starts with; used for the header row of empty sections."""
        return []


class EcucConfigYamlExporter(Generic[ModelType]):
    def __init__(self, mapper: EcucConfigModelMapper[ModelType]) -> None:
        self.mapper = mapper

    def export(self, model: ModelType, output_path: Union[str, os.PathLike]) -> None:
        try:
            import yaml
        except ImportError as e:
            raise ImportError("pyyaml is required for YAML export: pip install pyyaml") from e

        data = self.mapper.to_dict(model)
        filtered_data = {section: [{key: value for key, value in row.items() if value is not None and value != []} for row in rows] for section, rows in data.items()}
        with open(output_path, "w", encoding="utf-8") as file:
            yaml.safe_dump(filtered_data, file, sort_keys=False)


class EcucConfigXlsxExporter(ExcelReporter, Generic[ModelType]):
    def __init__(self, mapper: EcucConfigModelMapper[ModelType]) -> None:
        super().__init__()
        self.mapper = mapper

    def headers_for(self, section: str, rows: List[Dict[str, Any]]) -> List[str]:
        """Mapper headers first, then any further keys in first-seen order (rows of one section may differ)."""
        headers = list(self.mapper.headers(section))
        for row in rows:
            for key in row:
                if key not in headers:
                    headers.append(key)
        return headers

    def export(self, model: ModelType, output_path: Union[str, os.PathLike]) -> None:
        data = self.mapper.to_dict(model)
        for index, (sheet_name, rows) in enumerate(data.items()):
            if index == 0:
                sheet = self.wb.active
                if sheet is not None:
                    sheet.title = sheet_name
            else:
                sheet = self.wb.create_sheet(sheet_name)
            headers = self.headers_for(sheet_name, rows)
            self.write_title_row(sheet, headers)
            for row_index, row in enumerate(rows):
                for column_index, header in enumerate(headers):
                    value = row.get(header)
                    format = None
                    if isinstance(value, list):
                        value = "\n".join(format_list_item(item) for item in value)
                        format = {"alignment": Alignment(wrap_text=True)}
                    self.write_cell(sheet, row_index + 2, column_index + 1, value, format)
            self.auto_width(sheet)
        self.save(output_path)


class EcucConfigExporter(Generic[ModelType]):
    """Dispatches an export to the YAML or XLSX exporter by output file extension."""

    def __init__(self, mapper: EcucConfigModelMapper[ModelType], label: str) -> None:
        self.label = label
        self._exporters: Dict[str, Union[EcucConfigYamlExporter[ModelType], EcucConfigXlsxExporter[ModelType]]] = {"yaml": EcucConfigYamlExporter(mapper), "xlsx": EcucConfigXlsxExporter(mapper)}

    def export(self, model: ModelType, output_path: Union[str, os.PathLike]) -> None:
        extension = os.path.splitext(os.fspath(output_path))[1].lower().lstrip(".")
        if extension == "yml":
            extension = "yaml"
        exporter: Optional[Union[EcucConfigYamlExporter[ModelType], EcucConfigXlsxExporter[ModelType]]] = self._exporters.get(extension)
        if exporter is None:
            raise ValueError("Unsupported %s configuration export format: %s" % (self.label, extension))
        exporter.export(model, output_path)
