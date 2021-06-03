import tensorflow as tf

# 开始一个交互式会话，以便得到计算结果：
sess = tf.InteractiveSession()

# Define a 5x5 Identity matrix

I_matrix = tf.eye(5)
print(I_matrix.eval())


# Define a Variable initialized to a 10x10 identity matrix
X = tf.Variable(tf.eye(10))
X.initializer.run()
print(X.eval())

# create a random 5 x 10 matrix
A = tf.Variable(tf.random_normal([5, 10]))
A.initializer.run()
print(A.eval())

# Multiply two matrices
product = tf.matmul(A, X)
print("product",product.eval())

# create a random matrix of 1s and 0s, size 5x10
b = tf.Variable(tf.random_uniform([5,10], 0, 2, dtype=tf.int32))
b.initializer.run()
print("b",b.eval())
# Cast to float32 data type
b_new = tf.cast(b, dtype=tf.float32)

# Add the two matrices
t_sum = tf.add(product, b_new)
t_sub = product - b_new
print("A * X _b\n", t_sum.eval())
print("A * X _b\n", t_sub.eval())

# 所有加法、减、除、乘（按元素相乘）、取余等矩阵的算术运算都要求两个张量矩阵是相同的数据类型，否则就会产生错误。
# 可以使用 tf.cast() 将张量从一种数据类型转换为另一种数据类型




























