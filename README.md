# Lunch bot

Bot for suggestions where to lunch

Run local build:

```console
LUNCH_BOT_FLASK_CONFIG=$(pwd)/docker/flask_cfg.py FLASK_ENV=development FLASK_APP=lunch_bot:app poetry run flask run --debugger --reload
```

## Code formatting

To format code type the following:

```console
$ black lunch_bot
```

To sort imports:

```console
$ isort -rc lunch_bot
```

```

## Project structure:
├── docker                          <- Files related to deployment via docker
|   ├── Dockerfile
|   ├── flask_cfg.py
|   └── gunicorn_cfg.py
|
├── iac                             <- Files related to deployment via docker
|   ├── ci
|   |   ├── build.yaml              <- Describes how and on what event to build project
|   |   ├── deploy-prod.yaml        <- Describes how and on what event to deploy project to pord
|   |   └── deploy-test.yaml        <- Describes how and on what event to deploy project to test
|   └── template-nomad.hcl          <- Get and set env vars. Set other variables of app 
├── tests          
|   └── test_api.py                 <- Api tests
|
├── lunch_bot 
    ^--------------------------------- Name of service in snake case
|   ├── __init__.py                 <- Says that folder is module
|   ├── error_handlers.py           <- Caught errors handlers 
|   ├── errors.py                   <- Custom errors implementation
|   ├── log.py                      <- Loguru sink, formatter and logger patch for correlation_id
|   ├── main.py                     <- Main file with configuration
|   ├── py.typed                    <- Says that module is typed
|   ├── routes.py                   <- Application routes
|   └── validator.py                <- Implement your data validator here 
│
├── .env.sample                     <- Excample of .env file. You can use it to set environment variables.
├── .gitignore                      <- Git will ignore matching files and folders
├── .gitlab-ci.yml                  <- Combines instructions from iac folder
├── pyproject.toml                  <- Dependencies. execute in console `poetry install` to install them. `poetry add LIB_NAME` to add new dependency.
├── README.md                       <- file you are reading
└── setup.cfg                       <- linter and isort settings
```

Repository created from [bcd-flask-template](https://github.com/biocad/bcd-flask-template) using template version [b97990cfc11719e5d71c629b9d51340f842d3cbd](https://github.com/biocad/bcd-flask-template/commit/b97990cfc11719e5d71c629b9d51340f842d3cbd).