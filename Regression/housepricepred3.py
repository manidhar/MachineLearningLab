import pandas as pd
from sklearn import linear_model,model_selection,metrics
import math

house_train=pd.read_csv('C:/Manidhar/MachineLearningLab/datasets/HomePrice/train.csv')
house_train.info()
house_train.shape

dims=['LotArea']

X_train=house_train[dims]
X_train.info()

y_train=house_train['SalePrice']

lr=linear_model.Lasso()

lr.fit(X_train,y_train)

lr.coef_
lr.intercept_

# estimators will have scoring funciton
# Resubstitution strategy. Score is calculated using explained variance
lr.score(X_train,y_train)
y_predict=lr.predict(X_train)
metrics.explained_variance_score(y_train,y_predict) # this is called train score
meansqr=metrics.mean_squared_error(y_train,y_predict) # this is called train error
math.sqrt(meansqr)
