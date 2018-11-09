import numpy as np
import os


def Naive_bayes():
	data_path = str(os.path.abspath(os.path.dirname(os.getcwd())))
	data_path += "/" + "data_statistic_every"
	data_name = os.listdir(data_path)
	True_cnt = 0
	all_cnt = 0
	for class_name in data_name:
		data_class_name = data_path + '/' + class_name
		data_class_index = os.listdir(data_class_name)
		length_train = int(len(data_class_index)*0.8)
		for i in range(int(len(data_class_index)*0.2)):
			word_list = []
			with open(data_class_name+'/'+data_class_index[i+length_train]) as test:
				# print('The class of this file is: '+ class_name)
				test_input = test.readlines()
				for j in test_input:
					# print(j)
					if len(j.strip('\n').split(':')) < 2:continue
					word, time = j.strip('\n').split(':')
					if int(time) >= 1:
						word_list.append(word)

			class_path = './data/class'
			class_div = os.listdir(class_path)
			Probi = -1000000
			class_re = ''
			for i in class_div:
				dic_class = dict()
				with open(class_path+'/'+i, 'r', encoding='utf-8') as train:
					train_read = train.readlines()
					for j in train_read:
						if len(j.strip('\n').split(':')) < 2: continue
						word, pro = j.strip("\n").split(":")
						dic_class[word] = float(pro)
					pro_1 = 1
					for k in word_list:
						# print(k)
						pro_1 = pro_1+dic_class[k]
					pro_1  = pro_1+(float(len(data_class_index))/18828)
					if pro_1 > Probi:
						Probi = pro_1
						class_re = i

			# print('The class recognized by Naive Bayes is: '+class_re)
			if class_re == class_name+'.txt':
				# print("Resule is True.")
				True_cnt+=1
				all_cnt+=1
			else:
				# print("Result is False")
				all_cnt+=1
			# print('Probility is: ' + str(Probi))
			# print('True/all = '+str(True_cnt)+'/'+str(all_cnt)+'   '+str(float(True_cnt)/all_cnt) +'\n')
			if all_cnt % 100 == 0:
				print('True/all = ' + str(True_cnt) + '/' + str(all_cnt) + '   ' + str(float(True_cnt) / all_cnt) + '\n')
		print('True/all = ' + str(True_cnt) + '/' + str(all_cnt) + '   ' + str(float(True_cnt) / all_cnt) + '\n')

Naive_bayes()