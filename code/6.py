import pandas as pd
import numpy as np
import warnings
warnings.simplefilter("ignore")
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import metrics
import matplotlib as mpl
from sklearn.metrics import accuracy_score

data = pd.read_csv('../data/heart.csv')
y = data['output']
x = data.iloc[:,0:13]
Xtrain, Xtest, Ytrain, Ytest = train_test_split(x,y,test_size=0.3,random_state=0)
#summary
logit_model = sm.Logit(Ytrain, Xtrain).fit()
print(logit_model.summary())
#confusion matrix-train
def predict(pre):
    for i in list(pre.index):
        if pre[i]>=0.5:
            pre[i] = 1
        else:
            pre[i] = 0
    return(pre)
prediction = logit_model.predict(Xtrain)
prediction = predict(prediction)
cm = metrics.confusion_matrix(Ytrain, prediction)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
#all_sample_title = 'Accuracy Score: {0}'.format(score)
#accuracy_score(y_test, y_pred)
all_sample_title = 'Accuracy Score: {0}'.format(accuracy_score(Ytrain, prediction))
plt.title(all_sample_title, size = 15);
#confusion matrix-test
prediction2 = logit_model.predict(Xtest)
prediction2 = predict(prediction2)
cm = metrics.confusion_matrix(Ytest, prediction2)
plt.figure(figsize=(9,9))
sns.heatmap(cm, annot=True, fmt=".3f", linewidths=.5, square = True, cmap = 'Blues_r');
plt.ylabel('Actual label');
plt.xlabel('Predicted label');
#all_sample_title = 'Accuracy Score: {0}'.format(score)
all_sample_title = 'Accuracy Score: {0}'.format(accuracy_score(Ytest, prediction2))
plt.title(all_sample_title, size = 15);