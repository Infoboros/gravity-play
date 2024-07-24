from dataclasses import dataclass

from core.controllers.solar import SolarController, SolarDTO
from core.models import System, Window

@dataclass
class SystemDTO:
    solar: SolarDTO
    planets: []


class SystemController:
    def __init__(
            self,
            system: System,
            solar_controller: SolarController
    ):
        self.system = system
        self.solar_controller = solar_controller

    @staticmethod
    async def create_random_system(window: Window) -> 'SystemController':
        system = await System.objects.acreate(window=window)
        solar_controller = await SolarController.create_random_solar(system)
        return SystemController(
            system,
            solar_controller
        )

    def get_render_info(self) -> SystemDTO:
        return SystemDTO(
            solar=self.solar_controller.get_render_info(),
            planets=[]
        )

    async def next_state(self):
        pass
