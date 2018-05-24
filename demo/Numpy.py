# numpy 数组库
import numpy as np

# 从列表转换数组
a_list = list(range(10))
b = np.array(a_list)
print((b))
print(type(b))

# 生成数组,默认float
a = np.zeros(10, dtype=int)
print(a)
# 二维
a = np.zeros((4, 4), dtype=int)
print(a)
a = np.full((3, 3), "哈", dtype=str)
print(a)

b = np.full_like(a, "变")
print(b)

# 数组切片
var = ((1, 2, 3), (3, 4, 5), (6, 7, 8))
c = np.array(var)
print(c)
# 前两行 前1列
print(c[:2, :1])
# 前两行 前1行
print(c[:2][:1])
# 维度
print(c.ndim)
# 形状
print(c.shape)
# 大小
print(c.size)
# dytpe, int 64位， 8字节
print(c.dtype)
# item size 8 字节
print(c.itemsize)
# nbytes 一共72个字节
print(c.nbytes)
# 运算
a = np.array(list(range(10)))
aa = np.full((3, 3), 1.0)
bb = np.full((2, 3), 2.0)
# 一维运算
print(a + 1)
# 二维
print(bb + 1)
#
a = np.linspace(0, 2 * np.pi, 5)
print(a)
# 转化成sin
b = np.sin(a)
print(b)

# %timeit sum()
a = np.full((2, 10), 1)
# 变形
b = a.reshape(5, 4)
print(b)
# 排序
l = [(1, 2, 3),
     (34, 12, 4),
     (32, 6, 33)]
a = np.array(l)
print(a)
# a= np.sort(a)
# axis 0 ，行排序，1 列排序
# kind：排序的算法，提供了快排、混排、堆排
a.sort(axis=1)
print(a)

# 拼接
a = np.array([(1, 2),[1,2]])
b = np.array([(2, 4), (3, 6)])
c = np.concatenate([a, b],axis=1)
print(c)
