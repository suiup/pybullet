import tensorflow as tf

# 定义了一个常量字符串
message = tf.constant('Hello world')
with tf.Session() as sess:
    print(sess.run(message).decode())