import os

import matplotlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.gridspec import GridSpec


work_dir = os.path.dirname(os.path.realpath(__file__))

sns.set_theme(context='paper', style='whitegrid')
matplotlib.style.use('seaborn-white')

# hard-coded data here
success_rate = {
    'wechat': {
        'Success': 104258,
        'Failure': 28855,
        'Timeout': 12094,
        'AppNotFound': 4405,
        'SyntaxError': 8401,
        'TypeError': 3369,
        'Other': 586
    },
    'baidu': {
        'Success': 21319,
        'Failure': 490,
        'Timeout': 444,
        'AppNotFound': 7,
        'SyntaxError': 18,
        'TypeError': 12,
        'Other': 9
    }
}

# hard-coded labels here
tier1 = ['Success', 'Failure']
tier2 = ['Timeout', 'AppNotFound', 'SyntaxError', 'TypeError', 'Other']
mixed = ['Success', 'Timeout', 'AppNotFound',
         'SyntaxError', 'TypeError', 'Other']

# explode parameter for pie chart
explode = [0., 0.1]

# select colors
palette = sns.color_palette(n_colors=8)[2:]

# create 2x2 figure with gridspec
# upper two for pies and lower two for horizontal bars
fig = plt.figure(figsize=(8, 6), constrained_layout=True)
gs = GridSpec(
    nrows=2, ncols=2,
    height_ratios=[9, 1], hspace=0.05, wspace=1,
    left=0.05, right=0.98,
    top=0.9, bottom=0.2, figure=fig)

axid = 0
for idx, host in enumerate(['wechat', 'baidu']):
    axid = idx
    ax: plt.Axes = fig.add_subplot(gs[axid])
    axid += 2

    # draw pies
    wedges, texts = ax.pie(
        [success_rate[host][k] for k in tier1],
        radius=1,
        explode=explode
    )

    # annotate pie charts
    # see <https://matplotlib.org/stable/gallery/pie_and_polar_charts/pie_and_donut_labels.html>
    kw = dict(arrowprops=dict(arrowstyle="-"), zorder=0, va="center")
    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1) / 2 + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        ha = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        key = tier1[i]
        ax.annotate(
            f'{key}: {success_rate[host][key]:,}',
            xy=(x, y),
            xytext=(1.1*np.sign(x), 1.4*y),
            horizontalalignment=ha,
            fontsize=18,
            fontweight='bold',
            **kw
        )

    title_host = ['Wechat', 'Baidu']
    ax.set_title(f'{title_host[idx]}', fontsize=20, fontweight='bold')

    # draw bars
    ax = fig.add_subplot(gs[axid])
    ax.axis('off')
    ax.set_title('Failure Details', fontsize=18, fontweight='bold')

    # collect failure details
    vals = []
    for k in tier2:
        vals.append(success_rate[host][k])

    # normalize values
    norm_factor = sum(vals)
    for i in range(len(vals)):
        vals[i] = vals[i] / norm_factor

    # draw barh one-by-one so that they can be labeld with legend()
    bottom = 0
    for i, v in reversed(sorted(enumerate(vals), key=lambda x: x[1])):
        ax.barh(
            0,  # all bars lie on the same ytick
            v,  # end value
            left=bottom,  # cummulative start value
            label=f'{tier2[i]}: {success_rate[host][tier2[i]]:,}',
            color=palette[i])
        bottom += v

    # legend
    ax.legend(
        ncol=1,
        loc='upper center', bbox_to_anchor=(0.5, -0.1),
        prop=dict(weight='bold', size=18))

# fig.tight_layout()
fig.savefig(
    os.path.join(work_dir, 'pie-success-rate.pdf'),
    bbox_inches='tight')
