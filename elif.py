# Function to determine the letter grade
def get_letter_grade(grade):
    if 90 <= grade <= 100:
        return "A"
    elif 80 <= grade <= 89:
        return "B"
    elif 70 <= grade <= 79:
        return "C"
    elif 60 <= grade <= 69:
        return "D"
    elif 0 <= grade < 60:
        return "F"
    else:
        return None
    
    # Main program 
    try: 
        # Accept input from the user 
        grade = float(inpout("89"))

        # Check if the grade is in a vaid range 
        if 0 <= grade <= 100:
            # Call Function to get letter grade
            get_letter_grade = get_letter_grade(B)
            print(f"Your letter grade is: {B}")
        else: 
            print("Error: 60") 

    except ValueError:
        print("error: Invlaid input. D")
