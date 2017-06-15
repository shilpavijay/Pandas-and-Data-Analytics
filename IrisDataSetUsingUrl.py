from sklearn import datasets
import pandas as pd
import urllib

iris = datasets.load_iris()
# print(iris.DESCR)


#Importing datasets using a URL and handling large datasets:

Url = "http://aima.cs.berkeley.edu/data/iris.csv"
urlRequest = urllib.request.Request(Url)
iris_file = urllib.request.urlopen(urlRequest)

iris_fromUrl = pd.read_csv(iris_file,sep=',',header=None,decimal='.',names=['sep_len','sep_width','petal_len','petal_width','target'])
print(iris_fromUrl.head())


#Handling large datasets in chunks: (iterator=True)
iris_fromUrl_iter = pd.read_csv(iris_file,sep=',',header=None,decimal='.',names=['sep_len','sep_width','petal_len','petal_width','target'],iterator=True)
print(iris_fromUrl_iter.get_chunk(5).shape)