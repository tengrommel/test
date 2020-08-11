# 深度学习是什么
- 卷积审计网络
- 循环神经网络

# 神经网络

- 机器学习简介
    - 机器学习是什么---无序数据转化为价值的方法
    - 机器学习价值 --- 从数据中抽取规律,并用来预测未来
    - 机器学习应用举例
        - 分类问题 --- 图像识别、垃圾邮件识别
        - 回归问题 --- 股价预测、房价预测
        - 排序问题 --- 点击率预估、推荐
        - 生成问题 --- 图像生成、图像风格转换、图像文字描述生成
    - 机器学习岗位职责
        - 数据处理（采集+去噪）
        - 模型训练（特征+模型）
        - 模型的评估和优化(MSE、F1-score、AUC+调参)
        - 模型应用(A/B测试)
- 深度学习简介
    - 深度学习与机器学习
        - 机器学习是实现人工智能的方法
        - 深度学习是实现机器学习算法的技术
    - 深度学习算法合集
        - 卷及神经网络
        - 循环神经网络
        - 自动编码器
        - 稀疏编码
        - 深度信念网络
        - 限制波尔兹曼机
        - 深度强化学习 = 深度学习 +　强化学习
- 神经网络
    - 神经元
    - 逻辑回归模型
    - 神经网络训练
        - 随机梯度下降
            - 每次只使用一个样本
        - Ｍini-Batch梯度下降
            - 每次使用小部分数据进行训练
            - 梯度下降存在震荡的问题
            - 梯度下降存在局部极值和saddle point的问题
        - 动量梯度下降
- Tensorflow基础
    - 神经元的Tensorflow实现
    - 神经网络的Tensorflow实现
- 神经网络Tensorflow实战

# DATA Container

- list
- np.array
- tf.Tensor

# What's Tensor

- scalar: 1.1
- vector: [1.1], [1.1, 2.2,...]
- matrix: [[1.1,2.2], [3.3, 4.4], [5.5, 6.6]]
- tensor: rank>2

TF is a computing lib

- int float double
- bool
- string

# outline

- from numpy, list
- zeros, ones
- fill
- random
- constant
- Application

# Scalar

- loss = mse(out, y)
- accuracy

#　索引与切片

Indexing
    
   - Basic indexing
       - [idx][idx][idx]
   - Same with Numpy
   - [idx, idx, ...]
   - start:end
   - start:end:step
   
# 维度变换

- shape, ndim
- reshape
- expand_dims/squeeze
> 增加和减少维度
- transpose
- broadcast_to
    - expand
    - without copying data
    - tf.broadcast_to
    
how to understand?

- When it has no axis
    - Create new concept
    - [classes, students, score] + [scores]
- When it has dim of size 1
    - Treat it shared by all
    - [classes, students, scores] + [students, 1]
    
# 排序

- Sort/argsort
- Topk
- Top-5 Acc

# 全连接层

out=f(X@W+b)

# Layers

- input
- hidden
- output

# Multi-Layers

    keras.Sequential([layer1, layer2, layer3])


# y  R

- linear regression
- naive classification with MSE
- other general prediction
- out = relu(X@W + b)
    - logits

# y 0,1
    
- binary classification
- Image Generation


函数

- out = relu(X@W+b)
- sigmoid

# 误差计算

# 梯度下降

- 导数
- 偏微分
- 梯度

# Typical Loss