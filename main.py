def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Количество строк:'))
m = int(input('Количество столбцов'))
value = input(f'Значение')
print('Матрица')
matrix = get_matrix(n, m, value)