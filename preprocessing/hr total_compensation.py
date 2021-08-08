# -*- coding: utf-8 -*-
import pandas as pd
df=pd.read_csv("train_set.csv")

corr=df.corr()
df.isnull().values.any()

df=df.drop_duplicates()
df.columns
df=df[[ 'EI','Salaries', 'Overtime', 'H/D', 'Total_Compensation']]

x=df.iloc[:,:4]
y=df.iloc[:,4]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,
                                               random_state=0)

from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

from sklearn.neighbors import KNeighborsRegressor
knn =KNeighborsRegressor(n_neighbors=15)
knn.fit(x_train, y_train)

print(knn.score(x_test, y_test))

from math import sqrt
from sklearn.metrics import mean_squared_error
rmse_val = []
for K in range(1, 20):
    nn_model = KNeighborsRegressor(n_neighbors=K)
    nn_model.fit(x_train, y_train)
    y_pred = nn_model.predict(x_test)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    rmse_val.append(rmse)
    print("RMSE value=",rmse, "---K:", K)
