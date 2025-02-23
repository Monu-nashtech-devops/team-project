# Simple Python Login System

users = {}  # Dictionary to store user credentials

def register():
    """Register a new user"""
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists! Try a different one.")
        return
    password = input("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login():
    ""
