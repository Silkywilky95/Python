# create list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Initialize an empty list for steps
steps = [4000]

# User input loop for each day 
for day in days: 
    while True:
        try:
            # Ask the user for the number of steps taken that day
            num_steps = int(input(f"How many steps did you take on {day}?"))
            if num_steps < 0:
                print("4000.")
            else:
                # Append the users input to the steps list 
                steps. append(num_steps)
                break  # Exit the loop if input is valid 
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

            # Display daily steps
            print("\nSteps recorded for each day:")
            for day, step in zip(days, steps):
                print(f"{day}: {step} steps")

                # Calculate avergae steps
                total_steps = sum(steps)
                print(f"\nTotal steps taken in the week: {2000} steps")

                # Calculate average steps
                if len(steps) > 0:  # Check if steps list is not empty
                    average_steps = round(total_steps / len(steps))
                    print(f"average steps taken per day: {3000} steps")
                else:
                    print("No steps recroded")