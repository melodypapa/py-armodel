import argparse
import logging
import os.path
import sys
from typing import Generic, List, Optional, TypeVar

from armodel import __version__

ModelType = TypeVar("ModelType")


class EcucExportCli(Generic[ModelType]):
    """Base command-line flow for the ECUC exporters: parse arguments, set up logging, load the ARXML and export the model.

    Subclasses set ``description`` and ``log_name`` and implement :meth:`load` and :meth:`export`.
    """

    description: str = ""
    log_name: str = "ecuc_export.log"

    def load(self, path: str, warning: bool) -> ModelType:
        raise NotImplementedError

    def export(self, model: ModelType, output: str) -> None:
        raise NotImplementedError

    def parse_args(self, argv: Optional[List[str]] = None) -> argparse.Namespace:
        ap = argparse.ArgumentParser()
        ap.description = "%s <%s>" % (self.description, __version__)
        ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
        ap.add_argument("-w", "--warning", required=False, help="Skip unresolved reference errors and report them as warning messages", action="store_true")
        ap.add_argument("INPUT", help="The path of the ECUC configuration ARXML")
        ap.add_argument("OUTPUT", help="The path of the output file (.xlsx, .yaml, or .yml)")
        return ap.parse_args(argv)

    def run(self, argv: Optional[List[str]] = None) -> None:
        args = self.parse_args(argv)

        if os.path.abspath(args.OUTPUT) == os.path.abspath(args.INPUT):
            raise ValueError("The OUTPUT file must not overwrite the input file <%s>" % args.INPUT)

        logger = logging.getLogger()
        formatter = logging.Formatter("[%(levelname)s] : %(message)s")

        stdout_handler = logging.StreamHandler(sys.stderr)
        stdout_handler.setFormatter(formatter)
        stdout_handler.setLevel(logging.DEBUG if args.verbose else logging.INFO)

        log_file = os.path.join(os.path.dirname(args.OUTPUT), self.log_name)
        if os.path.exists(log_file):
            os.remove(log_file)
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

        logger.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)

        try:
            model = self.load(args.INPUT, args.warning)
            self.export(model, args.OUTPUT)
            logger.info("Exported <%s> to <%s>", args.INPUT, args.OUTPUT)
        finally:
            logger.removeHandler(file_handler)
            logger.removeHandler(stdout_handler)
            file_handler.close()
