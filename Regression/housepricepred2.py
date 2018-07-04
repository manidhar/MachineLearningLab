import pandas as pd
from sklearn import linear_model

house_train=pd.read_csv('C:/Manidhar/MachineLearningLab/datasets/HomePrice/train.csv')
house_train.info()
house_train.shape

dims=['LotArea','YrSold']

X_train=house_train[dims]
X_train.info()

y_train=house_train['SalePrice']

lr1=linear_model.LinearRegression()

lr1.fit(X_train,y_train)

lr1.coef_
lr1.intercept_

house_test=pd.read_csv('C:/Manidhar/MachineLearningLab/datasets/HomePrice/test.csv')
house_test.info()
house_test.shape

X_test=house_test[dims]
house_test['SalePrice']=lr1.predict(X_test)
house_test.info()
house_test.shape
