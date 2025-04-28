import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import matplotlib

# 设置纹理线宽
matplotlib.rcParams["hatch.linewidth"] = 3.0
plt.rcParams.update({"font.size": 14})


# 数据
methods = ["Prompt Instruct", "Prompt Instruct (web)", "PrivSniffer"]

no_anonymity = [0.61, 0.63, 0.70]
with_anonymity_baseline = [0.24, 0.26, 0.43]
with_anonymity = [0.19, 0.22, 0.12]
mask_percent = [23.7, 16.1]

x = np.arange(len(methods))  # x轴位置
x_cost = len(methods)
width = np.float64(0.3)  # 柱子宽度

# 颜色风格
base_colors = [
    "#0E606B",
    "#1597A5",
    "#FEB3AE",
]  

# 创建图形
fig, ax = plt.subplots(figsize=(10, 5))

# 绘制“无匿名”时柱子
bars_no = ax.bar(x - width, no_anonymity, width, label="No", color=base_colors[0])

# anonymity baseline
for i in range(len(methods)):
    ax.bar(
        x[i],
        with_anonymity_baseline[i],
        width,
        color=base_colors[1],
        alpha=1.0,
        hatch="///",
        edgecolor="white",
        linewidth=1,
    )

# anonymity privsniffer
for i in range(len(methods)):
    ax.bar(
        x[i] + width,
        with_anonymity[i],
        width,
        color=base_colors[2],
        alpha=1.0,
        hatch="\\\\",
        edgecolor="white",
        linewidth=1,
    )


# 设置标签和标题
ax.set_ylabel("PII Accuracy (TPR)")
# ax.set_title("不同检测方法下匿名影响对比")
xticks = x.tolist() + [x_cost]
xticklabels = methods + ["Mask Cost"]
ax.set_xticks(xticks)
ax.set_xticklabels(xticklabels)
ax.set_xlabel("PII Detection Method")   
ax.set_ylim(0, 0.75)


# 绘制右侧y轴
# mask_percent
ax2 = ax.twinx()
ax2.bar(x_cost - width / 2, mask_percent[0], width, color=base_colors[1], alpha=1.0, hatch="///", edgecolor="white", linewidth=1)
ax2.bar(x_cost + width / 2, mask_percent[1], width, color=base_colors[2], alpha=1.0, hatch="\\\\", edgecolor="white", linewidth=1)
ax2.set_ylim(0, 40)
ax2.set_ylabel("Mask Text Percentage (%)")

ax2.vlines(x = 2.575, ymin=0, ymax=40, color='black', linestyle='-', alpha=0.7, linewidth=0.5, zorder=8)


# 单独绘制图例
legend_handles = [
    Patch(
        facecolor=base_colors[0],
        label="No Anonymization",
        edgecolor="white",
        linewidth=1,
    ),
    Patch(
        facecolor=base_colors[1],
        label="Masked by Prompt Instruct (web)",
        edgecolor="white",
        linewidth=1,
        hatch="///",
        alpha=1,
    ),
    Patch(
        facecolor=base_colors[2],
        label="Masked by PrivSniffer",
        edgecolor="white",
        linewidth=1,
        hatch="\\\\",
        alpha=1,
    ),
]

ax.legend(ncols=3, handles=legend_handles, title="Sanitization method", loc="upper center", bbox_to_anchor=(0.5, 1.25), frameon=True, handletextpad=0.2, labelspacing=0.2).set_zorder(5)


# 美化布局
plt.tight_layout()
plt.savefig("application.pdf", bbox_inches="tight", pad_inches=0)
