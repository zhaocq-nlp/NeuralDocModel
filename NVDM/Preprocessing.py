# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
import numpy


class Preprocessing:

    def __init__(self, maxdf=0.95, max_words=2000):
        self.maxdf = maxdf
        self.max_features = max_words


    def fit(self, data):
        doc = []
        fp = open(data, 'r')
        for line in fp:
            doc.append(line.strip())
        fp.close()
        doc = numpy.array(doc)

        count = CountVectorizer(max_df=self.maxdf, stop_words='english', max_features=self.max_features)
        count.fit(doc)
        return (count.transform(doc)>0).astype(numpy.float32), count.vocabulary_


