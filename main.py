import math
import numpy


def math_pi(n):
    return format(math.pi, f".{n}f")


def numpy_pi(n):
    return format(numpy.pi, f".{n}f")


if __name__ == "__main__":
    decimal_places = int(input("Enter the number of decimal places to round pi to: "))
    if decimal_places < 49 and decimal_places > 0:
        pi_value = math_pi(decimal_places)
        print(f"The value of pi using Math.PI, rounded to {decimal_places} decimal places is: {pi_value}")

        pi_value = numpy_pi(decimal_places)
        print(f"The value of pi using NumPy.PI, rounded to {decimal_places} decimal places is: {pi_value}")
    else:
        print("These libraries can only determine Pi to 48 places.")

    print(format(math.pi, f".{5}f"))

    print(format(numpy.pi, f".{5}f"))


