# from absl import logging

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

import tensorflow_hub as hub
import sentencepiece as spm
import numpy as np
import os
import re

class WordEmbedder:
    def __init__(self) :
        module = hub.Module("https://tfhub.dev/google/universal-sentence-encoder-lite/2")

        self.input_placeholder = tf.sparse_placeholder(tf.int64, shape=[None, None])
        self.encodings = module(
            inputs=dict(
                values=self.input_placeholder.values,
                indices=self.input_placeholder.indices,
                dense_shape=self.input_placeholder.dense_shape))

        self.sess = tf.Session()
        
        spm_path = self.sess.run(module(signature="spm_path"))

        self.sp = spm.SentencePieceProcessor()
        with tf.io.gfile.GFile(spm_path, mode="rb") as f:
            self.sp.LoadFromSerializedProto(f.read())

        self.sess.run([tf.global_variables_initializer(), tf.tables_initializer()])
        
    def process_to_IDs_in_sparse_format(self, sentences):
        # An utility method that processes sentences with the sentence piece processor
        # 'sp' and returns the results in tf.SparseTensor-similar format:
        # (values, indices, dense_shape)
        ids = [self.sp.EncodeAsIds(x) for x in sentences]
        max_len = max(len(x) for x in ids)
        dense_shape=(len(ids), max_len)
        values=[item for sublist in ids for item in sublist]
        indices=[[row,col] for row in range(len(ids)) for col in range(len(ids[row]))]
        return (values, indices, dense_shape)

    def get_embedding(self, messages:[str]) :
        values, indices, dense_shape = self.process_to_IDs_in_sparse_format(messages)

        message_embeddings = self.sess.run(
            self.encodings,
            feed_dict={self.input_placeholder.values: values,
                        self.input_placeholder.indices: indices,
                        self.input_placeholder.dense_shape: dense_shape})
        
        return message_embeddings


# we = WordEmbedder()
# out = we.get_embedding(['Generate words', 'Generate me words', 'THis sucks', 'generate me phrases'])
# print(np.inner(out[0],out[1]))
# print(np.inner(out[0],out[2]))
# print(np.inner(out[0],out[3]))
