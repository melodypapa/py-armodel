from armodel.cli.ecuc_export_common import run_ecuc_export
from armodel.parser import OsEcucParser
from armodel.report import OsConfigExporter


def main():
    run_ecuc_export(
        "Export the semantic OS configuration (OsApplication, OsTask, OsAlarm, OsIsr, OsScheduleTable) from an ECUC ARXML file.",
        "os_ecuc_export.log",
        lambda path, warning: OsEcucParser().load(path, warning=warning),
        lambda model, output: OsConfigExporter().export(model, output),
    )


if __name__ == "__main__":
    main()
