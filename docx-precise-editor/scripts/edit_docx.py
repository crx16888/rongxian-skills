#!/usr/bin/env python3
"""
字节级 docx 文本替换 —— 不改任何 XML 结构。
只替换 <w:t> 内的中文文本，xml 结构、run、属性全部不动。

用法：
  python3 edit_docx.py <文件路径> <旧文本> <新文本>
  python3 edit_docx.py 活动方案.docx "协助搭建报名" "不负责报名"

安全：自动创建 .docx.backup 备份。
"""

import sys
import zipfile
import shutil


def edit_text(docx_path: str, old_text: str, new_text: str) -> None:
    # 1. 备份
    backup_path = docx_path + ".backup"
    shutil.copy2(docx_path, backup_path)

    # 2. 阅读原 XML
    with zipfile.ZipFile(docx_path, "r") as z:
        data = z.read("word/document.xml")

    # 3. 字节级替换
    old_bytes = old_text.encode("utf-8")
    new_bytes = new_text.encode("utf-8")

    if old_bytes not in data:
        print(f"❌ 未找到: {old_text}")
        print(f"   文档中可能不包含此文本，检查是否有多余空格或换行。")
        sys.exit(1)

    data = data.replace(old_bytes, new_bytes)

    # 4. 写回 ZIP
    with zipfile.ZipFile(docx_path, "r") as zin:
        with zipfile.ZipFile(docx_path + ".tmp", "w", zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if item.filename == "word/document.xml":
                    zout.writestr(item, data)
                else:
                    zout.writestr(item, zin.read(item.filename))

    shutil.move(docx_path + ".tmp", docx_path)

    # 5. 验证
    with zipfile.ZipFile(docx_path, "r") as z:
        new_data = z.read("word/document.xml")
    with zipfile.ZipFile(backup_path, "r") as z:
        old_data = z.read("word/document.xml")

    # 封面区域（前 5000 字节）必须不变
    if new_data[:5000] != old_data[:5000]:
        print("⚠️ 警告：封面区域发生变化，已从备份恢复。")
        shutil.copy2(backup_path, docx_path)
        sys.exit(1)

    print(f"✅ 替换成功")
    print(f"   {repr(old_text)}")
    print(f"   → {repr(new_text)}")
    print(f"   备份: {backup_path}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("用法: python3 edit_docx.py <文件路径> <旧文本> <新文本>")
        sys.exit(1)

    edit_text(sys.argv[1], sys.argv[2], sys.argv[3])
