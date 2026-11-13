# 给 agent 的说明

这个仓库是一个单文件健身房照片展示网站（`index.html` + `photos/`），同时也是一个 skill 的模板。当前品牌是 `IN MAX`，共 **7 章 / 28 张**演示照片：硬拉 / 臀腿 / 肩部 / 瑜伽 / 减脂 / 舞蹈 / 普拉提。

- **想用自己的照片做一个这样的网站**：读 `skills/photo-album/SKILL.md`，按流程走。照片按训练项目分文件夹，风格要从用户自己的照片里读出来，不要照抄本站风格。
- **想修改本站**：`index.html` 顶部的「风格区」（CSS `:root`、JS `THEME`、`CHAPTERS`、`CONTACT`、`TEXT_TILES`，以及「声音：风格区」）放的是可变的风格值，其余部分是引擎。改引擎之前，先读 `skills/photo-album/references/components.md` 里对应部件的契约。
- **照片层级**：不同章节的照片分别放在 `photos/sq/<章节>/` 与 `photos/full/<章节>/`；`CHAPTERS` 的 `src` 是带章节目录的相对路径（如 `dance/dance-02-leap`），`photos/tints.js` 的键名与它完全一致。换照片或改目录结构，要重跑 `prepare_photos.py --label-from-folder`（会顺带调用 `bake_tints.py`）。
- **方图必须铺满**：`photos/sq` 用默认的 640×640 居中裁切，不要加 `--sq-fit`。等比缩进浅色底会在格子四边留纸白，手风琴细条的胶囊圆角和照片环「上栏圆上两角 / 下栏圆下两角」都会落在白底上看不见，看起来像直角；CSS 的圆角值本身没问题。
- **加章**：`CHAPTERS` 加一条的同时，`LB_SND` / `VOICE` / `SCENES` 三个数组都要补到相同项数；首页手风琴卡由 `buildHero()` 遍历全部章节自动生成，但要检查窄屏 `--slim` 还给不给展开卡留够宽度。
- **联系页**：`#/contact` 的内容来自 `THEME` 旁边的 `CONTACT` 常量，顶部导航的 `Contact us` 在 `Album` 左侧；不要再把联系方式塞回首页 hero-top。
- **本地运行**：`python3 -m http.server 8765`，然后访问 http://localhost:8765 。不能用 `file://` 打开，否则读不到照片像素：首页染色会退回 `photos/tints.js` 的预烘色块，风格台和大图失效。换了 `photos/sq` 要重跑 `skills/photo-album/scripts/bake_tints.py`。
- **版权**：当前 `photos/` 是 AI 生成的演示素材；换成真实会员 / 教练照片前先取得肖像授权，未成年人照片不要用，也不要把照片复制到别的项目里。
