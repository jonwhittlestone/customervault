import asyncio

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient

from src.main import app


@pytest.fixture(scope="session")
def event_loop():
    return asyncio.get_event_loop()


@pytest.fixture(scope="module", autouse=True)
async def client():
    """Async server client that handles lifespan and teardown"""

    async with LifespanManager(app):
        async with AsyncClient(app=app, base_url="http://test") as _client:
            try:
                yield _client
            except Exception as exc:  # pylint: disable=broad-except
                print(exc)
