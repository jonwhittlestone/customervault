# customervault-api

## Getting started

- Installation without Docker
- Run App
- Commit with `pre-commit`

#### 1. Clone this repo & change working dir to backend

    $ cd ./api

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
```shell
poetry run uvicorn src.main:app --reload --host localhost --port 7998
```

- API available at http:///127.0.0.1:7998/
- Swagger UI docs available at http:///127.0.0.1/docs
- ReDoc docs available at http://localhost:7998/redoc

#### 11. Build
    $ poetry build -f sdist
#### 12. Before committing ensure changes will be accepted in CI/CD

    $ poetry run flake8 .
    $ poetry run isort .
    $ poetry run mypy .
    $ poetry run black .
    $ poetry run pre-commit run --all-files

## Docker

The Dockerfile uses multi-stage builds to run lint and test stages before building the production stage. If linting or testing fails the build will fail.

Build `development` stage image with:

```shell
docker build --network host --tag customervault-api --file docker/Dockerfile . --target development
```

Build image with:

```shell
docker build --network host --tag customervault-api --file docker/Dockerfile .
```

Run the container

```shell
docker run \
    -p 7998:7998 \
    customervault-api:latest
```

Run the container tests

```shell

```

Get a shell inside the container with:

```shell
docker run -it customervault-api:latest /bin/bash
```

## Deploying to Heroku

1. Log in to Heroku with Heroku CLI

```shell
heroku login
```

2. Log in to Container Registry

```shell
heroku container:login
```

3. With the image built (see above), push it to container registry
```shell
cd docker;
heroku container:push web -a customervault-pd --context-path ..
```

4. And then release it

```shell
heroku container:release web -a customervault-pd
```

5.



## License

This project is licensed under the terms of the MIT license.
