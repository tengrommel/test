import tensorflow as tf

w = tf.Variable(1.0)
b = tf.Variable(2.0)
x = tf.Variable(3.0)

with tf.GradientTape() as t1:
    with tf.GradientTape() as t2:
        y = x * w + b
    dy_dw, dy_db = t2.gradient(y, [w, b])
d2y_d2w = t1.gradient(dy_dw, w)

print(dy_db)
print(dy_dw)
print(d2y_d2w)