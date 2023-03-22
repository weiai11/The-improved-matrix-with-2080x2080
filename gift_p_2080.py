# 验证正确
import numpy as np
np.set_printoptions(suppress=True)
import sys
from IPython.core import debugger
debug = debugger.Pdb().set_trace
#g0c
p=[0,17,34,51,16,33,50,3,48,1,18,35,32,49,2,19,4,21,38,55,20,37,54,7,52,5,22,39,36,53,6,23,8,25,42,59,24,41,58,11,56,9,26,43,40,57,10,27,8,29,46,63,28,45,62,15,60,13,30,47,44,61,14,31]
#p=[0,17,34,51,48,1,18,35,32,49,2,19,16,33,50,3,4,21,38,55,52,5,22,39,36,53,6,23,20,37,54,7,8,25,42,59,56,9,26,43,40,57,10,27,24,41,58,11,12,29,46,63,60,13,30,47,44,61,14,31,28,45,62,15]
print(len(p))
matrix = np.zeros([2080,2080],dtype=int)
# p1=0,1,2,3....63
p1 = []
# 第1到64bit的拉线
for a in range(0,64):
    p1.append(a)
    matrix[a][p[a]] = 1


def summision(v):
    sum = 0
    for k in range(v, 64):
        sum = sum + k
    sum = sum + 63
    return sum
# 拉线函数  j为行 num是递加的行数
def permutation(x,num):
    index = 63 - num
    px=[]
    for a in range(x,x+num):
        px.append(a)
        for i,j in zip(p1,px):
            if(i<num):
                if((p[int(index)]<p[i+index+1])&(p[int(index)]==0)):
                        matrix[j][summision(64 - p[int(index)]) + p[(i + index + 1 )]- p[int(index)]] = 1
                elif(p[int(index)]<p[i+index+1]):
                    matrix[j][summision(64-p[int(index)])+p[(i+index+1)]-p[int(index)]] = 1
                else:
                    matrix[j][summision(64-p[i+index+1])+p[int(index)]-p[(i+index+1)]] = 1
            else:
                break
    return matrix
def result():
    permutation(64,63)
    permutation(127,62)
    permutation(189,61)
    permutation(250,60)
    permutation(310,59)
    permutation(369,58)
    permutation(427,57)
    permutation(484,56)
    permutation(540,55)
    permutation(595,54)
    permutation(649,53)
    permutation(702,52)
    permutation(754,51)
    permutation(805,50)
    permutation(855,49)
    permutation(904,48)
    permutation(952,47)
    permutation(999,46)
    permutation(1045,45)
    permutation(1090,44)
    permutation(1134,43)
    permutation(1177,42)
    permutation(1219,41)
    permutation(1260,40)
    permutation(1300,39)
    permutation(1339,38)
    permutation(1377,37)
    permutation(1414,36)
    permutation(1450,35)
    permutation(1485,34)
    permutation(1519,33)
    permutation(1552,32)
    permutation(1584,31)
    permutation(1615,30)
    permutation(1645,29)
    permutation(1674,28)
    permutation(1702,27)
    permutation(1729,26)
    permutation(1755,25)
    permutation(1780,24)
    permutation(1804,23)
    permutation(1827,22)
    permutation(1849,21)
    permutation(1870,20)
    permutation(1890,19)
    permutation(1909,18)
    permutation(1927,17)
    permutation(1944,16)
    permutation(1960,15)
    permutation(1975,14)
    permutation(1989,13)
    permutation(2002,12)
    permutation(2014,11)
    permutation(2025,10)
    permutation(2035,9)
    permutation(2044,8)
    permutation(2052,7)
    permutation(2059,6)
    permutation(2065,5)
    permutation(2070,4)
    permutation(2074,3)
    permutation(2077,2)
    permutation(2079,1)
    return matrix
result()
#debug()
mytext = open('1.txt', mode = 'w',encoding='utf-8')

np.set_printoptions(threshold=sys.maxsize)
print(matrix,file=mytext)
print(len(matrix[0]))
mytext.close()
# w+ 是读加写权限
# np.set_printoptions(threshold=sys.maxsize)
# print(matrix)
# # （1，2）到（1，64）
# # p2=64,65,66...126
# p2 = []
# for b in range(64,127):
#     p2.append(b)
#     for i,j in zip(p1,p2):
#         if(i<63):
#             matrix[j][int(p[i+1])+62] = 1
# # （2，3）到（2，64）
# p3=[]
# for c in range(127,189):
#     p3.append(c)
#     for i,j in zip(p1,p3):
#         if(i<62):
#             matrix[j][int(p[i+2])+934] =1
# # (3,4)到（3，64）
# p4=[]
# for d in range(189,250):
#     for i,j in zip(p1,p4):
#         if(i<61):
#             matrix[j][int(p[i+3])+1580] =1
# np.set_printoptions(threshold=sys.maxsize)
# print(matrix)