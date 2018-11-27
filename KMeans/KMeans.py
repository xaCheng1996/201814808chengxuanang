import numpy as np
import argparse, os
from KMeans.data_helper import read_dictionary
from KMeans.data_helper import random_embedding
from KMeans.data_helper import json_read

parser = argparse.ArgumentParser(description='BiLSTM-CRF for Chinese NER task')
parser.add_argument('--embedding_dim', type=int, default=128, help='dimension of embedding matrix')
args = parser.parse_args()

word2id = read_dictionary('./word2id.pkl')
for i in word2id:
		print(i)

embedding = random_embedding(word2id, args.embedding_dim)

