import argparse
import logging
import os.path
import sys

from armodel import __version__
from armodel.lib.cli_args_parser import InputFileParser
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable import (
    Referrable,
)
from armodel.parser.arxml_parser import ARXMLParser


def perform_uuid_duplicate_check(args):
    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'uuid_check.log')

    if os.path.exists(log_file):
        os.remove(log_file)

    if args.verbose:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

    logger.setLevel(logging.DEBUG)

    if args.verbose:
        stdout_handler.setLevel(logging.DEBUG)
    else:
        stdout_handler.setLevel(logging.INFO)

    if args.verbose:
        logger.addHandler(file_handler)
    logger.addHandler(stdout_handler)

    try:
        options = {}
        if args.warning:
            options['warning'] = True

        inputs = []
        inputs.append(args.INPUT)
        parser = InputFileParser(inputs)
        filenames = parser.parse()

        document = AUTOSAR().getInstance()
        parser = ARXMLParser(options)

        for filename in filenames:
            parser.load(filename, document)

        with open(args.OUTPUT, 'w') as f_out:
            logger.info("Writing the duplicate UUIDs to <%s>", args.OUTPUT)
            for uuid in document.getDuplicateUUIDs():
                ar_objects = document.getARObjectByUUID(uuid)
                if len(ar_objects) > 1:
                    f_out.write("Duplicate UUID found: %s \n" % uuid)
                    for ar_object in ar_objects:
                        if isinstance(ar_object, Referrable):
                            f_out.write("  - %s (%s)\n" % (ar_object.getFullName(), type(ar_object).__name__))
                        else:
                            raise NotImplementedError("Unsupported type <%s>" % type(ar_object))

    except Exception as e:
        logger.error(e)
        if args.verbose:
            raise e


def main():
    version = __version__

    ap = argparse.ArgumentParser()
    ap.description = "arxml-format ver: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("--log", required=False, help="Log all information to file")
    ap.add_argument("-w", "--warning", required=False, help="Skip the error and report it as warning message", action="store_true")

    ap.add_argument("INPUT", help="The path of AUTOSAR ARXML file")
    ap.add_argument("OUTPUT", help="The path of output ARXML file")

    args = ap.parse_args()

    perform_uuid_duplicate_check(args)


if __name__ == "__main__":
    main()
