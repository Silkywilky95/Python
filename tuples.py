""" I used chat gtp to make this code to get caught up in class

https://chatgpt.com/share/6715a3cc-ab54-8011-80cb-81cb12e9a739

"""


# Define the main function
def main():
    # Create a tuple named programming_classes
    programming_classes = ('Intro to Python', 'Advanced Python', 'Database Essentials', 
                           'Web Development Basics', 'Data Structures in Python', 
                           'Web Design Fundamentals')

    # Use a for loop to print each class in the tuple
    print("Programming Classes:")
    for course in programming_classes:
        print(course)

    # Print the number of classes using the len function
    print("\nTotal number of classes:", len(programming_classes))

# Call the main function
if __name__ == "__main__":
    main()
