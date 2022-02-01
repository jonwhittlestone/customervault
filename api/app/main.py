import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)
    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()


def start():
    """
    Configuration of uvicorn
    For more settings see uvicorn.config
    """
    uvicorn.run(app=app, host="127.0.0.1", port=7998, server_header=False)


if __name__ == "__main__":
    start()


@app.get("/")
def read_root():
    return {"Hello": "Customer"}


@app.get("/healthcheck", status_code=status.HTTP_200_OK)
def perform_healthcheck():
    """
    Simple route for the GitHub Actions to healthcheck on.

    More info is available at:
    https://github.com/akhileshns/heroku-deploy#health-check

    It basically sends a GET request to the route & hopes to get a "200"
    response code. Failing to return a 200 response code just enables
    the GitHub Actions to rollback to the last version the project was
    found in a "working condition". It acts as a last line of defense in
    case something goes south.

    Additionally, it also returns a JSON response in the form of:

    {
      'healtcheck': 'Everything OK!'
    }
    """
    return {"healthcheck": "Everything OK!"}
