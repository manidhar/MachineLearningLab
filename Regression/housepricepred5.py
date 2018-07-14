import pandas as pd
from sklearn import linear_model,model_selection,metrics
import math

# 1. Data
house_train=pd.read_csv('C:/Manidhar/MachineLearningLab/datasets/HomePrice/train.csv')

# 2. EDA
house_train.info()
house_train.shape


# 3. Preprocessing [Filling the missing data (Imputation), converting categoric to continious using onehot encodeing, Data normalization or standardization, Data Transformation]
# MSSubclass, Street need to convert this into onehot as it is categoric

cat_to_continues=['MSSubClass','Street']
house_train=pd.get_dummies(house_train,columns=cat_to_continues)
house_train.info()
house_train.columns

# Functional style of programming
# These are called Ordinal Features with relation
mappings={'Po' :1,'Fa':2,'TA':3,'Gd':4,'Ex':5}
features1 =['ExterQual','ExterCond','BsmtCond','BsmtQual','KitchenQual','HeatingQC','GarageQual','GarageCond','FireplaceQu']
for f1 in features1:
    house_train[f1]=house_train[f1].map(mappings)
    house_train.loc[house_train[f1].isnull() == True,f1]=0

# 4. Feature Engineering [Feature selection based on feature importance, Filtering features,Create new features if required, transforming of features]
dims=['LotArea','OverallQual','OverallCond','MSSubClass_20', 'MSSubClass_30', 'MSSubClass_40', 'MSSubClass_45',
       'MSSubClass_50', 'MSSubClass_60', 'MSSubClass_70', 'MSSubClass_75',
       'MSSubClass_80', 'MSSubClass_85', 'MSSubClass_90', 'MSSubClass_120',
       'MSSubClass_160', 'MSSubClass_180', 'MSSubClass_190', 'Street_Grvl',
       'Street_Pave']

dims.extend(features1)
dims
X_train=house_train[dims]
X_train.info()
y_train=house_train['SalePrice']

# 5. Model Building
mylr=linear_model.LinearRegression()
mylr.fit(X_train,y_train)
mylr.coef_
mylr.intercept_

# 6. Model Evaluation

# estimators will have scoring funciton
# Resubstitution strategy. Score is calculated using explained variance
mylr.score(X_train,y_train)
y_predict=mylr.predict(X_train)
metrics.explained_variance_score(y_train,y_predict) # this is called train score
meansqr=metrics.mean_squared_error(y_train,y_predict) # this is called train error
math.sqrt(meansqr)

# Resampling score or CV score
model_selection.cross_val_score(mylr,X_train,y_train,cv=10).mean()

