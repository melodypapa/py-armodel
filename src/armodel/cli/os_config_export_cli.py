from armodel.cli.ecuc_export_common import EcucExportCli
from armodel.data_models.ecuc import OsOs
from armodel.parser import OsEcucParser
from armodel.report import OsConfigExporter


class OsEcucExportCli(EcucExportCli[OsOs]):
    description = "Export the semantic OS configuration (OsApplication, OsTask, OsAlarm, OsIsr, OsScheduleTable) from an ECUC ARXML file."
    log_name = "os_ecuc_export.log"

    def load(self, path: str, warning: bool) -> OsOs:
        return OsEcucParser().load(path, warning=warning)

    def export(self, model: OsOs, output: str) -> None:
        OsConfigExporter().export(model, output)


def main():
    OsEcucExportCli().run()


if __name__ == "__main__":
    main()
