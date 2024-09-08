# Assignment-07

# Number Explorer Program

This Python program is an interactive tool that allows users to explore their favorite numbers in a fun and informative way. The program performs several tasks, including identifying whether numbers are even or odd, calculating squares, finding the sum, and checking if the sum is a prime number.

## How It Works

1. The program starts by asking the user to enter their name.
2. It then asks the user to input three of their favorite numbers.
3. The program stores these numbers in a list and performs the following operations:
   - Determines if each number is even or odd.
   - Computes the square of each number.
   - Calculates the sum of the three numbers.
   - Checks whether the sum is a prime number.

After processing the numbers, the program provides a personalized message that includes the user's name and the results of these calculations.

## Features

- **Even or Odd Check**: For each number, the program determines whether it is even or odd and displays this information to the user.
- **Square Calculation**: The program calculates the square of each number and prints the results.
- **Sum Calculation**: The program computes the sum of the three numbers provided by the user.
- **Prime Number Check**: It checks whether the sum is a prime number and notifies the user.
- **Personalized Experience**: The program greets the user by name and provides fun, encouraging messages throughout the interaction.

## Code Example

Here’s a simple code example from the program:

```python
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    # Greet the user and ask for their name
    name = input("Enter your name: ")
    print(f"Hello {name}, let's explore some numbers!")

    # Ask for the user's favorite three numbers
    num1 = int(input("Enter your first favorite number: "))
    num2 = int(input("Enter your second favorite number: "))
    num3 = int(input("Enter your third favorite number: "))
    
    # Store the numbers in a list
    favorite_numbers = [num1, num2, num3]

    # Check if the numbers are even or odd
    even_odd_info = []
    for num in favorite_numbers:
        if num % 2 == 0:
            even_odd_info.append((num, "even"))
        else:
            even_odd_info.append((num, "odd"))

    # Print the even/odd information
    print("\nEven or odd status of your numbers:")
    for num, status in even_odd_info:
        print(f"{num} is {status}")

    # Print the square of each number
    print("\nSquares of your favorite numbers:")
    for num in favorite_numbers:
        print(f"The square of {num} is {num**2}")

    # Calculate and print the sum of the three numbers
    total_sum = sum(favorite_numbers)
    print(f"\nThe sum of your numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print("The sum is a prime number!")
    else:
        print("The sum is not a prime number.")

    print(f"Thanks for exploring numbers, {name}!")

# Run the program
if __name__ == "__main__":
    main()
