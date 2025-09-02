users = {
    "Shobhit":"12345",
    "Pushkar":"password123",
    "AtharvaP":"querty",
}
for i in range(1,4):

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username in users:
        if users[username] == password:
            print("Login Successful")
    else:
        print("Login Failed")
        if i == 3:
            print("Max login attempts reached")
        print("Attempt: ", i)
