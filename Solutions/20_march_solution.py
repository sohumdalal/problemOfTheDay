'''
Problem Of The Day - 3/20/2025

Create a class Matrix to represent 2D matrices.

Attributes:
- data (list of lists)

Methods:
 __repr__(): String representation of the matrix.
__add__(other): Adds two matrices element-wise.
__mul__(other): If other is a number, multiply each element. If other is a Matrix, perform matrix multiplication.

Hint: Look-up matrix operations!

'''

class Matrix:
    def __init__(self, data):
        # Ensure data is a valid 2D list (list of lists)
        if not all(isinstance(row, list) for row in data):
            raise ValueError("Matrix must be a list of lists.")
        if not all(len(row) == len(data[0]) for row in data):
            raise ValueError("All rows must have the same length.")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __repr__(self):
        """String representation of the matrix"""
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        """Element-wise addition of two matrices"""
        if not isinstance(other, Matrix) or self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition.")
        
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        """Matrix multiplication or scalar multiplication"""
        if isinstance(other, (int, float)):  # Scalar multiplication
            result = [[self.data[i][j] * other for j in range(self.cols)] for i in range(self.rows)]
            return Matrix(result)

        elif isinstance(other, Matrix):  # Matrix multiplication
            if self.cols != other.rows:
                raise ValueError("Matrix multiplication not possible (columns of A must match rows of B).")

            # Initialize result matrix with zeros
            result = [[0 for _ in range(other.cols)] for _ in range(self.rows)]
            
            # Matrix multiplication logic
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(self.cols):
                        result[i][j] += self.data[i][k] * other.data[k][j]
            
            return Matrix(result)

        else:
            raise TypeError("Unsupported multiplication type.")


# Example Usage:
A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])
C = Matrix([[2, 0], [1, 3]])

# Print matrices
print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
print("\nA + B:")
print(A + B)

# Scalar Multiplication
print("\nA * 2:")
print(A * 2)

# Matrix Multiplication
print("\nA * C:")
print(A * C)
