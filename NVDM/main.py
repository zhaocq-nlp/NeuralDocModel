# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import TfidfVectorizer
from NVDMConfig import  NVDMConfig
from Preprocessing import Preprocessing
import sys
from NVDM import *


def save_vocabulary(vocab_file, vocabulary):
    fp = open(vocab_file, 'w')
    for term, id in vocabulary.iteritems():
        fp.write(term + ' ' + str(id) + '\n')
    fp.close()


if __name__ == "__main__":

    sys.argv = ['main.py', '-config', 'config.ini']

    config = NVDMConfig(sys.argv)
    preprocessing = Preprocessing(maxdf=config.maxdf, max_words=config.freq_words)
    x, vocab = preprocessing.fit(config.data)

    save_vocabulary(config.vocabulary, vocab)

    print 'Finish loading data'

    nvdm = NVDModel(n_input=x.shape[1],
                n_latent=config.n_latent,
                n_hidden_enc=config.n_hidden_enc)