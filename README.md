# ERIC

# How to Run the Application

## Continuous Integration (CI)

1. You need to have a `.github/workflows/python-app.yml` file.
2. Once you write it, GitHub will automatically run the CI.

## Continuous Deployment (CD)

1. You need to have a Heroku account.
2. Using the Heroku CLI, type the command `heroku login`.
3. Then, run the command `heroku create`.
4. Use the command `heroku authorizations:create` to create a token to push the code to Heroku.
5. Store the token in GitHub secrets.
6. Store the Heroku app name as well in secrets.

