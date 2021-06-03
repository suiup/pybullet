import tensorflow as tf

cons01 = tf.constant([[3]])
cons02 = tf.constant([[5]])
cons3 = tf.matmul(cons01, cons02)

with tf.Session() as sess:
    result = sess.run(cons01)
    result2 = sess.run(cons02)
    print(result)
    print(result2)
    result3 = sess.run(cons3)
    print(result3)

