def replace_letter(wrong, correct, word):
    try:
        with open(r"LAB03\Text07.txt", 'r+') as file_obj:
            content = file_obj.read()
            new_content = content.replace(word, word.replace(wrong, correct))
            file_obj.seek(0)
            file_obj.write(new_content)
            file_obj.truncate()
        print("File updated successfully.")
    except FileNotFoundError:
        print("The file does not exist.")
    except IOError:
        print("Issue occurred while reading or writing the file.")
    except Exception as e:
        print(str(e))

# Example usage:
replace_letter('S', 'T', 'Salha')