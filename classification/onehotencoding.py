from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer,OneHotEncoder,VectorAssembler,Imputer

# Creating spark Context
spark=SparkSession.builder.getOrCreate()

# loading data into spark data frame from csv file
df2=spark.read.csv('C:/Manidhar/MachineLearningLab/datasets/titanic/trainCopy.csv',header=True)

# Show number of rows in the spark Dataframe
df2.count()

# Show Schema details of the spark Dataframe
df2.printSchema()

# creating new spark data frame based on the selected columns
df3=df2.select('Pclass','Survived','Sex','Embarked')
df3.show(n=5)
df3.printSchema()

# Aggregation on Specific cloumn
df3.groupBy('Embarked').agg({'Embarked':'count'}).show()

# show summary of cloumns
df3.describe().show()

# Applying OneHot on Embared Column

# Step 1 : Convert the column to set of numbers using String Indexer. Hear each category will be assigned with a number based on its occurences (i.e Mode)
df3=StringIndexer(inputCol='Embarked',outputCol='EntryPoints').fit(df3).transform(df3)
df3.show(n=15)

# Step 2: Apply OneHot on Newly created StringIndexer column
df3=OneHotEncoder(inputCol='EntryPoints',outputCol='EntryLocations',dropLast=False).transform(df3)
df3.show(15)

# comibine all feature columns in to one column to pass it to the model
df3=VectorAssembler(inputCols=[''])
