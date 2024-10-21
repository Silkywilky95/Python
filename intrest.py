""" i used chat gtp to make this code to get caught up in class
https://chatgpt.com/share/67159d10-1edc-8011-9923-6205646c2166
"""


def calculate_interest(principal, rate, time):
    # Apply the formula for simple interest
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Gather input from the customer
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the rate of interest: "))
investment_time = float(input("Enter the time (in years): "))

# Call the function and store the result
calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

# Print the result in a user-friendly formatted string
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
at an interest rate of {interest_rate}% over a period of {investment_time} years is: \
${calculated_interest:,.2f}")
