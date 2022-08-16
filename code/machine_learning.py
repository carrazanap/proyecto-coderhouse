from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
import numpy as np

#Carga dateset
df_happiness = pd.read_csv('./data/Happiness_final.csv')

#Modelo de regrasion lineal
reg = LinearRegression()
labels = df_happiness["Score"].values

train = df_happiness.drop(["Country","Score"],axis=1)

#Imputo las valores NaN
from sklearn.impute import SimpleImputer
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imp_mean.fit(train)
train = imputer.transform(train)
x_train, x_test, y_train, y_test = train_test_split(train, labels, test_size=0.10, random_state=2)
#Entreno el modelo
reg.fit(x_train, y_train)
#Score de mi modelo
print("Score Linear Regression Model: ",reg.score(x_test,y_test))

#Modelo GradientBoostingRegressor
gbr = ensemble.GradientBoostingRegressor(n_estimators=400,max_depth=5,min_samples_split=2,learning_rate=0.1,loss='squared_error')
#Entreno el modelo
gbr.fit(x_train, y_train)
#Score de mi modelo
print("Score Gradient Boosting Regressor Model: ",gbr.score(x_test,y_test))