from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import json

with open('./data1.json', 'r') as f:
    singular_union = json.load(f)

with open('./data2.json', 'r') as f:
    singular_union_clean = json.load(f)

with open('./data3.json', 'r') as f:
    index = json.load(f)

with open('./data4.json', 'r') as f:
    lrgnn_s = json.load(f)

with open('./data5.json', 'r') as f:
    prognn_s = json.load(f)

length = len(singular_union)


singular_union_ = singular_union + [0] * (length - len(singular_union))
singular_union_clean_ = singular_union_clean + [0] * (length - len(singular_union_clean))

x = list(range(length))

fig=plt.figure(figsize=(10,8))
plt.plot(x, singular_union_, label='Union of Perturbed Subgraph \nand Clean Subgraph', linewidth=4, alpha=0.8)
plt.vlines([x[i] for i in index], [-0.2 for i in index], [singular_union[i] for i in index],
           linestyles='dashed', linewidth=1.2, colors='#625E5E', label='Perturbed Subgraph')
plt.plot(x, lrgnn_s, label='LRGNN', linewidth=4, alpha=0.8)
plt.plot(x, prognn_s, label='Pro-GNN', linewidth=4, alpha=0.8)
plt.vlines([200], [0], [14],
           linestyles='dashed', linewidth=3, colors='red', alpha=0.8)
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

#绘制内嵌图
axins = ax.inset_axes((0.3, 0.3, 0.35, 0.25))
axins.plot(x, singular_union_, label='Union of Perturbed Subgraph \nand Clean Subgraph', linewidth=4, alpha=0.8)
axins.plot(x, lrgnn_s, label='LRGNN', linewidth=4, alpha=0.8)
axins.plot(x, prognn_s, label='Pro-GNN', linewidth=4, alpha=0.8)
axins.vlines([200], [0], [14], linestyles='dashed', linewidth=4, colors='red', alpha=0.8)
axins.vlines([x[i] for i in index], [-0.2 for i in index], [singular_union[i] for i in index],
           linestyles='dashed', linewidth=1.6, colors='#625E5E', label='Perturbed Subgraph')
axins.set_xlim(180, 400)
axins.set_ylim(0, 1)
axins.spines['bottom'].set_linewidth(1.5)
axins.spines['top'].set_linewidth(1.5)
axins.spines['left'].set_linewidth(1.5)
axins.spines['right'].set_linewidth(1.5)
mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec='black', lw=1.5)

plt.annotate('',xy=(190,13.7),xytext=(-100,13.7),arrowprops=dict(arrowstyle="<-",connectionstyle="arc3",linewidth=3,color='red'))
plt.annotate('',xy=(210,13.7),xytext=(500,13.7),arrowprops=dict(arrowstyle="<-",connectionstyle="arc3",linewidth=3,color='red'))
plt.text(-150, 12.7, 'Ideal C', fontsize=20, color='#435275')
plt.text(230, 12.7, 'Ideal P', fontsize=20, color='#435275')

plt.show()
plt.savefig('./union_perturb.pdf', bbox_inches='tight')