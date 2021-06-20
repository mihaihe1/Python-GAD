def sum_1(*args, **kwargs):
    sum = 0
    for x in args:
        if isinstance(x, (int, float)):
            sum += x

    return sum


def sum_2(n):
    if n == 0:
        return 0

    return n + sum_2(n-1)


def sum_3(n):
    if n == 0:
        return 0

    if n % 2 == 1:
        return sum_3(n-1)

    return n + sum_3(n-2)


def sum_4(n):
    if n < 0:
        return 0

    if n % 2 == 0:
        return sum_4(n-1)

    return n + sum_4(n-2)


def is_int():
    x = input()
    try:
        x = int(x)
    except ValueError:
        return 0
    else:
        return x


print(sum_1(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_1())
print(sum_1(2, 4, 'abc', param_1=2))

print(sum_2(8))

print(sum_3(6))
print(sum_3(7))

print(sum_4(7))
print(sum_4(8))

print(is_int())
