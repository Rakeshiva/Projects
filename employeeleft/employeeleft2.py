import pandas as pd

df=pd.read_csv("HR_comma_sep.csv")


#3. One Hot Encoding
df = pd.get_dummies(df, columns=['sales', 'salary'], drop_first=True)


#splitting data into x and y
x=df.drop(columns='left')
y=df.left


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,
                                               random_state=0)
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)


from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
p1=make_pipeline(StandardScaler(),RandomForestClassifier())

p1.fit(x_train,y_train)
y_pred=p1.predict(x_test)

print(p1.score(x_test,y_test))


















