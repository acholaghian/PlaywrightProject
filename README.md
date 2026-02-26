This is a simple test automation framework based on Playwright and Pytest. It has some test cases, page objects, Pytest fixtures, and an environment file which the framework gets the base URL and credentials from.

SETUP

1) Install Python 3.12 or greater.
2) Clone this repository.
3) In a terminal, navigate to the project root directory in your local cloned repo, and run the following:

`pip install -r requirements.txt`

4) Still in the terminal, run the following:

`playwright install`

This installs the browser binaries for Playwright to use in test runs.

5) In the project_root/config folder, duplicate the file `env.example.json`. Change the name to just `env.json` and open it. You will need to put a username and password into this file, to run the tests without friction. These credentials can be found at https://theinternet.herokuapp.com/login

PLEASE NOTE: Normally such auth credentials would be shared securely among team members, and never divulged. I have opted to maintain the best practice of NOT committing credentials into the repository. However, given that this is a personal portfolio project, for the sake of expediency, I outlined where the credentials can be found.

6) After putting the credentials into `env.json`, you should now be able to run all the tests. Simply entering `pytest` will run them all, but if you want to actually see the tests run, use this command:

`pytest --headed --slowmo=1000`

This will tell Playwright to run the tests with actual browser windows, and execute the testing steps at a visible pace.