# ERIC


**How to Run the application**
---------------------------------

*CI*
1)you need to have a .github/workflows/python-app.yml file
2) once you write it github will automatically run the CI

*CD*

1) You need to have Heroku account
2) using the Heroku CLI type command "heroku login"
3)Then you run the command "heroku create"
4)use the command "heroku authorizations:create" to create a token to push the code to heroku
5)Store the token in github secrets
6)Store the heroku app name as well in secrets

