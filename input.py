# Budget Percentage Calculator
# This program calculates the percentage of a user's total budget that is spent 
# in various categories such as Housing, Utilities, Groceries, etc.

def calculate_percentage(amount_spent, total_budget):
    """
    This function calculates the percentage of a given amount spent from the total budget.
    :param amount_spent: Amount spent in a specific category
    :param total_budget: Total budget provided by the user
    :return: Percentage of the total budget
    """
    return (amount_spent / total_budget) * 100

def main():
    """
    Main function to collect budget data, calculate percentages, and display the results.
    """
    # Step 1: Prompt user to input their total budget
    total_budget = float(input("Enter your total budget: $"))

    # Step 2: Prompt user to input spending for different categories
    housing = float(input("Enter the amount spent on Housing (rent or mortgage): $"))
    utilities = float(input("Enter the amount spent on Utilities: $"))
    groceries = float(input("Enter the amount spent on Groceries: $"))
    transportation = float(input("Enter the amount spent on Transportation: $"))
    health_care = float(input("Enter the amount spent on Health Care: $"))
    personal_care = float(input("Enter the amount spent on Personal Care: $"))
    clothing = float(input("Enter the amount spent on Clothing: $"))
    debt = float(input("Enter the amount spent on Debt: $"))

    # Step 3: Calculate percentages for each category
    housing_percentage = calculate_percentage(housing, total_budget)
    utilities_percentage = calculate_percentage(utilities, total_budget)
    groceries_percentage = calculate_percentage(groceries, total_budget)
    transportation_percentage = calculate_percentage(transportation, total_budget)
    health_care_percentage = calculate_percentage(health_care, total_budget)
    personal_care_percentage = calculate_percentage(personal_care, total_budget)
    clothing_percentage = calculate_percentage(clothing, total_budget)
    debt_percentage = calculate_percentage(debt, total_budget)

    # Step 4: Display the budget breakdown in a user-friendly format
    print("\n------- Budget Breakdown -------")
    print(f"Housing: ${housing:.2f} ({housing_percentage:.2f}%)")
    print(f"Utilities: ${utilities:.2f} ({utilities_percentage:.2f}%)")
    print(f"Groceries: ${groceries:.2f} ({groceries_percentage:.2f}%)")
    print(f"Transportation: ${transportation:.2f} ({transportation_percentage:.2f}%)")
    print(f"Health Care: ${health_care:.2f} ({health_care_percentage:.2f}%)")
    print(f"Personal Care: ${personal_care:.2f} ({personal_care_percentage:.2f}%)")
    print(f"Clothing: ${clothing:.2f} ({clothing_percentage:.2f}%)")
    print(f"Debt: ${debt:.2f} ({debt_percentage:.2f}%)")
    print("-------------------------------")

# Execute the main function
if __name__ == "__main__":
    main()
