import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  
import seaborn as sns
import matplotlib as mpl
import plotnine as p9
import itertools
import sqlalchemy as sqla
import warnings
warnings.simplefilter("ignore")
from collections import Counter

data = pd.read_csv('../data/heart.csv')

data['output'] = data['output'].astype('object')
data['sex'] = data['sex'].astype('object')
data['cp'] = data['cp'].astype('object')
data['fbs'] = data['fbs'].astype('object')
data['restecg'] = data['restecg'].astype('object')
data['exng'] = data['exng'].astype('object')
data['slp'] = data['slp'].astype('object')
data['caa'] = data['caa'].astype('object')
data['thall'] = data['thall'].astype('object')

num_col = ['age','trtbps','chol','thalachh','oldpeak']
num = data[num_col]


fig,ax=plt.subplots(2,3,figsize=(15,10))
fig.patch.set_facecolor('#f6f5f7')
for i,idx in enumerate(num.columns):
    sns.histplot(ax=ax[i%2,i//2],x=num[idx],color='tomato',kde=True,alpha=0.6)
    ax[i%2,i//2].set_title(idx,fontweight='medium')
    ax[i%2,i//2].set_facecolor('#f6f5f7')
    for z in ["top","right"]:
        ax[i%2,i//2].spines[z].set_visible(False)
ax[1,2].set_visible(False)

corrPearson = num.corr(method="spearman")
figure = plt.figure(figsize=(10,8))
sns.heatmap(corrPearson,annot=True,cmap='RdYlGn', vmin=-1, vmax=+1)
plt.title("PEARSON")
plt.xlabel("COLUMNS")
plt.ylabel("COLUMNS")
plt.show()

def cal_pccs(x, y, n):
    """
    warning: data format must be narray
    :param x: Variable 1
    :param y: The variable 2
    :param n: The number of elements in x
    :return: pccs
    """
    sum_xy = np.sum(np.sum(x*y))
    sum_x = np.sum(np.sum(x))
    sum_y = np.sum(np.sum(y))
    sum_x2 = np.sum(np.sum(x*x))
    sum_y2 = np.sum(np.sum(y*y))
    pcc = (n*sum_xy-sum_x*sum_y)/np.sqrt((n*sum_x2-sum_x*sum_x)*(n*sum_y2-sum_y*sum_y))
    return pcc

age = data.iloc[:,0]
trtbps = data.iloc[:,1]
chol = data.iloc[:,2]
thalachh = data.iloc[:,3]
oldpeak = data.iloc[:,-1]
n = data.shape[0]

print(cal_pccs(age,trtbps,n))
print(cal_pccs(age,chol,n))
print(cal_pccs(age,thalachh,n))
print(cal_pccs(age,oldpeak,n))
print(cal_pccs(trtbps,chol,n))
print(cal_pccs(trtbps,thalachh,n))
print(cal_pccs(trtbps,oldpeak,n))
print(cal_pccs(chol,thalachh,n))
print(cal_pccs(chol,oldpeak,n))
print(cal_pccs(thalachh,oldpeak,n))
