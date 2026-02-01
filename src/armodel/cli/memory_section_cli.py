import argparse
import pkg_resources
import logging
import sys
import os.path

from armodel.models.M2.AUTOSARTemplates.AutosarTopLevelStructure import AUTOSAR
from armodel.parser import ARXMLParser
from armodel.lib import InputFileParser, SystemSignalAnalyzer

def main():
    version = pkg_resources.require("armodel")[0].version

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("-f", "--format", required= False, help= "Specify the short or long name of Sw-C. [short|long]")
    
    ap.add_argument("INPUT", help = "The path of AUTOSAR XML", nargs='+')

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    #base_path = os.path.dirname(args.Output)
    log_file = os.path.join(".", 'system-signals.log')

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

        document = AUTOSAR().getInstance()
        parser = ARXMLParser({'warning': True})

        format = "short"
        if args.format is not None and args.format.lower() == "long":
            format = "long"

        for filename in filenames:
            parser.load(filename, document)

        analyzer = SystemSignalAnalyzer()
        analyzer.import_data(document)
        analyzer.print_out({
            'format': format,
        })
        
    except Exception as e:
        print(e)
        #raise e

if __name__ == "__main__":
    main()