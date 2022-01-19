import uvicorn
from fastapi import FastAPI
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
