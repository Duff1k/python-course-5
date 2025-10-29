# -*- coding: utf-8 -*-
from typing import Optional
from Drone import Drone
from GPSNavigator import GPSNavigator
from EmergencyLanding import EmergencyLanding

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):

    def __init__(
        self,
        id: str,
        current_location: str,
        altitude: float = 0.0,
        package: Optional[str] = None,
        current_speed: float = 0.0,
        battery_level: float = 100.0,
    ) -> None:
        super().__init__(
            id=id,
            current_location=current_location,
            altitude=altitude,
            current_speed=current_speed,
            battery_level=battery_level,
        )
        self.package: Optional[str] = package

    def load_package(self, package_name: str) -> None:
        self.package = package_name

    def deliver_package(self) -> None:
        if self.altitude == 0.0:
            if self.package:
                print(f"Посылка {self.package} доставлена!")
                self.package = None
            else:
                print("Нет посылки для доставки.")
        else:
            print("Нельзя доставить: дрон не на земле.")

    def get_info(self) -> str:
        base = super().get_info()
        package_info = self.package if self.package is not None else "—"
        return f"{base} | Посылка: {package_info}"
