from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler,StringIndexer
from pyspark.ml.classification import DecisionTreeClassifier
spark=SparkSession.builder.getOrCreate()
df2=spark.read.csv('C:/Manidhar/MachineLearningLab/datasets/titanic/train.csv',header=True)
df2.show()
df2.describe().show()
df2.printSchema()
df3=df2.select('Pclass','Sex','Survived')
df3.printSchema()
df3.show()
df4=df2.filter(df2.Age>40).select('Pclass','SibSp','Survived')
df4.show()
df3=StringIndexer(inputCol='Sex',outputCol='Gender').fit(df3).transform(df3)
df3=df3.drop('Sex')
df3.show()

df4.count()
df5=df2.filter(df2.Age>20).select('Pclass','SibSp','Survived')
df5.count()
df3=df3.select(df3.Pclass.cast('double'),df3.SibSp.cast('double'),df3.Survived.cast('double'),df3.Fare.cast('double'))
df3.printSchema()
df3=VectorAssembler(inputCols=['Pclass','SibSp','Fare'],outputCol='Features').transform(df3)
df3.show()

dt1=DecisionTreeClassifier(featuresCol='Features',labelCol='Survived',maxDepth=10,impurity='entropy')
model=dt1.fit(df3)
model.depth
print(model.toDebugString)
