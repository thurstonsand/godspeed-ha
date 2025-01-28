"""Tests for Godspeed api."""

import asyncio

import aiohttp
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from custom_components.godspeed.api import GodspeedApiClient


async def test_api(hass, aioclient_mock, caplog):
    """Test API calls."""

    # To test the api submodule, we first create an instance of our API client
    api = GodspeedApiClient("test", "test", async_get_clientsession(hass))

    # Mock the GET response
    aioclient_mock.get(
        "https://jsonplaceholder.typicode.com/posts/1", json={"test": "test"}
    )

    assert await api.async_get_data() == {"test": "test"}

    # Mock the PATCH response
    aioclient_mock.patch(
        "https://jsonplaceholder.typicode.com/posts/1", json={"title": "test_title"}
    )

    await api.async_set_title("test_title")

    # Reset mock completely for timeout test
    aioclient_mock.clear_requests()
    aioclient_mock._mocks.clear()  # Reset all registered URLs

    # Test timeout
    aioclient_mock.get(
        "https://jsonplaceholder.typicode.com/posts/1", exc=asyncio.TimeoutError
    )

    assert await api.async_get_data() is None

    # Reset mock completely for client error test
    aioclient_mock.clear_requests()
    aioclient_mock._mocks.clear()

    # Test client error
    aioclient_mock.get(
        "https://jsonplaceholder.typicode.com/posts/1", exc=aiohttp.ClientError
    )

    assert await api.async_get_data() is None

    # Reset mock completely for HTTP error test
    aioclient_mock.clear_requests()
    aioclient_mock._mocks.clear()

    # Test HTTP error
    aioclient_mock.get("https://jsonplaceholder.typicode.com/posts/1", status=404)

    assert await api.async_get_data() is None
