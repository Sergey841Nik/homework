
def get_matrix(n, m, value):
    matrix = []
    for row in range(n):
        _ = []
        for column in range(m):
            _.append(value)
        matrix.append(_)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# И для наглядности
# Чтобы матрица выглядела как матрица
import numpy as np

def get_matrix(n, m, value):
    matrix = []
    for row in range(n):
        _ = []
        for column in range(m):
            _.append(value)
        matrix.append(_)
    return np.array(matrix)

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
