from sympy import *

# Mendefinisikan variabel x sebagai simbol
x = Symbol('x')

# Mendefinisikan fungsi f
f = (6 / (x**2 - x - 2)) - (2 / (x - 2))

# Menghitung limit dari fungsi f saat x mendekati 0
limit_f = Limit(f, x, 2)
result = limit(f, x, 2)

# Menampilkan hasil limit
pprint(limit_f)
print("Hasilnya adalah ", result)
