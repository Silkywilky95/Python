"""
I used chat gtp to make this code to get my late work in

https://chatgpt.com/share/670845e4-c314-8011-af77-5457197bdaec

"""


# Define the custom_song function
def custom_song(object_in_sky, adjective1, place, action, comparison_noun, adjective2, resembling_object, emotion):
    song = f"""
    Twinkle, twinkle, little {object_in_sky},
    How I wonder what you are!
    Up above the {place} so {adjective1},
    Like a {comparison_noun} {action} in the sky.
    
    Twinkle, twinkle, little {object_in_sky},
    How I wonder what you are!
    You remind me of a {adjective2} {resembling_object},
    Filling me with {emotion} from afar.
    """
    print(song)

# Collect user input
object_in_sky = input("Enter an object in the sky (e.g., star, moon): ")
adjective1 = input("Enter an adjective to describe the object: ")
place = input("Enter a place (e.g., forest, ocean): ")
action = input("Enter a type of action (e.g., glowing, shining): ")
comparison_noun = input("Enter a noun for comparison (e.g., diamond, light): ")
adjective2 = input("Enter another adjective to describe the comparison noun: ")
resembling_object = input("Enter an object the noun resembles: ")
emotion = input("Enter an emotion (e.g., joy, wonder): ")

# Call the function with user inputs
custom_song(object_in_sky=object_in_sky, adjective1=adjective1, place=place, action=action, 
            comparison_noun=comparison_noun, adjective2=adjective2, resembling_object=resembling_object, 
            emotion=emotion)
