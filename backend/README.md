# customervault-backend

## Installation without Docker -> Run App -> Commit with `pre-commit`

#### 1. Clone this repo & change working dir to backend

    $ cd ./backend

#### 2. Install [poetry](https://github.com/python-poetry/poetry#installation)

#### 3. Set [poetry config](https://python-poetry.org/docs/configuration/#virtualenvsin-project) to install to a virtualenv in the workspace
    $ poetry config virtualenvs.in-project true
#### 4. Ensure cache is healthy
    $ poetry run pip --version || rm -rf .venv

#### 5. Install dependencies
    $ poetry install
#### 6. Verify installation
    $ poetry check
#### 7. Install the pre-commit git hook scripts
    $ pre-commit install
#### 8. Run test
    $ poetry run test

#### 9. Check [coverage](https://coverage.readthedocs.io/en/coverage-5.5/install.html)
    $ poetry run coverage html

#### 10. Run application locally

    $ poetry run start
    # Or another way
    $ uvicorn src.main:app --port 7998 --reload

- API available at http:///localhost:7998/
- Swagger UI docs available at http://localhost:7998/docs
- ReDoc docs available at http://localhost:7998/redoc

#### 11. Build
    $ poetry build -f sdist
## License

This project is licensed under the terms of the MIT license.
