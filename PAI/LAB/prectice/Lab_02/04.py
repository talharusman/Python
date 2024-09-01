
def MyFunction():
    name = input("Sir Ente your good name: ")
    print(f"hallow sir {name}")
    print("I hope you are fine, let me know how I can help you!")

    response = input("Are you fine? (yes/no): ")

    if response.lower() == "yes":
        print("Share your problem with us: ")
        problem = input()
        print("Thanks for your feedback, we will resolve your problem.")
    else:
        print("\n\n\n")
        print("             Okay! Good to see you, stay connected             ")
        print("\n\n\n")

MyFunction()
