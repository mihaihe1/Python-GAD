a = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

b = a[:]
b.sort()
print(b)

c = a[:]
c.sort(reverse=True)
print(c)

print(b[1::2])

print(b[::2])

print(b[2::3])