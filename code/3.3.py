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

print(p9.ggplot(data, p9.aes(x = 'chol',fill = 'output')) + p9.geom_density(alpha=.2))

print(p9.ggplot(data, p9.aes(x = 'thalachh',fill = 'output')) + p9.geom_density(alpha=.2))

plt.figure(figsize=(10,7))
plt.style.use("fivethirtyeight")
plt.title("effect of heart attack with increase in age and heart rate")
sns.lineplot(x=data['age'],y=data['thalachh'],hue=data['output'])
