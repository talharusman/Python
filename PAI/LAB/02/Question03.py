def convert_url(user_url):
    if user_url.startswith("http://www."):
        domain_name = user_url[11:]
        new_url = domain_name + ".com"
        print(f"The converted URL is: {new_url}")
    else:
        print("Invalid URL. Please enter a URL starting with http://www.")

user_url = input("Enter a URL starting with http://www.: ")
convert_url(user_url)