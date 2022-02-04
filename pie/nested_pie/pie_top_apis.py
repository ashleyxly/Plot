# https://matplotlib.org/stable/gallery/pie_and_polar_charts/nested_pie.html

import os
import json
import matplotlib
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.gridspec import GridSpec
from collections import defaultdict

hosts = ['wechat', 'baidu']
mode = 'source'

matplotlib.style.use('seaborn-white')

# use paired palette and hard-code inner and outer colors
# https://matplotlib.org/stable/tutorials/colors/colormaps.html
palette = sns.color_palette('Paired')
t1_colors = palette[1:11:2]
t2_colors = palette[0:10:2]

# create figure and axis
fig = plt.figure(figsize=(4, 9))
gs = GridSpec(nrows=2, ncols=1, hspace=0.3)

for axid, host in enumerate(hosts):
    api2cnts = defaultdict(lambda: defaultdict(int))

    work_dir = os.path.dirname(os.path.realpath(__file__))
    resource_dir = os.path.join(work_dir, 'resources')
    api_cat_dir = os.path.join(resource_dir, 'categorized_api')
    app2api_path = os.path.join(resource_dir, host, 'app2api.csv')
    api_cat_path = os.path.join(api_cat_dir, f'{host}-api2cat.json')

    # mapping from APIs to their categories
    with open(api_cat_path, 'r', encoding='utf-8') as fi:
        api2cat = json.load(fi)

    # file recording the APIs contained in each app
    with open(app2api_path, 'r', encoding='utf-8') as fi:
        app2apis = fi.readlines()[1:]

    # read csv by lines and count top APIs
    total = 0
    for line in app2apis:
        app, type, api, number = line.strip().split(',')
        if type[:-1] != mode:
            continue
        cat = api2cat[mode][api]
        api2cnts[cat][api] += int(number)
        total += int(number)

    max_per_cat = 3  # only choose top-3 APIs for each category
    cur = 0
    top_apis = {}
    for cat, api2cnt in api2cnts.items():
        top_api_list = []
        top_cnt_list = []
        other = 0
        cur = 0
        # only retain top APIs that accounts for more than 1% of the total
        # other APIs are grouped together as 'Others'
        for api, cnt in reversed(sorted(api2cnt.items(), key=lambda x: x[1])):
            if cur < max_per_cat and cnt > 0.01 * total:
                cur += 1
                top_api_list.append(api)
                top_cnt_list.append(cnt)
            else:
                other += cnt
        top_api_list.append('Others')
        top_cnt_list.append(other)
        top_apis[cat] = (top_api_list, top_cnt_list)

    # labels
    if mode == 'sink':
        sorted_cat_labels = ['Internet', 'Local Write', 'Open API', 'Device Contact']
    else:
        sorted_cat_labels = ['Device Information', 'User Input', 'Location', 'Local Read', 'Open API']

    # calculate sum for each category
    # will be used for drawing the inner pie (Categories and counts)
    sums = []
    valid_cat = []
    for cat in sorted_cat_labels:
        if cat in top_apis:
            valid_cat.append(cat)
            top_api, top_cnt = top_apis[cat]
            sums.append(sum(top_cnt))

    ax: plt.Axes = fig.add_subplot(gs[axid])

    # set colors for inner pie
    colors = []
    for i, k in enumerate(sorted_cat_labels):
        if k in valid_cat:
            colors.append(t1_colors[i])

    # plot inner pie
    # use wedgeprops width to draw donuts, instead of pies
    wedges, texts = ax.pie(
        sums, colors=colors,
        radius=0.5,
        wedgeprops=dict(width=0.3, edgecolor='w'),
    )

    # create legend
    # if axid == 0:
    #     ax.legend(
    #         wedges, valid_cat,
    #         ncol=3, loc='lower center',
    #         bbox_to_anchor=(0.5, 1.15),
    #         frameon=False,
    #         prop=dict(size=18, weight='bold')
    #     )

    # collect data for outer pies (APIs and counts)
    counts = []
    labels = []
    colors = []
    for i, cat in enumerate(sorted_cat_labels):
        if cat in top_apis:
            valid_cat.append(cat)
            top_api, top_cnt = top_apis[cat]
            for api, cnt in zip(top_api, top_cnt):
                counts.append(cnt)
                labels.append(api)
                if api == 'Others':
                    # set color of Others to white
                    # so that Others is 'invisible'
                    colors.append('w')
                else:
                    colors.append(t2_colors[i])

    # NOTE: the radius - width here must be equal to the radius of inner pie
    wedges, texts = ax.pie(
        counts, colors=colors,
        radius=1.,
        wedgeprops=dict(width=0.5, edgecolor='w')
    )

    # annotate outer pies
    kw = dict(
        arrowprops=dict(arrowstyle="-", lw=1, edgecolor='k'), va="center")

    for p, lbl, v in zip(wedges, labels, counts):
        if lbl == 'Others':
            continue
        ang = (p.theta2 - p.theta1) / 2 + p.theta1
        x = np.cos(np.deg2rad(ang))
        y = np.sin(np.deg2rad(ang))
        haidx = -1 if x < 0.1 else 1
        ha = {-1: "right", 1: "left"}[haidx]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        # hard-coded coordinate to avoid labels overlapping
        if lbl != 'wx.getStorage':
            xytext = (1.35*haidx, 1.5*y)
        else:
            xytext = (1.35*haidx, 1.5*(y-0.1))
        ax.annotate(
            f'{lbl}: {v:,}',
            xy=(x, y),
            horizontalalignment=ha,
            xytext=xytext,
            **kw,
            fontsize=18,
            fontweight='bold'
        )

    ax.set_title(['Wechat', 'Baidu'][axid], fontsize=20, fontweight='bold')

fig.savefig(os.path.join(work_dir, 'pie-source-top-apis.pdf'), bbox_inches='tight')
