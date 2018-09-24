from pyspark.sql import SparkSession
spark=SparkSession.builder.getOrCreate()

# 1. Loading the data into spark dataframe
train_data=spark.read.csv('C:/Manidhar/DataScience/DataSets/New York City Taxi Fare Prediction/train.csv',header=True)
# EDA (Exploratory Data Analysis)
train_data.printSchema()
train_data.count()
train_data.show(n=1)
X_train=train_data
X_train.dtypes
X_train.describe().show()
X_train.select('key').show(truncate=False)
X_train.filter(X_train.dropoff_longitude.isNull()).count()
X_train.count()
X_train.select('pickup_longitude').describe().show()
