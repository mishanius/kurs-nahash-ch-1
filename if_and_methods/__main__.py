from utils.register_utils import varify_name, get_current_year


def simple_func(x, y, z):
    """
    calculates x*y*z + 15
    :param x: a number
    :param y: a number
    :param z: a number
    :return: a number which represent the result
    """
    result = x * y * z + 15
    return result


if __name__ == '__main__':
    # result_calc = simple_func(1, 2, 3)
    # x = print(result_calc)
    # print(x)
    x = varify_name("Michael")
    y = get_current_year()
    print(y)
