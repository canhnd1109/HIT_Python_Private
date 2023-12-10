import numpy as np

class Matrix:
    def __init__(self, n, m, value=None) -> None:
        self.n = n 
        self.m = m
        self.value = value if value else [[0] * m for _ in range(n)]
        
    def __str__(self) -> str:
        # Better format
        return "\n".join(["\t".join([str(j) for j in i]) for i in self.value])
    
    def __inverse__(self):
        n = len(self.value)
        augmented_value = [row + [int(i == j) for j in range(n)] for i, row in enumerate(self.value)]

        # Apply Gauss-Jordan elimination
        for i in range(n):
            # Normalize the pivot row
            pivot = augmented_value[i][i]
            for j in range(2 * n):
                augmented_value[i][j] /= pivot

            # Eliminate other rows
            for k in range(n):
                if k != i:
                    factor = augmented_value[k][i]
                    for j in range(2 * n):
                        augmented_value[k][j] -= factor * augmented_value[i][j]

        # Extract the inverse matrix from the augmented matrix
        inverse_matrix = [row[n:] for row in augmented_value]

        return inverse_matrix

    # Cộng 2 ma trận
    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Hai ma trận không cùng kích thước")
        result = Matrix(self.n, self.m)
        
        # for i in range(self.n):
        #     for j in range(self.m):
        #         result.value[i][j] = self.value[i][j] + other.value[i][j]

        result.value = np.add(self.value, other.value)
        return result
        
    # Trừ 2 ma trận
    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("Hai ma trận không cùng kích thước")
        result = Matrix(self.n, self.m)
        # for i in range(self.n):
        #     for j in range(self.m):
        #         result.value[i][j] = self.value[i][j] - other.value[i][j]
        result.value = np.subtract(self.value, other.value)
        return result
    
    # Nhân 2 ma trận
    def __mul__(self, other):
        # Kiểm tra 2 ma trận có thể nhân với nhau hay không
        if self.m != other.n:
            raise ValueError("Hai ma trận không cùng kích thước")
        
        result = Matrix(self.n, self.m)
        
        # # hàng của ma trận 1
        # for i in range(self.n):
        #     # Hàng của ma trận 2
        #     for j in range(other.m):
        #         # Cột của ma trận 2
        #         for k in range(self.m):
        #             result.value[i][j] += self.value[i][k] * other.value[k][j]
        
        result.value = np.dot(self.value, other.value)  
        return result
    
    # Chia 2 ma trận
    def __truediv__(self, other):
        if other.m != other.n:
            raise ValueError("Hai ma trận không vuông nên không thể chia được")
        
        result = Matrix(self.n, self.m)
        inverse_matrix = np.linalg.inv(other.value)
        
        result.value = np.dot(inverse_matrix, self.value)
        
        return result
    
    def __eq__(self, other):
        if self.n != other.n or self.m != other.m:
            return False
        
        for i in range(self.n):
            for j in range(self.m):
                if self.value[i][j] != other.value[i][j]:
                    return False
        return True
    
# Create 2 matrix 3x3
matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
matrix2 = Matrix(2, 2, [[5, 6], [7, 8]])
print("\n\n")
print("Cộng 2 ma trận")
print(matrix1 + matrix2)

print("Trừ 2 ma trận")
print(matrix1 - matrix2)

print("Nhân 2 ma trận")
print(matrix1 * matrix2)

# Chỉ đúng với ma trận vuông
print("Chia 2 ma trận ")
print(matrix1 / matrix2)

print('\n',"Ma trận giống nhau" if matrix1 == matrix2 else "Ma trận khác nhau")