import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams, gridspec
import matplotlib.pylab as pylab
import seaborn as sn
import matplotlib.ticker as mticker

#######################################################################################################################
# Adjust rcParams
print(rcParams.keys())

params = {
    'font.weight': 'bold',

    'legend.fontsize': 45,

    'xtick.labelsize': 35,
    'ytick.labelsize': 35,

    'axes.labelsize': 45,
    'axes.labelweight': 'bold',

    'lines.linewidth': 3.5,

    'figure.figsize': [20, 8],

    'grid.alpha': 0.3,
    'grid.linestyle': (5, 9),
}

pylab.rcParams.update(params)

######################################################################################################

sn.set_theme(style="whitegrid")
sn.set_context("paper", font_scale=3.8, rc={'line.linewidth': 3})  # Set font size
color_list = sn.color_palette('Set2')  # Generate color list from pre-set palette

######################################################################################################
# Plot AUC
x_auc = np.arange(6)
width = 0.3

s1_sc_auc = [0.813, 0.817, 0.705, 0.819, 0.821, 0.682]
s1_un_auc = [0.791, 0.724, 0.674, 0.806, 0.674, 0.671]
s2_sc_auc = [0.810, 0.825, 0.700, 0.819, 0.827, 0.691]
s2_un_auc = [0.722, 0.681, 0.586, 0.799, 0.709, 0.689]
s3_sc_auc = [0.751, 0.826, 0.704, 0.819, 0.697, 0.685]
s3_un_auc = [0.656, 0.814, 0.640, 0.820, 0.500, 0.649]

fig = plt.figure()
gs = gridspec.GridSpec(1, 2, width_ratios=[2.8, 1])  # Declare layout of 1 row and 2 columns; Determine width ratio
ax = fig.add_subplot(gs[0, 0])  # Draw at position (0, 0)

# Scatter plot
ax.scatter(x_auc - width, s1_sc_auc, marker='o', label='Sequence 1 (Schedule)', color=color_list[0], s=400)
ax.scatter(x_auc - width, s1_un_auc, marker='D', label='Sequence 1 (All)', color=color_list[0], s=400)
ax.scatter(x_auc, s2_sc_auc, marker='o', label='Sequence 2 (Schedule)', color=color_list[1], s=400)
ax.scatter(x_auc, s2_un_auc, marker='D', label='Sequence 2 (All)', color=color_list[1], s=400)
ax.scatter(x_auc + width, s3_sc_auc, marker='o', label='Sequence 3 (Schedule)', color=color_list[2], s=400)
ax.scatter(x_auc + width, s3_un_auc, marker='D', label='Sequence 3 (All)', color=color_list[2], s=400)

# Plot vertical lines
x_sep_auc = [0.5, 1.5, 2.5, 3.5, 4.5]
ax.set(ylim=[0.45, 0.85])
ax.vlines(x_sep_auc, 0.45, 0.85, colors='black', linestyles='dashed')

# Set xticks
ax.xaxis.set_major_locator(mticker.FixedLocator(x_auc.tolist()))
ax.xaxis.set_major_formatter(mticker.FixedFormatter(['Q1', 'Q2', 'Q4', "Q5", 'Q6', 'Q8']))

# Set width of axes
ax.spines['bottom'].set_linewidth(3.5)  # Set width of the bottom axis
ax.spines['left'].set_linewidth(3.5)  # Set width of left axis
ax.spines['right'].set_linewidth(3.5)  # Set width of the right axis
ax.spines['top'].set_linewidth(3.5)  # Set width of the top axis

ax.set_xlabel('Query')
ax.set_ylabel('AUC')

# Plot epsilon_ax (use the right axis of graph (0,0))
epsilon1 = [3.0, 1.8, 0.6]
epsilon2 = [5.0, 7.0, 10.0]
epsilon3 = [3.0, 2.1, 3.3]
epsilon4 = [5.0, 0.5, 3.0]
epsilon5 = [3.0, 3.3, 4.2]
epsilon6 = [2.5, 4.0, 0.5]
epsilon7 = [3.0, 1.8, 3.6]
epsilon8 = [4.0, 5.6, 2.4]

epsilons_ax = [epsilon1, epsilon2, epsilon4, epsilon5, epsilon6, epsilon8]
epsilons_ax1 = [epsilon3, epsilon7]

ax_eps = ax.twinx()  # Share the x-axis with 'ax'
# Plot lines
for i in range(len(epsilons_ax)):
    eps = epsilons_ax[i]
    x = [i - width, i, i + width]
    ax_eps.plot(x, eps, '-', label='', linewidth=4, color=color_list[3], markersize=14)

