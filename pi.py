import math

a = 2 * math.sqrt(2) / 9801

k = 0
sum = 0
term = 1
while term > 1e-15:
    x = math.factorial(4 * k) * (1103 + 26390 * k)
    y = math.factorial(k)**4 * 396**(4 * k)
    term = x / y
    sum = sum + term
    k = k + 1

result = 1 / (a * sum)
print(result, math.pi)