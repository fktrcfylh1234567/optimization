def fibonacci_method(f, a, b, n):
    fn = fibonacci_number(n + 1)
    fn_prev = fibonacci_number(n)

    left = a + (fn - fn_prev) / fn * (b - a)
    right = a + fn_prev / fn * (b - a)

    for _ in range(n):
        if f(left) > f(right):
            a = left
            left = right
            right = b - left + a
        else:
            b = right
            right = left
            left = b - right + a

    return (a + b) / 2


def fibonacci_number(n):
    res = 1
    prev = 0
    for i in range(2, n + 1):
        res, prev = prev, res
        res += prev
    return res
