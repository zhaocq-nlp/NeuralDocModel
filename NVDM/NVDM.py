# -*- coding: utf-8 -*-

import tensorflow as tf
import numpy
from collections import OrderedDict


class NVDModel:

    def __init__(self, n_input, n_latent, n_hidden_enc):
        # initialize network
        self.prng = numpy.random.RandomState()

        sigma_init = 0.01

        x = tf.placeholder(tf.float32, [None, n_input], name='input')

        # encoder
        # x->hidden layer
        W_xh = tf.Variable(tf.random_normal([n_input, n_hidden_enc],
                                             mean=0., stddev=sigma_init, dtype=tf.float32))
        b_xh = tf.Variable(tf.zeros([n_hidden_enc], dtype=tf.float32))
        # hidden layer -> latent variables (mu & log sigma^2)
        W_hmu = tf.Variable(tf.random_normal([n_hidden_enc, n_latent],
                                             mean=0., stddev=sigma_init, dtype=tf.float32))
        b_hsigma = tf.Variable(tf.zeros([n_latent], dtype=tf.float32))

        # decoder
        W_zx = tf.Variable(tf.random_normal([n_latent, n_input],
                                             mean=0., stddev=sigma_init, dtype=tf.float32))
        b_zx = tf.Variable(tf.zeros([n_input], dtype=tf.float32))

        # create functions
        h_encoder = tf.nn.relu(tf.mat_mul(x, W_xh) + b_xh)





        pass


