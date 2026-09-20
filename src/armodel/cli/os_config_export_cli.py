import argparse
import logging
import os.path
import sys

from armodel import __version__
from armodel.parser import OsEcucParser
from armodel.report import OsConfigExporter


def main():
    version = __version__

    ap = argparse.ArgumentParser()
    ap.description = "Export the semantic OS configuration (OsApplication, OsTask) from an ECUC ARXML file. <%s>" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("-w", "--warning", required=False, help="Skip unresolved reference errors and report them as warning messages", action="store_true")
    ap.add_argument("INPUT", help="The path of the ECUC OS configuration ARXML", nargs="+")
    ap.add_argument("OUTPUT", help="The path of the output file (xlsx or yaml)")
    ap.add_argument("--format", required=False, choices=["xlsx", "yaml"], default="xlsx", help="Export format (default: xlsx)")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter("[%(levelname)s] : %(message)s")

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, "os_ecuc_export.log")

    if os.path.exists(log_file):
        os.remove(log_file)

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)

    else:
        stdout_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        output_path = os.path.abspath(args.OUTPUT)
        input_path = os.path.abspath(args.INPUT[0])
        if output_path == input_path:
            raise ValueError("The OUTPUT file must not overwrite the input file <%s>" % args.INPUT[0])

        os_os = OsEcucParser().load(args.INPUT[0], warning=args.warning)
        OsConfigExporter().export(os_os, args.OUTPUT, args.format)
    except Exception as e:
        # print(e)
        raise e


if __name__ == "__main__":
    main()
