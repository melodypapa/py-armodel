from typing import List

import logging
import os, re

class InputFileParser:
    def __init__(self, args: List[str]) -> None:
        self._args = args
        self._filenames = []                # type: List[str]
        self._logger = logging.getLogger()

    def _parse_file_list(self, file):
        with open(file) as f_in:
            for line in f_in:
                self._filenames.append(line.strip())

    def _parse_dir_files(self, dir_name):
        for (root, _, files) in os.walk(dir_name, topdown=False):
            for file in files:
                m = re.match(r'.*\.arxml$', file, re.I)

                if m:
                    self._filenames.append(os.path.join(root, file))

    def parse(self) -> List[str]:
        for input_file in self._args:
            if os.path.isdir(input_file):
                self._parse_dir_files(input_file)
            else:
                if input_file[0] == "@":
                    self._logger.debug("Parse ARXML list file %s " % input_file)
                    self._parse_file_list(input_file[1:])
                else:
                    self._filenames.append(input_file)

        return self._filenames