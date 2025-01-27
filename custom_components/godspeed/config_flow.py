"""Config flow for Godspeed integration."""

from __future__ import annotations

from typing import Any

from homeassistant.config_entries import (
    CONN_CLASS_CLOUD_POLL,
    ConfigFlow,
    ConfigFlowResult,
)
from homeassistant.util import slugify
import voluptuous as vol

from .consts import DOMAIN

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required("api_access_token"): str,
    }
)


class GodspeedConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Godspeed."""

    VERSION = 1
    CONNECTION_CLASS = CONN_CLASS_CLOUD_POLL

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}

        # Uncomment the next 2 lines if only a single instance of the integration is allowed:
        # if self._async_current_entries():
        #     return self.async_abort(reason="single_instance_allowed")

        if user_input is None or user_input == {}:
            return self.async_show_form(
                step_id="user",
                data_schema=STEP_USER_DATA_SCHEMA,
                errors=errors,
            )

        api_access_token = slugify(user_input["api_access_token"])
        # Create entry
        return self.async_create_entry(
            title="Godspeed",
            data={"api_access_token": api_access_token},
        )
