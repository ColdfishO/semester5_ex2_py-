# 1
for i in range(5):
    print(i)
for i in range(4, 8):
    print(i)
for i in range(1, 20, 3):
    print(i, end=" ")

print('\n')
# 2

for i in range(2, 21, 2):
    print(i, end=" ")

print('\n')

for i in range(19, 0, -2):
    print(i)

print('\n')
for i in range(1, 11):
    print(i**2)

print('\n')
# 3

n = int(input('Podaj pierwszą liczbę: '))
m = int(input('Podaj drugą liczbę: '))
if n > m:
    for i in range(n, m-1, -1):
        print(i, end=' ')
else:
    for i in range(n, m+1):
        print(i, end=' ')

print('\n')
# 4

n = int(input('Podaj liczbę: '))
suma = 0
for i in range(1, n+1):
    suma += i
print(suma)

print('\n')
# 5

suma = 0
n = 0
while suma <= 1000000:
    n += 1
    suma += n

print(n)

print('\n')
# 6

suma = 0
n = 0
while suma <= 10:
    n += 1
    suma += 1/n

print(n)

print('\n')
# 7
n = int(input('Podaj liczbę:'))
i = 0
while i <= n:
    if i*i == n:
        print(n, 'jest kwadratem', i)
        i += 1
    else:
        i += 1

print('\n')
# 8
n = int(input('Podaj liczbę:'))
silnia = 1
for i in range(1, n+1):
    silnia *= i
print('silnia', n, 'wynosi', silnia)

print('\n')
# 9
n = int(input('Podaj liczbę:'))
m = int(input('Podaj potęgę:'))
potega = n
while m < 0:
    m = int(input('Wprowadź ponownie potęgę (liczba dodatnia):'))
if m == 0:
    print('1')
elif m == 1:
    print(n)
else:
    for i in range(2, m + 1):
        potega *= n
    print(potega)

print('\n')
# 10
n = int(input('Podaj liczbę:'))
k = 0
for i in range(1, n+1):
    if n % i == 0:
        k += 1

print(n, 'ma', k, 'dzielników')

print('\n')
# 11
n = int(input('Podaj liczbę:'))
ans = 1
while n <= 1:
    n = int(input('Podaj liczbę większą od 1:'))
else:
    for k in range(2, n):
        if n % k == 0:
            ans -= 1
if ans == 1:
    print(n, 'jest liczbą pierwszą')
else:
    print(n, 'jest liczbą złożoną')

print('\n')
# 12
for i in range(2, 201):
    ans = 1
    for k in range(2, i):
        if i % k == 0:
            ans -= 1
    if ans == 1:
        print(i, end=' ')