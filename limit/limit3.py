from sympy import *

# Mendefinisikan variabel x sebagai simbol
x = Symbol('x')

# Mendefinisikan fungsi f
f = (9 - x**2) / (4 - sqrt(x**2 + 7))

# Menghitung limit dari fungsi f saat x mendekati 0
limit_f = Limit(f, x, 3)
result = limit(f, x, 3)

# Menampilkan hasil limit
pprint(limit_f)
print("Hasilnya adalah ", result)
