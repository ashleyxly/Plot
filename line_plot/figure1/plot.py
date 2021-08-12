import json
from matplotlib import pyplot as plt
import matplotlib.patches as patches

with open('./data1.json', 'r') as f:
	singular_union_clean_ = json.load(f)

with open('./data2.json', 'r') as f:
	index_b = json.load(f)

x = list(range(len(singular_union_clean_)))

fig=plt.figure(figsize=(10,8))
plt.plot(x, singular_union_clean_, label='Union of Perturbed Subgraph \nand Clean Subgraph ', linewidth=4, alpha=0.8)
plt.vlines([x[i] for i in index_b], [-0.2 for i in index_b],
           [singular_union_clean_[i] for i in index_b], linestyles='dashed', linewidth=1.2, colors='#625E5E', label='Perturbed Subgraph')
plt.legend(fontsize=22)
plt.xlabel('Order', fontsize=30)
plt.ylabel('Singular Value', fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

ax=plt.gca()
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

rect=patches.Rectangle((2200, -0.7),350,1.3,linewidth=2, edgecolor='r',facecolor='none', linestyle='--')
ax.add_patch(rect)

plt.show()
plt.savefig('./union_clean.pdf', bbox_inches='tight')