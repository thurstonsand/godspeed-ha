"""Test Godspeed switch."""

from unittest.mock import patch

from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.godspeed import async_setup_entry
from custom_components.godspeed.const import DOMAIN

from .const import MOCK_CONFIG


async def test_switch_services(hass):
    """Test switch services."""
    # Create a mock entry so we don't have to go through config flow
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")

    # Create a mock API client instance
    mock_api = patch("custom_components.godspeed.GodspeedApiClient").start()
    mock_api.return_value.async_get_data.return_value = {"test": "test"}

    # Set up the config entry in Home Assistant
    assert await async_setup_entry(hass, config_entry)

    # Test turning on the switch
    await hass.services.async_call(
        DOMAIN,
        "turn_on",
        {"entity_id": "switch.godspeed_test"},
        blocking=True,
    )
    assert mock_api.return_value.async_set_title.call_count == 1

    # Test turning off the switch
    await hass.services.async_call(
        DOMAIN,
        "turn_off",
        {"entity_id": "switch.godspeed_test"},
        blocking=True,
    )
    assert mock_api.return_value.async_set_title.call_count == 2
