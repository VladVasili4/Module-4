from fake_math import divide as df
from true_math import divide as dt

num1 = df(99, 3)
num2 = df(99, 0)
num3 = dt(88.8, 4)
num4 = dt(88.8, 0)

print(num1, num2, num3, num4, sep = '\n')

