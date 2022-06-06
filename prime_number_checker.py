import math


def is_prime(num):
    for i in range(2, math.ceil(num/2)):
        if num % i == 0:
            print("{num} is not a prime number".format(num=num))
            return False
    print("{num} is a prime number".format(num=num))
    return True

is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)