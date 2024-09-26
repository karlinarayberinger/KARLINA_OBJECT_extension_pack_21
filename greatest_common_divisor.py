#########################################################################################
# file: greatest_common_divisor.py
# type: Python
# date: 26_SEPTEMBER_2024
# author: karbytes
# license: PUBLIC_DOMAIN 
#########################################################################################

def print_greatest_common_divisor_computation_steps(A, B, output):
    """
    Use the Euclidean algorithm to compute the greatest common divisor of positive integers A and B.
    Print each step of that iterative process to the output (i.e. console or file).
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
    A = 1
    B = 1
    input_additional_values = 1

    """
    If the file named greatest_common_divisor.txt does not already exist 
    inside of the same file directory as the file named greatest_common_divisor.cpp, 
    create a new file named greatest_common_divisor_output.txt in that directory.
    
    Open the plain-text file named greatest_common_divisor_output.txt
    and set that file to be overwritten with program data.
    """
    with open("greatest_common_divisor_output.txt", "w") as file:

        # Print an opening message to the command line terminal.
        print("\n\n--------------------------------")
        print("Start Of Program")
        print("--------------------------------")

        # Print an opening message to the file output stream.
        file.write("--------------------------------\n")
        file.write("Start Of Program\n")
        file.write("--------------------------------\n")

        # Print "This Python program computes the greatest common divisor of two natural numbers and prints the steps involved." to the command line terminal and to the file output stream.
        print("\n\nThis Python program computes the greatest common divisor of two natural numbers and prints the steps involved.")
        file.write("\n\nThis Python program computes the greatest common divisor of two natural numbers and prints the steps involved.")

        # Continue input and computation loop until user inputs 0 for input_additional_values.
        while input_additional_values != 0:
            print("\n\nEnter the first value (A): ", end="")
            A = int(input())

            print("\n\nEnter the second value (B): ", end="")
            B = int(input())

            print_greatest_common_divisor_computation_steps(A, B, file)

            # Ask the user whether or not to continue inputting values.
            print("\n\nWould you like to input new values for A and B? (Enter 1 if YES. Enter 0 if NO): ", end="")
            input_additional_values = int(input())

        # Print a closing message to the command line terminal.
        print("\n\n--------------------------------")
        print("End Of Program")
        print("--------------------------------\n\n")

        # Print a closing message to the file output stream.
        file.write("\n\n--------------------------------\n")
        file.write("End Of Program\n")
        file.write("--------------------------------\n")

# Program entry point
if __name__ == "__main__":
    main()
