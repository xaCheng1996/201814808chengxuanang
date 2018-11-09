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







