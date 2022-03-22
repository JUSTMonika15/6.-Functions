"""CSC 161 Quiz: Functions

Lihang Liu
Lab Section TR 2:00-3:15pm
Spring 2022
"""

import math


def inverse_square(d):
    val = (1 / (4 * math.pi * (d ** 2)))
    return val


def brightness(d, L):
    b = L * (inverse_square(d))
    return(b)


def main():
    distance = float(input("Please enter the distance "
                           "of a star, in meters: "))
    
    luminosity = float(input("Please enter the "
                             "luminosity of this star, in watts : "))
    
    brightness_value = brightness(distance, luminosity)
    print("The star brightness is ", brightness_value, "W/m^2")


if __name__ == '__main__':
    main()
