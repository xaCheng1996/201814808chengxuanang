"""
主将tf-idf的文件以倒排索引方式存储，并检测停用词
"""
import os

path = './data_tf_idf'
path_new = './data_tf_idf_inverted'
files = os.listdir(path)

for file in files:
	file_list = os.listdir(path + '/' + file)
	for file_text in file_list:
		with open(path + '/' + file + '/' + file_text, "r", encoding='utf-8') as input:
			input = input.readlines()
			with open('./data/stopword.txt','r',encoding='utf-8') as stopword:
				stopword = stopword.readlines()
				dic_stop = dict()
				for i in dic_stop:
					dic_stop[str(i).replace("\n", "")] = 1

				for index in range(len(input)):
					j = input[index].replace("\n", "").split(":")
					if float(j[1]) > 0 and dic_stop.get(j[0]) is None:
						if os.path.exists(path_new + '/' + file) is False:
							os.mkdir(path_new + '/' + file)
						with open(path_new + '/' + file + '/' + file_text, 'a', encoding='utf-8') as output:
							output.write(j[0] + ':' + j[1] + '\n')
