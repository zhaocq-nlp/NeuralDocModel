# -*- coding: utf-8 -*-
from Parameter import *


class NVDMConfig(object):
    """
    Class for the configuration of the architecture of MLP.
    """
    def __init__(self, argv):
        '''
        initialize the configuration of NVDM
        :param argv: command line
        :return: None
        '''
        self.parameter = cmd_parser(argv)
        self.maxdf, self.freq_words, self.mode, self.data, self.vocabulary, \
            self.n_latent, self.n_hidden_enc, self.n_hidden_dec = self.parse()


    def parse(self):

        maxdf = self.parameter.getfloat('maxdf', 0.95)
        freq_words = self.parameter.getint('freq_words', 2000)
        mode = self.parameter.get('mode')
        data = self.parameter.get('data')
        vocabulary = self.parameter.get('vocabulary', 'vocabulary')

        n_latent = self.parameter.get('n_latent')
        n_hidden_enc = self.parameter.get('n_hidden_enc')
        n_hidden_dec = self.parameter.get('n_hidden_dec')

        return maxdf, freq_words, mode, data, vocabulary, \
            n_latent, n_hidden_enc, n_hidden_dec

