users = {}

def register():
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists. Try another.")
        return
    
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

# Call the function to register a user
register()
