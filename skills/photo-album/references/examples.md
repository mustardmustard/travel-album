# 示例：同一套流程，四种截然不同的结果

第一份是模板原始站的 GYM 基线 DNA，作为防撞衫检查的对照基准。后三份是虚构的，用来示范：照片证据不同，流程得出的决定会差多远。（旧版的 JAPAN 基准已更换为 GYM 基线。）

**它们不是可以套用的成品。** 新站的 DNA 必须从新照片里读出来，然后过 `style-dna.md` 第 6 节的防撞衫检查。

---

## A. GYM（模板原始站，GYM 基线）

```yaml
program: "一次训练：从最重的一组硬拉，收在最后一个呼吸"
venue: 城市综合训练馆（力量区 + 团课区）
portrait_release: "会员与教练均已签署肖像授权；未成年人照片已排除；仅用于本馆展示"
evidence:   # analyze_photos.py 实测
  tone: dark / contrast: hard / chroma: muted / temperature: cool
  hue_spread: concentrated, dominant_hue: 207° / night_share: .52 / portrait_share: .78
  accent_candidates: 护腕橙 #E2642C (18°), 杠铃片蓝 #2E6FD0 (217°), 镁粉白 #EDEAE1
color:
  paper: "#0F1419"   # tone 偏暗、night_guess 过半 → 深色纸，让顶光与镜面高光发亮；镜面亮斑不是夜景，看图确认过
  ink: "#EAF0F4"
  accent: "#F26A2E"  # 护腕 / 杠铃片边缘的 #E2642C 提纯，色相 18° → 16°。母题：护腕、杠铃片、地垫边缘的橙，四章都出现，全站签名
  on_accent: "#0F1419"
type:
  display: Archivo, stretch: expanded (--stretch 125%), case: upper (--case uppercase, upper:true)
  cjk: Noto Sans SC
  why: 器械铭牌、项目编号、组次标签都是宽体全大写，经得住点阵化
hero: { word: GYM, sub: "Training / 26 / 11", line: "Deadlift · Glutes · Shoulders · Yoga" }
motion: { character: 利落·力量, drift: .0032, follow: .075, spring: .06, damp: .82, repel: 60, gather: 950, develop: 1250 }
texture:
  dots: circle
  styles: [orig, ink, dot, block]   # 油墨橙黑双色像器械铭牌和海报；网点像镜面颗粒；色块给出调色板
sound: { scale: "[0,2,3,5,7,9,10] 多利亚", base: 57, presence: .9 }
chapters:
  - { en: DEADLIFT,  zh: 硬拉, exercise: 传统硬拉,               body_part: 后链 / 臀·腘绳·背, intensity: 极重·爆发,     equipment: 杠铃·镁粉·腰带,   mood: 重,       ambient: 124BPM kick 每拍 + offbeat open hat + sub 根音 + stab 每 2 小节, voice: stab }
  - { en: GLUTES,    zh: 臀腿, exercise: 臀推 / 深蹲 / 腿举,     body_part: 臀·股四头,         intensity: 中高·持续酸胀, equipment: 深蹲架·臀推凳,     mood: 持续酸胀, ambient: 126BPM kick 四拍 + 16 分 hat + offbeat bass 切分 + 反拍 stab, voice: stab }
  - { en: SHOULDERS, zh: 肩部, exercise: 侧平举 / 推举 / 面拉,   body_part: 三角肌,             intensity: 中·精准轻快,   equipment: 哑铃·龙门架,       mood: 精准轻快, ambient: 128BPM kick + clap 落 2/4 拍 + 16 分 hat + lead 短句, voice: lead }
  - { en: YOGA,      zh: 瑜伽, exercise: 伸展体式 / 收操,         body_part: 全身·呼吸,          intensity: 低·慢与留白,   equipment: 瑜伽垫,             mood: 慢与呼吸, ambient: 100BPM soft kick 每 2 拍 + 长 stab/pad + air 气息 + 留白, voice: lead }
swaps: []
```

共 16 张：每章 1 张氛围/器械图 + 3 张动作图；顺序是主项 → 下肢辅助 → 上肢 → 收操，强度与音量由重到轻。

---

## B. 铁馆（虚构）

