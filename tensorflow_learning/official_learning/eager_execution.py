import tensorflow as tf

tf.enable_eager_execution()

examples = tf.random_normal([10])
print(examples)