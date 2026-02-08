import argparse
import logging
import os.path
import sys

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.parser.connector_xlsx_parser import ConnectorXlsReader
from armodel.writer.arxml_writer import ARXMLWriter


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("-w", "--warning", required= False, help= "Skip the error and report it as warning message", action= "store_true")
    ap.add_argument("INPUT", help = "The path of input ARXML file")
    ap.add_argument("MAPPING", help = "The path of connector excel file which exports with connector2xlsx")
    ap.add_argument("OUTPUT", help = "The path of output ARXML file")

    args = ap.parse_args()

    logger = logging.getLogger()

    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'connector_update.log')

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
        options = {}
        if args.warning:
            options['warning'] = True

        document = AUTOSAR().getInstance()
        parser = ARXMLParser(options)
        parser.load(args.INPUT, document)

        reader = ConnectorXlsReader()
        reader.read(args.MAPPING)
        reader.update(document)

        writer = ARXMLWriter()
        writer.save(args.OUTPUT, document)

    except Exception as e:
        #print(e)
        logger.error(e)
        raise e

if __name__ == "__main__":
    main()
