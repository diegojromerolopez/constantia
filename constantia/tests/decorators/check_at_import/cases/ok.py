from constantia import consts


@consts(['x', 'y', 'z'], check_at='import')
def func():
    x = 1
    y = 2
    z = 3
    return x, y, z
