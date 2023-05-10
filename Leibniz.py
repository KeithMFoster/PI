# Calculation of PI using Leibniz formula

# Function to calculate PI using Leibniz
def leibniz_pi(n):
    pi = 0
    # n = 10 ** 7
    add = True
    for i in range(1, n, 2):
        if add:
            pi += 1 / i
        else:
            pi -= 1 / i
        add = not add
    return pi * 4


# Reading number of terms to be considered in Leibniz formula
terms = int(input("Enter number of terms: "))

# Function call
pi = leibniz_pi(terms)

# Displaying result
print("Pi = ", pi)