# encoding=utf-8
import numpy as np
from numpy.linalg import *

def main():
    lst = [[1, 3, 4], [2, 3, 4]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    print(np_lst)
    np_lst = np.array(lst, dtype=np.float32)
    print(np_lst)

    #创建一维数组
    print("arange创建一维数组")
    print(np.arange(1,10,dtype=np.int8))
    print("linspace创建一维等差数组")
    print(np.linspace(1,10,5,True,True,dtype=np.int8))
    print("logspace创建一维等比数组")
    print(np.logspace(1,10,10,endpoint=True,base=2))
    print("常用属性")
    print(np_lst.shape)
    # 维数
    print(np_lst.ndim)
    # 数据类型
    print(np_lst.dtype)
    # 元素字节大小
    print(np_lst.itemsize)
    # 元素个数
    print(np_lst.size)
    # 常用数组
    print(np.zeros([2, 2]))
    print(np.ones([2, 2]))
    # 2行4列随机数矩阵
    print(np.random.rand(2, 4))
    # 单个随机数
    print(np.random.rand())
    # 生成单个1-10之间的随机整数
    print(np.random.randint(1, 10, size=(3,4)))
    # 生成2行4列的正态分布随机矩阵
    print(np.random.randn(2, 4))
    # 在指定一维数组范围中生成单个随机数
    print(np.random.choice([1, 2, 3]))
    # 生成在1-10范围内20个正态分布的随机数
    print(np.random.beta(1, 10, 20))

    # 常用操作
    print("排序")
    lst4 = np.random.randint(1, 10, size=(3, 4))
    print("排序前：",lst4)
    print("排序后sort()：", np.sort(lst4,axis=0))
    print("排序后显示索引argsort()：", np.argsort(lst4,axis=0))
    # 生成1-11（取头不取尾）的数组
    print(np.arange(1, 11))
    # 将数组变为2行5列的矩阵
    print(np.arange(1, 11).reshape([2, 5]))
    # 将数组转为自然指数
    print(np.exp(lst))
    # 将数组转为自然指数的平方
    print(np.exp2(lst))
    # 将数组开方
    print(np.sqrt(lst))
    # 将数组用sin三角函数计算
    print(np.sin(lst))
    # 将数组求对数
    print(np.log(lst))
    print("按列求和sum(axis=0)")
    print(np_lst.sum(axis=0))
    print("按列求和,忽略NaN，nansum(axis=0)")
    print(np.nansum(np_lst,axis=0))
    print("按列求最大值(axis=0)")
    print(np_lst.max(axis=0))
    print(np.amax(np_lst,axis=0))
    print("按行求平均值(axis=1)")
    print(np_lst.mean(axis=1))
    print(np.mean(np_lst,axis=1))
    lst1 = np.array([1, 1, 1, 1])
    lst2 = np.array([2, 2, 2, 2])
    print("一维数组的切片访问(取头不取尾)")
    print(lst1[1:3])
    print("一维数组的切片访问(取头不取尾，步长2)")
    print(lst1[1::1])
    print("数组相加")
    print(lst1 + lst2)
    print("数组相减")
    print(lst1 - lst2)
    print("数组相乘")
    print(lst1 * lst2)
    print("数组相除")
    print(lst1 / lst2)
    print("数组二次方")
    print(lst2 ** 2)
    print("矩阵相乘")
    print(np.dot(lst1.reshape([2,2]),lst2.reshape([2,2])))
    print("矩阵拼接")
    print(np.concatenate((lst1,lst2)))
    print(np.hstack((lst1,lst2)))
    print("矩阵拼接，升维")
    print(np.vstack((lst1,lst2)))
    print("矩阵切割")
    print(np.split(lst1,2))

    print("线性方程组相关操作")

    print("生成单位矩阵")
    print(np.eye(3))
    print(np.identity(3))
    lst3 = np.array([[1,2],[3,4]])
    print("矩阵的逆")
    print(inv(lst3))
    print("矩阵的转置")
    print(lst3.transpose())
    print(lst3.T)
    print("矩阵的行列式")
    print(det(lst3))
    print("求特征值与特征向量")
    print(eig(lst3))
    print("解方程组")
    print(solve(lst3,np.array([[5],[7]])))

    print("其他数学操作")
    print("快速傅立叶变换")
    print(np.fft.fft(lst1))
    print("coef相关系数")
    print(np.corrcoef([1,0,1],[0,2,1]))
    print("生成一元多次函数")
    print(np.poly1d(lst1))
if __name__ == "__main__":
    main()
