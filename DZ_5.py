
class Transport:
    def __init__(self, id, current_location):
        self.id = id
        self.current_speed = 0
        self.current_location = current_location
        self.battery_level = 100

    def move(self, new_location, speed):
        required_charge = speed
        if self.battery_level < required_charge:
            print("Недостаточно заряда для поездки.")
            return
        self.current_location = new_location
        self.current_speed = speed
        self.battery_level = max(self.battery_level - speed, 0)

    def charge(self, amount):
        self.battery_level = min(self.battery_level + amount, 100)

    def get_info(self):
        return f"Транспорт {self.id}: скорость {self.current_speed}, место {self.current_location}, заряд {self.battery_level}%"

class ElectricScooter(Transport):
    def __init__(self, id, current_location):
        super().__init__(id, current_location)
        self.is_rented = False

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)

    def get_info(self):
        state = "арендован" if self.is_rented else "не арендован"
        return f"Самокат {self.id}: {state}, скорость {self.current_speed}, место {self.current_location}, заряд {self.battery_level}%"

class Drone(Transport):
    def __init__(self, id, current_location):
        super().__init__(id, current_location)
        self.altitude = 0

    def take_off(self, value):
        self.altitude += value

    def land(self):
        self.altitude = 0

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не взлетел.")
            return
        super().move(new_location, speed)
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")

    def get_info(self):
        return f"Дрон {self.id}: скорость {self.current_speed}, место {self.current_location}, заряд {self.battery_level}%, высота {self.altitude} м"


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    def perform_emergency_landing(self):
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, current_location):
        super().__init__(id, current_location)
        self.package = None

    def load_package(self, package_name):
        self.package = package_name

    def deliver_package(self):
        if self.altitude == 0 and self.package:
            print(f"Посылка {self.package} доставлена!")
            self.package = None
        else:
            print("Дрон не на земле, невозможно доставить посылку.")

    def get_info(self):
        package_info = self.package if self.package else "нет посылки"
        return f"Дрон доставки {self.id}: скорость {self.current_speed}, место {self.current_location}, заряд {self.battery_level}%, высота {self.altitude} м, посылка: {package_info}"


if __name__ == "__main__":
    # Transport
    t1 = Transport("T-001", "Склад")
    print(t1.get_info())
    t1.move("Пункт А", 20)
    print(t1.get_info())
    t1.charge(10)
    print(t1.get_info())

    # ElectricScooter
    scooter = ElectricScooter("ES-001", "Парк")
    print(scooter.get_info())
    scooter.move("Магазин", 15)
    scooter.is_rented = True
    scooter.move("Магазин", 15)
    print(scooter.get_info())
    scooter.charge(20)
    print(scooter.get_info())

    # Drone
    d1 = Drone("D-001", "Гараж")
    print(d1.get_info())
    d1.move("Город", 10)
    d1.take_off(50)
    d1.move("Город", 10)
    print(d1.get_info())
    d1.land()
    print(d1.get_info())

    # DeliveryDrone
    dd = DeliveryDrone("DD-001", "Склад")
    print(dd.get_info())
    route = dd.calculate_route(dd.current_location, "Дом клиента")
    print(route)
    dd.take_off(100)
    dd.load_package("Книга")
    print(dd.get_info())
    dd.move("Дом клиента", 30)
    dd.deliver_package()
    dd.land()
    dd.deliver_package()
    print(dd.get_info())

    dd.perform_emergency_landing()
    print(dd.get_info())
