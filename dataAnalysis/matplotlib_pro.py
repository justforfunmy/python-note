import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


# 解决中文乱码问题
#sans-serif就是无衬线字体，是一种通用字体族。
#常见的无衬线字体有 Trebuchet MS, Tahoma, Verdana, Arial, Helvetica, 中文的幼圆、隶书等等。
mpl.rcParams['font.sans-serif']=['SimHei'] #指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus']=False #用来正常显示负号


data = pd.read_csv('../files/watcher.csv')
# print(data.values)
# 转置
data2 = data.T
y = data2.values[2]
x = data2.values[0]
plt.plot(x,y,'o')
# plt.hist(y)
plt.show()
