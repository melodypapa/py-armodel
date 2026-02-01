import argparse
import pkg_resources
import logging
import sys
import os.path

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser import ARXMLParser
from armodel.lib import InputFileParser
from armodel.report import ConnectorXlsReport

def main():
    version = pkg_resources.require("armodel")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("-w", "--warning", required= False, help= "Skip the error and report it as warning message", action= "store_true")
    ap.add_argument("INPUT", help = "The path of AUTOSAR XML", nargs='+')
    ap.add_argument("OUTPUT", help = "The path of output excel file")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.OUTPUT)
    log_file = os.path.join(base_path, 'connector.log')

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
        parser = InputFileParser(args.INPUT)
        filenames = parser.parse()

        options = {}
        if args.warning:
            options['warning'] = True

        document = AUTOSAR().getInstance()
        parser = ARXMLParser(options)

        for filename in filenames:
            parser.load(filename, document)

        writer = ConnectorXlsReport()
        writer.import_data(document)
        writer.write(args.OUTPUT)
        
    except Exception as e:
        #print(e)
        raise e

if __name__ == "__main__":
    main()