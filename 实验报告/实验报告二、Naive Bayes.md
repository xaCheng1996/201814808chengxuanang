# 实验报告二、Naive Bayes

### 实验介绍：

在实验一的基础上，采用实验一的数据集和相关数据，执行朴素贝叶斯算法。

### 数据集：

20news-18828

### 字典规模：

250K

过滤词频>=5，约为4W+

过滤词频>=15, 约为两万（19367）

过滤词频>=50,为7833

本实验以词频50为基准过滤

### 实验步骤：

#### 1、计算方式

针对每一篇文章，需要计算的是每篇文章的属于某一类的概率：
$$
p_i = \sum_{i=1}^{词数} {log(出现的每个词的概率p_m)}
$$
其中，
$$
p_m为文章中出现的所有词汇的概率，计算方式为
p_m = \frac{本词在某一类中出现的次数}{本类出现的所有的词数}
$$


#### 2、Naive Bayes

2.1 数据预处理

数据在knn中已经做到了比较完整的处理，我们拥有任意文件的词频和词数（规模较大，未上传github，有云盘链接），进行部分简单处理即可。处理的结果在./Naive Bayes/data/class中。

2.2 训练/测试

按照1的计算方式直接计算，注意由于取了log，需要将概率定位一个无穷小值。

```
			Probi = -1000000
			class_re = ''
			for i in class_div:
				dic_class = dict()
				with open(class_path+'/'+i, 'r', encoding='utf-8') as train:
					train_read = train.readlines()
					for j in train_read:
						if len(j.strip('\n').split(':')) < 2: continue
						word, pro = j.strip("\n").split(":")
						dic_class[word] = float(pro)
					pro_1 = 1
					for k in word_list:
						# print(k)
						pro_1 = pro_1+dic_class[k]
					pro_1  = pro_1+(float(len(data_class_index))/18828)
					if pro_1 > Probi:
						Probi = pro_1
						class_re = i
```



测试集范围为20%

### 实验结果

运行时间极短，不到五分钟。

准确度acc: True/all = 2984/3759 0.7938281457834531

