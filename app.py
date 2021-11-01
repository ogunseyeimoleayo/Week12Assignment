# Using Flask, python's framework for web application
from flask import Flask, render_template, request

app = Flask(__name__)

# Creating a global variable registered_user to keep the list of all users who registered
registered_user = []


# Creating class user showing characteristics of the users that is going to be inputted
class Users:
    def __init__(self, firstname, lastname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password


# This method renders the landing page - index.html
@app.route("/")
def main():
    return render_template('index.html')


# This method handles the rendering of the login page with GET and
# also authenticates the user with the POST method.
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # check the list of registered user for username and password
        for user in registered_user:
            if request.form['username'] == user.username and request.form['password'] == user.password:
                return render_template('user.html')
        else:
            error = 'Invalid Credentials. Please try again.'
    # renders the login page if method is GET or the credential is invalid
    return render_template('login.html', error=error)


# This method handles the user's registration with POST
# and renders the registration page with GET
@app.route("/showSignUp", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        # checks if there is a match between the password and confirm_password
        if request.form['password'] != request.form['confirm_password']:
            error = 'Password mismatch. Please try again.'
        else:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            registered_user.append(Users(firstname, lastname, email, username, password))
            return render_template('index.html', message="Please log in with your new username and password")
    # renders the register.html page if method is GET or if an error occurred
    return render_template('register.html', error=error)


# This is the main method where execution starts
if __name__ == "__main__":
    app.run()
