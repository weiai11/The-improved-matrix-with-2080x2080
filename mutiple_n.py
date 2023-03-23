import sys
from C_change1 import result

import numpy as np
from IPython.core import debugger
debug = debugger.Pdb().set_trace
# 矩阵多次幂乘方函数
def matrixPow(Matrix,n):
    if(type(Matrix)==list):
        Matrix=np.array(Matrix)
    if(n==1):
        return Matrix
    else:
        return np.matmul(Matrix,matrixPow(Matrix,n-1))

C13=matrixPow(result(),14)
debug()
mytext=open('2.txt', mode='w', encoding='utf-8')
np.set_printoptions(threshold=sys.maxsize)
print(C13,file=mytext)
mytext.close()
