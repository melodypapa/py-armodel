import argparse
import logging
import os.path
import sys
from typing import Any, Callable, List, Optional

from armodel import __version__


def run_ecuc_export(description: str, log_name: str, load: Callable[[str, bool], Any], export: Callable[[Any, str], None], argv: Optional[List[str]] = None) -> None:
    """Shared CLI flow for the ECUC exporters: parse arguments, set up logging, load the ARXML and export the model.

    ``load(input_path, warning)`` returns the semantic model; ``export(model, output_path)`` writes it.
    """
    ap = argparse.ArgumentParser()
    ap.description = "%s <%s>" % (description, __version__)
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("-w", "--warning", required=False, help="Skip unresolved reference errors and report them as warning messages", action="store_true")
    ap.add_argument("INPUT", help="The path of the ECUC configuration ARXML")
    ap.add_argument("OUTPUT", help="The path of the output file (.xlsx, .yaml, or .yml)")

    args = ap.parse_args(argv)

    if os.path.abspath(args.OUTPUT) == os.path.abspath(args.INPUT):
        raise ValueError("The OUTPUT file must not overwrite the input file <%s>" % args.INPUT)

    logger = logging.getLogger()
    formatter = logging.Formatter("[%(levelname)s] : %(message)s")

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.DEBUG if args.verbose else logging.INFO)

    log_file = os.path.join(os.path.dirname(args.OUTPUT), log_name)
    if os.path.exists(log_file):
        os.remove(log_file)
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        model = load(args.INPUT, args.warning)
        export(model, args.OUTPUT)
        logger.info("Exported <%s> to <%s>", args.INPUT, args.OUTPUT)
    finally:
        logger.removeHandler(file_handler)
        logger.removeHandler(stdout_handler)
        file_handler.close()
