# Accept five names fro the user
names = [] # initialize an empty list to store names

# Loop to get five names from the user
for i in range(5):
    name= input(f"Enter name {i + 1:} ") # Prompt user for a name 
    names.append(name)  # Append the entered name to the list


    # Implement Bubble sort to the list
    def bubble_sort(arr): 
        n = len(arr)  # Get length of the array
        for i in range(n):
            # Track if a swap was made during this pass
            swapped =  False 
            for j in range(0, n - i - 1):
                # Compare adjacent elements 
                if arr[j] > arr[j+ 1]:
                    # Swap if they are in the wrong order
                    arr[j], arr[j + 1], arr[j]
                    swapped = True # A swap has occured 
                    # If no swaps were made, the array is sorted 
                    if not swapped:
                        break

    # Sort names using the Bubble sort algorithm 
    bubble_sort(names)

    # print the sorted list
    print("\nSorted list of names:")
    print(names)  # Display the sorted list

    # Reverse the sorted list using a Python list method
    names.reverse()  # Reverse the order of the list

    # Print the final reversed list
    print("\nReversed sorted list of names:")
    print(names)  # Display the reversed list


     
    