import numpy as np
import argparse, os
from KMeans_mod.data_helper import json_read
from sklearn.cluster import KMeans
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn.mixture import GaussianMixture
from sklearn import metrics as mr
from gensim import models
from gensim import corpora
from sklearn.externals import joblib

parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--embedding_dim', type=int, default=32, help='dimension of embedding matrix')
args = parser.parse_args()

data, labels = json_read('./Tweets.txt')
data_new = []
for i in data:
	while len(i) < 20:
		i.append('<PAD>')
	# print(i)
	data_new.append(i)
dictionary = corpora.Dictionary(data_new)
corpus = [dictionary.doc2bow(text) for text in data_new]
# print(corpus)
model = models.TfidfModel(corpus)
model.save("my_model.tfidf")

model = models.TfidfModel.load('my_model.tfidf')

tfidf_vec = []
for i in range(len(corpus)):
	string = corpus[i]
	string_tfidf = model[string]
	tfidf_vec.append(string_tfidf)
# print(tfidf_vec)

tf_idf = []
for i in tfidf_vec:
	li = [0]*5099
	for j in i:
		# print(j[0])
		if len(j) < 2:continue
		li[j[0]] = j[1]
	# while len(temp)<20:
	# 	temp.append(0)
	# print(li)
	tf_idf.append(li)
# wordvector = np.array(wordvector).reshape([2472,640])
tf_idf = (np.array(tf_idf))
# print(int(len(tf_idf)*0.8))
# train, val = tf_idf[:int(len(tf_idf)*0.8)], tf_idf[int(len(tf_idf)*0.8):]
# label_train, label_test = labels[:int(len(tf_idf)*0.8)], labels[int(len(tf_idf)*0.8):]

kmeans = KMeans(n_clusters=89)
s = kmeans.fit_predict(tf_idf)
print('NML of KMeans:' + str(mr.normalized_mutual_info_score(labels, s)))

Af = AffinityPropagation(preference=-50).fit_predict(tf_idf)
print('NML of AffinityPropagation:' + str(mr.normalized_mutual_info_score(labels, Af)))

ms = MeanShift(n_jobs=8).fit_predict(tf_idf)
print('NML of MeanShift:' + str(mr.normalized_mutual_info_score(labels, ms)))

sc = SpectralClustering(n_clusters=89).fit_predict(tf_idf)
print('NML of SpectralClustering:' + str(mr.normalized_mutual_info_score(labels, sc)))

ac = AgglomerativeClustering(n_clusters=89).fit_predict(tf_idf)
print('NML of Ward hierarchical clustering:' + str(mr.normalized_mutual_info_score(labels, ac)))

db = DBSCAN().fit_predict(tf_idf)
print('NML of DBSCAN:' + str(mr.normalized_mutual_info_score(labels, db)))
#
gm = GaussianMixture(n_components=10).fit_predict(tf_idf)
print('NML of GaussianMixture:' + str(mr.normalized_mutual_info_score(labels, gm)))