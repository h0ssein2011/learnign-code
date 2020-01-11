import pandas as pd
import numpy as np
address = '~/Lats Win Files/C/python/kaggle-and-other-Online-competitions/human-resources-analytics/HR_comma_sep.csv'

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv(address)
print(df.shape)

print(df.info())

#for simplicity neglect object vars
object_vars = [col for col in df.columns if df[col].dtype == 'object']

df_reduced = df.drop(object_vars ,axis= 1 )
print(df_reduced.isnull().sum())

#fortunately we dont have null values so dot need fill missing vals techniques here
X=df_reduced.drop('left' ,axis= 1)
y=df_reduced['left']

X_train,X_valid,y_train,y_valid = train_test_split(X,y,train_size=0.8 , random_state=0)

clf=LogisticRegression()
clf.fit(X_train ,y_train)
pred_lr=clf.predict(X_valid)
print(pred_lr)

def confution_matrix(y_pred,y):
    true_positive = np.sum(y == 1 and y==y_pred)
    false_positive = np.sum(y == 1 and y!=y_pred)

    true_negative = np.sum(y == 0 and y==y_pred)
    false_nagative =np.sum(y == 0 and y!=y_pred)

    return True_positive ,false_positive ,true_negative,false_nagative

print(confution_matrix(pred_lr,y_valid))