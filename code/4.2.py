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
sqlite_file = '../data/heart4.sqlite'
heart4 = sqla.create_engine('sqlite:///' + sqlite_file)
data.to_sql('heart4',heart4,if_exists = 'append')
print(pd.read_sql_query('select avg(age),avg(trtbps),avg(chol),avg(thalachh),avg(oldpeak),exng from heart4 group by exng',heart4))
#density plot
print(p9.ggplot(data, p9.aes(x = 'age',fill = 'exng')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'trtbps',fill = 'exng')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'thalachh',fill = 'exng')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'chol',fill = 'exng')) + p9.geom_density(alpha=.2))
print(p9.ggplot(data, p9.aes(x = 'oldpeak',fill = 'exng')) + p9.geom_density(alpha=.2))
# categorical variable
cp_legends = ['type 1', 'type 2','type 3','type 4']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='cp', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Chest Pain type', labels = cp_legends)
plt.title(' Different Types of Chest Pain Distribution in Different Exng', fontsize=18)
plt.show()

fbs_legends = ['False','True']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='fbs', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Fasting Blood Sugar > 120 mg/dl ', labels = fbs_legends)
plt.title('Fasting Blood Sugar > 120 mg/dl Distribution in Different Exng', fontsize=18)
plt.show()

restecg_legends = ['Normal','Having ST-T wave abnormality','Showing left ventricular hypertrophy']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='restecg', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Resting electrocardiographic results', labels = restecg_legends)
plt.title('Resting Electrocardiographic Results Distribution in Different Exng', fontsize=18)
plt.show()

sex_legends = ['Female', 'Male']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='sex', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Exercise induced angina', labels = sex_legends)
plt.title('Exercise Induced Angina Distribution in Different Exng', fontsize=18)
plt.show()

cca_legends = ['0','1','2','3']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='caa', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Number of Major Vessels', labels = cca_legends)
plt.title('Number of Major Vessels Distribution in Different Exng', fontsize=18)
plt.show()

thall_legends = ['0','1','2','3']
sns.set(font_scale=1.3)
ax = sns.countplot(x = 'exng', hue='thall', data=data, palette='husl')
plt.xlabel('Exng')
plt.ylabel('Count')
plt.legend(title = 'Maximun Heart Rate Achieve', labels = thall_legends)
plt.title('Thallum Stress Test Result Distribution in Different Exng', fontsize=18)
plt.show()