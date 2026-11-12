# 给 agent 的说明

这个仓库是一个单文件健身房照片展示网站（`index.html` + `photos/`），同时也是一个 skill 的模板。

- **想用自己的照片做一个这样的网站**：读 `skills/photo-album/SKILL.md`，按流程走。照片按训练项目分文件夹，风格要从用户自己的照片里读出来，不要照抄本站风格。
- **想修改本站**：`index.html` 顶部的「风格区」（CSS `:root`、JS `THEME`、`CHAPTERS`、`TEXT_TILES`，以及「声音：风格区」）放的是可变的风格值，其余部分是引擎。改引擎之前，先读 `skills/photo-album/references/components.md` 里对应部件的契约。
- **本地运行**：`python3 -m http.server 8765`，然后访问 http://localhost:8765 。不能用 `file://` 打开，否则读不到照片像素：首页染色会退回 `photos/tints.js` 的预烘色块，风格台和大图失效。换了 `photos/sq` 要重跑 `skills/photo-album/scripts/bake_tints.py`。
- **版权**：当前 `photos/` 是 AI 生成的演示素材；换成真实会员 / 教练照片前先取得肖像授权，未成年人照片不要用，也不要把照片复制到别的项目里。
