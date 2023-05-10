import math as mp
from decimal import *

def pi_chudn(n):
    getcontext().prec = n + 50
    k = 0
    pi_chud = 0
    while k < n:
        pi_chud += (((Decimal(-1)) ** k) * (Decimal(mp.factorial(6 * k))) * (13591409 + 545140134 * k)) / Decimal(
            (mp.factorial(3 * k) * ((mp.factorial(k)) ** 3) * (640320 ** ((3 * k) + (Decimal(1.5))))))
        k += 1
    pi_chud = (Decimal(pi_chud) * 12)
    pi_chud = (Decimal(pi_chud ** (-1)))
    return int(pi_chud * 10 ** n)

def pi_infinite(n):
    pi = 0
    for i in range(n):
        term = ((-1) ** i) / (2 * i + 1)
        pi += term
    pi *= 4
    return pi


def main():
    exact_pi_val = str(
        31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201)
    decimal_places = 100000000
    decimal_display = 500

    # First up Chudnovsky Method
    print("Using the Chudnovsky Method")
    pi_value = str(pi_chudn(decimal_places))
    print(f"The value of calculated pi to 500 decimal places is: {pi_value[0:decimal_display]}")
    print(f"Pi true value is: {exact_pi_val[0:decimal_display]}")
    if pi_value[0:decimal_display] == exact_pi_val[0:decimal_display]:
        print("Both are equal")

    # Let's just print out a summary up to 20 values.
    print("Using the Infinite Series Method")
    pi_value = format(pi_infinite(decimal_places), f".{decimal_places}f")
    print(f"The value of calculated pi to 500 decimal places is: {pi_value[0:decimal_display]}")
    print(f"Pi true value is: {exact_pi_val[0:decimal_display]}")
    if pi_value[0:decimal_display] == exact_pi_val[0:decimal_display]:
        print("Both are equal")


if __name__ == "__main__":
    main()