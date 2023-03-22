import numpy as np
import math
import itertools
np.set_printoptions(suppress=True)
import sys
from IPython.core import debugger
debug = debugger.Pdb().set_trace
# 第一个s盒的输入掩码对应的第几bit：1——0 2——1 3(0,1)——64 4——2 5(0,2)——65 6(1,2)——128  8——3 9(0,3)——66 10(1,3)——129 12(2,3)——189
# index_double=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]]
# 第一个s盒中，第ibit通过s盒影响
x0=[[2],[0,2],[1,2],[3],[2,3]]
x1=[[0,1],[0,2],[3],[0,3],[1,3],[2,3]]
x2=[[1,2]]
x3=[[0,2]]
# 第（1，2）bit影响 x02 [0,3]、[1,3]有问题
x01=[[0,1],[2],[0,2],[1,3],[3],[0,3],[1,2]]
x02=[[2],[0,2],[1,2],[0,3],[1,3],[2,3]]
x03=[[2],[0,2],[1,2],[3],[2,3]]
x12=[[0,1],[2],[3],[0,3],[1,3],[2,3]]
x13=[[1],[1,2],[3],[0,3],[1,3],[2,3]]
x23=[[0],[1],[0,3],[1,3]]

matrix = np.zeros([2080,2080],dtype=int)
# 转换为行
def summision(v):
    sum = 0
    for k in range(v, 64):
        sum = sum + k
    sum = sum + 63
    return sum

# 第一个s盒  1bit——>1bit/2bit
def sbox1(a):
    arr=[]
    if(a%4 == 0):
        num = int(a / 4)
        for b in x0:
            # 如果1bit——>1bit
            if(len(b)!=2):
                b = b[0] + 4*num
                arr.append(b)
            # 1bit——>2bit
            elif(len(b)==2):
                if(a<=4):
                    index = 64 - b[0]
                    b = summision(index) + b[1]-b[0]
                    arr.append(b)
                else:
                    index = (16-num)*4
                    b = summision(index) +b[1] - b[0]
                    arr.append(b)
    elif (a % 4 == 1):
        num = int(a / 4)
        for b in x1:
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = (16-num)*4
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    elif (a % 4 == 2):
        num = int(a / 4)
        for b in x2:
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = (16-num)*4
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    else:
        for b in x3:
            num = int(a / 4)
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = (16-num)*4
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    return arr

# s盒内部2bit的传播
def sbox2(a,b):
    arr=[]
    if ((a+b)==1+int(a/4)*8):
        num= int(a/4)
        for o in x01:
            # 如果1bit——>1bit
            if (len(o) != 2):
                r = o[0] + 4 * num
                arr.append(r)
            # （*，*）2bit的传播
            elif (len(o) == 2):
                if (a <= 4):
                    index = 64 - o[0]
                    r = summision(index) + o[1] - o[0]
                    arr.append(r)
                else:
                    index = 64 - (o[0] + 4 * num)
                    r = summision(index) + o[1] - o[0]
                    arr.append(r)
    elif ((a+b)==2+int(a/4)*8):
        num = int(a / 4)
        for o in x02:
            if (len(o) != 2):
                r = o[0] + 4 * num
                arr.append(r)
            elif (len(o) == 2):
                if (a <= 4):
                    index = 64 - o[0]
                    r = summision(index) + o[1] - o[0]
                    arr.append(r)
                else:
                    index = 64 - (o[0] + 4 * num)
                    r = summision(index) + o[1] - o[0]
                    arr.append(r)
    elif (((a+b)==3+int(a/4)*8) and (a%4==0)):
        num = int(a / 4)
        for b in x03:
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = 64 - (b[0] + 4 * num)
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    elif(((a+b)==3+int(a/4)*8) and (a%4==1)):
        for b in x12:
            num = int(a / 4)
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = 64 - (b[0] + 4 * num)
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    elif ((a + b) == 4 + int(a / 4) * 8):
        for b in x13:
            num = int(a / 4)
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = 64 - (b[0] + 4 * num)
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
    else:
        for b in x23:
            num = int(a / 4)
            if (len(b) != 2):
                b = b[0] + 4 * num
                arr.append(b)
            elif (len(b) == 2):
                if (a <= 4):
                    index = 64 - b[0]
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)
                else:
                    index = 64 - (b[0] + 4 * num)
                    b = summision(index) + b[1] - b[0]
                    arr.append(b)

    return arr

# sbox2(0,2) 验证正确
# a代表行 b代表第1bit c代表第2bit 2bit分别是两个s盒的
def double1(a,b,c):

    for i in sbox1(b):
        matrix[a][i] = 1
    for i in sbox1(c):
        matrix[a][i] = 1

# 2bit为s盒内部
def double2(a,b,c):
    for i in sbox2(b,c):
        matrix[a][i] = 1
    # debug()
# double2(65,0,2) 验证正确
def result():
    # 输出前64bit
    for i in range(0,64):
        for b in sbox1(i):
            matrix[i][b] = 1

    # 输出64——2079行
    # (k,m)
    n=64
    for k in range(0,63):
        for m in range(k+1,64):
                if(m<=int(k/4)*4+3):
                    double2(n,k,m)
                    n = n+1

                else:
                    double1(n, k, m)
                    n = n + 1
    return matrix
mytext = open('2.txt', mode = 'w',encoding='utf-8')
np.set_printoptions(threshold=sys.maxsize)
print(matrix,file=mytext)
mytext.close()
