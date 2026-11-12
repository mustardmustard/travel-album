---
name: photo-album
description: >-
  把一文件夹健身房训练照片做成一个单文件的互动照片展示网站：照片环、会躲鼠标并染上照片颜色的点阵大字、横滑章节页、实时风格台、点阵显影的单张大图和放大镜，以及每章不同的现场合成轻快钢琴声音。风格从用户自己的照片里读出来，所以每家馆做出来都不一样。
  Turn a folder of gym / fitness / training photos into a single-file interactive photo-display website (photo ring, particle type tinted by photos, chapters by training program, live print styles, a particle-developing photo viewer with loupe, per-chapter synthesized light, brisk piano sound) whose visual and sonic style is derived from the user's own photos. Use when someone wants a gym album, fitness portfolio, workout showcase, training gallery or studio site "like this one" or "in this style". 触发词：gym / fitness / 健身 / 训练 / workout / 健身房照片展示 / 训练相册.
---

# Photo Album：照片即材料的健身房照片展示

本仓库的 `index.html` 既是作品，也是模板。这份 skill 教你做两件事：读懂它为什么长这样，然后用**另一家馆的照片**做出一个同样完成度、风格却完全属于那些照片的网站。

## 先记住这一句

> **不变的是引擎和原理，变的是风格 DNA。** 风格 DNA 从照片里读出来，跟用户确认后，再填进模板的旋钮里。

五条原理，详见 `references/principles.md`。动手之前先读一遍：

1. **照片是唯一的原材料**：所有颜色、形状、声音都从像素里算出来。
2. **外壳克制**：纸、墨、一个来自照片的强调色、一套字体。
3. **一切都有物理感**：惯性、回弹、飞行、显影，没有硬切。
4. **每章一种训练质感**：同时落在画面、交互、声音三个层面。
5. **单文件、零构建、零音频文件**：执行 `python3 -m http.server` 就能跑。

## 文件地图

| 文件 | 什么时候读 |
|---|---|
| `references/principles.md` | 开始前，必读 |
| `references/style-dna.md` | 第 2–3 步，必读。照片 → DNA 的映射表、健身项目识别线索表、确认问题、防撞衫检查和健身专属规则 |
| `references/examples.md` | 第 2 步。模板原始站的 GYM 基线 DNA，加 3 份截然不同的示例 |
| `references/components.md` | 第 4 步。每个部件的契约、旋钮和可替换形式 |
| `references/sound.md` | 第 4 步。轻快钢琴乐器族、按训练强度/项目选的音阶、每章声音配方、音量预算 |
| `chapters.json` | 第 1 步。站点根目录下的项目 manifest：每章一条 `dir` + `label` + `photos:[{src,w,h,from}]`，`src` 是带章节目录的相对路径（如 `cutting/cutting-01-cardio`），直接抄进 `CHAPTERS` |
| 项目分组（按项目分文件夹生成 manifest） | 第 1 步。照片按训练项目放进子文件夹（本站 7 个：`deadlift/`、`glutes/`、`shoulders/`、`yoga/`、`cutting/`、`dance/`、`pilates/`），由 `prepare_photos.py` 的 `--label-from-folder` 模式读取并输出 `chapters.json`；这是既有脚本的一个开关，没有独立的分类脚本文件 |
| `scripts/prepare_photos.py` | 第 1 步。按章节生成 `photos/sq/<章节>/`、`photos/full/<章节>/`，并自动调用 `bake_tints.py`；加 `--label-from-folder` 时额外输出 `chapters.json`（`--order` 可定章节顺序） |
| `scripts/bake_tints.py` | 递归扫描 `photos/sq/<章节>/`，生成 `photos/tints.js`：每张方图的 32×32 色块，键名是 `章节/名字`。读不到像素时首页点阵字靠它染色。手动换过 `photos/sq` 后重跑 |
| `scripts/analyze_photos.py` | 第 1 步。递归扫描 `photos/full/<章节>/`，生成 `dna-seed.json`（含按项目分组的 `exercise_draft_by_label` 和按颜色粗分的 `chapter_draft_by_color`）和 `contact.jpg`；只在自己的 `--out` 目录里找 `chapters.json` |
| `../../index.html` | 模板。顶部的「风格区」是要填的地方，其余是引擎 |

