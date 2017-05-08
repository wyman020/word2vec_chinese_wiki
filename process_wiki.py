#!/usr/bin/python
#coding=utf-8
"""
@Author: Wyman Leung(terryLiang020@foxmail.com)
@time: 17/5/8 上午3:29
"""

from __future__ import print_function

import logging
import os.path

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    input_path = '../res/zhwiki-latest-pages-articles.xml.bz2'
    output_path = '../output/wiki.zh.txt'

    logger = logging.getLogger(os.path.basename(__file__))
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(os.path.basename(__file__)))
    logger.info("input_path: %s" % input_path)
    logger.info("output_path: %s" % output_path)

    i = 0
    output = open(output_path, 'w')
    wiki = WikiCorpus(input_path, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(' '.join(text) + "\n")
        i = i + 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")

    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
