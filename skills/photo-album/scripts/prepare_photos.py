#!/usr/bin/env python3
"""把健身房原始照片整理成网站要的两套图，并打印 CHAPTERS 用的宽高。

照片按训练项目分文件夹存放（deadlift/、glutes/、shoulders/、yoga/、cutting/、dance/、pilates/），
每个文件夹是一章，文件名用英文动作名（如 deadlift-lockout.jpg）；站点 index.html 的 CHAPTERS
需要每张的 src / w / h。

默认（不加 --label-from-folder）：只处理 src 顶层文件，输出扁平结构：
  photos/sq/<名字>.jpg    640×640 方图，用在首页照片环上
  photos/full/<名字>.jpg  长边 1600，保留原始比例，用在章节页和大图上

加 --label-from-folder：不同章的照片分别放进不同子文件夹，站点也照这个层级取图：
  photos/sq/<章节>/<名字>.jpg
  photos/full/<章节>/<名字>.jpg
  chapters.json 里每张的 src 写成 "<章节>/<名字>"（相对 photos/sq 与 photos/full 的路径，不含扩展名），
  直接抄进 index.html 的 CHAPTERS 即可；photoURL("sq", src) 会拼成 photos/sq/<章节>/<名字>.jpg。

用法：
  python3 prepare_photos.py <原始照片文件夹> [--out 网站根目录] [--full 1600] [--sq 640]
  python3 prepare_photos.py <原始照片文件夹> --label-from-folder [--sq-fit] \
      [--order deadlift,glutes,shoulders,yoga,cutting,dance,pilates] --out 网站根目录

--label-from-folder：递归读取 src 下按项目命名的子文件夹，文件夹名当章节标签，
  输出 chapters.json（[{"dir","label","photos":[{"src","w","h","from"}]}]）。
--order：逗号分隔的章节名，决定 chapters.json 里的章节顺序（不填按文件夹名字母序）；
  没列在里面的文件夹会按字母序追加在后面。
--sq-fit：首页方图不做居中裁切，而是把原图等比缩到 640 以内、居中贴在 640×640 的浅色底上，
  避免硬拉 / 深蹲这类竖幅全身动作被裁掉手脚；默认仍是 ImageOps.fit 居中裁切。

需要 Pillow（pip install pillow）。会按 EXIF 方向转正，文件名转成小写短横线；纯中文文件名
用「项目文件夹名 + 序号」兜底并在 stderr 提示。最后会自动调用 bake_tints.py 生成 photos/tints.js
（直接双击 index.html 打开时，首页点阵字靠它染色；键名与 CHAPTERS 的 src 一致）。
stdout 打印每张的 src / w / h JSON，可直接抄进 index.html 的 CHAPTERS；分组信息见 chapters.json。
"""
import argparse, json, re, sys, unicodedata
from pathlib import Path

try:
    from PIL import Image, ImageOps
except ImportError:
    sys.exit("需要 Pillow：pip install pillow")

EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".tif", ".tiff"}
PAPER = (250, 250, 248)


def slug(name):
    """文件名转 ASCII 短横线；纯非 ASCII（如中文）会退化成空字符串，由调用方兜底。"""
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s


