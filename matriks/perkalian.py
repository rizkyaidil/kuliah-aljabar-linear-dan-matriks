import numpy as np

# Matriks A
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Matriks B
B = np.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

# Perkalian matriks A dan B
C = np.dot(A, B)

print("Matriks C:")
print(C)