def fibonacci_method(f, a, b, n):
    prev_ftmp = fibonacci_number(n)
    top_ftmp = fibonacci_number(n + 1)
    ltmp = a + (top_ftmp - prev_ftmp) / top_ftmp * (b - a)
    rtmp = a + prev_ftmp / top_ftmp * (b - a)

    for i in reversed(range(n)):
        if f(ltmp) > f(rtmp):
            a = ltmp
            ltmp = rtmp
            rtmp = a + b - ltmp
        else:
            b = rtmp
            rtmp = ltmp
            ltmp = a + b - rtmp

    return (a + b) / 2


def fibonacci_number(n):
    res = 1
    prev = 0
    for i in range(2, n + 1):
        res, prev = prev, res
        res += prev
    return res
