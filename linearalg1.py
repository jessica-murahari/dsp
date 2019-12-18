# Importing numpy as np
import numpy as np
A = np.array([[6, 1, 1],[4, -2, 5],[2, 8, 7]])
# Determinant of a matrix
print"Determinant of A:","\n",np.linalg.det(A)
# Inverse of matrix A
print"Inverse of A:","\n",np.linalg.inv(A)
# Rank of a matrix
print"Rank of A:","\n",np.linalg.matrix_rank(A)
# Trace of matrix A
print"Trace of A:","\n",np.trace(A)
#power of a matrix
print"Matrix A raised to power 2:","\n",np.linalg.matrix_power(A, 2)
#Eigen value of A
print"eigen value of A:","\n",np.linalg.eigvals(A)
#matrix and vector products
#scalar
prod=np.dot(3,4)
print"dot product of scalar values:","\n",prod
#vectors
a=2+3j
b=8+2j
prod1=np.dot(a,b)
print"dot product of vectors:","\n",prod1
#martix product of two arrays
B=np.diag((1,2,3))
print"matrix product:","\n",np.matmul(A,B)
#inner product of two arrays
print"inner product:","\n",np.inner(A,B)
#outer product of two arrays
print"outer product:","\n",np.outer(A,B)
#solving equations
print"solution of linear equations:","\n",np.linalg.solve(A,B)
#matrix or vector norm
print"norm of A:","\n",np.linalg.norm(A)




