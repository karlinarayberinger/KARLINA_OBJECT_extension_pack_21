# greatest_common_divisor.py
# Author: karbytes
# Date: 26_SEPTEMBER_2024
# License: PUBLIC_DOMAIN

def print_greatest_common_divisor_computation_steps(A, B, output):
    """
    Use the Euclidean algorithm to compute the greatest common divisor of positive integers A and B.
    Prints each step of that iterative process to the output (console or file).
    """
    i = 0
    remainder = 0
    output.write("\n\nComputing the greatest common divisor of A and B using the Euclidean algorithm...")
    while B != 0:
        remainder = A % B
        output.write(f"\n\nstep_{i}: A = {A}, B = {B}, gcd(A,B) = A % B = {remainder}.")
        A = B
        B = remainder
        i += 1
    output.write(f"\n\nThe greatest common divisor of A and B is {A}\n")

def main():
    # Declare and initialize variables
    A = 1
    B = 1
    input_additional_values = 1

    # Open output file for writing (overwrites if file already exists)
    with open("greatest_common_divisor_output.txt", "w") as file:

        # Opening messages
        print("\n\n--------------------------------")
        print("Start Of Program")
        print("--------------------------------")

        file.write("--------------------------------\n")
        file.write("Start Of Program\n")
        file.write("--------------------------------\n")

        print("\n\nThis Python program computes the greatest common divisor of two natural numbers and prints the steps involved.")
        file.write("\n\nThis Python program computes the greatest common divisor of two natural numbers and prints the steps involved.")

        # Continue input and computation loop
        while input_additional_values == 1:
            print("\n\nEnter the first value (A): ", end="")
            A = int(input())

            print("\n\nEnter the second value (B): ", end="")
            B = int(input())

            print_greatest_common_divisor_computation_steps(A, B, file)

            # Ask the user whether or not to continue inputting values.
            print("\n\nWould you like to input new values for A and B? (Enter 1 if YES. Enter 0 if NO): ", end="")
            input_additional_values = int(input())

        # Closing messages
        print("\n\n--------------------------------")
        print("End Of Program")
        print("--------------------------------\n\n")

        file.write("\n\n--------------------------------\n")
        file.write("End Of Program\n")
        file.write("--------------------------------\n")

# Program entry point
if __name__ == "__main__":
    main()
