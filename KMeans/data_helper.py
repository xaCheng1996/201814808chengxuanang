import json
import pickle
import os
import numpy as np
def vocab_build(vocab_path, data, min_count):
	"""

	:param vocab_path:
	:param corpus_path:
	:param min_count:
	:return:
	"""
	word2id = {}
	for sent_ in data:
		for word in sent_:
			if word not in word2id:
				word2id[word] = [len(word2id)+1, 1]
			else:
				word2id[word][1] += 1
	low_freq_words = []
	for word, [word_id, word_freq] in word2id.items():
		if word_freq < min_count and word != '<NUM>' and word != '<ENG>':
			low_freq_words.append(word)
	for word in low_freq_words:
		del word2id[word]


	new_id = 1
	for word in word2id.keys():
		word2id[word] = new_id
		new_id += 1
	word2id['<UNK>'] = new_id
	word2id['<PAD>'] = 0

	# print(len(word2id))
	with open(vocab_path, 'wb') as fw:
		pickle.dump(word2id, fw)


def read_dictionary(vocab_path):
	"""

	:param vocab_path:
	:return:
	 """
	vocab_path = os.path.join(vocab_path)
	with open(vocab_path, 'rb') as fr:
		word2id = pickle.load(fr)
	print('vocab_size:', len(word2id))
	return word2id


def random_embedding(vocab, embedding_dim):
	"""

	:param vocab:
	:param embedding_dim:
	:return:
	"""
	embedding_mat = np.random.uniform(-0.25, 0.25, (len(vocab), embedding_dim))
	embedding_mat = np.float32(embedding_mat)
	return embedding_mat

def json_read(file):
	with open(file, 'r', encoding='utf-8') as read:
		list = []
		input = read.readlines()
		for i in input:
			data = json.loads(i)
			list.append(str(data['text']).split())
		# vocab_build('word2id.pkl', list, min_count=1)

	return list
# data = json_read('./Tweets.txt')
# word2id = read_dictionary('./word2id.pkl')
# for i in word2id:
# 		print(i)