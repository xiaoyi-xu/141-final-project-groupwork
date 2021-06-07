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

sqlite_file = '../data/heart2.sqlite'

heart2 = sqla.create_engine('sqlite:///' + sqlite_file)

data.to_sql('heart2',heart2,if_exists = 'append')

output0 = pd.read_sql_query('select age,trtbps,chol,thalachh,oldpeak,output from heart2 where output = 0 ',heart2)

output1 = pd.read_sql_query('select age,trtbps,chol,thalachh,oldpeak,output from heart2 where output = 1 ',heart2)

print(output0. describe())

print(output1. describe())
