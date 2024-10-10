# Function to calculate the area of a square
def square(side):
    area = side * side  # Calculate the area of the square
    print("The area of the square is " + str(area) + " square units.")  # Display the result

# Function to calculate the area of a circle
def circle(radius):
    pi = 3.14  # Approximation of π (pi)
    area = pi * radius * radius  # Calculate the area of the circle
    print("The area of the circle is " + str(area) + " square units.")  # Display the result

# Test the functions with chosen values
square(4)
circle(5)
