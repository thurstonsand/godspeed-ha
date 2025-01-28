"""Test Godspeed setup process."""

from unittest.mock import patch

from homeassistant.exceptions import ConfigEntryNotReady
import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.godspeed import (
    GodspeedDataUpdateCoordinator,
    async_reload_entry,
    async_setup_entry,
    async_unload_entry,
)
from custom_components.godspeed.const import DOMAIN

from .const import MOCK_CONFIG


# We can pass fixtures as defined in conftest.py to tell pytest to use the fixture
# for a given test. We can also leverage fixtures and mocks that are available in
# Home Assistant using the pytest_homeassistant_custom_component plugin.
# Assertions allow you to verify that the return value of whatever is on the left
# side of the assertion matches with the right side.
async def test_setup_unload_and_reload_entry(hass):
    """Test entry setup and unload."""
    # Create a mock entry so we don't have to go through config flow
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

    # Mock the API client
    with patch(
        "custom_components.godspeed.GodspeedApiClient.async_get_data",
        return_value={"test": "test"},
    ):
        # Set up the entry and assert that the values set during setup are where we expect
        assert await async_setup_entry(hass, config_entry)
        assert DOMAIN in hass.data and config_entry.entry_id in hass.data[DOMAIN]
        assert isinstance(
            hass.data[DOMAIN][config_entry.entry_id], GodspeedDataUpdateCoordinator
        )

        # Reload the entry and assert that the data from above is still there
        await async_reload_entry(hass, config_entry)
        assert DOMAIN in hass.data and config_entry.entry_id in hass.data[DOMAIN]
        assert isinstance(
            hass.data[DOMAIN][config_entry.entry_id], GodspeedDataUpdateCoordinator
        )

        # Unload the entry and verify that the data has been removed
        assert await async_unload_entry(hass, config_entry)
        assert config_entry.entry_id not in hass.data[DOMAIN]


async def test_setup_entry_exception(hass):
    """Test ConfigEntryNotReady when API raises an exception during entry setup."""
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

    # In this case we simulate an error during the API call
    with patch(
        "custom_components.godspeed.GodspeedApiClient.async_get_data",
        side_effect=Exception("Test error"),
    ), pytest.raises(ConfigEntryNotReady):
        assert await async_setup_entry(hass, config_entry)
