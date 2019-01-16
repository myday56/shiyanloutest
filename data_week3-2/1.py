import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

df = pd.read_csv('beijing_house_price.csv')

df.head()

df = df.drop_duplicates()

df.corr()

pearson_max = np.abs(df.corr().iloc[-2]).sort_values(ascending=False)[1:4]

features_names = pearson_max.index.values

features_names

features = df[features_names]

target = df.iloc[:,[-2]]

target

x_train,x_test,y_train,y_test = train_test_split(features,target,test_size=0.3,random_state=10)

poly_features = PolynomialFeatures(degree=3)

x_train_feature = poly_features.fit_transform(x_train)

# x_train

x_test_feature = poly_features.fit_transform(x_test)

model = LinearRegression()

model.fit(x_train_feature, y_train)

y_pred = model.predict(x_test_feature)

mae = mean_absolute_error(y_test, y_pred)

mae

