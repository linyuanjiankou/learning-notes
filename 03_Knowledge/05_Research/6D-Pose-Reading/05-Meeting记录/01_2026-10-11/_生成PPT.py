# -*- coding: utf-8 -*-
"""生成本次个人 Meeting 的 PPT。依赖 python-pptx。用法：python _生成PPT.py"""
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "个人Meeting.pptx")

CJK = "微软雅黑"
DARK = RGBColor(0x1F, 0x2A, 0x37)
ACCENT = RGBColor(0x2E, 0x74, 0xB5)
GRAY = RGBColor(0x5A, 0x63, 0x72)
LIGHT = RGBColor(0xF2, 0xF5, 0xF9)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
BLANK = prs.slide_layouts[6]


def set_run(run, size=18, bold=False, color=DARK, name=CJK):
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = name
    rPr = run._r.get_or_add_rPr()
    for tag in ("a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is None:
            el = rPr.makeelement(qn(tag), {})
            rPr.append(el)
        el.set("typeface", name)


def textbox(slide, x, y, w, h):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    return tf


def bar(slide, x, y, w, h, color=ACCENT):
    sh = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = color
    sh.line.fill.background(); sh.shadow.inherit = False
    return sh


def title_bar(slide, text, idx=None):
    bar(slide, 0, 0, 13.333, 1.05, DARK)
    tf = textbox(slide, 0.55, 0.16, 11.5, 0.75)
    p = tf.paragraphs[0]
    set_run(p.add_run(), 26, True, RGBColor(0xFF, 0xFF, 0xFF)); p.runs[0].text = text
    if idx:
        tf2 = textbox(slide, 12.1, 0.22, 0.9, 0.6)
        p2 = tf2.paragraphs[0]; p2.alignment = PP_ALIGN.RIGHT
        set_run(p2.add_run(), 18, True, RGBColor(0x9F, 0xC5, 0xEA)); p2.runs[0].text = idx


def bullets(slide, items, x=0.7, y=1.4, w=12.0, h=5.6, size=18, gap=6):
    tf = textbox(slide, x, y, w, h)
    first = True
    for it in items:
        text, level, kind = it if isinstance(it, tuple) else (it, 0, "bullet")
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.space_after = Pt(gap); p.level = level
        sized = size - (2 if level else 0)
        if kind == "head":
            set_run(p.add_run(), size + 2, True, ACCENT); p.runs[-1].text = text
        elif kind == "sub":
            set_run(p.add_run(), sized, False, GRAY); p.runs[-1].text = "– " + text
        elif kind == "plain":
            set_run(p.add_run(), sized, False, DARK); p.runs[-1].text = text
        else:
            set_run(p.add_run(), sized, False, DARK); p.runs[-1].text = "•  " + text
    return tf


def table_slide(slide, headers, rows, x=0.7, y=1.45, w=11.9, h=4.6, col_w=None, size=14):
    shape = slide.shapes.add_table(len(rows) + 1, len(headers), Inches(x), Inches(y), Inches(w), Inches(h))
    tbl = shape.table
    if col_w:
        for i, cw in enumerate(col_w):
            tbl.columns[i].width = Inches(cw)
    for j, htxt in enumerate(headers):
        c = tbl.cell(0, j)
        c.fill.solid(); c.fill.fore_color.rgb = ACCENT
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = c.text_frame; tf.word_wrap = True
        p = tf.paragraphs[0]
        set_run(p.add_run(), size, True, RGBColor(0xFF, 0xFF, 0xFF)); p.runs[0].text = htxt
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = tbl.cell(i + 1, j)
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor(0xFF, 0xFF, 0xFF) if i % 2 == 0 else LIGHT
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf = c.text_frame; tf.word_wrap = True
            p = tf.paragraphs[0]
            set_run(p.add_run(), size, False, DARK); p.runs[0].text = val
    return tbl


# 1 封面
s = prs.slides.add_slide(BLANK)
bar(s, 0, 0, 13.333, 7.5, DARK)
bar(s, 0, 4.55, 13.333, 0.09, ACCENT)
tf = textbox(s, 1.0, 2.35, 11.3, 1.6)
p = tf.paragraphs[0]
set_run(p.add_run(), 40, True, RGBColor(0xFF, 0xFF, 0xFF)); p.runs[0].text = "6D Pose Estimation"
p2 = tf.add_paragraph()
set_run(p2.add_run(), 28, True, RGBColor(0xFF, 0xFF, 0xFF)); p2.runs[0].text = "学习进展汇报"
tf2 = textbox(s, 1.0, 4.8, 11.3, 1.2)
p = tf2.paragraphs[0]
set_run(p.add_run(), 18, False, RGBColor(0xC9, 0xD6, 0xE4)); p.runs[0].text = "个人 Meeting ｜ 2026-10-11"
p = tf2.add_paragraph()
set_run(p.add_run(), 16, False, RGBColor(0x9F, 0xC5, 0xEA)); p.runs[0].text = "学习阶段 · 建领域地图 + 精读论文 + 熟悉复现"

# 2 目录
s = prs.slides.add_slide(BLANK)
title_bar(s, "目录", "Agenda")
for k, a in enumerate(["01  方向与定位", "02  进展总览", "03  阅读地图：六阶段", "04  阶段一的关键收获",
                        "05  精读的三篇论文", "06  观察与思考", "07  待讨论的问题", "08  下一步计划"]):
    tf = textbox(s, 1.6 + (k // 4) * 6.0, 1.7 + (k % 4) * 1.25, 5.4, 1.0)
    p = tf.paragraphs[0]
    set_run(p.add_run(), 22, True, DARK); p.runs[0].text = a

# 3 方向与定位
s = prs.slides.add_slide(BLANK)
title_bar(s, "方向与自我定位", "01")
bullets(s, [
    ("研究方向：机器人多模态感知 / 具身智能", 0, "head"),
    ("切入点：6D Pose Estimation（3D 平移 + 3D 旋转，SE(3) 位姿）", 0, "bullet"),
    ("当前定位：学习 / 入门期 —— 建领域地图 + 精读论文 + 熟悉复现流程（尚未进入 Project）", 0, "bullet"),
    ("为什么选它：", 0, "head"),
    ("感知 → 抓取 / 操作的关键上游；BOP 评测生态成熟，便于低成本验证", 1, "sub"),
], y=1.6, size=20, gap=14)

# 4 进展总览
s = prs.slides.add_slide(BLANK)
title_bar(s, "进展总览", "02")
for k, (big, sub) in enumerate([("精读 3 篇", "BOP · PoseCNN\nπ₀.₅（领域外）"),
                                ("6 阶段 / 46 篇", "阅读地图\nP0 16 · P1 17 · P2 13"),
                                ("5/5", "总表已填充\n阶段总结 1 篇"),
                                ("3/6", "阶段一进度\n6D Pose 是什么")]):
    x = 0.7 + k * 3.05
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.7), Inches(2.8), Inches(2.1))
    sh.fill.solid(); sh.fill.fore_color.rgb = LIGHT
    sh.line.color.rgb = ACCENT; sh.shadow.inherit = False
    tf = sh.text_frame; tf.word_wrap = True
    p = tf.paragraphs[0]; p.alignment = PP_ALIGN.CENTER
    set_run(p.add_run(), 26, True, ACCENT); p.runs[0].text = big
    for line in sub.split("\n"):
        pp = tf.add_paragraph(); pp.alignment = PP_ALIGN.CENTER
        set_run(pp.add_run(), 14, False, GRAY); pp.runs[0].text = line
tf = textbox(s, 0.7, 4.3, 12.0, 2.4)
p = tf.paragraphs[0]
set_run(p.add_run(), 20, True, RGBColor(0xC0, 0x39, 0x2B)); p.runs[0].text = "当前最大卡点：代码复现 —— 计划已建，尚未动手跑通"
p = tf.add_paragraph()
set_run(p.add_run(), 18, False, DARK); p.runs[0].text = "•  目标 A（bop_toolkit + LM-O 评测）未启动"
p = tf.add_paragraph()
set_run(p.add_run(), 18, False, DARK); p.runs[0].text = "•  MR6D 仅略读，未深入；阶段一 3/6，剩 SSD-6D / DeepIM 未读"

# 5 阅读地图：六阶段
s = prs.slides.add_slide(BLANK)
title_bar(s, "阅读地图：六阶段", "03")
tf = textbox(s, 0.7, 1.25, 12.0, 0.6)
p = tf.paragraphs[0]
set_run(p.add_run(), 16, False, GRAY)
p.runs[0].text = "自己设计的 6D Pose 论文阅读计划：六阶段、共 46 篇，每往下一阶段就拆掉一行前提假设。"
table_slide(s, ["阶段", "主题", "篇数"],
            [["阶段一", "6D Pose 到底是什么（进行中 3/6）", "6"],
             ["阶段二", "2D → 3D → Pose 的核心路线", "7"],
             ["阶段三", "RGB-D 与现代 6D Pose", "8"],
             ["阶段四", "Category-level / CAD-free", "7"],
             ["阶段五", "Novel Object（重点关注）", "9"],
             ["阶段六", "Open-Vocabulary / Foundation / Open World", "9"]],
            col_w=[1.6, 8.5, 1.8], y=1.95, h=4.2, size=15)

# 6 阶段一关键收获
s = prs.slides.add_slide(BLANK)
title_bar(s, "阶段一的关键收获：6D Pose 是什么", "04")
bullets(s, [
    ("任务定义：给定图像，估计「已知刚体实例」相对相机坐标系的 R, t", 0, "head"),
    ("前提矩阵 = 阶段一到六的路线图：每往下一阶段，就拆掉一行前提", 0, "head"),
    ("输入模态 RGB-D → 纯 RGB → 基础模型；是否需要 CAD；训练时是否见过；视角是否固定", 1, "sub"),
    ("两条 pipeline（最有用的区分）", 0, "head"),
    ("model-based（BOP）：GT / 良好 mask → 匹配 / 回归 → 位姿；瓶颈 = 遮挡、光照", 1, "sub"),
    ("unseen（MR6D）：分割 → 识别 → 位姿，无对象特定训练；瓶颈 = 2D 分割质量", 1, "sub"),
    ("它把「方法本身好不好」和「上游环节好不好」分开了 —— MR6D 的「pipeline 表现不佳」，很大一部分是分割的问题", 0, "plain"),
], y=1.45, size=18, gap=9)

# 6 精读的三篇论文
s = prs.slides.add_slide(BLANK)
title_bar(s, "精读的三篇论文", "05")
table_slide(s, ["论文", "年份", "一句话", "我的批判 / 关注点"],
            [["BOP", "2018", "统一 8 数据集 / 任务 / 指标（VSD），横评 15 种方法，提供赛道与尺子", "数字全来自 2018 年前方法集合，引用需限定时效"],
             ["PoseCNN", "2018", "语义标注 + 中心投票估平移 + 四元数回归估旋转，SLoss 处理对称", "「端到端」打折（投票层不可导）；ADD-S 75.9 阈值口径不一致"],
             ["π₀.₅（领域外）", "2025", "VLM → VLA，两阶段训练 + 异构数据协同训练，陌生新家完成 10–15 分钟长时程任务", "能力与数据强绑定（400h 真实数据 + 互联网 + 语义指令）"]],
            col_w=[1.9, 1.1, 5.9, 3.0], y=1.4, h=3.5, size=13)
tf = textbox(s, 0.7, 5.3, 12.0, 1.2)
p = tf.paragraphs[0]
set_run(p.add_run(), 15, True, ACCENT); p.runs[0].text = "另：MR6D（2025，工业移动机器人 6D pose 评测基准）本次仅略读，未深入，暂不作为重点。"
p = tf.add_paragraph()
set_run(p.add_run(), 14, False, GRAY); p.runs[0].text = "三篇均包含自己的批判，非抄录作者结论。"

# 7 观察与思考
s = prs.slides.add_slide(BLANK)
title_bar(s, "观察与思考", "06")
bullets(s, [
    ("瓶颈已被标出，定量关系尚未建立", 0, "head"),
    ("MR6D 只指出「2D 分割是瓶颈」，没有「分割 IoU 降到 X → 位姿 AR 掉到 Y」的定量曲线", 1, "sub"),
    ("MR6D 的场景是「变窄」而非「变宽」", 0, "head"),
    ("实用场景接触的是高确定性物品 → 结论不能外推到开放世界（对具身智能方向是关键提醒）", 1, "sub"),
    ("「只用深度比 RGB 更鲁棒」是观察，不是机制", 0, "head"),
    ("BOP 记录了这一规律，但未给出解释", 1, "sub"),
    ("PoseCNN 的「中心投票」在严重自遮挡 + 远距离下可能失效", 0, "head"),
    ("其鲁棒性依赖「中心被遮挡时可见像素仍能投对中心」；可见像素过少时该假设不成立", 1, "sub"),
], y=1.4, size=17, gap=7)

# 8 待讨论
s = prs.slides.add_slide(BLANK)
title_bar(s, "待讨论的问题", "07")
bullets(s, [
    ("Q1  下一步：优先补阶段二方法论文（PVNet 等），还是先跑通 bop_toolkit 评测复现？", 0, "head"),
    ("阶段一 3/6，方法论文目前只读了 PoseCNN", 1, "sub"),
    ("Q2  复现起点选「bop_toolkit 评测流程 + LM-O」，而不是复现网络，是否正确？", 0, "head"),
    ("两篇都是 benchmark，复现评测口径比复现网络更适合入门", 1, "sub"),
    ("Q3  6D Pose 主线与 π₀.₅ 这类具身智能 VLA 主线，如何分配精力？", 0, "head"),
    ("Q4  入门期需要本机 GPU 吗？能否申请或使用组内资源？", 0, "head"),
], y=1.4, size=17, gap=8)

# 9 下一步
s = prs.slides.add_slide(BLANK)
title_bar(s, "下一步计划（下次 Meeting 前）", "08")
table_slide(s, ["优先级", "事项", "前置 / 说明"],
            [["★", "目标 A：bop_toolkit + LM-O 跑通评测，复现 ADD-S / VSD / AR", "无（纯 CPU）"],
             ["★", "阶段二 P0 精读：PVNet / CDPN / DPOD / Pix2Pose", "阶段一收口后"],
             ["", "补完阶段一：SSD-6D / DeepIM", "阶段一收口"],
             ["", "归并 9 条术语卡为统一词表", "散在 9.25 / 9.26"]],
            col_w=[1.3, 7.6, 3.0], y=1.6, h=3.6, size=15)
tf = textbox(s, 0.7, 5.6, 12.0, 0.8)
p = tf.paragraphs[0]
set_run(p.add_run(), 15, False, GRAY); p.runs[0].text = "节奏：≥ 2 周一次；中间有重要结果随时讨论。"

# 10 结束
s = prs.slides.add_slide(BLANK)
bar(s, 0, 0, 13.333, 7.5, DARK)
bar(s, 0, 4.55, 13.333, 0.09, ACCENT)
tf = textbox(s, 1.0, 2.1, 11.3, 2.2)
p = tf.paragraphs[0]
set_run(p.add_run(), 30, True, RGBColor(0xFF, 0xFF, 0xFF)); p.runs[0].text = "需要帮助"
for t in ["•  入门期路径：先跑通复现评测，还是更早精读方法论文",
          "•  本机 / 组内 GPU 资源（决定方法类复现能否跑通）",
          "•  6D Pose 主线与具身智能 VLA 主线的精力分配"]:
    pp = tf.add_paragraph()
    set_run(pp.add_run(), 18, False, RGBColor(0xC9, 0xD6, 0xE4)); pp.runs[0].text = t
tf2 = textbox(s, 1.0, 4.9, 11.3, 1.0)
p = tf2.paragraphs[0]
set_run(p.add_run(), 22, True, RGBColor(0x9F, 0xC5, 0xEA)); p.runs[0].text = "谢谢 · 欢迎讨论"

prs.save(OUT)
print("saved:", OUT)
print("slides:", len(prs.slides._sldIdLst))
