def check_last_letter(input_string):
   
    last_letter = input_string[-1].lower()  # Get the last letter and convert to lowercase
    vowels = 'aeiou'  # Define the vowels

    if last_letter in vowels:
        print(f"The last letter '{last_letter}' is a vowel.")
    else:
        print(f"The last letter '{last_letter}' is a consonant.")

    return

user_input = input("Enter a string: ")

check_last_letter(user_input)