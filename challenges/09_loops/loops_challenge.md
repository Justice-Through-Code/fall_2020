# Loops Challenge: Log In/Sign Up Page

<img src="https://image.freepik.com/free-vector/login-template_1017-6719.jpg" width="800">


In this challenge, you're given a script called `login_challenge.py` that you'll be working on to create a mock up of a log in/sign up page on a website. To get started, make a folder inside your `jtc_class_code/challenges` called `09_loops`, and put `login_challenge.py` in it.

## Main Challenge: Create the basic log in and sign up functionality.

In this challenge, you will be creating a python program which will ask users to sign up or log in for a hypothetical website. You will store their usernames and a four digit password of their choosing in two lists (in a real website, this password would need to be encrypted for security reasons but we won't worru about that for now). The program begins by asking the user if they wish to log in or sign up. If they choose to login, the program will ask them for their username, and then their password. If the username is one which your program has saved and the password is the one originally input with this username, the terminal will print out "Successfully logged in!" and otherwise will print out "Your username or password is incorrect." The user will then be sent back to the "main page" where they can choose to sign up or log in again (yes, this isn't the accurate reaction to a user logging in but we do this for simplicity's sake). If a user chooses to sign in, they are asked for a username. If that username is already in use, they are told "Sorry, that username is already taken" and they go back to the home page. Otherwise, they input a password and the user's username and password are saved in the correct lists. 

### Extra Challenge 1: 

If a user tries to sign up with an already used username, they are not sent back to the "main page" to type in 1 or 2 again, but rather they have the opportunity to input another new username (this will require a new inner loop). Keep in mind, this can happen more than once. The user should be asked for a username until they input one which isn't already in use.

#### Extra Challenge 2:

If a user logs in and their username isn’t one of the saved users, the program tells them “This username is not associated with an account” but if the password is incorrect, the program tells them “Your password is incorrect." This allows for users to get more information as to what they did wrong, instead of the broad response "Your username or password is incorrect."

### Extra Challenge 3:

Make your program’s sign up feature only accept usernames which are emails. At sign up, if a username is input which isn’t a valid email, the user is told and asked to input a new username.

### SUPER CHALLENGE:

Add a forgot your password option to the program which asks a user a security question whose answer was set during sign up. If they respond correctly, they can input a new password. (You will need a new list for the security question responses)

### Pushing to github:

Great job! Now, as the final part of your workflow for this challenge, let's stage (`git add`), commit (*don't forget a commit message*), and push the `login_challenge.py` script you worked on to your `jtc_class_code` github repository. 

* Remember to check your Github repo online at the end to make sure this worked

**Congrats! You finished the login challenge!**
