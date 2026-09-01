"""Parser/writer round-trip tests for the AUTOSAR top-level root element
(R23-11, AUTOSAR_FO_TPS_GenericStructureTemplate, Table E.1, p.421).

The root carries four spec attributes: adminData, arPackage, fileInfoComment,
introduction. There is no dedicated readAUTOSAR/writeAUTOSAR — the parser's
load() populates the root via getAdminData/readARPackages/getFileInfoComment/
getDocumentationBlock and the writer's save() via setAdminData/writeARPackages/
setFileInfoComment/writeDocumentationBlock (XSD group AUTOSAR sequence order).
"""

import pytest

from armodel.models import AUTOSAR
from armodel.parser.arxml_parser import ARXMLParser
from armodel.writer.arxml_writer import ARXMLWriter

NS = "http://autosar.org/schema/r4.0"


@pytest.fixture(autouse=True)
def reset_autosar():
    AUTOSAR.getInstance().new()
    yield
    AUTOSAR.getInstance().new()


@pytest.fixture
def parser():
    AUTOSAR.getInstance().new()
    return ARXMLParser(options={"warning": True})


def _write_doc(tmp_path, inner: str) -> str:
    doc = (
        '<?xml version="1.0" encoding="UTF-8"?>\n' '<AUTOSAR xmlns="%s" ' 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' 'xsi:schemaLocation="%s AUTOSAR_4-0-3.xsd">\n' "%s\n" "</AUTOSAR>\n"
    ) % (NS, NS, inner)
    path = tmp_path / "root.arxml"
    path.write_text(doc)
    return str(path)


ROOT_INNER = """
  <FILE-INFO-COMMENT>
    <SDGS>
      <SDG GID="g1">
        <SDG-CAPTION>
          <SHORT-NAME>file comment caption</SHORT-NAME>
        </SDG-CAPTION>
      </SDG>
    </SDGS>
  </FILE-INFO-COMMENT>
  <ADMIN-DATA>
    <LANGUAGE>EN</LANGUAGE>
  </ADMIN-DATA>
  <INTRODUCTION>
    <P xml:lang="EN">intro text</P>
  </INTRODUCTION>
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>Pkg1</SHORT-NAME>
    </AR-PACKAGE>
  </AR-PACKAGES>
"""


def test_load_root_reads_all_four_attributes(parser, tmp_path):
    document = AUTOSAR.getInstance()
    parser.load(_write_doc(tmp_path, ROOT_INNER), document)

    fic = document.getFileInfoComment()
    assert fic is not None
    assert len(fic.getSdgs()) == 1

    admin = document.getAdminData()
    assert admin is not None
    assert admin.getLanguage() is not None

    assert document.getIntroduction() is not None

    pkgs = document.getARPackages()
    assert len(pkgs) == 1
    assert pkgs[0].getShortName() == "Pkg1"


def test_save_root_round_trips_all_four_attributes(parser, tmp_path):
    document = AUTOSAR.getInstance()
    document.setARRelease("R23-11")
    parser.load(_write_doc(tmp_path, ROOT_INNER), document)

    out = tmp_path / "out.arxml"
    ARXMLWriter().save(str(out), document)

    document2 = AUTOSAR.getInstance()
    document2.new()
    parser.load(str(out), document2)

    assert document2.getFileInfoComment() is not None
    assert len(document2.getFileInfoComment().getSdgs()) == 1
    assert document2.getAdminData() is not None
    assert document2.getIntroduction() is not None
    assert len(document2.getARPackages()) == 1


def test_load_root_without_optional_attributes_is_none(parser, tmp_path):
    inner = """
      <AR-PACKAGES>
        <AR-PACKAGE>
          <SHORT-NAME>PkgOnly</SHORT-NAME>
        </AR-PACKAGE>
      </AR-PACKAGES>
    """
    document = AUTOSAR.getInstance()
    parser.load(_write_doc(tmp_path, inner), document)

    assert document.getFileInfoComment() is None
    assert document.getAdminData() is None
    assert document.getIntroduction() is None
    assert len(document.getARPackages()) == 1
    assert document.getARPackages()[0].getShortName() == "PkgOnly"
