from armodel.cli.ecuc_export_common import run_ecuc_export
from armodel.parser import BswmEcucParser
from armodel.report import BswmConfigExporter


def main():
    run_ecuc_export(
        "Export the BswM configuration (BswMAction, BswMActionList) from an ECUC ARXML file.",
        "bswm_ecuc_export.log",
        lambda path, warning: BswmEcucParser().load(path, warning=warning),
        lambda model, output: BswmConfigExporter().export(model, output),
    )


if __name__ == "__main__":
    main()
