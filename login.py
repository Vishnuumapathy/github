correct_username = "user123"
correct_password = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password.")