from dataclasses import dataclass
from random import randint

from core.models import System, Solar


@dataclass
class SolarDTO:
    x: float
    y: float
    color: str
    radius: float


class SolarController:
    COLOR_ELEMENTS = '0123456789ABCDEF'

    @staticmethod
    def get_random_color() -> str:
        return f"""#{''.join(
            [
                SolarController.COLOR_ELEMENTS[
                    randint(0, len(SolarController.COLOR_ELEMENTS) - 1)
                ]
                for _ in range(6)
            ]
        )}"""

    def __init__(self, solar: Solar):
        self.solar = solar

    @staticmethod
    async def create_random_solar(system: System) -> 'SolarController':
        solar = await Solar.objects.acreate(
            system=system,
            x=0.5,
            y=0.5,
            radius=randint(2, 4) / 10,
            color=SolarController.get_random_color()
        )
        return SolarController(solar)

    def get_render_info(self) -> SolarDTO:
        return SolarDTO(
            color=self.solar.color,
            radius=self.solar.radius,
            x=self.solar.x,
            y=self.solar.y
        )
