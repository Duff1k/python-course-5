from __future__ import annotations
from typing import Optional


class Transport:

    def __init__(self, id: str, current_location: str):
        self.id: str = id
        self.current_speed: float = 0.0
        self.current_location: str = current_location
        self.battery_level: float = 100.0

    def _consume_battery_for_speed(self, speed_delta: float) -> None:
        needed = max(speed_delta, 0) * 1.0
        if self.battery_level < needed:
            print("Недостаточно заряда для поездки.")
            return
        self.battery_level = max(self.battery_level - needed, 0)

    def move(self, new_location: str, new_speed: float) -> None:
        if new_speed < 0:
            new_speed = 0

        needed = new_speed * 1.0
        if self.battery_level < needed:
            print("Недостаточно заряда для поездки.")
            return

        self.battery_level -= needed
        self.current_location = new_location
        self.current_speed = new_speed

    def charge(self, to_level: float) -> None:
        self.battery_level = min(max(to_level, 0), 100)

    def get_info(self) -> str:
        return (
            f"ID: {self.id}; "
            f"speed: {self.current_speed}; "
            f"location: {self.current_location}; "
            f"battery: {self.battery_level}%"
        )


class ElectricScooter(Transport):

    def __init__(self, id: str, current_location: str, is_rented: bool = False):
        super().__init__(id, current_location)
        self.is_rented: bool = is_rented

    def move(self, new_location: str, new_speed: float) -> None:
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, new_speed)


class Drone(Transport):

    def __init__(self, id: str, current_location: str):
        super().__init__(id, current_location)
        self.altitude: float = 0.0

    def take_off(self, to_altitude: float) -> None:
        # Взлёт на указанную высоту
        if to_altitude <= 0:
            self.altitude = 0.0
            return
        self.altitude = to_altitude

    def land(self) -> None:
        # Посадка: высота в 0
        self.altitude = 0.0

    def move(self, new_location: str, new_speed: float) -> None:
        if self.altitude <= 0:
            print("Дрон должен быть в воздухе, чтобы перемещаться.")
            return

        before_location = self.current_location
        super().move(new_location, new_speed)

        if self.current_location == new_location and new_speed >= 0:
            print(f"Дрон летит в {self.current_location} на высоте {self.altitude} м.")



class GPSNavigator:
    def calculate_route(self, from_location: str, to_location: str) -> str:
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    def perform_emergency_landing(self) -> None:
        if hasattr(self, "current_speed"):
            self.current_speed = 0
        if hasattr(self, "altitude"):
            self.altitude = 0
        if hasattr(self, "battery_level"):
            self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id: str, current_location: str):
        super().__init__(id, current_location)
        self.package: Optional[str] = None

    def load_package(self, package_name: str) -> None:
        self.package = package_name

    def deliver_package(self) -> None:
        if self.package is None:
            print("Нет посылки для доставки.")
            return

        if self.altitude != 0:
            print("Предупреждение: дрон должен находиться на земле для доставки.")
            return

        print(f"Посылка \"{self.package}\" доставлена!")
        self.package = None

    def get_info(self) -> str:
        base = super().get_info()
        pkg = self.package if self.package is not None else "—"
        return f"{base}; altitude: {self.altitude} м; package: {pkg}"


# код (demo)
if __name__ == "__main__":
    print("=== Transport ===")
    t = Transport("T-1", "Depot")
    print(t.get_info())
    t.move("Center", 12)
    print(t.get_info())
    t.charge(80)
    print(t.get_info())
    print()

    print("=== ElectricScooter ===")
    s = ElectricScooter("S-1", "Dock-7", is_rented=False)
    s.move("Street-1", 10)
    s.is_rented = True
    s.move("Street-1", 10)
    print(s.get_info())
    print()

    print("=== Drone ===")
    d = Drone("D-1", "Warehouse")
    d.move("Point-A", 15)
    d.take_off(50)
    d.move("Point-A", 15)
    print(d.get_info())
    d.land()
    print(d.get_info())
    print()

    print("=== DeliveryDrone ===")
    dd = DeliveryDrone("DD-1", "Hub")
    print(dd.calculate_route("Hub", "Client-42"))
    dd.load_package("Order#42")
    dd.take_off(30)
    dd.move("Client-42", 20)
    print(dd.get_info())
    dd.deliver_package()
    dd.land()
    dd.deliver_package()
    print(dd.get_info())
    dd.take_off(10)
    dd.current_speed = 5
    dd.perform_emergency_landing()
    print(dd.get_info())
