def show_info(**details):
    info_string = ""
    for key, value in details.items():
        # Add each key-value pair to the string in a readable format
        info_string += f"{key.capitalize()}: {value}\n"

    return info_string.strip()

print(show_info(name="Talha Rusman", age=18, occupation="AI ka chita"))
