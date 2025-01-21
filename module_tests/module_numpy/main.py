import numpy as np

numpy_1_demensional_array = np.array([1,2,3])
numpy_2_demensional_array = np.array([[1,2,3],[4,5,6]])

print(numpy_1_demensional_array*2)
print(numpy_2_demensional_array*2)
print('-'*10)
print(numpy_1_demensional_array**2)
print(numpy_2_demensional_array**2)
print('-'*10)

# numpy.arange cria arrays unidimensionais com valores incrementados regularmente.

arrange_1 = np.arange(10)
arrange_2 = np.arange(2, 3, 0.1)
arrange_3 = np.arange(10, dtype = float)


print(arrange_1)
print(arrange_2)
print(arrange_3)
print('-'*10)
"""
funções gerais de criação de ndarray 

As funções de criação ndarray, por exemplo numpy.ones, numpy.zeros, e random definem arrays com base no formato 
desejado. 
As funções de criação ndarray podem criar arrays com qualquer dimensão especificando quantas dimensões e comprimento ao 
longo dessa dimensão em uma tupla ou lista.

"""

# numpy.zeros criará um array preenchido com 0 valores com o formato especificado. O dtype padrão é float64:

print(np.zeros((2,3), dtype=int))
print('-'*10)

# numpy.ones criará um array preenchido com valores 1. É idêntico a zerosem todos os outros aspectos como tal:
print(np.ones((2,3), dtype=int))
print('-'*10)

"""
Replicar, unir ou mutar matrizes existentes

Depois de criar arrays, você pode replicar, unir ou mutar esses arrays existentes para criar novos arrays. 
Quando você atribui um array ou seus elementos a uma nova variável, você tem que explicitamente numpy.copy o array, 
caso contrário, a variável será passada como referência ao array original. Considere o seguinte exemplo:
"""

a = np.array([1, 2, 3, 4, 5, 6])
b = a[:2]
b += 1
print('a =', a, '; b =', b)
print('-'*10)

"""
Nesse caso, a variável b foi passada como referência aos dois primeiros valores de a.

Se você quiser criar um novo array, use a numpy.copy
"""
c = np.arange(0, 4)
d = c.copy()
d[-1] = 5
print(c)
print(d)
print('-'*10)

"""
Há uma série de rotinas para unir matrizes existentes, por exemplo numpy.vstack, numpy.hstack, e numpy.block. Aqui está
um exemplo de união de duas matrizes 2 por 2  em uma matriz 4x2 utilizando numpy.block:
"""

matriz1 = np.array([[1,2],[3,4]])
matriz2 = np.array([[5,6],[7,8]])

print(np.block(
    [[matriz1[0]],
     [matriz1[1]],
     [matriz2[0]],
     [matriz2[1]]
     ]
))
print('-'*10)
A = np.ones((2, 2), int)
B = 2 * A
print(np.block([[A], [B]]))
print('-'*10)