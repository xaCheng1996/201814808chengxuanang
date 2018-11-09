"""
1、读取单词频率
2、计算各类中的概率
"""
import os
import numpy as np
import data_statistic_every

def frequency_all_load():
	with open('./data/word_frequency_all.txt', 'r', encoding='utf-8') as input:
		input_read = input.readlines()
		word_list = []
		index_list = []
		for i in input_read:
			word, index = str(i).strip("\n").split(':')
			word_list.append(word)
			index_list.append(index)

		return word_list, index_list


def frequency_class_load(class_name):
	# print(os.path.abspath(os.path.dirname(os.getcwd())))
	data_path = str(os.path.abspath(os.path.dirname(os.getcwd())))
	data_path += "/" + "data_statistic_every" + '/' + class_name
	data_name = os.listdir(data_path)
	# print(data_name)
	dic_word = dict()
	time_all = 0
	for index_na in range(int(len(data_name)*0.8)):
		index = data_name[index_na]
		with open(data_path+'/'+index, 'r', encoding='utf-8') as input:
			input_read = input.readlines()
			for i in range(int(len(input_read))):
				if len(str(input_read[i]).strip('\n').split(':')) < 2:continue
				word, time = str(input_read[i]).strip('\n').split(':')
				# print(word)
				# print(time)
				time_all += int(time)
				if dic_word.get(word) is None:
					dic_word[word] = int(time)
				else:
					dic_word[word] += int(time)
	print(time_all)
	find_all = 0
	with open('./data/class/' + class_name + '.txt', 'w', encoding='utf-8') as output:
		for key in dic_word.keys():
			# print(key + str(dic_word[key]))
			find_all += dic_word[key]
			output.write(key+':'+str(np.log((dic_word[key]+1)/(time_all+7833)))+'\n')
		print(find_all)

data_path = str(os.path.abspath(os.path.dirname(os.getcwd())))
data_path += "/" + "data_statistic_every"
data_name = os.listdir(data_path)
for i in data_name:
	frequency_class_load(i)