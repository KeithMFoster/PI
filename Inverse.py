import math


def calculate_pi(n):
    pi = 0
    for i in range(n):
        term = (2 / (math.sqrt(2 - 2 * math.sqrt(1 - (i / n) ** 2))))
        pi += term
        pi *= 2 / n
    return pi


def main():
    decimal_places = 5
    pi_value = format(calculate_pi(decimal_places), f".{decimal_places}f")
    print(f"The value of pi to {decimal_places} decimal places is: {pi_value}")


if __name__ == "__main__":
    main()