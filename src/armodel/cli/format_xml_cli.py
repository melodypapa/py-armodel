import argparse
import sys
import pkg_resources
import xml.etree.ElementTree as ET
from xml.dom import minidom
import logging
import re


def patch_xml(xml: str) -> str:
    xml = re.sub(r"\<([\w-]+)\/\>", r"<\1></\1>", xml)
    # xml = re.sub(r"<([\w-]+)\s+(\w+)=(\"[\w-]+\")\/>", r"<\1 \2=\3></\1>", xml)
    # xml = re.sub(r"&quot;", '"', xml)
    return xml


def perform_format(args):
    try:
        # Load XML file 
        logging.info("Loading XML file: %s" % args.INPUT)
        tree = ET.parse(args.INPUT)
        ET.register_namespace("", "http://autosar.org/schema/r4.0")
        root = tree.getroot()

        # Save the XML file
        xml = ET.tostring(root, encoding="UTF-8", xml_declaration=True, short_empty_elements=False)
        
        dom = minidom.parse(args.INPUT)
        xml = dom.toprettyxml(indent="  ", encoding="UTF-8")

        xml = patch_xml(xml.decode())

        lines = xml.splitlines()

        logging.info("Saving XML file: %s" % args.OUTPUT)

        with open(args.OUTPUT, "w", encoding="utf-8") as f_out:
            for line in lines:
                if line.strip() == "":
                    continue
                f_out.write(line + "\n")
        
    except Exception as e:
        logging.error(e)
        sys.exit(1)
        

def main():
    version = pkg_resources.require("armodel")[0].version

    ap = argparse.ArgumentParser()
    ap.description = "arxml-format ver: %s" % version
    ap.add_argument("INPUT", help="The path of XML file")
    ap.add_argument("OUTPUT", help="The path of XML file")

    args = ap.parse_args()

    perform_format(args)


if __name__ == "__main__":
    main()
