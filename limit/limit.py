from sympy import *

# Mendefinisikan variabel x sebagai simbol
x = Symbol('x')

# Mendefinisikan fungsi f
f = (x**2 + 3*x) / x

# Menghitung limit dari fungsi f saat x mendekati 0
limit_f = Limit(f, x, 0)
result = limit(f, x, 0)

# Menampilkan hasil limit
pprint(limit_f)
print("Hasilnya adalah ", result)
