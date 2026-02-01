import argparse
import pkg_resources
import logging
import sys
import os.path

from armodel.transformer.admin_data import AdminDataTransformer
from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer import ARXMLWriter


def perform_format(args):
    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'arxml_format.log')

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

        document = AUTOSAR().getInstance()
        parser = ARXMLParser(options)
        parser.load(args.INPUT, document)

        if args.remove_admin_data:
            transform = AdminDataTransformer()
            transform.remove(document)

        writer = ARXMLWriter()
        writer.save(args.OUTPUT, document)
        
    except Exception as e:
        # print(e)
        logger.error(e)
        if args.verbose:
            raise e


def main():
    version = pkg_resources.require("armodel")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "arxml-format ver: %s" % version
    ap.add_argument("-v", "--verbose", required=False, help="Print debug information", action="store_true")
    ap.add_argument("--log", required=False, help="Log all information to file")
    ap.add_argument("-w", "--warning", required=False, help="Skip the error and report it as warning message", action="store_true")
    ap.add_argument("--remove-admin-data", required=False, help="Remove all the AdminData", action="store_true")
    ap.add_argument("INPUT", help="The path of AUTOSAR ARXML file")
    ap.add_argument("OUTPUT", help="The path of output ARXML file")

    args = ap.parse_args()

    perform_format(args)


if __name__ == "__main__":
    main()
