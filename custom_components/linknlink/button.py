"""Support for linknlink buttons."""
from __future__ import annotations

import logging
import socket
import asyncio

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import LinknLinkCoordinator
from .entity import LinknLinkEntity

_LOGGER = logging.getLogger(__name__)

BUTTONS: tuple[ButtonEntityDescription, ...] = (
    ButtonEntityDescription(
        key="rmkey_pwr",
        name="pwr",
    ),
    ButtonEntityDescription(
        key="rmkey_mute",
        name="mute",
    ),
    ButtonEntityDescription(
        key="rmkey_up",
        name="up",
    ),
    ButtonEntityDescription(
        key="rmkey_down",
        name="down",
    ),
    ButtonEntityDescription(
        key="rmkey_left",
        name="left",
    ),
    ButtonEntityDescription(
        key="rmkey_right",
        name="right",
    ),
    ButtonEntityDescription(
        key="rmkey_ok",
        name="ok",
    ),
    ButtonEntityDescription(
        key="rmkey_home",
        name="home",
    ),
    ButtonEntityDescription(
        key="rmkey_menu",
        name="menu",
    ),
    ButtonEntityDescription(
        key="rmkey_back",
        name="back",
    ),
    ButtonEntityDescription(
        key="rmkey_volume_up",
        name="volume_up",
    ),
    ButtonEntityDescription(
        key="rmkey_volume_down",
        name="volume_down",
    ),
    ButtonEntityDescription(
        key="rmkey_set",
        name="set",
    ),
    ButtonEntityDescription(
        key="rmkey_voice",
        name="voice",
    ),
        ButtonEntityDescription(
        key="rmkey_channel1",
        name="channel1",
    ),
    ButtonEntityDescription(
        key="rmkey_channel2",
        name="channel2",
    ),
        ButtonEntityDescription(
        key="rmkey_tv_av",
        name="tv_av",
    ),
)

buttonDic = {}

def cabk(data: str):
    print(f"trigger {data}")
    buttonDic[data].press()

async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the linknlink sensor."""

    coordinator: LinknLinkCoordinator = hass.data[DOMAIN][config_entry.entry_id]
    if "rmkey_pwr" in coordinator.data:
        buttonDic.clear()
        entities = []
        for description in BUTTONS:
            entity = LinknLinkButton(coordinator, description)
            entities.append(entity)
            buttonDic[description.key] = entity
        async_add_entities(entities)
        # 注册回调
        coordinator.api.cb = cabk


class LinknLinkButton(LinknLinkEntity, ButtonEntity):
    """Representation of a linknlink button."""

    def __init__(
        self,
        coordinator: LinknLinkCoordinator,
        description: ButtonEntityDescription,
    ) -> None:
        """Initialize the button."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{coordinator.api.mac.hex()}-{description.key}"

    def press(self) -> None:
        """Handle the button press."""
        print("button press1.")
        print(self.entity_description)

    async def async_press(self) -> None:
        """Handle the button press."""
        print("button press2.")
        print(self.entity_description)