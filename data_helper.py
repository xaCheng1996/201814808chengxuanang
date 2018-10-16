"""
author:xaCheng
data_load:加载数据（按照输入的路径）, 由于编码方式的问题，其实是专门用于加载原始数据文件的
data_split:textblob自带的分词
data_recover:返回一个词典，格式是词语:词频，根据输入过滤词表
datas_statistics_all和data_statistics_every:统计所有文件和单个文件的词频，和recover的词典结合
"""
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


def data_statistic_all():
	"""
	:param data: 空
	:return: 不输出，统计文件的词频，文件存储
	"""
	file_frequency = "./data_statistic_every"
	with open("./data/dict_50.txt", "r", encoding="utf-8") as dictionary:
		dic = dict()
		for i in dictionary.readlines():
			j = i.replace("\n", "")
			dic[j] = 0
		index = 0
		files = os.listdir(file_frequency)
		for file in files:
			file_list = os.listdir(file_frequency + "/" + file)
			for file_text in file_list:
				with open(file_frequency + "/" + file + "/" + file_text, "r", encoding="utf-8") as frequency_every:
					frequency_every = frequency_every.readlines()
					for i in frequency_every:
						if len(i) < 2 :continue
						j = i.split(":")
						# print(j)
						if int(j[1]) > 0:
							dic[j[0]] += 1
				index += 1
				if index % 1000 == 0:
					print(index)

		with open("./data/word_frequency_all.txt", "a", encoding="utf-8") as output:
			for key in dic.keys():
				output.write(key + ":" + str(dic[key]) + "\n")

# data_statistic_all()


def data_statistic_every():
	"""
	:param data: 空
	:return: 不输出，统计文件的词频，文件存储
	"""
	with open("./data/dict_50.txt", "r", encoding="utf-8") as dictionary:
		dic = dict()
		for i in dictionary.readlines():
			j = i.replace("\n", "")
			dic[j] = 0

		path = "./20news-18828"
		files = os.listdir(path)

		os.mkdir("./data_statistic_every")
		dic_file = dict()
		index = 0
		for file in files:
			file_list = os.listdir(path + "/" +file)
			os.mkdir("./data_statistic_every/" + file)
			for file_txt in file_list:
				dic_file[index] =  "./data_statistic_every/" + file + "/" + file_txt
				index += 1

		index = 0
		with open("./data/data_split.txt", "r", encoding="utf-8") as data_split:
			data_sp = data_split.readlines()
			for i in data_sp:
				for key in dic.keys():
					dic[key] = 0
				for j in i.split(", "):
					j = j.replace("\"", "").replace("'", "").replace("]", "")
					# print(dic.get(j))
					if dic.get(j) is not None:
						dic[j] += 1
				with open(dic_file[index], "a",encoding="utf-8") as output:
					index += 1
					for key in dic.keys():
						output.write(key + ":" + str(dic[key]) + "\n")
					output.write("\n")

# data_statistic_every()