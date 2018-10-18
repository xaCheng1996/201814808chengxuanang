# Data Mining Homework

--Data Mining project from SDU= =

#### update 2018-10-8

添加了数据集

#### update 2018-10-12

建立词典

总词典25W+，如果要做KNN压力太大了

过滤词频>=5，约为4W+

过滤词频>=15, 约为两万（19367）

过滤词频>=50,为7833

#### update 2018-10-13

完成bag-of-words，为了便于表示，输出只保留向量中为1的维度。

实例

*[207, 3947, 5256, 181, 5366, 1477, 1059, 2779, 2547, 1669, 3844, 5777, 4545, 5942, 5458, 223, 1403, 2485, 2873, 6536, 3107, 5378, 427, 994, 1324, 1849, 4521, 3394, 3394, 6536, 200, 5117, 175, 4361, 335, 4521, 5378, 6016, 1544, 309, 4348, 2547, 5779, 3587, 5429, 4361, 5779, 7482, 1403, 2116, 994, 104, 994, 2149, 178, 4961, 7325, 5368, 5257, 3107, 2370, 3107, 5773, 4289, 2983, 5779, 3807, 5140, 3971, 1594, 2500, 4961, 5366, 3396, 5779, 2452, 596, 184, 2567, 2116, 5941, 7646, 3394, 2116, 4795, 4186, 4744, 5366, 994, 1867, 2035, 6424, 770, 5779, 596, 5378, 5815, 3394, 2178, 1340, 5212, 2116, 3176, 4299, 4744, 2983, 1509, 1403, 4348, 2116, 3394, 994, 5779, 3807, 5140, 2983, 6536, 5779, 3620, 4361, 1945, 4961, 5033, 4361, 5779, 4849, 5212, 5779, 4340, 4361, 5212, 4316, 668, 3197, 3394, 3971, 7123, 994, 5798, 591, 5366, 2567, 3075, 2567, 5378, 5942, 5815, 5366, 3176, 4749, 4803, 3176, 4504, 5378, 1217, 4803, 3176, 4504, 5378, 5941, 3504, 5147, 5751, 3396, 3504, 4504, 5378, 5941, 7011, 5147, 5751, 3396, 5212, 1753, 2076, 181, 5366, 3176, 2423, 2090, 4361, 5366, 4206, 5779, 1845, 3176, 5382, 994, 1090, 4348, 231, 6536, 3187, 729, 5806, 2567, 181, 1217, 1157, 2983, 5942, 3396, 7116, 4186, 2647, 994, 4186, 2402, 7338, 5751, 2423, 2529, 4961, 5779, 6428, 5378, 5798, 1544, 5993, 2983, 6536, 7338, 2567, 3394, 5779, 4316, 746, 52, 3176, 5043, 1403, 6536, 2567, 4504, 5378, 1452, 5685, 4186, 5779, 5975, 2076, 945, 4361, 2423, 6773, 591, 5132, 4177, 945, 2355, 994, 5779, 4849, 336, 4504, 945, 5662, 830, 175, 994, 4186, 4521, 5366, 3176, 6393, 3628, 5378, 1509, 4961, 5779, 4636, 4361, 5779, 5229, 5779, 6180, 498, 591, 5043, 4316, 1574, 3396, 7116, 4186, 2647, 994, 4186, 2402, 7338, 5751, 2423, 2090, 4361, 6575, 5378, 5798, 1544, 5815, 2378, 4961, 2983, 6536, 591, 2779, 5395, 4316, 3176, 3396, 7338, 5990, 4803, 3176, 3396, 5043, 5132, 706, 1544, 4186, 7427, 994, 4186, 5043, 2983, 6536, 7338, 5990, 3394, 6536, 2287, 5043, 5366, 181, 5132, 1115, 3176, 3191, 5779, 5037, 3187]*

#### update 2018-10-16

// 忘记需要加tf-idf了很尴尬= =

更新了tf-idf

更新了文件结构，使用了数个文件夹保存中间信息。

具体而言，目前的目录情况是：

├─.idea
│  └─inspectionProfiles
├─20news-18828
│  ├─alt.atheism
│  ├─comp.graphics
│  ├─comp.os.ms-windows.misc
├─data
├─data_statistic_every
│  ├─alt.atheism
│  ├─comp.graphics
│  ├─comp.os.ms-windows.misc
├─data_tf_idf
│  ├─alt.atheism
│  ├─comp.graphics
│  ├─comp.os.ms-windows.misc

├─Vector_space_model.py

├─data_helper.py

└─__pycache__

20news-1882等三个文件夹结构都是原始数据结构，这里只展示前三个文件夹，实际上有20类。

data_helper.py保存大部分文件读取的方法，具体说明见注释

Vector_space_model.py保存VSM表示的各项方法，写的比较混乱，我尽量写写注释

data文件夹保存字典和词频表

data_statistic_every保存每个文件的词频，主要为了计算tf值

data_tf_idf保存每个文件的tf_idf值



对于data_statistics_every和data_tf_idf两个文件夹，由于文件过大，所以只上传了一部分示例数据，全体数据在这里：

data_statistic_every:

https://drive.google.com/drive/folders/11dIrmusfwRR_Gocx7hLKfA-X4XiK4EvL?usp=sharing

data_tf_idf:

https://drive.google.com/drive/folders/1ZV1XccJmWgEJpeXC19uvB2wfHK2J73YP?usp=sharing

如果太慢的话请联系我= =人肉送U盘



#### update 18-10-18

KNN主体程序完成。

训练集/测试集：0.9/0.1

k默认为4。

耗时极大，准确性尚未统计。

预计采样部分数据进行统计。