## 流程

### 第 0 步：确认输入

- 照片文件夹：8–40 张都可以。推荐 28 张（7 章 × 4 张，每章 1 张氛围/器械图 + 3 张动作图），本仓库当前模板站就是 7 章 28 张。不到 24 张时，照片环会循环补满四条边；不到 8 张的话，首页建议换成照片堆（见 `components.md` 第 1 节）。超过 40 张，首页会很挤，可以挑选一下。
- **照片按训练项目分组**：把照片放进按项目命名的子文件夹，本站 7 章为 `deadlift/` 硬拉、`glutes/` 臀腿、`shoulders/` 肩部、`yoga/` 瑜伽、`cutting/` 减脂、`dance/` 舞蹈、`pilates/` 普拉提；顺序是力量主项 → 收操 → 有氧 → 团课 → 控制。这是后面分章和配声音的依据，不要只按颜色分。**站点照片也按同一套子文件夹存放**：`photos/sq/<章节>/`、`photos/full/<章节>/`。
- **肖像授权**：画面里有会员、教练或路人时先拿到书面 consent；未成年人照片一律排除；记下授权范围，后面写进 `portrait_release`、`credit` 和 `license`。拿不到授权的照片换成器械空镜、局部特写或背影。
- 新站放在哪个文件夹。**不要在本仓库里覆盖现有站点。**
- 照片版权归用户。如果混有别人的作品（比如用其他风格 skill 生成的图），记下作者和许可，后面写进 `credit` 和 `license`。器械品牌 logo 与商标也要留意：别拿商标色当强调色，商用时另行确认商标使用授权。

### 第 1 步：整理和测量照片

```bash
python3 skills/photo-album/scripts/prepare_photos.py <照片文件夹> --label-from-folder --sq-fit \
    --order deadlift,glutes,shoulders,yoga,cutting,dance,pilates --out <新站文件夹>
python3 skills/photo-album/scripts/analyze_photos.py <新站文件夹>/photos/full --out <新站文件夹>
```

- 第一个脚本把不同章的照片分别写进 `photos/sq/<章节>/` 与 `photos/full/<章节>/`，打印每张的 `src`、`w`、`h`，并写出 `chapters.json`（每章 `dir` + `label`，照片 `src / w / h / from`）。**`src` 带章节目录**（如 `dance/dance-02-leap`），直接抄进 `CHAPTERS` 就能被 `photoURL()` 拼成正确路径。
- `--order` 决定 `chapters.json` 里的章节顺序（不填按文件夹名字母序）；`CHAPTERS` 里的展示顺序由你另行决定，不必和它一致。
- 两个脚本用同一个 `--out`：`analyze_photos.py` 只在自己的 `--out` 目录里找 `chapters.json`，放一起才能给 `contact.jpg` 标出项目、让 `dna-seed.json` 带上 `exercise_draft_by_label`（没有 manifest 时它是空数组）。它递归扫描 `photos/full` 下各章节子文件夹，按 `src` 匹配标签。
- 竖幅全身动作多时给第一个脚本加 `--sq-fit`（方图等比缩进浅色底，不居中裁切），避免头脚被切掉；默认仍是 640×640 居中裁切。`--sq-fit` 和 manifest 无关，可单独开关。
- `bake_tints.py` 由第一个脚本自动调用，递归收齐所有章节的方图；`tints.js` 的键名与 `CHAPTERS` 的 `src` 完全一致，改过目录结构一定要重跑，否则首页悬停时会全部退回强调色。
- 脚本需要 Pillow（`pip install pillow`）。纯中文文件名会被 `slug()` 过滤成空字符串，脚本会用「项目文件夹名 + 序号」兜底并在 stderr 提示；文件名里留一段英文动作名最省心。

### 第 2 步：读照片，起草 DNA

