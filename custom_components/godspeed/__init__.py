"""
Custom integration to integrate Godspeed with Home Assistant.

For more details about this integration, please refer to
https://github.com/thurstonsand/godspeed-ha
"""

from __future__ import annotations

from dataclasses import dataclass
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform


@dataclass
class RuntimeData:
    """Runtime data for the Godspeed"""

    api_key: str


_LOGGER: logging.Logger = logging.getLogger(__package__)

PLATFORMS: list[Platform] = [Platform.TODO]

type GodspeedConfigEntry = ConfigEntry[RuntimeData]
