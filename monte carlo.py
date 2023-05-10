import random
import math


def calculate_pi(num_points):
    inside_unit_circle = 0
    for i in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance_from_origin = math.sqrt(x**2 + y**2)
        if distance_from_origin <= 1:
            inside_unit_circle += 1
    pi = 4 * (inside_unit_circle / num_points)
    return pi


if __name__ == '__main__':
    num_points = int(input("Enter the number of points to use in the Monte Carlo simulation: "))
    pi_value = calculate_pi(num_points)
    print(f"The calculated value of pi is: {pi_value}")