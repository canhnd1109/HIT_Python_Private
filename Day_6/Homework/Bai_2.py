def matrix_transposition(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # tạo ra một ma trận bằng 0 cùng kích thước với ma trận ban đầu 
    matrix_transposition = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            matrix_transposition[i][j] = matrix[j][i]

    for i in matrix_transposition:
        print(i)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Ma trận ban đầu:")
for i in matrix:
    print(i)

print("Ma trận chuyển vị:")
matrix_transposition(matrix)