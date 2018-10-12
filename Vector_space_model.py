"""
Bag-of-words without N-gram
"""
import data_helper
from textblob import TextBlob

file = "./20news-18828"
frequency = 0

def build_dic(path):
	dic_origin = data_helper.data_load(path)
	dic_split = data_helper.data_split(dic_origin)
	dic_re = data_helper.data_recover(dic_split, frequency)
	with open("./dict_" + str(frequency) + ".txt", "w+", encoding="utf-8") as output:
		for i in dic_re:
			output.write(str(i) + "\n")

# build_dic(file)

def load_dic():
	with open("./dict_50.txt", "r", encoding="utf-8") as load_dic:
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
	# print(dic.keys())
	with open("./data_split.txt", "r", encoding="utf-8") as data_sp:
		data_split = data_sp.readlines()
		for i in data_split:
			li = []
			for j in i.split(", "):
				j = j.replace("\"", "").replace("'", "").replace("]", "")
				# print(dic.get(j))
				if dic.get(j) is not None:
					li.append(dic.get(j))
			print(li)

