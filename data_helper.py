import os
from textblob import TextBlob
from textblob import Word
def data_load(path):
	"""
	:param path: path of document
	:return: dict(),dict[category]:list[]
	"""
	index = 0
	files = os.listdir(path)
	dic_data = dict()
	for file in files:
		file_list = os.listdir(path + "/" +file)
		list = []
		for file_txt in file_list:
			# print(path + "/" + file + "/" + file_txt)
			data = open(path + "/" + file + "/" + file_txt,'r',encoding="ISO-8859-1")
			data_output = data.readlines()
			data_output = str(data_output).lower()
			index += 1
			list.append(data_output)
		# print(list)
		dic_data[file] = list
			# for i in data_output:
			# 	print(i)
	# print(index)
	return dic_data
# dic = data_load("./20news-18828")

def data_split(data):
	"""
	:param data: data from data_load
	:return: 分词后的数据
	"""
	index = 0
	for key in data.keys():
		data_now = data[key]
		senten = TextBlob(str(data_now).replace("\\\\n", "").replace("\\\\t", "").replace("\\","").replace("'",""))
		data[key] = senten.words
		index += 1
		print(index)
		# print(data[key])
	return data
# data_split(dic)

def data_recover(data, frequency):
	"""
	:param data:  data from data_slpit
	:return: set
	"""
	index = 0
	s = set()
	dic = dict()
	for key in data.keys():
		data_now = data[key]
		for i in data_now:
			w = Word(i)
			w.lemmatize()
			w.lemmatize('v')
			# print(w)
			if index%100 == 0:
				print(str(index) + " " +w)
			if dic.get(w) is not None:
				dic[w] += 1
			else:
				dic[w] = 1
			if w not in s and dic[w] >= frequency:
				index += 1
				s.add(w)
		print(len(s))
	return s