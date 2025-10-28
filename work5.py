class Transport:
    def __init__(self, id, current_location, current_speed=0, battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, speed):
        required_charge = speed
        if self.battery_level < required_charge:
            print("Недостаточно заряда для поездки.")
            return
        self.current_location = new_location
        self.current_speed = speed
        self.battery_level = max(0, self.battery_level - required_charge)

    def charge(self, value):
        self.battery_level = min(100, self.battery_level + value)

    def get_info(self):
        return (f"ID: {self.id}, Скорость: {self.current_speed}, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, id, current_location, is_rented=False):
        super().__init__(id, current_location)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)


class Drone(Transport):
    def __init__(self, id, current_location, altitude=0):
        super().__init__(id, current_location)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height
        print(f"Дрон поднялся на высоту {self.altitude} м.")

    def land(self):
        self.altitude = 0
        print("Дрон приземлился.")

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не может двигаться: он на земле.")
            return
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        super().move(new_location, speed)


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
    def __init__(self, id, current_location, altitude=0, package=None):
        super().__init__(id, current_location, altitude)
        self.package = package

    def load_package(self, package_name):
        self.package = package_name
        print(f"Посылка '{package_name}' загружена.")

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!")
                self.package = None
            else:
                print("Нет посылки для доставки.")
        else:
            print("Дрон не может доставить посылку в воздухе!")

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info}, Высота: {self.altitude} м, Посылка: {self.package}"


if __name__ == "__main__":
    t = Transport("T001", "Центр города")
    print(t.get_info())
    t.move("Парк", 10)
    print(t.get_info())
    t.charge(5)
    print(t.get_info())
    print()

    s = ElectricScooter("S001", "Площадь")
    s.move("Улица Ленина", 15)
    s.is_rented = True
    s.move("Улица Ленина", 15)
    print(s.get_info())
    print()

    d = Drone("D001", "Склад")
    d.move("Офис", 20)
    d.take_off(50)
    d.move("Офис", 20)
    d.land()
    print(d.get_info())
    print()

    dd = DeliveryDrone("DD001", "Склад")
    print(dd.calculate_route("Склад", "Дом клиента"))
    dd.load_package("Документы")
    dd.take_off(100)
    dd.move("Дом клиента", 30)
    dd.perform_emergency_landing()
    dd.deliver_package()
    dd.land()
    dd.deliver_package()
    print(dd.get_info())
