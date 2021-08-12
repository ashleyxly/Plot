import json
import pandas as pd
import seaborn as sn
from matplotlib import pyplot as plt

with open('./data1.json', 'r') as f:
    normal_edges_l = json.load(f)

with open('./data2.json', 'r') as f:
    adversarial_edges_l = json.load(f)

d = {'': ['Normal Edges' for i in normal_edges_l]+['Adversarial Edges' for i in adversarial_edges_l], 'Order': normal_edges_l+adversarial_edges_l}
df = pd.DataFrame(data=d)

sn.set_context("paper", font_scale=2.2, rc={'line.linewidth':3})
fig, ax = plt.subplots(figsize=(10,8))
sn.histplot(df, x='Order', bins=200, kde=True, stat="density", hue='', common_norm=False)
plt.xlabel('Weights in Low-rank Matrix', fontsize=30)
plt.ylabel('KDE Density', fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax=plt.gca()
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
plt.show()
plt.savefig('./polblogs_l.pdf')