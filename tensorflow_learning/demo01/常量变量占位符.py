import tensorflow as tf

# 常量是其值不能改变的张量。
# 变量：当一个量在会话中的值需要更新时，使用变量来表示。
#   例如，在神经网络中，权重需要在训练期间更新，可以通过将权重声明为变量来实现。
#   变量在使用前需要被显示初始化。另外需要注意的是，常量存储在计算图的定义中，每次加载图时都会加载相关变量。
#   换句话说，它们是占用内存的。另一方面，变量又是分开存储的。它们可以存储在参数服务器上。

# 占位符：用于将值输入 TensorFlow 图中。
# 它们可以和 feed_dict 一起使用来输入数据。
# 在训练神经网络时，它们通常用于提供新的训练样本。在会话中运行计算图时，可以为占位符赋值。
# 这样在构建一个计算图时不需要真正地输入数据。需要注意的是，占位符不包含任何数据，因此不需要初始化它们。



# TensorFlow 常量
t_1 = tf.constant(4)

t_2 = tf.constant([4,3,2])

t_3 = tf.zeros([2,3])

t_4 = tf.zeros_like(t_3)
#创建一个形如 [M，N]、元素均为 1 的矩阵
t_5 = tf.ones([2,3])
# tf.linspace(start,stop,num)  从初值到终值等差排布的序列
t_6 = tf.linspace(2.0, 5.0, 5)

# 从开始（默认值=0）生成一个数字序列，增量为 delta（默认值=1），直到终值（但不包括终值) tf.range(start,limit,delta)
t_7 = tf.range(10)


# TensorFlow 允许创建具有不同分布的随机张量：
# 1. 使用以下语句创建一个具有一定均值（默认值=0.0）和标准差（默认值=1.0）、形状为 [M，N] 的正态分布随机数组：
t_random01 = tf.random_normal([2,3], mean=2.0, stddev=4, seed=12)

# 2. 创建一个具有一定均值（默认值=0.0）和标准差（默认值=1.0）、形状为 [M，N] 的截尾正态分布随机数组：
t_random02 = tf.truncated_normal([1,5], stddev=2, seed=12)


# 3. 要在种子的 [minval（default=0），maxval] 范围内创建形状为 [M，N] 的给定伽马分布随机数组，请执行如下语句：
t_random03 = tf.random_uniform([2,3], maxval=4, seed=12)


# 4. 要将给定的张量随机裁剪为指定的大小，使用以下语句：
t_random04 = tf.random_crop(t_random03, [2,5], seed=12)
#  很多时候需要以随机的顺序来呈现训练样本 tf.random_shuffle() 来沿着它的第一维随机排列张量
tf.random_shuffle(t_random03)

# 随机生成的张量受初始种子值的影响。要在多次运行或会话中获得相同的随机数，应该将种子设置为一个常数值。
# 当使用大量的随机张量时，可以使用 tf.set_random_seed() 来为所有随机产生的张量设置种子。以下命令将所有会话的随机张量的种子设置为 54：
tf.set_random_seed(54)




# TensorFlow 变量

# 它们通过使用变量类来创建

rand_t = tf.random_uniform([50, 50], 0, 10, seed=0)
t_a = tf.Variable(rand_t)
t_b = tf.Variable(rand_t)
# 注意：变量通常在神经网络中表示权重和偏置。


# 下面的代码中定义了两个变量的权重和偏置。
# 权重变量使用正态分布随机初始化，均值为 0，标准差为 2，权重大小为 100×100。
# 偏置由 100 个元素组成，每个元素初始化为 0。在这里也使用了可选参数名以给计算图中定义的变量命名：
weights = tf.Variable(tf.random_normal([100, 100], stddev=2))
bias = tf.Variable(tf.zeros[100], name='biases')

# 在前面的例子中，都是利用一些常量来初始化变量，也可以指定一个变量来初始化另一个变量。下面的语句将利用前面定义的权重来初始化 weight2：
weights2 = tf.Variable(weights.initial_value(), name='w2')


# 变量的定义将指定变量如何被初始化，但是必须显式初始化所有的声明变量。在计算图的定义中通过声明初始化操作对象来实现：
initial_op = tf.global_variables_initializer()

# 每个变量也可以在运行图中单独使用 tf.Variable.initializer 来初始化：
# bias = tf.Variable(tf.zeros([100, 100]))
# with tf.Session as sess:
#     sess.run(bias.initializer)

saver = tf.train.Saver



# TensorFlow 占位符
# 介绍完常量和变量之后，我们来讲解最重要的元素——占位符，它们用于将数据提供给计算图。
# 可以使用以下方法定义一个占位符：
# tf.placeholder(dtype,shape=None,name=None)
# dtype 定占位符的数据类型，并且必须在声明占位符时指定。在这里，为 x 定义一个占位符并计算 y=2*x，使用 feed_dict 输入一个随机的 4×5 矩阵
x = tf.placeholder("float")
y = 2 * x
data = tf.random_uniform([4, 5], 10)
with tf.Session() as sess:
    x_data = sess.run(data)
    print(sess.run(y, feed_dict={x: x_data}))


















