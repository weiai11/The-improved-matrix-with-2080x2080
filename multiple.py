import numpy as np
import A
import B_g0c
import B
import sys
from IPython.core import debugger
debug = debugger.Pdb().set_trace

C1=np.dot(A.A,B.B)
# C2=np.dot(C1,C1)
# C3=np.dot(C2,C2)
# debug()
mytext=open('2.txt', mode='w', encoding='utf-8')
np.set_printoptions(threshold=sys.maxsize)
print(C1,file=mytext)
mytext.close()

# mytext = open('1.txt', mode = 'w',encoding='utf-8')
# np.set_printoptions(threshold=sys.maxsize)
# print(C,file=mytext)
# mytext.close()
# # 矩阵乘方的算法这样做是错误的
# A=[[5,2],[1,2]]
# B=[[1,2],[1,2]]
# C1=np.dot(A,B)
# C=matrixPow(C1,2)
# # C2=np.dot(C1,C1)
# # C3=np.dot(C2,C2)
# print(C1)
# print(C)
# print(C3)