1. 打开 `contact.jpg` 亲眼看。只看数字是读不出动作、器械、身体部位、训练强度和场馆光线的；照片按项目分了文件夹时，编号旁会带 `label`。
2. 读 `dna-seed.json` 的 `summary`、`accent_candidates`、`paper_ink`、`chapter_draft_by_color` 和 `exercise_draft_by_label`。其中 `chapter_draft_by_color` 只是按颜色粗分的辅助信号，正式分章以 `exercise_draft_by_label` 的项目标签为准（见 `style-dna.md` 第 4 节）。
3. 按 `references/style-dna.md` 的格式，在新站根目录写 `style-dna.yaml`。规矩：
   - **每个决定都写出处**：来自哪张照片、哪个数字，或者用户的哪句话；
   - 强调色只能从照片里来，器械品牌 logo 和商标色不算候选；
   - 起草两套方向：A 贴近照片本来的训练质感，B 在器械母题或反差上更大胆；
   - 填 `portrait_release`，把肖像授权范围写清楚。
4. **防撞衫检查**（`style-dna.md` 第 6 节）：跟 `examples.md` 里的 GYM 基线 DNA 比，至少 4 项不同。

### 第 3 步：跟用户确认，最多 4 个问题，一次一个

问题清单在 `style-dna.md` 第 5 节。每个问题都附上你的推荐答案和理由，用户回答"按你的来"也可以。

跳过的标准：用户原话里**直接**给出了答案，才跳过。比如用户说"不要声音"或"门店大屏，声音默认关"，就跳过第 4 题。如果只能从原话里推测，比如"收操为主"推出"声音轻一点"，那就仍然要问，只是把推测写成你的推荐答案。

问完之后定稿 `style-dna.yaml`。

### 第 4 步：搭站

1. 把本仓库的 `index.html` 复制到新站文件夹。照片在第 1 步已经放进新站的 `photos/` 了。**不要把本仓库的照片带过去。**
2. 按 DNA 填「风格区」，这些地方都有 `风格区` 注释，搜得到：

   | 位置 | 填什么 |
   |---|---|
   | `<title>`、Google Fonts 的 `<link>` | display 字体和中文配字（馆名、口号里的英文走 display） |
   | CSS `:root` | `--bg`、`--ink`、`--accent`、`--on-accent`、`--cjk`、`--display`、`--stretch`、`--case`、`--ph`、`--ease` |
   | JS `THEME` | 标题、logo、年份、hero、字体（`upper` 要和 `--case` 一致）、音阶、`presence`、`motion`；门店大屏把 `soundOn` 设为 false |
   | `CHAPTERS` | 每章 `en / zh / dir / line` 和照片 `src / w / h / cap`。**`src` 必须带章节目录**（`dance/dance-02-leap`），`dir` 与 `chapters.json` 的目录一致；第三方作品加 `credit` 和 `license`，人像照片补上肖像授权说明 |
   | `CONTACT` | 联系页的场馆名、微信、联系人、电话；改这里就够了，`initContact()` 会生成 `#/contact` 的清单和复制按钮 |
   | `TEXT_TILES` | 两块文字砖（一句口号 + 统计数字） |
   | 「声音：风格区」 | `RING_SND`（首页旋律和乐器）、`LB_SND`、`VOICE`、`SCENES`，按 `sound.md` 的配方给每章重写。**四个数组/对象都要和 `CHAPTERS` 一一对应**，加章必须同步加项 |

3. 风格台：按 DNA 的 `texture.styles` 保留或改写效果函数。接口和效果配方见 `components.md` 第 4 节。
4. DNA 的 `swaps` 里有替换项时，按 `components.md` 对应部件的"同级替代"去改。**最多 2 个，并且保持对外接口不变。**
5. 全局搜一遍旅游词残留，搜到就换掉。要不分大小写地搜：

   ```bash
   grep -niE "旅行|travel|旅の|japan|日本|tokyo|osaka|kobe|kyoto|度假|景点|游记|vacation|sightseeing|trip" index.html
   ```

   再确认健身词已经进站（搜不到就说明风格区没填完）：

   ```bash
   grep -niE "training|deadlift|glutes|shoulders|yoga|cutting|dance|pilates|workout|gym|训练|健身|硬拉|臀腿|肩|瑜伽|减脂|舞蹈|普拉提|组|次" index.html
   ```

   风格区注释里描述原模板站的话，比如"宽体无衬线，像站牌和招牌"，也要改成新站自己的理由（器械铭牌、项目编号、组次标签）。
6. 写一份新站自己的 `README.md`：怎么在本地运行、怎么换照片、署名与版权、肖像授权与商标说明。结构可以参考本仓库的 README。

