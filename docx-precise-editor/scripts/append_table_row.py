#!/usr/bin/env python3
"""
在 docx 案例表格末尾追加一行，列宽/字体/对齐完全对齐已有行。
用于活动方案中「案例参考」表格的增补。

用法：
  python3 append_table_row.py <文件路径> <JSON数据>
  python3 append_table_row.py 方案.docx '{"col1":"Trae on Campus","col2":"一天制","col3":"从组队到路演的全流程Mini Hackathon"}'

安全：自动创建 .docx.backup 备份。
"""

import sys
import json
import zipfile
import shutil
import re


def find_last_tr_before_tbl(data: bytes, after_text: str) -> tuple:
    """在 after_text 之后找到最近的 </w:tr> 和其后的 </w:tbl>"""
    pos = data.find(after_text.encode("utf-8"))
    if pos == -1:
        raise ValueError(f"未找到标记文字: {after_text}")

    tbl_pos = data.find(b"</w:tbl>", pos)
    last_tr = data.rfind(b"</w:tr>", 0, tbl_pos)

    return last_tr, tbl_pos


def extract_row_style(data: bytes, tr_start: int) -> dict:
    """从已有行提取列宽、字体、对齐信息"""
    row_xml = data[tr_start:data.find(b"</w:tr>", tr_start) + 7]

    # 提取列宽
    widths = []
    for m in re.finditer(rb'<w:tcW w:w="(\d+)" w:type="dxa"/>', row_xml):
        widths.append(int(m.group(1)))

    # 提取字体
    fonts = re.findall(rb'(<w:rFonts[^/]*/>)', row_xml)
    default_font_xml = '<w:rFonts w:ascii="宋体" w:hAnsi="宋体" w:eastAsia="宋体"/>'.encode("utf-8")
    font_xml = fonts[0] if fonts else default_font_xml

    # 提取字号
    sz_match = re.search(rb'<w:sz w:val="(\d+)"/>', row_xml)
    sz_val = sz_match.group(1) if sz_match else b"19"

    # 对齐
    jc_match = re.search(rb'<w:jc w:val="(\w+)"/>', row_xml)
    jc_val = jc_match.group(1) if jc_match else b"center"

    return {"widths": widths, "font_xml": font_xml, "sz": sz_val, "jc": jc_val}


def build_cell(width: int, text: str, style: dict) -> bytes:
    """构建一个表格单元格"""
    return (
        b'<w:tc><w:tcPr>'
        b'<w:tcW w:w="' + str(width).encode() + b'" w:type="dxa"/>'
        b'<w:vAlign w:val="center"/>'
        b'</w:tcPr>'
        b'<w:p><w:pPr><w:spacing w:before="0" w:after="0" w:line="300" w:lineRule="auto"/></w:pPr>'
        b'<w:r><w:rPr>'
        + style["font_xml"] +
        b'<w:b w:val="0"/><w:sz w:val="' + style["sz"] + b'"/>'
        b'</w:rPr>'
        b'<w:t>' + text.encode("utf-8") + b'</w:t>'
        b'</w:r></w:p></w:tc>'
    )


def append_table_row(docx_path: str, row_data: list[str], after_text: str) -> None:
    # 1. 备份
    backup_path = docx_path + ".backup"
    shutil.copy2(docx_path, backup_path)

    with zipfile.ZipFile(docx_path, "r") as z:
        data = z.read("word/document.xml")

    # 2. 定位：最后一行 → 表格尾
    last_tr, tbl_end = find_last_tr_before_tbl(data, after_text)

    # 3. 提取样式
    style = extract_row_style(data, last_tr)
    if len(style["widths"]) < len(row_data):
        style["widths"] = style["widths"] + [4353] * (len(row_data) - len(style["widths"]))

    # 4. 构建新行
    cells = b"".join(
        build_cell(style["widths"][i], row_data[i], style)
        for i in range(len(row_data))
    )

    new_row = (
        b'<w:tr><w:trPr><w:jc w:val="' + style["jc"] + b'"/></w:trPr>'
        + cells +
        b'</w:tr>'
    )

    # 5. 插入到最后一个 </w:tr> 后面、</w:tbl> 前面
    between = data[last_tr + 7:tbl_end]
    data = data[:last_tr + 7] + b"\n" + between + new_row + data[last_tr + 7:]

    # 6. 写回
    with zipfile.ZipFile(docx_path, "r") as zin:
        with zipfile.ZipFile(docx_path + ".tmp", "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, data)
                else:
                    zout.writestr(item, zin.read(item.filename))

    shutil.move(docx_path + ".tmp", docx_path)

    print(f"✅ 已在「{after_text}」之后追加一行")
    print(f"   列数: {len(row_data)}")
    print(f"   数据: {row_data}")
    print(f"   备份: {backup_path}")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python3 append_table_row.py <文件路径> <JSON数组> [标记文字]")
        print("示例: python3 append_table_row.py 方案.docx '[\"列1\",\"列2\",\"列3\"]' '阶跃星辰'")
        sys.exit(1)

    docx_path = sys.argv[1]
    row_data = json.loads(sys.argv[2])
    after_text = sys.argv[3] if len(sys.argv) > 3 else ""

    append_table_row(docx_path, row_data, after_text)
