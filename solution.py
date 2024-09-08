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
