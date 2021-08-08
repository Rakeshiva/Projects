# -*- coding: utf-8 -*-


import pandas as pd
df=pd.read_csv("house_rental_data.csv.txt")

#Insights of Data
df.info() 
df.describe()
df.duplicated().sum()

#visulization
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(df)
sns.heatmap(df.corr(),annot=True)
sns.catplot(data=df, x='Sqft' , y='Price' , kind ='bar',height=4,aspect=2)
#2. Store\ing into x and y
x = df.iloc[:,1:-1].values
y = df.iloc[:,-1].values

#3. Spliting into train and test 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=0)

#4. Standardizing the values
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)


#5. Training the model
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from math import sqrt

nnr = KNeighborsRegressor(n_neighbors = 2)
nnr.fit(x_train, y_train)
print(nnr.score(x_test, y_test))

#Finding the better value of K
rmse_val = []
for K in range(1, 20):
    nn_model = KNeighborsRegressor(n_neighbors=K)
    nn_model.fit(x_train, y_train)
    y_pred = nn_model.predict(x_test)
    rmse = sqrt(mean_squared_error(y_test, y_pred))
    rmse_val.append(rmse)
    print("RMSE value=",rmse, "---K:", K)

