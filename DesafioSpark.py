#import findspark
#findspark.init()

from pyspark import SparkContext,SparkConf
from pyspark.sql import SQLContext
from  pyspark.sql import types
from pyspark.sql.functions import sum,col

conf = SparkConf().setAppName('NASAKennedySpaceCenter').setMaster('local')
sc = SparkContext(conf=conf)
sqlContext = SQLContext(sc)


def readTxt(stringDelimiter,pathFile): 
    df = sqlContext.read.format('com.databricks.spark.csv').options(delimiter= stringDelimiter).options(inferSchema=True).load(pathFile)
    return df

def returnDF():
    july = readTxt(' ','')
    aug  = readTxt(' ','')
    df= july.union(aug)
    df = df.withColumn('bytes', df['_c7'].cast(types.LongType()))
    df = df.selectExpr('_c0 AS host','SUBSTRING(_c3,2,11) as dataRequisicao','_c5 AS Requisicao','_c6 AS CodigoHTTP','bytes')
    return df.cache()

df = returnDF()

def returnErros404():
    return df.filter(df['CodigoHTTP'] == 404)

#1. Número de hosts únicos
df.select(df['host']).distinct().count()

#2. Total de erros 404
returnErros404().count()

#3. Os 5 URLs que mais causaram erro 404
returnErros404().select(df['Requisicao']).groupBy(df['Requisicao']).count().sort(col('count').desc()).show(5,truncate = False)

#4. Quantidade de erros 404 por dia
returnErros404().select(df['dataRequisicao']).groupBy(df['dataRequisicao']).count().sort(col('count').desc()).show()

#5. O total de bytes retornados
df.select(sum(df['bytes'])).show()

