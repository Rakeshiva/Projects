
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
#2. Storeing into x and y
x = df.loc[:,df.columns!='Price']
y = df.loc[:,df.columns=='Price']
#3. Spliting into train and test 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.25,random_state=0)


from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
p1=make_pipeline(StandardScaler(),LinearRegression())

p1.fit(x_train,y_train)
y_pred=p1.predict(x_test)

print(p1.score(x_test,y_test))


##Polynomial linear Regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 7)
x_poly = poly_reg.fit_transform(x)

lin_reg_poly = LinearRegression()
lin_reg_poly.fit(x_poly, y)
y_pred = lin_reg_poly.predict(x_poly)
print(lin_reg_poly.score(x_poly, y))