```yaml
program: "地下铁馆，一组一组把重量往上加"
venue: 老厂房改造的力量举铁馆
portrait_release: "教练已签署肖像授权；会员均为背影或局部；未成年人照片已排除"
evidence:
  tone: dark / contrast: hard / chroma: muted / temperature: warm
  hue_spread: concentrated, dominant_hue: 28° / night_share: .68 / portrait_share: .55
  accent_candidates: 锈红 #7A3B2A (14°), 钨丝灯 #E8A93C (38°), 生铁 #4A4E52
color:
  paper: "#14100E"   # 低光钨丝、暗调过半 → 深色纸；钨丝灯是亮光源，深纸让它发亮
  ink: "#EFE8DC"
  accent: "#E8542A"  # 锈红 #7A3B2A 提纯。旧杠铃片边缘、锈迹、旧海报在 3 章里反复出现，是这组照片的母题
type:
  display: Big Shoulders Display (800), case: upper
  cjk: Noto Sans SC
  why: 窄而高，像杠铃杆和立柱；重、克制
hero: { word: IRON, sub: "Training / 26 / 11", line: "Deadlift · Squat · Press · Carry" }
motion: { character: 机械·工业器械, drift: .005, follow: .11, spring: .09, damp: .74, repel: 50, gather: 750, develop: 900 }
texture:
  dots: square    # 像铸铁块、像编号牌
  styles: [orig, riso, pixel, block]   # riso 双色像旧海报；像素马赛克像铸铁颗粒
sound: { scale: "[0,3,5,7,10] 小调五声", base: 55, presence: 1.3 }
chapters:
  - { en: DEADLIFT, zh: 硬拉, exercise: 传统硬拉,     body_part: 后链,       intensity: 极重·爆发, equipment: 杠铃·镁粉,   mood: 重,     ambient: 128BPM kick 每拍 + 饱和 sub, voice: stab }
  - { en: SQUAT,    zh: 深蹲, exercise: 背蹲 / 前蹲,   body_part: 股四头·臀, intensity: 重·持续,   equipment: 深蹲架,       mood: 持续,   ambient: 126BPM 切分 stab,        voice: stab }
  - { en: PRESS,    zh: 推举, exercise: 卧推 / 实力推, body_part: 胸·肩·三头, intensity: 中·精准,   equipment: 卧推架·杠铃, mood: 精准,   ambient: 124BPM 明亮 lead,        voice: lead }
  - { en: CARRY,    zh: 行走, exercise: 农夫行走,     body_part: 握力·核心, intensity: 中低·收尾, equipment: 哑铃·壶铃,   mood: 收尾,   ambient: 100BPM 铺底 + sweep,     voice: lead }
swaps:
  - 大图显影 → 扫描线显影   # 质感是"铸铁、编号牌"，点阵由粗到细像印刷，跟老厂房铭牌的气质冲突
```

跟 GYM 基线不同的地方：纸、强调色色相、字体、动效、粒子、风格台、音阶、乐器，8 项全不同。

---

## C. 高温瑜伽馆（虚构）

```yaml
program: "40 度房间里，把呼吸拉得比动作长"
venue: 高温瑜伽馆
portrait_release: "团课会员均签署肖像授权；未成年人照片已排除；仅用于馆内展示"
evidence:
  tone: bright / contrast: soft / chroma: moderate / temperature: warm
  hue_spread: mixed / night_share: .02 / portrait_share: .7
  accent_candidates: 柚木 #C98A4B (30°), 雾白 #EFE6D8, 垫子绿 #6E8F76 (140°)
color:
  paper: "#FBF4E8"   # 明亮偏暖 → 浅色暖纸
  ink: "#2A2620"
  accent: "#D98C4A"  # 柚木地板 / 更衣区木色，几乎每张都有；不取垫子绿，因为那只是一张垫子的偶然色
type:
  display: Fraunces (700), case: mixed
  cjk: Noto Serif SC
  why: 人文衬线、大小写混排，像呼吸一样不使劲
hero: { word: BREATHE, sub: "Training / 26 / 11", line: "Flow · Balance · Stretch · Rest" }
motion: { character: 柔软·柔韧, drift: .0018, follow: .05, spring: .035, damp: .88, repel: 75, gather: 1200, develop: 1700 }
texture:
  dots: line      # 粒子画成随速度拉长的短线，像呼吸里拉长的雾（旋钮，不算 swaps）
  styles: [orig, line, riso, block]   # 线稿：伸展的边缘；riso 双色像木地板与雾；色块保留
sound: { scale: "[0,2,4,7,9] 大调五声", base: 64, presence: .6 }
chapters:
  - { en: FLOW,     zh: 流动, exercise: 拜日式串联,   body_part: 全身,     intensity: 低中·连贯, equipment: 瑜伽垫,       mood: 连贯,   ambient: 104BPM 软铺底 + 稀疏 hat, voice: lead }
  - { en: BALANCE,  zh: 平衡, exercise: 站立体式,     body_part: 足踝·核心, intensity: 中·专注,   equipment: 瑜伽垫,       mood: 专注,   ambient: 102BPM 轻 stab,           voice: stab }
  - { en: STRETCH,  zh: 伸展, exercise: 前屈 / 开髋,   body_part: 髋·腘绳,   intensity: 低·持续,   equipment: 瑜伽砖·伸展带, mood: 持续,   ambient: 100BPM 长音铺底,          voice: lead }
  - { en: REST,     zh: 休息, exercise: 摊尸式 / 收操, body_part: 全身·呼吸, intensity: 最低·留白, equipment: 毛毯·瑜伽垫,   mood: 慢与呼吸, ambient: 96BPM 只留铺底与留白,    voice: lead }
swaps:
  - 首页照片环 → 无限网格漂移   # 动效性格是"柔软·柔韧"；四条边带的环形流动太"力量"，跟呼吸留白的整面墙冲突
```

