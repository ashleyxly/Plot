import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib

plt.rcParams["font.weight"] = "bold"


matplotlib.rcParams['figure.figsize'] = [5,5] # for square canvas
matplotlib.rcParams['figure.subplot.left'] = 0.19
matplotlib.rcParams['figure.subplot.bottom'] = 0.37
matplotlib.rcParams['figure.subplot.right'] = 0.97
matplotlib.rcParams['figure.subplot.top'] = 0.92

fig,ax = plt.subplots(figsize=(4.5,4))

sns.set(context='paper',style='ticks')
df = pd.read_csv('pi.csv')

x=np.arange(df['Type'].shape[0])
size=np.array([8 for _ in x])
width = .3
#plots


#df['cloud'][df['cloud'].shape[0]-1]=0

#ours=df['Ours']*10
bar_a = ax.bar(x-width*3/2, df['Ours'],width,label='Ours',color='darkorange')
bar_b = ax.bar(x-width/2, df["Edge-only"], width,label='Edge-only',hatch='o',color='darkmagenta')
bar_c = ax.bar(x+width/2, df['JointDNN'],width,label='JointDNN',hatch='x',color='darkblue')
font = {
'size'   : 18,
'weight':'bold'
}

t=np.array(df['Type'])
for i in range(t.shape[0]):
    p=t[i].find(' ')
    t[i]=t[i][:p]+'\n'+t[i][p+1:]

plt.title('Pi',fontsize=18)
plt.xticks(x,t)
#plt.xlabel('Type',font)
plt.yscale('log')
plt.ylabel('Energy (Wh)',font)
plt.legend(loc=1,ncol=2,fontsize=16,bbox_to_anchor=(1,-0.25))
plt.tick_params(labelsize=16)
plt.xticks(rotation=0)
plt.grid(linestyle='--')
                  
plt.savefig("enerygy_pi.eps")
plt.show()

