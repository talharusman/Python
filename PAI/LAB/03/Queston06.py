def write_question_to_file():
    try:
        sentence = input("Enter a sentence: ")
        sentence = sentence.strip()

        if sentence.endswith("?"):
            with open("questions.txt", "a") as f:
                f.write(sentence + "\n")
            print("Question written to questions.txt")
        else:
            print("The sentence is not a question.")

    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

write_question_to_file()