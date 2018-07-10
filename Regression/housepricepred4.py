import pandas as pd
from sklearn import linear_model,model_selection,metrics
import math
import numpy as np
house_train=pd.read_csv('C:/Manidhar/MachineLearningLab/datasets/HomePrice/train.csv')
house_train.info()
house_train.shape


# Preprocessing
# MSSubclass, Street need to convert this into onehot as it is categoric

cat_to_continues=['MSSubClass','Street']
house_train=pd.get_dummies(house_train,columns=cat_to_continues)
house_train.info()
house_train.columns
# FE
dims=['LotArea','OverallQual','OverallCond','MSSubClass_20', 'MSSubClass_30', 'MSSubClass_40', 'MSSubClass_45',
       'MSSubClass_50', 'MSSubClass_60', 'MSSubClass_70', 'MSSubClass_75',
       'MSSubClass_80', 'MSSubClass_85', 'MSSubClass_90', 'MSSubClass_120',
       'MSSubClass_160', 'MSSubClass_180', 'MSSubClass_190', 'Street_Grvl',
       'Street_Pave']

X_train=house_train[dims]
X_train.info()

y_train=np.log(house_train['SalePrice'])

# Model Building
mylr=linear_model.Lasso()

mylr.fit(X_train,y_train)

mylr.coef_
mylr.intercept_
mylr.n_iter_


# estimators will have scoring funciton
# Resubstitution strategy. Score is calculated using explained variance
mylr.score(X_train,y_train)
y_predict=mylr.predict(X_train)
metrics.explained_variance_score(y_train,y_predict) # this is called train score
meansqr=metrics.mean_squared_error(y_train,y_predict) # this is called train error
math.sqrt(meansqr)

# Resampling score or CV score
model_selection.cross_val_score(mylr,X_train,y_train,cv=10).mean()

