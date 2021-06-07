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

age_output = {'age':['<30','30-39','40-49','50-59','60-69','>70'],
       'output = 1':[1,11,50,65,32,6],
       'output = 0':[0,4,22,60,48,4],
       'total amount':[1,15,72,125,80,10],
       'proportion':[1,11/15,50/72,65/125,32/80,6/10]}
age_output = pd.DataFrame(age_output)
print(age_output)

def auto_text(rects):
    for rect in rects:
        ax.text(rect.get_x(), rect.get_height(), rect.get_height(), ha='left', va='bottom')



name_list = ['<30','30-39','40-49','50-59','60-69','>70']
num_list = [1,11,50,65,32,6]
num_list1 = [0,4,22,60,48,4]

index = np.arange(len(name_list))
width = 0.2

fig, ax = plt.subplots()
rect1 = ax.bar(index - width / 2, num_list, color ='lightcoral', width=width, label ='output = 1')
rect2 = ax.bar(index + width / 2, num_list1, color ='gold', width=width, label ='output = 0')

ax.set_title('Distribution of output in different age groups')
ax.set_xticks(ticks=index)
ax.set_xticklabels(name_list)
ax.set_ylabel('amount')

auto_text(rect1)
auto_text(rect2)

ax.legend(loc='upper right', frameon=False)
fig.tight_layout()
plt.show()