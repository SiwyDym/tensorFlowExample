import tensorflow as tf
# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
sess = tf.Session()


hello = tf.constant("Hello World")
print(sess.run(hello))

a = tf.constant(20)
b = tf.constant(22)

print('a + b = {0}'.format(sess.run(a + b)))