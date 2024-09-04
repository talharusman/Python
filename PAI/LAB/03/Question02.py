try:
    with open(r'text02.txt', 'r') as fileobj:
        content = fileobj.read()
except Exception as e:
    print(str(e))
else:
    original_word = input("Enter word which you want to replace: ")
    new_word = input("Enter new word: ")


    content = content.replace(original_word, new_word)

    with open(r'text02.txt', 'w') as fileobjw:
        fileobjw.write(content)