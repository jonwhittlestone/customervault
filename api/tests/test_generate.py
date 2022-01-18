import pytest
from httpx import AsyncClient
from starlette.status import HTTP_200_OK


@pytest.mark.asyncio
async def test_read_root(client: AsyncClient):
    response = await client.get(
        "/",
    )
    assert response.status_code == HTTP_200_OK
