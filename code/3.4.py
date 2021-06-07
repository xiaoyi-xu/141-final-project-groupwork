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

output_ticks = ['Less Chance', 'More Chance']
sex_legends = ['Female', 'Male']

sns.set(font_scale=1.3)
ax = sns.countplot(x = 'output', hue='sex', data=data, palette='husl')
ax.set_xticklabels(output_ticks)

plt.xlabel('Output')
plt.ylabel('Count')
plt.legend(title = 'Gender', labels = sex_legends)
plt.title('Gender Distribution in Different Chances', fontsize=18)


plt.show()

cp_legends = ['type 1', 'type 2','type 3','type 4']

sns.set(font_scale=1.3)
ax = sns.countplot(x = 'output', hue='cp', data=data, palette='husl')
ax.set_xticklabels(output_ticks)

plt.xlabel('Output')
plt.ylabel('Count')
plt.legend(title = 'Chest Pain type', labels = cp_legends)
plt.title(' Different Types of Chest Pain Distribution in Different Chances', fontsize=18)


plt.show()

cca_legends = ['0','1','2','3']

sns.set(font_scale=1.3)
ax = sns.countplot(x = 'output', hue='caa', data=data, palette='husl')
ax.set_xticklabels(output_ticks)

plt.xlabel('Output')
plt.ylabel('Count')
plt.legend(title = 'Number of Major Vessels', labels = cca_legends)
plt.title('Number of Major Vessels Distribution in Different Chances', fontsize=18)


plt.show()

exng_legends = ['Yes','No']

sns.set(font_scale=1.3)
ax = sns.countplot(x = 'output', hue='exng', data=data, palette='husl')
ax.set_xticklabels(output_ticks)

plt.xlabel('Output')
plt.ylabel('Count')
plt.legend(title = 'Exercise induced angina', labels = exng_legends)
plt.title('Exercise Induced Angina Distribution in Different Chances', fontsize=18)


plt.show()
