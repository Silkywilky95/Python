""" I used chat gtp to make this code to get caught up in class thank you

https://chatgpt.com/share/6715ac57-056c-8011-b647-d6b568fef18e

"""
# Step 1: Create the NATO phonetic alphabet dictionary
nato_alphabet = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar', 
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango', 
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

# Step 2: Develop the spelling program
def spell_word_with_nato(word):
    for letter in word.upper():
        if letter in nato_alphabet:
            print(nato_alphabet[letter])

# Step 3: Encapsulate logic within the main function
def main():
    user_input = input("Enter a word to spell with NATO phonetic alphabet: ")
    spell_word_with_nato(user_input)

# Step 4: Test the program
if __name__ == "__main__":
    main()


