import matplotlib.pyplot as plt
import numpy as np

plt.subplots(figsize=(16,9))

x=np.arange(0, 42, 7)
#数据集
y1=[83.49,80.93,76.92,75.92,72.86,70.11]
y2=[61.81,61.78,61.97,61.41,61.5,61.88]
y3=[29.18,29.18,29.18,29.18,29.18,29.18]
y4=[83.50,76.55,70.39,65.10,59.56,47.53]
#误差列表
std_err1=[0.47,0.77,0.83,0.47,0.93,1.0]
std_err2=[1.09,1.02,1.36,1.0,0.97,1.14]
std_err3=[0.0,0.0,0.0,0.0,0.0,0.0]
std_err4=[0.44,0.79,1.28,0.71,2.72,1.96]
tick_label=['0','5%','10%','15%','20%','25%']

error_params1=dict(elinewidth=2,ecolor='crimson',capsize=6)#设置误差标记参数
error_params2=dict(elinewidth=2,ecolor='crimson',capsize=6)#设置误差标记参数
error_params3=dict(elinewidth=2,ecolor='crimson',capsize=6)#设置误差标记参数
error_params4=dict(elinewidth=2,ecolor='crimson',capsize=6)#设置误差标记参数
#设置柱状图宽度
bar_width=1
#绘制柱状图，设置误差标记以及柱状图标签
plt.bar(x,y1,bar_width,yerr=std_err1,error_kw=error_params1,label='Our', color='#5B85F2')
plt.bar(x+bar_width,y2,bar_width,yerr=std_err2,error_kw=error_params2,label='Col Orthogonal', color='#E98F4E')
plt.bar(x+bar_width*2,y3,bar_width,yerr=std_err3,error_kw=error_params3,label='Random', color='gray')
plt.bar(x+bar_width*3,y4,bar_width,yerr=std_err4,error_kw=error_params4,label='GCN', color='#71C074')

plt.ylim((0, 90))
plt.xticks(x+bar_width*1.5,tick_label)#设置x轴的标签
#设置网格
plt.grid(True,axis='y',ls='--',alpha=0.4)
plt.xlabel('Perturbation Rate(%)', fontsize=30)
plt.ylabel('Test Accuracy', fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax=plt.gca()
ax.spines['bottom'].set_color('black')
ax.spines['top'].set_color('black')
ax.spines['left'].set_color('black')
ax.spines['right'].set_color('black')
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ax.set_facecolor('')

#显示图例
plt.legend(fontsize=25, loc='upper center', edgecolor='black', facecolor='white', ncol= 4, bbox_to_anchor=(0.5, 1.08))
#显示图形
plt.show()

plt.savefig('./init.pdf')