def sum_args(*args, **kwargs):
    sum = 0
    for x in args:
        if isinstance(x, (int, float)):
            sum += x
    for x in kwargs.values():
        if isinstance(x, (int, float)):
            sum += x

    return sum


def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n-1)


def sum_even(n):
    if n == 0:
        return 0

    if n % 2 == 1:
        return sum_even(n-1)

    return n + sum_even(n-2)


def sum_odd(n):
    if n < 0:
        return 0

    if n % 2 == 0:
        return sum_odd(n-1)

    return n + sum_odd(n-2)


def is_int():
    x = input()
    try:
        x = int(x)
    except ValueError:
        return 0
    else:
        return x


print(sum_args(1, 5, -3, 'abc', [12, 56, 'cad']))
print(sum_args())
print(sum_args(2, 4, 'abc', param_1=2))

print(sum_n(8))

print(sum_even(6))
print(sum_even(7))

print(sum_odd(7))
print(sum_odd(8))

print(is_int())