### 第 5 步：验收

起本地服务器（`python3 -m http.server 8765`），在浏览器里逐条检查。

**功能**
- [ ] 首页：照片环会流动，可推动，带惯性；点阵大字躲鼠标；悬停照片时变成章节名并染上照片颜色
- [ ] 首页手风琴卡数量 = 章节数，窄屏下展开的那张仍有可读宽度
- [ ] 顶部导航 `Contact us` 在 `Album` 左侧，`#/contact` 能显示场馆名 / 微信 / 联系人 / 电话，复制按钮可用，Back 能回到来处
- [ ] 每一章都能进入，横滑带惯性，照片保持原始比例；`photos/sq/<章节>/`、`photos/full/<章节>/` 全部 200，`tints.js` 键名与 `CHAPTERS.src` 完全一致
- [ ] 风格台 1–4 都能出图；色块效果给出调色板
- [ ] 大图：粒子飞出，由粗到细显影；左右切换；1–4 换风格；放大镜能放到看见像素；取色正常；Esc、返回键、点空白处都能关闭；`#/ch/N/M/view` 直接打开正常
- [ ] 声音：第一次点击后自动开启；每章环境声不同；大图事件音齐全；`LB_SND / VOICE / SCENES` 项数 = 章节数，逐章进入都不报 undefined；七章按训练质感分布（硬拉 108、臀腿 116、肩部 126、瑜伽 88、减脂 138、舞蹈 128、普拉提 100 BPM，全在一台钢琴上）；每章大图峰值在 0.10–0.32（测法见 `sound.md` 第 6 节）

**体验**
- [ ] 手机宽度（375px）下没有横向滚动；大图变成底部抽屉；按住照片能拖放大镜
- [ ] 开启 `prefers-reduced-motion` 时，动画退化成直接切换，功能完整
- [ ] 键盘可以走完全部流程（Tab、Enter、方向键、1–4、Esc）
- [ ] 控制台没有错误
- [ ] 门店/大屏部署时 `THEME.soundOn` 为 false，第一次点击后才开声

**风格**
- [ ] 随便指一个颜色，都能说出来自哪张照片（原理 1）
- [ ] 把照片换成灰块后，页面很空（原理 2）
- [ ] 闭上眼也能听出是哪一章、是重还是轻（原理 4）
- [ ] 跟原模板站（GYM 基线示例）并排放，一眼就能看出不是同一个站

**合规**
- [ ] 人像照片都有肖像授权记录（`portrait_release`、`credit`、`license`），未成年人照片已排除
- [ ] 器械品牌 logo 与商标没有变成强调色，也没有照搬进馆名和文字砖
- [ ] 图注只写训练感受，不写动作要领、不做教学示范

最后截图给用户看，并请用户自己听一遍声音。测量只能保证声音不爆、不哑，好不好听要人耳判断。

## 健身房展示的专属规矩

这几条是健身照片一定会碰到的，起草 DNA 和填站时都要过一遍，细节见 `style-dna.md` 第 7 节：

- **肖像授权**：会员、教练、路人的书面 consent，未成年人一律排除；`portrait_release` 必填，`credit` / `license` 写清授权范围。镜面反射里的人像也要算进去。
- **品牌 logo 与器械商标**：不是母题，强调色不从商标色里取；`TEXT_TILES`、馆名、`hero.word` 不照搬品牌名；商用另行确认商标授权。
- **低光、镜面、竖幅**：低光加镜面亮斑常被 `night_guess` 误判成夜景、`night_share` 偏高，`paper_ink` 会给深色纸候选，以看图为准；竖幅全身动作容易被 640×640 居中裁切切掉头脚，必要时用 `--sq-fit`。
- **图注不做教学示范**：只写训练感受，不写动作要领、组数次数和发力提示，避免动作误导和安全责任。
- **门店大屏声音默认关**：常年无人交互时把 `THEME.soundOn` 设为 false，由第一次点击开启。

## 踩过的坑

