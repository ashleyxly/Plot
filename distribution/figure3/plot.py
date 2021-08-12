from matplotlib import pyplot as plt
import matplotlib.patches as patches
import seaborn as sn
import json
import pandas as pd

with open('./data1.json', 'r') as f:
    index = json.load(f)

with open('./data2.json', 'r') as f:
    index_b = json.load(f)

d = {'': ['Perturbed Subgraph After Attacking' for i in index]+['Perturbed Subgraph Before Attacking' for i in index_b], 'Order': index+index_b}
df = pd.DataFrame(data=d)

sn.set_style('ticks')
sn.set_context("paper", font_scale=2.2, rc={'line.linewidth':3})
sn.color_palette("husl")
fig=plt.figure(figsize=(10,8))
plt.xlabel('Order', fontsize=30)
plt.ylabel('Density Distribution', fontsize=30)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
sn.histplot(df, x='Order', bins=25, kde=True, stat="density", hue='', common_norm=False)

ax=plt.gca()
rect=patches.Rectangle((2150, 0),360,0.0032,linewidth=2, edgecolor='r',facecolor='none', linestyle='--')
ax.add_patch(rect)
plt.show()
plt.savefig('./distribution.pdf', bbox_inches='tight')