
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

from warnings import filterwarnings
filterwarnings(action='ignore')

redwine = pd.read_csv('winequality-red.csv')
print(redwine.head())

redwine.info()

redwine.isnull().sum()

redwine.groupby('quality').mean()

redwine.quality.nunique()

redwine.quality.unique()

redwine.quality.mean()

"""The average quality of all the alcohol samples is 5.63.


"""

redwine.describe().T

redwine.alcohol.mean()

"""The average level of alcohol is 10.4229."""

redwine['quality_3'] = (redwine['quality'] > 2) & (redwine['quality'] < 4)
redwine.groupby('quality_3').size()

q3_true = redwine['quality_3'].sum()
print(q3_true)

redwine['quality_4'] = (redwine['quality'] > 3) & (redwine['quality'] < 5)
redwine.groupby('quality_4').size()

q4_true = redwine['quality_4'].sum()
print(q4_true)

redwine['quality_5'] = (redwine['quality'] > 4) & (redwine['quality'] < 6)
redwine.groupby('quality_5').size()

q5_true = redwine['quality_5'].sum()
print(q5_true)

redwine['quality_6'] = (redwine['quality'] > 5) & (redwine['quality'] < 7)
redwine.groupby('quality_6').size()

q6_true = redwine['quality_6'].sum()
print(q6_true)

redwine['quality_7'] = (redwine['quality'] > 6) & (redwine['quality'] < 8)
redwine.groupby('quality_7').size()

q7_true = redwine['quality_7'].sum()
print(q7_true)

redwine['quality_8'] = (redwine['quality'] > 7) & (redwine['quality'] < 9)
redwine.groupby('quality_8').size()

q8_true = redwine['quality_8'].sum()
print(q8_true)

"""* quality_3 -- 10/1599
* quality_4 -- 53/1599
* quality_5 -- 681/1599
* quality_6 -- 638/1599
* quality_7 -- 199/1599
* quality_8 -- 18/1599
"""

columns_to_drop = ['quality_3','quality_4','quality_5','quality_6','quality_7','quality_8']
redwine = redwine.drop(columns_to_drop, axis = 1)

"""Min and Max alcohol and quality"""

redwine.alcohol.min()

redwine.alcohol.max()

redwine.quality.min()

redwine.quality.max()

redwine.alcohol.mean()

"""* Min alcohol value: 8.4
* Max alcohol value: 14.9



---




* Min quality value: 3
* Max quality value: 8
"""

quality_counts = redwine['quality'].value_counts().sort_index()

plt.figure(figsize=(8, 6))
plt.bar(quality_counts.index, quality_counts.values, color='skyblue')

plt.xlabel('Wine Quality')
plt.ylabel('Count')

plt.show()

plt.figure(figsize=(10,10))
corr=redwine.corr()
sns.heatmap(corr,annot=True)

"""Feature Selection"""

redwine['good_quality'] = [1 if x >=7 else 0 for x in redwine['quality']]

X=redwine.drop(['quality', 'good_quality'], axis=1)
Y=redwine['good_quality']

redwine.good_quality.value_counts()

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.25, random_state=0)

score_df = pd.DataFrame(columns=['Algorithm', 'Accuracy'])

model = DecisionTreeClassifier(random_state=4)
model.fit(X_train,Y_train)
y_predict4=model.predict(X_test)


dtree_score = accuracy_score(Y_test, y_predict4)
dtree_score
