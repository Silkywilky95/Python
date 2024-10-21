"""i used chat gtp make this code to get caught up in class

https://chatgpt.com/share/67159dd4-5cd0-8011-b321-9b8a7fff409c

"""

# Global constants for conversion factors
POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def calculate_bmi(weight_pounds, height_inches):
    """Calculates BMI using weight in pounds and height in inches, after converting to metric units."""
    # Convert weight to kilograms and height to meters
    weight_kg = weight_pounds * POUNDS_TO_KG
    height_meters = height_inches * INCHES_TO_METERS

    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi

def bmi_category(bmi):
    """Determines the BMI category based on the calculated BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    """Main function to handle user input, calculate BMI, and display results."""
    # Get user input for weight and height
    weight_pounds = float(input("Enter your weight in pounds: "))
    height_inches = float(input("Enter your height in inches: "))

    # Calculate BMI
    bmi = calculate_bmi(weight_pounds, height_inches)

    # Get BMI category
    category = bmi_category(bmi)

    # Display results
    print(f"Your BMI is: {bmi:.2f}")
    print(f"Your BMI category is: {category}")

# Run the program
if __name__ == "__main__":
    main()
