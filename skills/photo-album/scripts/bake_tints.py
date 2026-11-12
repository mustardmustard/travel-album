#!/usr/bin/env python3
"""把每张方图缩成 32×32 的色块，写进 photos/tints.js（健身房照片展示用）。

直接双击 index.html（file://）打开时，浏览器不让网页读取照片像素，首页点阵字就没法染上照片的颜色。
页面读不到像素时，会改用这里预先算好的色块（photoTint → bakedTint），悬停音的音高也用它算亮度。

用法：
  python3 bake_tints.py [网站根目录，默认当前目录]

prepare_photos.py（把健身房照片按训练项目整理成 sq/full）跑完会自动调用它；
手动换了 photos/sq 里的图，再单独跑一次。
支持 jpg / png / webp，会递归扫描 photos/sq 下按章节分的子文件夹；
键名是相对 photos/sq 的路径、去掉扩展名，例如 "cutting/cutting-01-cardio"，
必须和 index.html 里 CHAPTERS 的 src 完全一致（扁平结构时仍是纯文件名）。
需要 Pillow（pip install pillow）。
"""
import base64, json, sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    sys.exit("需要 Pillow：pip install pillow")

SIZE = 32
EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def bake(root):
    sq = Path(root) / "photos" / "sq"
    # 递归：按章节分子文件夹后仍能全部收进来；键名用相对路径，和 CHAPTERS 的 src 对齐
    files = sorted(p for p in sq.rglob("*") if p.is_file() and p.suffix.lower() in EXTS)
    if not files:
        sys.exit(f"{sq} 里没有照片")
    data = {}
    for f in files:
        key = f.relative_to(sq).with_suffix("").as_posix()
        im = Image.open(f).convert("RGB").resize((SIZE, SIZE), Image.BOX)
        data[key] = base64.b64encode(im.tobytes()).decode()
    out = Path(root) / "photos" / "tints.js"
    out.write_text(
        "// 由 skills/photo-album/scripts/bake_tints.py 生成：每张方图缩成 32×32 的 RGB，base64。\n"
        "// 直接双击 index.html（file://）打开、读不到照片像素时，首页点阵字用它染色。换照片后重新运行脚本。\n"
        f"window.PHOTO_TINTS = {{ size:{SIZE}, data:{json.dumps(data, separators=(',', ':'))} }};\n"
    )
    print(f"写好了 {out}：{len(data)} 张，{out.stat().st_size // 1024} KB", file=sys.stderr)


if __name__ == "__main__":
    bake(sys.argv[1] if len(sys.argv) > 1 else ".")
