"""
Bag-of-words without N-gram
using tf-idf
"""
import data_helper
from textblob import TextBlob
import os
import math

file = "./20news-18828"
file_frequency = "./data_statistic_every"
file_tf_idf = "./data_tf_idf"
frequency = 0

def build_dic(path):
	dic_origin = data_helper.data_load(path)
	dic_split = data_helper.data_split(dic_origin)
	dic_re = data_helper.data_recover(dic_split, frequency)
	with open("./data/dict_" + str(frequency) + ".txt", "w+", encoding="utf-8") as output:
		for i in dic_re:
			output.write(str(i) + "\n")

# build_dic(file)

def load_dic():
	with open("./data/dict_50.txt", "r", encoding="utf-8") as load_dic:
		dic_word = dict()
		load_dic_now = load_dic.readlines()
		for index in range(len(load_dic_now)):
			dic_word[load_dic_now[index].replace("\n", "")] = index

		return dic_word


if __name__ == "__main__":

	"""
	数据分词，写入文件
	"""
	# data_origin = data_helper.data_load(file)
	# for key in data_origin.keys():
	# 	for i in data_origin[key]:
	# 		data_sp = TextBlob(str(i).strip().replace("\\n", ""))
	# 		with open("./data_split.txt", "a", encoding="utf-8") as output:
	# 			output.write(str(data_sp.words) + "\n")

	dic = load_dic()
	index = 0
	# print(dic.keys())
	dic_frequency = dict()
	dic_tf_idf = dict()
	with open("./data/word_frequency_all.txt", "r", encoding="utf-8") as frequency:
		frequency = frequency.readlines()
		for i in frequency:
			j = i.split(":")
			dic_frequency[j[0]] = int(j[1])

	files = os.listdir(file_frequency)
	for file in files:
		file_list = os.listdir(file_frequency + "/" + file)
		os.mkdir(file_tf_idf + "/" + file)
		for file_text in file_list:
			with open(file_frequency + "/" + file + "/" + file_text, "r", encoding="utf-8") as frequency_every:
				length = 0
				frequency_every = frequency_every.readlines()
				for i in frequency_every:
					if len(i) < 2:continue
					j = i.split(":")
					length += int(j[1])
				# print(length)
				print(file_frequency + "/" + file + "/" + file_text)
				for i in frequency_every:
					if len(i) < 2: continue
					j = i.split(":")
					tf = float(j[1])/length
					idf = math.log(18828/(dic_frequency[j[0]]+1))
					dic_tf_idf[j[0]] = tf*idf
			with open(file_tf_idf + "/" + file + "/" + file_text, "a", encoding="utf-8") as output:
				for key in dic_tf_idf.keys():
					output.write(key + ":" + str(dic_tf_idf[key])+ "\n")







