usernames = []
passwords = []

while (True):
#infinite loop used so user is constantly asked to login or sign up - not a great idea to use infinite loops in practice however. Use ctrl-c to exit the program at any time.

    response = input("Logging in? Type 1 and enter. Signing up? Type 2 and enter. ")

    if response == "1":
        print ("Log In")
        username = input("Username: ")
        password = input("Password: ")
        successfulLogin = False

        for index in range(len(usernames)):
            if usernames[index] == username and passwords[index] == password:
                successfulLogin = True
        if successfulLogin:
            print ("Successfully logged in!")
        else:
            print ("Your username or password is incorrect")

    elif response == "2":
        print ("Sign Up")
        username = input("Username: ")
        usedUsername = False

        for user in usernames:
            if user == username:
                usedUsername = True
        if usedUsername:
            print ("Sorry that username is already taken")
        else:
            password = input("Password: ")
            usernames.append(username)
            passwords.append(password)
            print ("Successfully signed up!")

    else:
        print ("Please type 1 or 2")
