""" i used chat gtp to make this code

https://chatgpt.com/share/6715a299-84dc-8011-8a45-5011f0578d32

"""

# Define the recursive function to calculate the factorial
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Define the main function to handle user input
def main():
    # Prompt the user to enter a non-negative integer
    num = int(input("Enter a non-negative integer: "))
    
    # Ensure the input is non-negative
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        # Call the factorial function and print the result
        result = factorial(num)
        print(f"The factorial of {num} is {result}.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
