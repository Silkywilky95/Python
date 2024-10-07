""" https://chatgpt.com/share/67041fe3-6afc-8011-b1d2-166f48dc3f2c

I used chat gtp to help me delevop this code"""


# Initialize the seating list
seating_list = list(range(1, 35))  # seats numbered 1 to 36

def display_available_seats():
    """Displays the current available seats."""
    print("Available seats:", seating_list)

def ticket_purchase():
    """Handles the ticket purchasing process."""
    while True:
        display_available_seats()
        try:
            # Prompt the customer to select a seat
            selected_seat = int(input("Just enter the seat number you wish to purchase already (or enter '0' to finish:"))

            if selected_seat == 0:
                print("Thank you for your giving us your money!")
                break

            # Check if the selected seat is valid and available 
            if selected_seat in seating_list:
                seating_list.remove(selected_seat)
                print(f"Seat {selected_seat} is now yours you sad soul!")
            else:
                print("Sorry, that seat is either already sold or the concert is cancelled because people dont wanna see taylor swift. Please choose another seat.")

        except ValueError:
            print("Invalid input. Enter a valid seat number or '0' to finish.")

# Run the ticket purchase function
ticket_purchase()
