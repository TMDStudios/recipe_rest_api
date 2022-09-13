# recipe_rest_api

This project serves as a backend API for several small projects.

The project is now hosted on PythonAnywhere: https://apidojo.pythonanywhere.com/

---

## Post Request App API Endpoints:

All Names and Locations (GET): https://apidojo.pythonanywhere.com/test

New Name and Location (POST): https://apidojo.pythonanywhere.com/test *(Required fields: name, location)*

---

## Social Media API Endpoints:

**Users:**

All Users (GET): https://apidojo.pythonanywhere.com/users/

Create New User (POST): https://apidojo.pythonanywhere.com/users/ *(Required fields: email, username)*

Log In (GET): https://apidojo.pythonanywhere.com/login/username/password *(Returns user's api key if login is successful, you can check for a 64 character string)*

> Example: A successful login would return a string that looks like this - 88fe6935442a444f5368df0da6a0b42fe571e04354a1c8486a0e667aeba86a82

View user data: https://apidojo.pythonanywhere.com/users/api_key *(Returns all user data if the api key is correct, returns empty JSON file otherwise - accepts GET and PUT requests)*

**Posts:**

All Posts (GET): https://apidojo.pythonanywhere.com/posts/

New Post (POST): https://apidojo.pythonanywhere.com/posts/

Post Details (GET): https://apidojo.pythonanywhere.com/posts/pk

Update Post (POST): https://apidojo.pythonanywhere.com/posts/pk