def make_square(im, size, fit):
    """方图：默认居中裁切；--sq-fit 时等比缩进 size×size 的浅色底、居中贴。"""
    if not fit:
        return ImageOps.fit(im, (size, size), Image.LANCZOS)
    canvas = Image.new("RGB", (size, size), PAPER)
    fitted = im.copy()
    fitted.thumbnail((size, size), Image.LANCZOS)
    canvas.paste(fitted, ((size - fitted.width) // 2, (size - fitted.height) // 2))
    return canvas


def group_dirs(src, order):
    """列出项目子文件夹；给了 --order 就按它排，其余按字母序追加。"""
    dirs = sorted(p for p in src.iterdir() if p.is_dir())
    if not order:
        return dirs
    wanted = [x.strip() for x in order.split(",") if x.strip()]
    by_name = {d.name: d for d in dirs}
    out = [by_name[n] for n in wanted if n in by_name]
    out += [d for d in dirs if d.name not in wanted]
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src", type=Path)
    ap.add_argument("--out", type=Path, default=Path("."))
    ap.add_argument("--full", type=int, default=1600)
    ap.add_argument("--sq", type=int, default=640)
    ap.add_argument("--label-from-folder", action="store_true",
                    help="按项目子文件夹分组，照片也写进对应子文件夹，输出 chapters.json")
    ap.add_argument("--order", default="", help="逗号分隔的章节顺序（仅在 --label-from-folder 下生效）")
    ap.add_argument("--sq-fit", action="store_true",
                    help="方图不裁切，等比缩进浅色底的 640×640")
    a = ap.parse_args()

    # 收集文件；label-from-folder 时按子文件夹分组，并记下每张图的章节标签
    file_label = {}
    groups = []
    if a.label_from_folder:
        for d in group_dirs(a.src, a.order):
            photos = sorted(p for p in d.rglob("*") if p.suffix.lower() in EXT)
            if photos:
                groups.append((d.name, photos))
                for p in photos:
                    file_label[p] = d.name
        files = [p for _, ps in groups for p in ps]
    else:
        files = sorted(p for p in a.src.iterdir() if p.suffix.lower() in EXT)
    if not files:
        sys.exit(f"{a.src} 里没有照片")
    full_base, sq_base = a.out / "photos" / "full", a.out / "photos" / "sq"

    # label-from-folder 时准备按项目分组的 chapters.json 容器
    by_label = {}
    chapters = []
    for label, _ in groups:
        by_label[label] = []
        chapters.append({"dir": label, "label": label, "photos": by_label[label]})

    out, used = [], set()
    fallback_seq = 0
    for p in files:
        try:
            im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        except Exception as e:
            print(f"跳过 {p.name}：{e}", file=sys.stderr)
            continue
        stem = slug(p.stem)
        if stem:
            base = stem
        else:
            # 纯中文等无法转成 ASCII 的文件名：用「项目文件夹名 + 序号」兜底，避免都撞成 photo
            prefix = slug(file_label.get(p, "")) or "photo"
            fallback_seq += 1
            base = f"{prefix}-{fallback_seq:02d}"
            print(f"{p.name} 无法转成英文文件名，用 {base} 兜底", file=sys.stderr)
        name = base
        k = 2
        while name in used:
            name, k = f"{base}-{k}", k + 1
        used.add(name)

        label = file_label.get(p)
        full_dir = full_base / label if label else full_base
        sq_dir = sq_base / label if label else sq_base
        full_dir.mkdir(parents=True, exist_ok=True)
        sq_dir.mkdir(parents=True, exist_ok=True)

        full = im.copy()
        full.thumbnail((a.full, a.full), Image.LANCZOS)
        full.save(full_dir / f"{name}.jpg", quality=86, optimize=True, progressive=True)
        make_square(im, a.sq, a.sq_fit).save(sq_dir / f"{name}.jpg", quality=84, optimize=True, progressive=True)
        # src 是相对 photos/sq 与 photos/full 的路径，和 bake_tints.py 的键名、CHAPTERS 的 src 对齐
        rec = {"src": f"{label}/{name}" if label else name, "w": full.width, "h": full.height, "from": p.name}
        out.append(rec)
        if a.label_from_folder:
            by_label[label].append(rec)
        print(f"{p.name} → {rec['src']}  {full.width}×{full.height}", file=sys.stderr)

    print(json.dumps(out, ensure_ascii=False, indent=2))
    if a.label_from_folder:
        (a.out / "chapters.json").write_text(json.dumps(chapters, ensure_ascii=False, indent=2), encoding="utf-8")
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from bake_tints import bake
    bake(a.out)


if __name__ == "__main__":
    main()
