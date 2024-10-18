n = int(input())

b = []

while n > 0:
    b.append(n % 2)
    n //= 2

b.reverse()

for i in b:
    print(i, end='')

print('\n')

def f(i):
    i = str(i)
    return i == i[::-1]

print(f(i))