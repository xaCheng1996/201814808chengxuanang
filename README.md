# Data Mining Homework

--Data Mining project from SDU= =

开发日志已经迁移。

### 任务1：KNN

核心程序文件有两个:

KNN.py

Vector_space_model.py

KNN包含相似度计算、分类和acc计算

Vector_space_model包含向量空间构建。

辅助文件一个：

Inverted_index.py

Inverted_index.py主要用于将原始数据转化为倒排索引格式，原始数据见开发日志分享的谷歌云链接。

运行方式：

`python3 KNN.py`

`（保证data_tf_idf_inverted文件夹与KNN.py在同目录）`

正确率：0.7408885341846235（2785/3759）

### 任务二：朴素贝叶斯分类器

辅助文件一个：

data_helpers.py

主文件一个：

Naive_Bayes.py

需要的词频数据基本都在上一个任务里完成了，这里只需要做一点小的归纳即可。

运行方式：

`python3 Naive_Bayes.py`

正确率：True/all = 2984/3759   0.7938281457834531

### 

## 任务三：聚类

基于sklearn、gensim进行的聚类测试。

首先使用gensim自带的corpora模块将tweets.txt转化为字典信息，随后调用gensim的TfidfModel方法直接计算词语的tf-idf值。

考虑为了精度使用word2vec，但是word2vec将每一个sample都转化为一个矩阵，sklearn提供的方法不支持矩阵输入作为sample的值，因此搁置。

使用NML作为结果的衡量标准，NML的具体解释可以看这里：

https://blog.csdn.net/gao1440156051/article/details/44343003

对于计算出的tf-idf值，直接调用sklearn中的相关方法进行计算，结果如下：

```
NML of KMeans:0.7703183779505454

NML of AffinityPropagation:0.6946841230646935

NML of MeanShift:0.7265625

NML of SpectralClustering:0.6445844502850135

NML of Ward hierarchical clustering:0.7618074723654134

NML of DBSCAN:0.10801213485085728

NML of GaussianMixture:0.709565553655379

```

