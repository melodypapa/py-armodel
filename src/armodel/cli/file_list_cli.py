import argparse
import pkg_resources
import logging
import sys
import os.path

from ..parser import FileListParser

def format_filename(filename, type: str):
    path, file = os.path.split(filename)
    base, ext = os.path.splitext(file)
    return os.path.join(path, base + "_" + type + ext)
        
def main():
    version = pkg_resources.require("armodel")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "Parse the folder to generate ARXML file list. <%s>" % version
    ap.add_argument("-v", "--verbose", required= False, help= "Print debug information", action= "store_true")
    ap.add_argument("--absolute", required= False, help="Absolute path or relative Path", action= "store_true")
    ap.add_argument("Input", help = "The path contains ARXML file", nargs='+')
    ap.add_argument("Output", help = "The text contains ARXML file list.")

    args = ap.parse_args()

    logger = logging.getLogger()
    
    formatter = logging.Formatter('[%(levelname)s] : %(message)s')

    stdout_handler = logging.StreamHandler(sys.stderr)
    stdout_handler.setFormatter(formatter)

    base_path = os.path.dirname(args.Output)
    log_file = os.path.join(base_path, 'armodel_file_list.log')

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
        file_parser = FileListParser()
        file_parser.parse(args.Input)
            
        with open(args.Output, "w") as f_out:
            for filename in file_parser.get_file_list():
                if args.absolute:
                    f_out.write("%s\n" % os.path.realpath(filename))
                else:
                    f_out.write("%s\n" % os.path.relpath(filename))

    except Exception as e:
        #print(e)
        raise e

if __name__ == "__main__":
    main()