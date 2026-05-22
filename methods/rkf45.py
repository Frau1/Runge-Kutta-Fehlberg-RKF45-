import math

def rkf45_solver(eq, x0, y0, h, xn):

    results = []

    x = x0
    y = y0

    while x < xn:

        def f(x, y):
            return eval(eq)

        k1 = h * f(x, y)

        k2 = h * f(
            x + h/4,
            y + k1/4
        )

        k3 = h * f(
            x + 3*h/8,
            y + 3*k1/32 + 9*k2/32
        )

        k4 = h * f(
            x + 12*h/13,
            y + 1932*k1/2197
            - 7200*k2/2197
            + 7296*k3/2197
        )

        k5 = h * f(
            x + h,
            y + 439*k1/216
            - 8*k2
            + 3680*k3/513
            - 845*k4/4104
        )

        k6 = h * f(
            x + h/2,
            y - 8*k1/27
            + 2*k2
            - 3544*k3/2565
            + 1859*k4/4104
            - 11*k5/40
        )

        y4 = y + (
            25*k1/216
            + 1408*k3/2565
            + 2197*k4/4104
            - k5/5
        )

        y5 = y + (
            16*k1/135
            + 6656*k3/12825
            + 28561*k4/56430
            - 9*k5/50
            + 2*k6/55
        )

        error = abs(y5 - y4)

        results.append({
            'x': round(x + h, 5),
            'y4': round(y4, 6),
            'y5': round(y5, 6),
            'error': round(error, 10)
        })

        x += h
        y = y5

    return results