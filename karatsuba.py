# Charles Dieterle
# Karatsuba Multiplication Algorithm
# 11 July 2019
# edited 25 July 2020

def karatsuba(x, y):
    """
    multiply using Karatsuba divide-and-conquer multiplication algorithm
    args: x, y - non-negative ints
    """
    # convert x and y to strings so they are subscriptable
    str_x, str_y = str(x), str(y)

    len_x = len(str_x)
    len_y = len(str_y)

    if len_x == 1 and len_y == 1:
        return x * y

    # make len_x and len_y equal by adding a buffer of zeros
    if len_x > len_y:
        for counter in range(0, len_x - len_y):
            str_y = "0" + str_y
            len_y += 1
    if len_x < len_y:
        for counter in range(0, len_y - len_x):
            str_x = "0" + str_x
            len_x += 1

    # make len_x and len_y even
    if len_x % 2 == 1:
        str_x = "0" + str_x
        str_y = "0" + str_y
        len_x += 1

    # body of karatsuba algorithm
    half_len = int(len_x / 2)
    a = int(str_x[:half_len])
    b = int(str_x[half_len:])
    c = int(str_y[:half_len])
    d = int(str_y[half_len:])
    return int((10 ** len_x - 10 ** half_len) * karatsuba(a, c) +
    10 ** half_len * karatsuba(a+b, c+d) +
    (1 - 10 ** half_len) * karatsuba(b, d))

#tests
print(karatsuba(1, 1) == 1,
      karatsuba(1, 2) == 2,
      karatsuba(12, 35) == 420,
      karatsuba(222, 222) == 49284,
      karatsuba(98594, 25) == 2464850,
      karatsuba(12345678, 1) == 12345678,
      karatsuba(6, 0) == 0,
      karatsuba(0, 500000) == 0,
      karatsuba(10000, 2000) == 20000000,
)