---

## D. 私教康复工作室（虚构）

```yaml
program: "一对一，把每个动作都拆慢、做准"
venue: 私教康复工作室
portrait_release: "会员均签署肖像授权（仅限本馆展示）；未成年人及未授权路人已排除；镜面反射人像一并核对"
evidence:
  tone: bright / contrast: normal / chroma: muted / temperature: cool
  hue_spread: concentrated, dominant_hue: 195° / night_share: .05 / portrait_share: .82
  accent_candidates: 器械蓝 #2E6F86 (195°), 弹力带黄 #D9C34A (52°), 墙面白 #ECEFF1
color:
  paper: "#F4F8F9"   # 亮、冷 → 浅色冷纸
  ink: "#1B2428"
  accent: "#2E86A8"  # 康复器械与弹力带的蓝，冷而克制，反复出现在器械与标识上；弹力带黄太跳，放弃
type:
  display: Space Mono (700), case: upper
  cjk: Noto Sans SC
  why: 等宽体像评估表、角度刻度、康复记录
hero: { word: REBUILD, sub: "Training / 26 / 11", line: "Assess · Mobilize · Load · Recover" }
motion: { character: 利落·精准, drift: .0028, follow: .08, spring: .055, damp: .84, repel: 58, gather: 900, develop: 1150 }
texture:
  dots: circle
  styles: [orig, scan, ascii, block]   # 扫描线像评估屏幕；ASCII 像角度刻度读数
sound: { scale: "[0,2,3,5,7,8,10] 自然小调", base: 60, presence: .7 }
chapters:
  - { en: ASSESS,   zh: 评估, exercise: 体态评估 / 关节活动度, body_part: 全身,       intensity: 最低·静态, equipment: 评估表·角度尺, mood: 冷静,   ambient: 100BPM 铺底 + 稀疏 sweep, voice: lead }
  - { en: MOBILIZE, zh: 活动, exercise: 弹力带激活 / 灵活性,   body_part: 肩髋·核心, intensity: 低·精准,   equipment: 弹力带·泡沫轴, mood: 精准,   ambient: 108BPM 轻 stab,           voice: stab }
  - { en: LOAD,     zh: 加载, exercise: 轻负荷抗阻,             body_part: 目标肌群,   intensity: 中·可控,   equipment: 小哑铃·绳索,   mood: 可控,   ambient: 116BPM kick + sub,          voice: stab }
  - { en: RECOVER,  zh: 放松, exercise: 拉伸 / 筋膜放松,         body_part: 全身·呼吸, intensity: 最低·收尾, equipment: 瑜伽垫·泡沫轴, mood: 慢与呼吸, ambient: 98BPM 只留铺底,          voice: lead }
swaps:
  - 大图显影 → 扫描线显影   # 质感是"评估屏幕、刻度"，点阵由粗到细像印刷，跟冷白临床气质冲突
```

---

## 看出来了什么

- **证据不同，决定就不同。** 深色纸、强调色、字体、动效、音阶，每一项都能追溯到 evidence 里的数字，或者看图得到的器械母题。
- **强调色永远只有一个，永远来自照片。** 照片颜色四散时更要克制；照片接近单色（B）时，就去找唯一的反差点。器械品牌 logo 与商标色不算候选。
- **替换部件是例外，不是常规。** 四份里只有三份各换了一个部件，而且都写了是哪条 DNA 跟默认部件冲突。
- **肖像授权是硬门槛。** 四份 DNA 都带 `portrait_release`；人像照片的 `credit` / `license` 写清授权范围，未成年人一律排除。
- **防撞衫都跟 A 的 GYM 基线比。** 基准已从 JAPAN 更换为 GYM 基线，至少 4 项不同（见 `style-dna.md` 第 6 节）。
