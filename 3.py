import math
e = 0.01
x = 0.2
a = 1
term = math.log(a) * x 
P = 1 + term
n = 2
while abs(term) >= e:
    term = (math.log(a) * n * x * n) / n
    P += term
    n += 1
print(P)
