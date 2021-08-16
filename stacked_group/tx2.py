import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

plt.rcParams["font.weight"] = "bold"


matplotlib.rcParams['figure.figsize'] = [5,5] # for square canvas
matplotlib.rcParams['figure.subplot.left'] = 0.05
matplotlib.rcParams['figure.subplot.bottom'] = 0.37
matplotlib.rcParams['figure.subplot.right'] = 0.97
matplotlib.rcParams['figure.subplot.top'] = 0.9

fig,ax = plt.subplots(figsize=(16,4))

sns.set(context='paper',style='ticks')
df = pd.read_csv('tx2.csv')

x=np.arange(df['Type'].shape[0])
size=np.array([8 for _ in x])
width = .2
#plots


#df['cloud'][df['cloud'].shape[0]-1]=0

bar_a = ax.bar(x-width/2, df["Ours Main"],width,label='Ours Other',color='darkorange')
ax.bar(x-width/2, df["Ours CPU"]+df["Ours GPU"]+df["Ours Transfer"],width,label='Ours Transfer',color='orange')
ax.bar(x-width/2, df["Ours CPU"]+df["Ours GPU"],width,label='Ours GPU',color='gold')
ax.bar(x-width/2, df["Ours CPU"],width,label='Ours CPU',color='khaki')
bar_b = ax.bar(x-width*3/2, df["Edge-only Main"], width,label='Edge-only Other',hatch='o',color='purple')
ax.bar(x-width*3/2, df["Edge-only CPU"]+df["Edge-only GPU"],width,label='Edge-only GPU',hatch='o',color='darkmagenta')
ax.bar(x-width*3/2, df["Edge-only CPU"],width,label='Edge-only CPU',hatch='o',color='mediumorchid')
bar_c = ax.bar(x+width/2, df['JointDNN Main'],width,label='JointDNN Other',hatch='x',color='midnightblue')
ax.bar(x+width/2, df["JointDNN CPU"]+df["JointDNN GPU"]+df["JointDNN Transfer"],width,label='JointDNN Transfer',hatch='x',color='darkblue')
ax.bar(x+width/2, df["JointDNN CPU"]+df["JointDNN GPU"],width,label='JointDNN GPU',hatch='x',color='mediumblue')
ax.bar(x+width/2, df["JointDNN CPU"],width,label='JointDNN CPU',hatch='x',color='blue')
font = {
'size'   : 18,
'weight':'bold'
}

t=np.array(df['Type'])
for i in range(t.shape[0]):
    p=t[i].split(' ')
    s=''
    for pp in p:
        s+=pp+'\n'
    t[i]=s
plt.title('TX2 Split&Transfer Learning',fontsize=18)
plt.xticks(x,t)
#plt.xlabel('Type',font)
plt.yscale('log')
plt.ylabel('Energy (Wh)',font)
plt.legend(loc=1,ncol=6,fontsize=16,bbox_to_anchor=(1.04,-0.3))
plt.tick_params(labelsize=16)
plt.xticks(rotation=0)
plt.grid(linestyle='--')
                  
plt.savefig("enerygy_tx2.eps")
plt.show()

