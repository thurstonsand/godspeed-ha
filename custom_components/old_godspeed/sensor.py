"""Sensor platform for Godspeed."""

from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import GodspeedEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([GodspeedSensor(coordinator, entry)])


class GodspeedSensor(GodspeedEntity):
    """godspeed Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON

    @property
    def device_class(self):
        """Return de device class of the sensor."""
        return "godspeed__custom_device_class"
