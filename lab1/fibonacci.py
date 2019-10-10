def fibonacci_method(f, a, b, n):
    fn = fibonacci_number(n + 1)
    fn_prev = fibonacci_number(n)

    x1 = a + (fn - fn_prev) / fn * (b - a)
    x2 = a + fn_prev / fn * (b - a)

    for i in range(n):
        print('N =', i + 1, 'a =', a, 'b =', b, 'x1 =', x1, 'x2 =', x2)
        if f(x1) > f(x2):
            a = x1
            x1 = x2
            x2 = b - x1 + a
        else:
            b = x2
            x2 = x1
            x1 = b - x2 + a

    return (a + b) / 2


def fibonacci_number(n):
    res = 1
    prev = 0
    for i in range(2, n + 1):
        res, prev = prev, res
        res += prev
    return res
