class Transport:
    def __init__(self, transport_id: str, current_location: str = "Гараж"):
        self.id = transport_id
        self.current_speed = 0
        self.current_location = current_location
        self.battery_level = 100  # от 0 до 100

    def move(self, new_location: str, speed: float):
        if self.battery_level <= 0:
            print("Недостаточно заряда для поездки.")
            return

        consumption = speed
        if self.battery_level < consumption:
            print("Недостаточно заряда для поездки.")
            return

        self.current_speed = speed
        self.current_location = new_location
        self.battery_level -= consumption
        if self.battery_level < 0:
            self.battery_level = 0

    def charge(self, amount: float):
        self.battery_level = min(100, self.battery_level + amount)

    def get_info(self) -> str:
        return (f"ID: {self.id}, Скорость: {self.current_speed}, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, scooter_id: str, current_location: str = "Парковка"):
        super().__init__(scooter_id, current_location)
        self.is_rented = False

    def move(self, new_location: str, speed: float):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)


class Drone(Transport):
    def __init__(self, drone_id: str, current_location: str = "База дронов"):
        super().__init__(drone_id, current_location)
        self.altitude = 0  # в метрах

    def take_off(self, height: float):
        self.altitude += height

    def land(self):
        self.altitude = 0

    def move(self, new_location: str, speed: float):
        if self.altitude <= 0:
            print("Дрон не может двигаться на земле.")
            return

        consumption = speed
        if self.battery_level < consumption:
            print("Недостаточно заряда для поездки.")
            return

        self.current_speed = speed
        self.current_location = new_location
        self.battery_level -= consumption
        if self.battery_level < 0:
            self.battery_level = 0

        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
class GPSNavigator:
    def calculate_route(self, from_location: str, to_location: str) -> str:
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    def perform_emergency_landing(self):
        # Предполагаем, что у объекта есть атрибуты altitude, current_speed, battery_level
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, drone_id: str, current_location: str = "Склад"):
        super().__init__(drone_id, current_location)
        self.package = None

    def load_package(self, package_name: str):
        self.package = package_name
        print(f"Посылка '{package_name}' загружена.")

    def deliver_package(self):
        if self.altitude != 0:
            print("Дрон должен быть на земле для доставки посылки.")
            return

        if self.package is None:
            print("Нет посылки для доставки.")
            return

        print(f"Посылка {self.package} доставлена!")
        self.package = None

    def get_info(self) -> str:
        base_info = super().get_info()
        package_info = f", Посылка: {self.package}" if self.package else ", Посылка: нет"
        return base_info + package_info

if __name__ == "__main__":
    print("=== Тестирование Transport ===")
    transport = Transport("T001", "Центр")
    print(transport.get_info())
    transport.move("Парк", 10)
    print(transport.get_info())
    transport.charge(20)
    print(transport.get_info())

    print("\n=== Тестирование ElectricScooter ===")
    scooter = ElectricScooter("S001", "Площадь")
    print(scooter.get_info())
    scooter.move("Улица Ленина", 5)  # не арендован
    scooter.is_rented = True
    scooter.move("Улица Ленина", 5)
    print(scooter.get_info())

    print("\n=== Тестирование Drone ===")
    drone = Drone("D001", "Аэропорт")
    print(drone.get_info())
    drone.move("Город", 20)  # не взлетел
    drone.take_off(50)
    drone.move("Город", 20)
    print(drone.get_info())
    drone.land()
    print(f"Высота после посадки: {drone.altitude}")

    print("\n=== Тестирование DeliveryDrone ===")
    delivery_drone = DeliveryDrone("DD001", "Склад")
    print(delivery_drone.get_info())
    print(delivery_drone.calculate_route("Склад", "Дом"))
    delivery_drone.load_package("Книга")
    print(delivery_drone.get_info())
    delivery_drone.take_off(30)
    delivery_drone.move("Дом", 15)
    delivery_drone.land()
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())

    print("\n=== Аварийная посадка ===")
    delivery_drone.take_off(100)
    delivery_drone.move("Новый адрес", 25)
    delivery_drone.perform_emergency_landing()
    print(delivery_drone.get_info())
