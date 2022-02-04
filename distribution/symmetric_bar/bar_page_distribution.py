import os
import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import defaultdict

from typing import List

page_keys = [
    '[0, 10)',
    '[10, 20)',
    '[20, 25)',
    '[25, 50)',
    '[50, 75)',
    '[75, 100)',
    '100+'
]


def get_page_group(n_pages: int):
    if n_pages < 10:
        return page_keys[0]
    if 10 <= n_pages and n_pages < 20:
        return page_keys[1]
    if 20 <= n_pages and n_pages < 25:
        return page_keys[2]
    if 25 <= n_pages and n_pages < 50:
        return page_keys[3]
    if 50 <= n_pages and n_pages < 75:
        return page_keys[4]
    if 75 <= n_pages and n_pages < 100:
        return page_keys[5]
    return page_keys[6]


work_dir = os.path.dirname(os.path.realpath(__file__))
resource_dir = os.path.join(work_dir, 'resources')
baidu_dir = os.path.join(resource_dir, 'baidu')
wechat_dir = os.path.join(resource_dir, 'wechat')

sns.set_theme(context='paper', style='white')
matplotlib.style.use('seaborn-white')

baidu_stats = pd.read_csv(os.path.join(baidu_dir, 'baidu.csv'))
wechat_stats = pd.read_csv(os.path.join(wechat_dir, 'wechat.csv'))

# group each mini app
baidu_name2group = {}
wechat_name2group = {}
for idx, row in baidu_stats.iterrows():
    # print(row['Name'], row['Pages'])
    grp = get_page_group(int(row['Pages']))
    baidu_name2group[row['Name']] = grp
for idx, row in wechat_stats.iterrows():
    # print(row['Name'], row['Pages'])
    grp = get_page_group(int(row['Pages']))
    wechat_name2group[row['Name']] = grp

# this part should be redundant but I dont want to remove it.
wechat_leaks = pd.read_csv(os.path.join(wechat_dir, 'app_2_leaks.csv'))
baidu_leaks = pd.read_csv(os.path.join(baidu_dir, 'app_2_leaks.csv'))
wechat_groups = defaultdict(list)
baidu_groups = defaultdict(list)
for idx, row in wechat_leaks.iterrows():
    name_version: str = row['App']
    name = name_version[:name_version.rindex('_')]

    if name not in wechat_name2group:
        continue

    grp = wechat_name2group[name]
    wechat_groups[grp].append(int(row['TotalLeaks']))

for idx, row in baidu_leaks.iterrows():
    name_version: str = row['App']
    name = name_version

    if name not in baidu_name2group:
        continue

    grp = baidu_name2group[name]
    baidu_groups[grp].append(int(row['TotalLeaks']))

baidu_group_size = np.array([
    len(baidu_groups[k]) for i, k in enumerate(page_keys)
])
wechat_group_size = np.array([
    len(wechat_groups[k]) for i, k in enumerate(page_keys)
])

# get normalized group size (proportion of each group)
nm_wechat_group_size = wechat_group_size / wechat_group_size.sum()
nm_baidu_group_size = baidu_group_size / baidu_group_size.sum()

# create figure
ax: List[plt.Axes]
fig, ax = plt.subplots(1, 2, figsize=(6, 3.5), sharey=True)

# make ytick labels on the left axis
ax[0].yaxis.tick_left()

# create barh for each host
bar1 = ax[0].barh(
    page_keys, nm_wechat_group_size, facecolor='C2', label='Wechat',
    edgecolor='darkgray', linewidth=2)
bar2 = ax[1].barh(
    page_keys, nm_baidu_group_size, facecolor='C0', label='Baidu',
    edgecolor='darkgray', linewidth=2)

# set bounds, labels and legends
ax[0].spines['right'].set_color('grey')
ax[1].spines['left'].set_color('grey')

ax[0].set_ylabel('# Pages', fontsize=14, fontweight='bold')
ax[0].set_xlabel('% MiniApps', fontsize=14, fontweight='bold')
ax[1].set_xlabel('% MiniApps', fontsize=14, fontweight='bold')
ax[0].set_yticklabels(page_keys, fontsize=14, fontweight='bold')

ax[0].legend(
    loc='lower left', bbox_to_anchor=(0, 1),
    prop=dict(size=14, weight='bold'))
ax[1].legend(
    loc='lower right', bbox_to_anchor=(1, 1),
    prop=dict(size=14, weight='bold'))

ax[0].set_xbound([0, 0.75])
ax[1].set_xbound([0, 0.75])

# flip ax0 to make the axes symmetric
ax[0].invert_xaxis()
fig.tight_layout()

# remove white spaces between axes
plt.subplots_adjust(wspace=0)

# annotate
for a in ax:
    a.set_xticks(
        np.arange(0., 0.8, 0.2),
        labels=[f'{x:.1f}' for x in np.arange(0., 0.8, 0.2)],
        fontsize=12, fontweight='bold')
for p, v in zip(bar1.patches, wechat_group_size):
    ax[0].text(
        p.get_x() + p.get_width() + 0.01,
        p.get_y() + p.get_height() / 2,
        f'{v:,}',
        ha="right", va="center",
        fontdict=dict(fontsize=14, weight='bold')
    )
for p, v in zip(bar2.patches, baidu_group_size):
    if p.get_width() < 0.5:
        ax[1].text(
            p.get_x() + p.get_width() + 0.01,
            p.get_y() + p.get_height() / 2,
            f'{v:,}', ha="left", va="center",
            fontdict=dict(fontsize=14, weight='bold')
        )
    else:
        ax[1].text(
            p.get_x() + p.get_width() - 0.01,
            p.get_y() + p.get_height() / 2,
            f'{v:,}',
            ha="right", va="center",
            fontdict=dict(fontsize=14, color='w', weight='bold')
        )

fig.savefig(os.path.join(work_dir, 'bar-page-distribution.pdf'), bbox_inches='tight')
