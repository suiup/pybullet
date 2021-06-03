import tensorflow as tf

Weights = tf.Variable(tf.random_uniform((4,3), -1.0, -1.0))

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(Weights))
