import os
import math
import copy
import numpy as np

file = "./data_tf_idf_inverted"
per = 0.1

def distance_compute(data_train, data_test):
	distance = 0
	train_vec = np.array(data_train)
	test_vec  = np.array(data_test)
	for i in range(len(data_train)):
		distance  += (data_train[i] - data_test[i]) * (data_train[i] - data_test[i])
	distance = math.sqrt(distance)
	return distance

def distance_compute_cos(data_train, data_test):
	son = 0
	mother_l = 0
	mother_r = 0
	train_vec = np.array(data_train)
	test_vec = np.array(data_test)
	# for i in range(len(data_train)):
	# 	son += data_train[i] * data_test[i]
	# 	mother_l += data_test[i]*data_test[i]
	# 	mother_r += data_train[i]*data_train[i]

	# print('mother_l:' + str(mother_l))
	# print('mother_r:' + str(mother_r))
	# mother_l = math.sqrt(mother_l)
	# mother_r = math.sqrt(mother_r)
	distance  = np.dot(train_vec, test_vec)/(np.linalg.norm(train_vec)*(np.linalg.norm(test_vec)))
	return distance

def data_expansion(dic_train, dic_test):
	list_train_new = []
	list_test_new = []
	dic_train_new = dict()
	dic_test_new = dict()

	for key in dic_train.keys():
		if dic_train_new.get(key) is None:
			dic_train_new[key] = dic_train[key]
	for key in dic_test.keys():
		if dic_train_new.get(key) is None:
			dic_train_new[key] = 0

	for key in dic_test.keys():
		if dic_test_new.get(key) is None:
			dic_test_new[key] = dic_test[key]
	for key in dic_train.keys():
		if dic_test_new.get(key) is None:
			dic_test_new[key] = 0

	dic_train_new = sorted(dic_train_new.items(), key=lambda x:x[0])
	dic_test_new = sorted(dic_test_new.items(), key=lambda x: x[0])
	# print(dic_train_new[100][1])
	# print(dic_test_new[100][1])
	for index in range(len(dic_train_new)):
		list_train_new.append(dic_train_new[index][1])
		list_test_new.append(dic_test_new[index][1])
	# print(list_test_new[50])
	# print(list_train_new[50])
	return list_train_new, list_test_new

def similarity_compute(path, per, dic_test, dic_file_train):
	dic = dict()
	files = os.listdir(path)
	index = 0
	# for file in files:
	# 	file_list = os.listdir(path + "/" + file)
	# 	data_len = int(per*len(file_list))
	# 	for i in range(len(file_list) - data_len):
	# 		file_now = path + "/" + file + "/" + file_list[(i + data_len)]
	#
	# 		with open(file_now, "r", encoding="utf-8") as data_train:
	# 			data_train = data_train.readlines()
	# 			dic_train = dict()
	# 			for i in data_train:
	# 				if(len(i.split(":")) < 2):continue
	# 				dic_train[i.split(":")[0]] = float(i.split(":")[1])
				# if (index != 0): break
				# print(len(dic_train))
				# print(file_now)
	for key in dic_file_train.keys():
		dic_train = dict()
		for i in dic_file_train[key]:
			if(len(i.split(":")) < 2):continue
			dic_train[i.split(":")[0]] = float(i.split(":")[1])
		list_train_new, list_test_new = data_expansion(dic_train, dic_test)
		# print(len(dic_test))
		# print(len(list_test_new))
		distance = distance_compute_cos(list_train_new, list_test_new)
		index += 1
		if index %5000==0:
			print(index)
		# print(file_now)
		key_file = key
		dic[key_file] = distance
	return dic


def KNN(path, per, k):
	files = os.listdir(path)
	index = 0
	index_right = 0

	dic_file_train = dict()
	for file in files:
		file_list = os.listdir(path + "/" + file)
		data_len = int(per*len(file_list))
		for i in range(len(file_list) - data_len):
			file_now = path + "/" + file + "/" + file_list[(i + data_len)]
			dic_test = dict()
			with open(file_now, "r", encoding="utf-8") as data_test:
				data_test = data_test.readlines()
				dic_file_train[file_now] = data_test


	for file in files:
		file_list = os.listdir(path + "/" + file)
		data_len = int(per*len(file_list))
		for i in range(data_len):
			file_final = path + "/" + file + "/" + file_list[i]
			dic_test = dict()
			with open(file_final, "r", encoding="utf-8") as data_test:
				data_test = data_test.readlines()
				for i in data_test:
					if (len(i.split(":")) < 2): continue
					dic_test[i.split(":")[0]] = float(i.split(":")[1])
			# if(index != 0):break
			dic =  similarity_compute(path, 0.1, dic_test,dic_file_train)
			dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
			print(file_final)
			score = 0
			index += 1
			print(index)
			dic_re = dict()
			for i in range(k):
				# print(dic[i])
				# print(dic[i][0].split("/")[2])
				# print(file_final.split("/")[2])
				# if dic[i][0].split("/")[2] == file_final.split("/")[2]:
				# 	score += 1
				if dic_re.get(dic[i][0].split("/")[2]) is None:
					dic_re[dic[i][0].split("/")[2]] = 1
				else:
					dic_re[dic[i][0].split("/")[2]] += 1
			dic_re = sorted(dic_re.items(), key=lambda x:x[1], reverse=True)
			print(dic_re)
			if dic_re[0][0] == file_final.split("/")[2]:
				index_right += 1
			print(index_right)
			# print(score)
		# 	with open("./result/KNN.txt", "a", encoding="utf-8") as output:
		# 		output.write("The test id: " + str(index) + ", category is :" + file_final + "\n")
		# 		for i in range(k):
		# 			output.write(dic[i][0] + " " + str(dic[i][1]) +  "\n")
		# 		if score >= k/2:
		# 			output.write("The result of KNN is True\n")
		# 			index_right += 1
		# 		else:
		# 			output.write("wrong answer\n")
		# 		output.write("\n")
		# with open("./result/KNN.txt", "a", encoding="utf-8") as output:
		# 	output.write("the acc is:" + str(index_right/index))

		print("the acc is:" + str(index_right/index))

if __name__ == "__main__":
	KNN(file, 0.2, 10)



