import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_text
import time

text_input = tf.constant(["(your text here)"])
print(text_input)
preprocessor = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
encoder_inputs = preprocessor(text_input)
encoder = hub.KerasLayer(
    "https://tfhub.dev/tensorflow/small_bert/bert_en_uncased_L-2_H-128_A-2/2",
    trainable=True)
s = time.perf_counter()
outputs = encoder(encoder_inputs)
print(time.perf_counter()-s)
pooled_output = outputs["pooled_output"]      # [batch_size, 512].
sequence_output = outputs["sequence_output"]  # [batch_size, seq_length, 512].
print(pooled_output)
print(sequence_output)