This is the current status of the Smarter University System (SUS) backend. The communication between instructors and students as well as across students is immensely important for an academic institution. The SUS is designed to support instructors in delivering their lectures more effectively and efficiently. It also aims to provide students with the information they need to participate with as little overhead as possible.

# Code organization

The source code is divided into three main directories:

* `app`: contains all the application source code
* `test`: specifies test cases that will execute functions in `app`
* `data`: contains JSON files that store the data that is managed in the application

# Setup

The majority of the application can be executed without installing any additional dependencies. You have several choices of running the program. You can run the tests in the `test` folder or you can write your own python module that calls the functions in the application.

The application also has the beginning of an API. The endpoints are specified in `app/api.py`. The API is implemented using the Flask framework. Hence, to be able to run the API (which is not required), you should set up a virtual environment and install the application dependencies from within the root directory (Unix and Mac commands):

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

The Windows commands are very similar. Please post on the discussion board if you need support with this setup.

Once the dependencies are installed, the server can be started by running:

```bash
python app/server.py
```

If you are in VSCode, you can run the `Server Start` runtime configuration. That allows you to debug the source code. You can then use Postman or any other API tool of your choice to submit API calls.

# Test

This repository already configures the tests to successfully run in VSCode. After you open the project in VSCode, you should be able to click on the erlenmeyer flask symbol in the right-hand menu bar. That should open a list of all current test cases.

For more information about running tests in VSCode, see:

https://code.visualstudio.com/docs/python/testing
