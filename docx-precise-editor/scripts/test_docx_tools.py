#!/usr/bin/env python3
import tempfile
import unittest
import zipfile
from pathlib import Path

from append_table_row import append_table_row
from edit_docx import edit_text


def make_docx(path: Path, document_xml: str) -> None:
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr(
            "[Content_Types].xml",
            '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"/>',
        )
        z.writestr("word/document.xml", document_xml.encode("utf-8"))


def read_document_xml(path: Path) -> bytes:
    with zipfile.ZipFile(path) as z:
        return z.read("word/document.xml")


class EditDocxTests(unittest.TestCase):
    def test_allows_authorized_text_near_start_without_touching_other_xml(self) -> None:
        xml = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            "<w:body>"
            "<w:p><w:r><w:t>封面标题</w:t></w:r></w:p>"
            "<w:p><w:r><w:t>协助搭建报名</w:t></w:r></w:p>"
            "</w:body></w:document>"
        )

        with tempfile.TemporaryDirectory() as tmp:
            docx_path = Path(tmp) / "plan.docx"
            make_docx(docx_path, xml)
            before = read_document_xml(docx_path)

            edit_text(str(docx_path), "协助搭建报名", "负责分组签到")

            after = read_document_xml(docx_path)
            self.assertEqual(
                after,
                before.replace("协助搭建报名".encode(), "负责分组签到".encode()),
            )


class AppendTableRowTests(unittest.TestCase):
    def test_appends_row_with_default_style_when_source_row_has_no_font(self) -> None:
        xml = (
            '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            "<w:body><w:tbl>"
            '<w:tr><w:tc><w:tcPr><w:tcW w:w="2000" w:type="dxa"/></w:tcPr>'
            "<w:p><w:r><w:t>阶跃星辰</w:t></w:r></w:p></w:tc></w:tr>"
            "</w:tbl></w:body></w:document>"
        )

        with tempfile.TemporaryDirectory() as tmp:
            docx_path = Path(tmp) / "plan.docx"
            make_docx(docx_path, xml)

            append_table_row(str(docx_path), ["Trae on Campus"], "阶跃星辰")

            after = read_document_xml(docx_path).decode("utf-8")
            self.assertIn("Trae on Campus", after)
            self.assertIn('w:eastAsia="宋体"', after)


if __name__ == "__main__":
    unittest.main()
