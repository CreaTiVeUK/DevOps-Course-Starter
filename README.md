# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install

```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Sign up to Azure and insert your Connection string & DB name in the .env file.
Create 2 oAuth apps in git (dev and prod) and insert your dev client id/secrets in the .env file and prod details in heroku i.e.:
    - Application name: to-do app
    - Homepage URL: http://localhost:5000
    - Authorization callback URL: http://localhost:5000/login/callback

## Running the App

Once all the dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Ansible deployment to additional nodes

1. Move into the ansible directory
2. Edit inventory.txt by adding the Managed Node IP Address to deploy the app to.
3. Create an ansible encrypted file to store your Mongo DB secrets by running
```bash
$ ansible-vault create --vault-id my_pass@prompt mongo_secrets.yml
```

You should see output similar to the following:
```bash
[DEPRECATION WARNING]: ...
New vault password (my_pass): 
Confirm new vault password (my_pass): 
```
Safely store your password and do not commit it!

4. Add and save your Mongo DB, Git and Flask secrets, by adding the following variables in and replacing the dots with your values:
secret_key=...
mongo_con_string=...
mongo_db_name=...
github_client_id=...
github_client_secret=...

5. Edit the inventory file by adding your managed node IPs, where you will deploy the app to i.e.:

[webserver]
123.123.123.123

6. Run the following to deploy:
```bash
$ ansible-playbook --ask-vault-pass deploy_todoApp.yaml -i inventory
```

7. In your browser enter the managed node IP address at port 5000 to view the app i.e.:
123.123.123.123:5000

## Dockerfile Image generation

1. Install Docker:
https://www.docker.com/products/docker-desktop/

2. Build and Run the image using any of the commands below for the required environments:
    
    Test (Reruns tests if any files recursivily matching the patterns were edited -> "*.py;*.html" ):
    ```bash
    $ docker build --target test --tag todo-app:test .
    $ docker run --env-file ./.env_test -it --mount type=bind,source="$(pwd)"/todo_app,target=/appcode/todo_app todo-app:test
    ```
    
    CI-Test:
    ```bash
    $ docker build --target ci-test --tag todo-app:ci-test .
    $ docker run --env-file ./.env_test todo-app:ci-test
    ```

    Development:
    ```bash
    $ docker build --target development --tag todo-app:dev .
    $ docker run --env-file ./.env -p 5000:5000 -it --mount type=bind,source="$(pwd)"/todo_app,target=/appcode/todo_app todo-app:dev
    ```

    Production:
    ```bash
    $ docker build --target production --tag todo-app:prod .
    $ docker run --env-file ./.env -p 8000:8000 todo-app:prod
    ```
    
    All:
    ```bash
    $ docker-compose up --build
    ```

## Testing the App

You can run the available tests pack, in development mode within the poetry environment by running the following from the project's root directory.

```bash
$ poetry run pytest
```

To run individual tests i.e.:

```bash
#poetry run pytest todo_app/tests/test_unit_tests.py::<Test Name>
poetry run pytest todo_app/tests/test_unit_tests.py::test_todo_items
```

## Heroku link to app
https://todo-app-simeon.herokuapp.com

## Licensing

MIT License

Copyright (c) [2022] [Simeon Penev]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.