- **双击 `index.html` 用 `file://` 打开时**，浏览器不让读像素。首页点阵字的染色和悬停音高会退回 `photos/tints.js` 里预烘的色块，所以 `tints.js` 一定要跟着照片重新生成，否则悬停时全是强调色；风格台和大图仍然需要本地服务器。
- **照片改用章节子文件夹后，键名要一起改**：`CHAPTERS.src` 写成 `cutting/cutting-01-cardio` 这类相对路径，`bake_tints.py` 用 `rglob` 递归扫描并以相对路径做键，两边完全一致才能染色。只挪文件、不改 `src`（或只改一边）会出现「图片都加载成功但悬停全是主色」的假故障。
- **加章忘了扩声音数组**：`LB_SND`、`VOICE`、`SCENES` 都是按 `CHAPTERS` 下标取的，新增章节时少加一项，进那一章就会拿到 `undefined`；`VOICE[ci]` 甚至会直接抛错。加章时三处一起加。
- **顶部导航塞了 5 个入口后窄屏会挤**：flex 项默认可收缩，链接文字会折行甚至被裁掉。窄屏要给 `.nav a` / `.about-trigger` 加 `white-space:nowrap;flex:none`，放不下时按断点先隐藏 `Chapters`（首页还有章节细导航和类目卡）。
- **纯中文文件名会被 `slug()` 变成 `photo`**：`slug()` 只留 ASCII，纯中文文件名（如 `硬拉1.jpg`）会退化成空字符串，多张会全撞成 `photo` 互相覆盖。现在的脚本会用「项目文件夹名 + 序号」兜底并在 stderr 提示，但最省心的还是文件名里留一段英文动作名（如 `deadlift-01.jpg`）。
- **竖幅全身动作被 640×640 居中裁切切掉**：首页方图默认 `ImageOps.fit` 居中裁切，硬拉、深蹲、站姿体式这类竖幅全身照头脚容易被切。`portrait_share` 高时先看成图，或用 `--sq-fit` 等比缩进浅色底。
- **会员肖像授权**：人像照片要拿到会员/教练的书面 consent，未成年人一律排除，`credit` / `license` 写清授权范围，DNA 里填 `portrait_release`。没有授权的照片宁可换器械空镜、局部特写或背影；镜面里的反射人像也算。
- **门店大屏声音默认关**：门店、前台大屏常年无人交互，浏览器不会自动播。把 `THEME.soundOn` 设为 false，由第一次点击开启，既避免静音或报错，也不打扰店内。
- **在浏览器里验证 `file://` 的退路**：把 `getImageData` 改成读到照片就抛 SecurityError，再悬停照片，看 `P.tinted` 是否为 true。
- **canvas 默认宽度是 300**。如果你按"尺寸变了才重设"的逻辑去改 canvas，而目标尺寸恰好是 150 × 2（dpr），就永远不会触发重设。要另外记住上一次的尺寸（参考 `LP.L`）。
- **合成触摸事件时，`setPointerCapture` 可能抛错**，要用 try/catch 包起来。
- **从 window 上派发的 keydown，`e.target` 不是 Node**，判断之前先用 `instanceof Node`。
- **有的预览面板在后台时会暂停 `requestAnimationFrame`**，动画看起来像"卡住"。验证时先截一张图把页面唤醒，或者直接读状态变量来确认。
- **跑动密的章（减脂 16 分跑动）叠上环境声，峰值容易冲上预算上限。** 降这一章乐器的力度 `v`、减少同时落下的音数或拉开 `pianoRun` 的 `gap`，不要动压缩器；压总线会把钢琴的槌击瞬态一起压没。
- **测声音峰值时数字跳得厉害**：和弦落点与混响尾巴的相位每轮不同，幕布转场还有一声风。测法见 `sound.md` 第 6 节，要多测几次取中位数。
- **验证脚本连续改网址时**，两次之间至少等 1.2 秒，让幕布转场走完。引擎已经处理了"转场途中又跳到大图"的竞态，但等转场走完的结果最稳定。
- **点阵大字用细字重时取不到足够的点。** display 字重要 ≥ 700。

## 署名

- 照片环和点阵大字的交互结构，参考了 Framer 模板 Squareo（Iconic Graphics）的思路。代码、设计和素材都是本仓库原创。
- 新站沿用这套结构时，建议在 README 里保留这句来源说明。
- 本仓库的照片归原作者所有，不随 skill 授权。
