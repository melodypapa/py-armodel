import logging
import os
import re
from typing import List

from colorama import Fore


class FileListParser:
    '''
        FileListParser supports to collect the arxml files from the following rules
         
    '''
    def __init__(self) -> None:
        self.file_list = []
        self.logger = logging.getLogger()

    def get_file_list(self) -> List[str]:
        return self.file_list
    
    def parse_text_file(self, file):
        try:
            with open(file) as f_in:
                for line in f_in:
                    if not line.startswith('#'):
                        self.file_list.append(line.strip())
        except IOError:
            self.logger.error(Fore.RED + "No such file or directory: %s" % os.path.realpath(file) + Fore.WHITE)

    def parse_dir_files(self, dir_name):
        for (root, _, files) in os.walk(dir_name, topdown=False):
            for file in files:
                m = re.match(r'.*\.arxml$', file, re.I)
                if m:
                    self.file_list.append(os.path.join(root, file))

    def parse(self, args: List[str]):
        for input_file in args:
            if os.path.isdir(input_file):
                self.parse_dir_files(input_file)
            else:
                if input_file[0] == "@":
                    logging.debug("Parse ARXML list file %s " % input_file)
                    self.parse_text_file(input_file[1:])
                else:
                    self.file_list.append(input_file)
