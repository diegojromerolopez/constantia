from constantia import consts


@consts('uppercase', check_at='runtime')
def func():
    MY_CONSTANT = [1, 2, 3]
    MY_CONSTANT = 20
