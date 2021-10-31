from flask import Flask, render_template, request

app = Flask(__name__)

registered_user = []


class users:
    def __init__(self, firstname, lastname, email, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.username = username
        self.password = password


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        for user in registered_user:
            if request.form['username'] == user.username and request.form['password'] == user.password:
                return render_template('user.html')
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


@app.route("/showSignUp", methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['confirmpassword']:
            error = 'Password mismatch. Please try again.'
        else:
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            registered_user.append(users(firstname, lastname, email, username, password))
            return render_template('index.html', message="Please log in with your new username and password")
    return render_template('register.html', error=error)


if __name__ == "__main__":
    app.run()
