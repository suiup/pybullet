import tensorflow as tf
import numpy as np

x_data = np.random.rand(100).astype(np.float32) # 产生一堆数组
y_data = x_data * 0.1 + 0.3 # 又是一堆数组
print(x_data)
print(y_data)

Weights = tf.Variable(tf.random_uniform([1], -1.0, -1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y-y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
# 初始化所有 variables
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # Very important
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))



