题目描述
数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述:
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述:
输出合并后的键值对（多行）

示例1
输入
4
0 1
0 2
1 2
3 4
输出
0 3
1 2
3 4

思路：其实很简单，但是不好AC：1.对key要排序，且按数值排序，非字典序，所以key要为数字而非字符；2.输出不必专门加'\n'

n = int(input())
d = dict()
for i in range(n):
    k, v = input().split()
    t = int(k)
    if t in d.keys():
        d[t] += int(v)
    else:
        d[t] = int(v)

for k in sorted(d.keys()):
    print(str(k) + " " + str(d[k]))
