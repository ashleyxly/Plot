import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import rcParams, gridspec
import matplotlib.pylab as pylab
import seaborn as sn
import matplotlib.ticker as mticker

print(rcParams.keys())

params = {
    'font.weight': 'bold',

    'legend.fontsize': 45,

    'xtick.labelsize': 35,
    'ytick.labelsize': 35,

    'axes.labelsize': 45,
    'axes.labelweight': 'bold',

    'lines.linewidth': 3.5,

    'figure.figsize': [16, 16],

    'grid.alpha': 0.3,
    'grid.linestyle': (5, 9),
}

pylab.rcParams.update(params)

sn.set_theme(style="whitegrid")
sn.set_palette('flare')
sn.set_context("paper", font_scale=4, rc={'line.linewidth': 3})

df = pd.read_csv("data_lambda_avg.csv", encoding='UTF-8')
x = np.arange(df['x'].shape[0])
width = 0.2

# stacked graph
gs = gridspec.GridSpec(2, 1, height_ratios=[1.5, 1])
ax = plt.subplot(gs[0])

plt.subplots_adjust(left=0.11, right=0.99, top=0.96, bottom=0.085)  # set margin

# Generate color series for different bars
num_stack = 7  # Number of stacks in a bar

# Adjusted color palette
color_list1 = sn.color_palette('flare_d', num_stack).as_hex()
color_list2 = sn.color_palette('Greens_d', num_stack).as_hex()
color_list3 = sn.color_palette('copper_r', num_stack).as_hex()
color_list4 = sn.color_palette('winter_r', num_stack+1).as_hex()
temp_list = []
for i in range(num_stack):
    temp_list.append(color_list4[i+1])
color_list4 = temp_list


def bar_plot(axes, data_x, width_bar, num_sec, sec_name, color_list, hatch, label):
    bottom = 0
    for i in range(num_sec):
        if i > 0:
            bottom += df[sec_name[i-1]]
        if i == int(num_sec / 2):
            axes.bar(x=data_x, height=df[sec_name[i]], width=width_bar, bottom=bottom, label=label,
                     color=color_list[i], hatch=hatch)  # Show the middle color on the legend
        else:
            axes.bar(x=data_x, height=df[sec_name[i]], width=width_bar, bottom=bottom,
                     color=color_list[i], hatch=hatch)


bar_plot(ax, x - width * 3 / 2, width, num_stack,
         ['sage_e1', 'sage_e2', 'sage_e3', 'sage_e4', 'sage_e5', 'sage_e6', 'sage_e7'],
         color_list1, 'o', 'Sage')
bar_plot(ax, x - width / 2, width, num_stack,
         ['sig_e1', 'sig_e2', 'sig_e3', 'sig_e4', 'sig_e5', 'sig_e6', 'sig_e7'],
         color_list2, '.', 'Sig')
bar_plot(ax, x + width / 2, width, num_stack,
         ['hard_e1', 'hard_e2', 'hard_e3', 'hard_e4', 'hard_e5', 'hard_e6', 'hard_e7'],
         color_list3, '+', 'DPlanner-Hard')
bar_plot(ax, x + width * 3 / 2, width, num_stack,
         ['soft_e1', 'soft_e2', 'soft_e3', 'soft_e4', 'soft_e5', 'soft_e6', 'soft_e7'],
         color_list4, 'x', 'DPlanner-Soft')

# Set width of axes
ax.spines['bottom'].set_linewidth(3.5)  # Set width of the bottom axis
ax.spines['left'].set_linewidth(3.5)  # Set width of left axis
ax.spines['right'].set_linewidth(3.5)  # Set width of the right axis
ax.spines['top'].set_linewidth(3.5)  # Set width of the top axis

ax.set_xlabel('$\lambda$')
ax.set_ylabel('Consumed Privacy Budget ($\epsilon$)')

