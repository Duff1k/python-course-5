# -*- coding: utf-8 -*-
from Transport import Transport
class Drone(Transport):

    def __init__(
        self,
        id: str,
        current_location: str,
        altitude: float = 0.0,
        current_speed: float = 0.0,
        battery_level: float = 100.0,
    ) -> None:
        super().__init__(
            id=id,
            current_location=current_location,
            current_speed=current_speed,
            battery_level=battery_level,
        )
        self.altitude = max(0.0, float(altitude))

    def take_off(self, delta_altitude: float) -> None:
        delta_altitude = float(delta_altitude)
        self.altitude = max(0.0, self.altitude + delta_altitude)

    def land(self) -> None:
        self.altitude = 0.0

    def move(self, new_location: str, speed: float) -> None:

        if self.altitude <= 0.0:
            print("Дрон не может перемещаться: он на земле.")
            return
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        super().move(new_location, speed)

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base} | Высота: {self.altitude} м"