# Add scatter points
eps_dot1 = []
eps_dot2 = []
eps_dot3 = []
for j in range(len(epsilons_ax)):
    eps_dot1.append(epsilons_ax[j][0])
    eps_dot2.append(epsilons_ax[j][1])
    eps_dot3.append(epsilons_ax[j][2])
ax_eps.scatter(x_auc - width, eps_dot1, marker='^', label='$\epsilon$ (Sequence 1)', color=color_list[3], s=400)
ax_eps.scatter(x_auc, eps_dot2, marker='p', label='$\epsilon$ (Sequence 2)', color=color_list[3], s=400)
ax_eps.scatter(x_auc + width, eps_dot3, marker='v', label='$\epsilon$ (Sequence 3)', color=color_list[3], s=400)

ax_eps.set(ylim=[0, 12])
ax_eps.set_ylabel('$\epsilon$')

######################################################################################################
# Plot CK Score
x_ck = np.arange(2)
width_ck = 0.2

s1_sc_ck = [0.388, 0.401]
s1_un_ck = [0.346, 0.379]
s2_sc_ck = [0.392, 0.400]
s2_un_ck = [0.286, 0.385]
s3_sc_ck = [0.395, 0.415]
s3_un_ck = [0.342, 0.386]

ax1 = fig.add_subplot(gs[0, 1])  # Draw at position (0, 1)
ax1.scatter(x_ck - width_ck, s1_sc_ck, marker='o', label='', color=color_list[0], s=400)
ax1.scatter(x_ck - width_ck, s1_un_ck, marker='D', label='', color=color_list[0], s=400)
ax1.scatter(x_ck, s2_sc_ck, marker='o', label='', color=color_list[1], s=400)
ax1.scatter(x_ck, s2_un_ck, marker='D', label='', color=color_list[1], s=400)
ax1.scatter(x_ck + width_ck, s3_sc_ck, marker='o', label='', color=color_list[2], s=400)
ax1.scatter(x_ck + width_ck, s3_un_ck, marker='D', label='', color=color_list[2], s=400)

x_sep_ck = [0.5]
ax1.set(ylim=[0.2, 0.5], xlim=[-0.5, 1.5])
ax1.vlines(x_sep_ck, 0.2, 0.5, colors='black', linestyles='dashed')

ax1.set_ylabel('CK Score')
ax1.set_xlabel('Query')

ax1.xaxis.set_major_locator(mticker.FixedLocator(x_ck.tolist()))
ax1.xaxis.set_major_formatter(mticker.FixedFormatter(['Q3', 'Q7']))

ax1.spines['bottom'].set_linewidth(3.5)
ax1.spines['left'].set_linewidth(3.5)
ax1.spines['right'].set_linewidth(3.5)
ax1.spines['top'].set_linewidth(3.5)

# ax1_eps
ax1_eps = ax1.twinx()
for i in range(len(epsilons_ax1)):
    eps = epsilons_ax1[i]
    x = [i - width, i, i + width]
    ax1_eps.plot(x, eps, '-', label='', linewidth=4, color=color_list[3], markersize=14)

ax1_eps.scatter(x_ck - width, [epsilon3[0], epsilon7[0]], marker='^', label='', color=color_list[3], s=400)
ax1_eps.scatter(x_ck, [epsilon3[1], epsilon7[1]], marker='p', label='', color=color_list[3], s=400)
ax1_eps.scatter(x_ck + width, [epsilon3[2], epsilon7[2]], marker='v', label='', color=color_list[3], s=400)

ax1_eps.set(ylim=[1, 4])
ax1_eps.set_ylabel('$\epsilon$')

######################################################################################################

# Rearrange the order of handles and labels
handles_ax, labels_ax = ax.get_legend_handles_labels()
handles_eps, labels_eps = ax_eps.get_legend_handles_labels()
handles = [handles_ax[0], handles_ax[2], handles_ax[4], handles_ax[1], handles_ax[3], handles_ax[5], handles_eps[0],
           handles_eps[1], handles_eps[2]]
labels = [labels_ax[0], labels_ax[2], labels_ax[4], labels_ax[1], labels_ax[3], labels_ax[5], labels_eps[0],
          labels_eps[1], labels_eps[2]]

fig.legend(handles=handles, labels=labels, loc='lower center', fancybox=True, framealpha=0, ncol=3, columnspacing=0.1,
           handletextpad=0, bbox_to_anchor=(0.5, -0.055))  # Set legend

plt.subplots_adjust(left=0.07, right=0.958, top=0.96, bottom=0.375, wspace=0.39)  # set margin

plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

plt.savefig('./macro_benchmark.pdf')
# plt.savefig('./macro_benchmark.png')
# plt.savefig('./macro_benchmark.eps')
plt.show()
