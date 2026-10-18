from armodel.cli.ecuc_export_common import EcucExportCli
from armodel.data_models.ecuc import BswmModule
from armodel.parser import BswmEcucParser
from armodel.report import BswmConfigExporter


class BswmEcucExportCli(EcucExportCli[BswmModule]):
    description = "Export the BswM configuration (BswMAction, BswMActionList) from an ECUC ARXML file."
    log_name = "bswm_ecuc_export.log"

    def load(self, path: str, warning: bool) -> BswmModule:
        return BswmEcucParser().load(path, warning=warning)

    def export(self, model: BswmModule, output: str) -> None:
        BswmConfigExporter().export(model, output)


def main():
    BswmEcucExportCli().run()


if __name__ == "__main__":
    main()
