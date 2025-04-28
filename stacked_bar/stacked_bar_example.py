import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# -------------------------------
# 1. 数据
# -------------------------------

# human 数据

human_stack = np.array([759, 819, 550, 656, 274, 328, 319, 298, 173, 108, 130, 28]) # 各个类别的ground truth数量
labels = ["FAM", "OCC", "LOC", "MAR", "SEX", "INC", "AGE", "APP", "EDU", "HEA", "POB", "NAM"]
human_total = human_stack.sum()

# Baseline 结果
baseline_methods = {
    'Llama-3-70B': {
        'TP': np.array([136, 125, 97, 79, 58, 39, 24, 48, 21, 12, 17, 14]),
        'FP': 4328
    },
    'gpt-4': {
        'TP': np.array([159, 226, 108, 134, 78, 104, 83, 54, 26, 14, 15, 6]),
        'FP': 3710 
    },
    'deepseek-r1': {
        'TP': np.array([176, 213, 125, 120, 114, 66, 93, 64, 35, 12, 17, 14]),
        'FP': 4014
    }
}

# PrivSniffer 结果
privsniffer_methods = {
    'Llama-3-70B': {
        'TP': np.array([206, 280, 136, 173, 134, 62, 97, 157, 43, 10, 24, 6]),
        'FP': 3843
    },
    'gpt-4': {
        'TP': np.array([429, 496, 161, 280, 172, 79, 116, 129, 44, 15, 37, 19]),
        'FP': 3054
    },
    'deepseek-r1': {
        'TP': np.array([450, 512, 170, 296, 198, 115, 145, 170, 62, 29, 47, 15]),
        'FP': 2997
    }
}

# -------------------------------
# 2. 设置绘图参数
# -------------------------------
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.8 # 柱子宽度
negative_scale = 0.3 # 对y的负轴（FP）进行缩放，避免FP过大导致柱子过长
matplotlib.rcParams['hatch.linewidth'] = 3.0 # 设置纹理hatch线宽
plt.rcParams.update({'font.size': 16})  # 设置字体大小

# 生成12个颜色用于stack（采用Set3色板）
cmap = matplotlib.colormaps['Set3']
colors = [cmap(i) for i in range(12)]


# 横轴位置安排：
x_pos = []
x_labels = []
method_order = []  # 存储绘图字典，方便循环绘图

# 添加Baseline
for i, (name, data) in enumerate(baseline_methods.items()):
    pos = i
    x_pos.append(pos)
    x_labels.append(name)
    method_order.append(('method', name, data))  # 类型标记为method

# 添加分组分隔（在Baseline和PrivSniffer之间插入间隔）
sep1 = max(x_pos) + 1.5

# 添加PrivSniffer 
base_count = len(baseline_methods)
for i, (name, data) in enumerate(privsniffer_methods.items()):
    pos = sep1 + i
    x_pos.append(pos)
    x_labels.append(name)
    method_order.append(('method', name, data))

# 分隔线后再放human
sep2 = max(x_pos) + 1.5
x_human = sep2
x_pos.append(x_human)
x_labels.append('Human')
method_order.append(('Human', 'Human', {'TP': human_stack}))

# -------------------------------
# 3. 绘制堆叠柱图
# -------------------------------
for (mtype, name, data), xpos in zip(method_order, x_pos):
    if mtype == 'Human':
        # 绘制human的12堆TP柱子
        bottom = 0
        for i in range(12):
            p = ax.bar(xpos, data['TP'][i], bar_width, bottom=bottom, color=colors[i], edgecolor='white', linewidth=0.5)
            bottom += data['TP'][i]
    else:
        # 对方法（Baseline或PrivSniffer）：
        # 1. 绘制TP的12堆
        tp = data['TP']
        bottom = 0
        for i in range(12):
            p = ax.bar(xpos, tp[i], bar_width, bottom=bottom, color=colors[i], edgecolor='white', linewidth=0.5)
            bottom += tp[i]
        # 2. 绘制FN：FN = human_total - sum(method_TP)
        FN = human_total - tp.sum()
        # 使用灰色表示FN
        p_fn = ax.bar(xpos, FN, bar_width, bottom=bottom, color='lightgray', edgecolor='white', linewidth=0.5, hatch='\\', alpha=0.6)

        # 3. 绘制FP为负值（从0向下绘制）
        FP = data['FP'] * negative_scale
        p_fp = ax.bar(xpos, -FP, bar_width, color='red', edgecolor='white', linewidth=0.5, hatch='/', alpha=0.6)


# -------------------------------
# 4. 绘制分隔线和设置坐标轴
# -------------------------------
# 在Baseline和PrivSniffer之间画一条垂直分隔线
ax.axvline(x=sep1 - bar_width, color='black', linestyle='--', linewidth=1)
# 在PrivSniffer和human之间画一条垂直分隔线
ax.axvline(x=sep2 - bar_width, color='black', linestyle='--', linewidth=1)

# 设置x轴刻度及标签
ax.set_xticks(x_pos, x_labels, rotation=25)
ax.tick_params(axis='x', length=0)

# 设置y轴范围：正轴最高与human_total相同（可略大以留空隙），负轴最低与所有方法中的最大FP一致
max_FP = max([data['FP'] for data in list(baseline_methods.values()) + list(privsniffer_methods.values())])
ax.set_ylim(-max_FP * negative_scale, human_total * 1.1)

# 设置y轴刻度：
y_ticks = np.array([0, 1000, 3000, 5000, -1000, -3000, -5000], dtype=np.float64)

# 负数按照scale 缩放
y_ticks[y_ticks < 0] *= negative_scale

y_ticks_labels = []
for tick in y_ticks:
    if tick >= 0:
        y_ticks_labels.append(f'{int(tick)}')
    else:
        y_ticks_labels.append(f'{int(-tick / negative_scale)}')

ax.set_yticks(y_ticks, y_ticks_labels)


for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

ax.axhline(0, color='black', linewidth=1) 


# 添加标签和标题 调整y值来控制位置
ax.text(-1.5, 1000, '# Correct (TP)', rotation=90, va='center', ha='center', color='black')
ax.text(-1.5, -2500 * negative_scale, '# FP', rotation=90, va='center', ha='center', color='red')
ax.text(-1.5, 3500, '# FN', rotation=90, va='center', ha='center', color='gray')

# 增加group label

ax.text(sep1 / 2 - bar_width, -8500 * negative_scale, "Prompt Instruct (+ web)", rotation=0, va='center', ha='center', color='black')
ax.text((sep1 + sep2) / 2 - bar_width, -8500 * negative_scale, "PrivSniffer", rotation=0, va='center', ha='center', color='black')

ax.set_title('TP,FP,FN of Detecting Clues')


# 图例
from matplotlib.patches import Patch
legend_handles = []

legend_handles.append(Patch(facecolor='lightgray', label='FN', edgecolor='white', linewidth=0.5, hatch='\\', alpha=0.6))
legend_handles.append(Patch(facecolor='red', label='FP', edgecolor='white', linewidth=0.5, hatch='/', alpha=0.6))
legend_handles.extend([Patch(facecolor=colors[j], label=labels[j]) for j in range(len(human_stack))])
ax.legend(handles=legend_handles, loc='upper right', bbox_to_anchor=(1.2, 1))



plt.tight_layout()
plt.savefig("stack_bar_clue.pdf", bbox_inches='tight', pad_inches=0)
