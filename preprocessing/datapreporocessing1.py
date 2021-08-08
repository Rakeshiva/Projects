# -*- coding: utf-8 -*-

import pandas as pd
df=pd.read_csv('HR_comma_sep.csv.txt')
df.columns
df.info()
df=df[['left','satisfaction_level', 'last_evaluation', 'number_project',
       'average_montly_hours', 'time_spend_company', 'Work_accident', 
       'promotion_last_5years', 'sales', 'salary']]


from sklearn import preprocessing
df[['average_montly_hours']] = preprocessing.scale(df[['average_montly_hours']])
df['number_project']=preprocessing.scale(df['number_project'])
df['time_spend_company']=preprocessing.scale(df['time_spend_company'])

#3. One Hot Encoding
df = pd.get_dummies(df, columns=['sales', 'salary'], drop_first=True)

#storing values
x=df.iloc[:,1:19]
y=df.iloc[:,0]

#training model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train, y_train)
y_pred = knn.predict(x_test)

print(knn.score(x_test, y_test))

