#!/usr/bin/python
#coding=utf-8
"""
@Author: Wyman Leung(terryLiang020@foxmail.com)
@time: 17/5/8 下午3:34
"""

import logging
import os
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':

    input_corpus_path = '../output/wiki.zh.seg.utf.txt'
    output_model_path = '../output/word2vec_train_output/wiki.zh.text.model'
    output_vector_path = '../output/word2vec_train_output/wiki.zh.text.vector'

    logger = logging.getLogger(os.path.basename(__file__))
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(os.path.basename(__file__)))
    logger.info("input_corpus_path: %s" % input_corpus_path)
    logger.info("output_model_path: %s" % output_model_path)
    logger.info("output_vector_path: %s" % output_vector_path)

    model = Word2Vec(LineSentence(input_corpus_path), size=25, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    # trim unneeded model memory = use(much) less RAM
    # model.init_sims(replace=True)
    model.save(output_model_path)
    model.wv.save_word2vec_format(output_vector_path, binary=False)
