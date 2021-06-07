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
import matplotlib.pyplot as plt  
import seaborn as sns

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
#sql
sqlite_file = '../data/heart3.sqlite'
heart3 = sqla.create_engine('sqlite:///' + sqlite_file)
data.to_sql('heart3',heart3,if_exists = 'append')
print(pd.read_sql_query('select avg(age),avg(trtbps),avg(chol),avg(thalachh),avg(oldpeak),sex from heart3 group by sex',heart3))

#
#density plot
print(p9.ggplot(data, p9.aes(x = 'age',fill = 'sex')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'trtbps',fill = 'sex')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'thalachh',fill = 'sex')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'chol',fill = 'sex')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'oldpeak',fill = 'sex')) + p9.geom_density(alpha=.2))

#
output_ticks = ['Less Chance', 'More Chance']
sex_legends = ['Female', 'Male']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='output', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Gender', labels = output_ticks)
plt.title('Output Distribution in Different genders', fontsize=18)
plt.show()

cp_legends = ['type 1', 'type 2','type 3','type 4']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='cp', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Chest Pain type', labels = cp_legends)
plt.title(' Different Types of Chest Pain Distribution in Different genders', fontsize=18)
plt.show()

fbs_legends = ['False','True']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='fbs', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Fasting Blood Sugar > 120 mg/dl ', labels = fbs_legends)
plt.title('Fasting Blood Sugar > 120 mg/dl Distribution in Different Sex', fontsize=18)
plt.show()

restecg_legends = ['Normal','Having ST-T wave abnormality','Showing left ventricular hypertrophy']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='restecg', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Resting electrocardiographic results', labels = restecg_legends)
plt.title('Resting Electrocardiographic Results Distribution in Different Genders', fontsize=18)
plt.show()

exng_legends = ['Yes','No']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='exng', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Exercise induced angina', labels = exng_legends)
plt.title('Exercise Induced Angina Distribution in Different Sex', fontsize=18)
plt.show()

cca_legends = ['0','1','2','3']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='caa', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Number of Major Vessels', labels = cca_legends)
plt.title('Number of Major Vessels Distribution in Different Genders', fontsize=18)
plt.show()

thall_legends = ['0','1','2','3']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'sex', hue='thall', data=data, palette='husl')
ax.set_xticklabels(sex_legends)
plt.xlabel('Sex')
plt.ylabel('Count')
plt.legend(title = 'Maximun Heart Rate Achieve', labels = thall_legends)
plt.title('Thallum Stress Test Result Distribution in Different Genders', fontsize=18)
plt.show()