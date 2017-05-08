#!/usr/bin/python
#coding=utf-8
"""
@Author: Wyman Leung(terryLiang020@foxmail.com)
@time: 17/5/8 下午7:58
"""
import os.path
import sys
from gensim.models import word2vec

model_path = '../output/word2vec_train_output/wiki.zh.text.model'
if os.path.isfile(model_path) == False:
	print("no such model_path.")
	sys.exit(1)

showWord = '自由', '法治', '人权', '一国两制';

model = word2vec.Word2Vec.load(model_path)

for word in showWord:
	result = model.most_similar(word.decode('utf-8'), topn=10)
	print '\t\t\t'+word+'\t\t\t'
	for e in result:
		print e[0], e[1]
	print '\t\t\tend\t\t\t\n'