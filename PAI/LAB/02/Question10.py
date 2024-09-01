def build_message(**info):
    message_parts = []
    for key, value in info.items():
        message_parts.append(f"{key.capitalize()}: {value}")
    return ", ".join(message_parts)

# Example usage:
message = build_message(name="Talha Rusman", age=20, city="Karachi", profession="Engineer")
print(message)