# Set xticks
t = np.array(df['x'])
ax.xaxis.set_major_locator(mticker.FixedLocator(x.tolist()))
ax.xaxis.set_major_formatter(mticker.FixedFormatter(t))

ax.set(ylim=[0, 25])
ax.legend(loc='upper center', fancybox=True, framealpha=0, ncol=4, columnspacing=0.4, handletextpad=0.4)
ax.set_title('(b) Queries of Different $\lambda$s (Adult)', fontdict={'weight': 'bold'})

# line graph
sn.set_palette('Set2')

x1 = [x[0] - width * 3 / 2, x[0] - width / 2, x[0] + width / 2, x[0] + width * 3 / 2]
x2 = [x[1] - width * 3 / 2, x[1] - width / 2, x[1] + width / 2, x[1] + width * 3 / 2]
x3 = [x[2] - width * 3 / 2, x[2] - width / 2, x[2] + width / 2, x[2] + width * 3 / 2]
x4 = [x[3] - width * 3 / 2, x[3] - width / 2, x[3] + width / 2, x[3] + width * 3 / 2]
x5 = [x[4] - width * 3 / 2, x[4] - width / 2, x[4] + width / 2, x[4] + width * 3 / 2]

y1 = [0.8202402532100678, 0.8290412724018097, 0.8274955451488495, 0.8140723586082459]
y2 = [0.8347672462463379, 0.8373280763626099, 0.8244379520416260, 0.8136060237884521]
y3 = [0.8379169046878815, 0.8220096588134765, 0.8282159864902496, 0.8136977255344391]
y4 = [0.8357203185558320, 0.8259735047817230, 0.8284175276756287, 0.8139891326427460]
y5 = [0.8222711980342865, 0.8367657124996185, 0.8301980853080749, 0.8129885017871856]

ax1 = plt.subplot(gs[1])   # Draw at the second graph

ax1.plot(x1, y1, '-', linewidth=4.5, color=sn.color_palette('Set2')[0])
ax1.plot(x2, y2, '-', linewidth=4.5, color=sn.color_palette('Set2')[0])
ax1.plot(x3, y3, '-', linewidth=4.5, color=sn.color_palette('Set2')[0])
ax1.plot(x4, y4, '-', linewidth=4.5, color=sn.color_palette('Set2')[0])
ax1.plot(x5, y5, '-', linewidth=4.5, color=sn.color_palette('Set2')[0])

ax1.scatter(x-width*3/2, [y1[0], y2[0], y3[0], y4[0], y5[0]], marker='o', label='Sage', s=400,
            color=sn.color_palette('Set2')[0])
ax1.scatter(x-width/2, [y1[1], y2[1], y3[1], y4[1], y5[1]], marker='D', label='Sig', s=400,
            color=sn.color_palette('Set2')[0])
ax1.scatter(x+width/2, [y1[2], y2[2], y3[2], y4[2], y5[2]], marker='s', label='DPlanner-Hard', s=400,
            color=sn.color_palette('Set2')[0])
ax1.scatter(x+width*3/2, [y1[3], y2[3], y3[3], y4[3], y5[3]], marker='^', label='DPlanner-Soft', s=400,
            color=sn.color_palette('Set2')[0])

ax1.xaxis.set_major_locator(mticker.FixedLocator(x.tolist()))
ax1.xaxis.set_major_formatter(mticker.FixedFormatter(t))

ax1.spines['bottom'].set_linewidth(3.5)
ax1.spines['left'].set_linewidth(3.5)
ax1.spines['right'].set_linewidth(3.5)
ax1.spines['top'].set_linewidth(3.5)

ax1.set_ylabel('AUC')
ax1.set_xlabel('$\lambda$')
ax1.set(ylim=[0.8, 0.86])

ax1.legend(loc='upper center', fancybox=True, framealpha=0, ncol=4, handletextpad=0.2, columnspacing=0.5)

plt.savefig('./lambda_avg.pdf')
plt.show()
