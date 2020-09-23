usernames = []
passwords = []

while (True):
#infinite loop used so user is constantly asked to login or sign up - not a great idea to use infinite loops in practice however. Use ctrl-c to exit the program at any time.

    response = input("Logging in? Type 1 and enter. Signing up? Type 2 and enter. ")

    if response == "1":
        print ("Log In")
        #ask the user for their username and password
        #run through the usernames list, checking if the user's input username is present, and if so, that the corresponding password matches as well
        #print out the correct response based on the username and password input

    elif response == "2":
        print ("Sign Up")
        #ask the user for a username
        #if the username is used already, tell the user and send them back to the main page
        #if not, ask for the users password and add their info to the lists

    else:
        #What should the program do when the user inputs a number which isn't 1 or 2?