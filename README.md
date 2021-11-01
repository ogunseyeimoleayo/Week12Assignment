# QueensMedicalCenter

### About the App
This a simple web application showing user registration and login.
It also shows how we can authentication user by making sure only users with invalid username and password are denied access
It also shows user authorization by making sure that registered users have access to the resources on the web portal, in
this case it is a "Successful Login" message.

### Pages
 * index.html - This is the entrypoint of the application, 
                 it is the landing page which has links to the other pages
 * login.html - This is the login page, it is called when the user clicks on the signing in link. 
                It accepts username and password.
 * register.html - This is the registration page, it is called when the signup link is clicked.
 * user.html - This page is rendered when user is logged in successfully.

### The Functions
All backend functions are in app.py file

### How to run
* Install Python and import Flask library
* Run python app.py to see the address of the application
* Open http://127.0.0.1:5000/ on browser to access the application

