class Transport:
    def __init__(self, id, current_location, speed = 0, battery_level = 100):
        self.id = id
        self.current_speed = speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, speed):
        required_charge = speed
        if self.battery_level < required_charge:
            print("Недостаточно заряда для поездки.")
            return
        self.current_location = new_location
        self.current_speed = speed
        self.battery_level -= required_charge

    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100

    def get_info(self):
        return f"ID: {self.id}, Скорость: {self.current_speed}, Местоположение: {self.current_location}, Заряд: {self.battery_level}%"


class ElectricScooter(Transport):
    def __init__(self, id, current_location, speed = 0, battery_level = 100, is_rented = False):
        super().__init__(id, current_location, speed, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)


class Drone(Transport):
    def __init__(self, id, current_location, speed = 0, battery_level = 100, attitude = 0):
        super().__init__(id, current_location, speed, battery_level)
        self.altitude = attitude

    def take_off(self, height):
        self.altitude += height

    def land(self):
        self.altitude = 0

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не может перемещаться, так как не взлетел.")
            return
        super().move(new_location, speed)
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")


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
    def __init__(self, id, current_location, speed = 0, battery_level = 100, attitude = 0, package = None):
        super().__init__(id, current_location, speed, battery_level, attitude)
        self.package = package
    def load_package(self, package_name):
        self.package = package_name
    def deliver_package(self):
        if self.altitude != 0:
            print("Дрон не может доставить посылку, так как находится в воздухе.")
            return
        if self.package is None:
            print("Нет посылки для доставки.")
            return
        print(f"Посылка {self.package} доставлена!")
        self.package = None
    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package}" if self.package else ", Посылка: Нет"
        return base_info + package_info


transport = Transport("T1000", "Гараж")
scooter = ElectricScooter("T500", "Парковка")
drone = Drone("T-X", "Аэродром")
delivery_drone = DeliveryDrone("T800", "Склад")


print("Класс транспорт")
print("Информация:", transport.get_info())
transport.move("Улица", 10)
print("После move:", transport.get_info())
transport.charge(20)
print("После charge:", transport.get_info())

print("\nСамокат")
print("Информация:", scooter.get_info())
scooter.move("Улица", 5)  # Не арендован
scooter.is_rented = True
scooter.move("Парк", 8)
print("После move:", scooter.get_info())
scooter.charge(15)
print("После charge:", scooter.get_info())

print("\nДрон")
print("Информация:", drone.get_info())
drone.move("Поле", 10)  # Не взлетел
drone.take_off(50)
drone.move("Лес", 15)
print("После move:", drone.get_info())
drone.land()
print("После land:", drone.get_info())
drone.charge(30)
print("После charge:", drone.get_info())

print("\nГрузовой дрон")
print("Информация:", delivery_drone.get_info())
delivery_drone.load_package("Книга")
print("После load_package:", delivery_drone.get_info())
delivery_drone.deliver_package()  # На земле
print("После deliver_package:", delivery_drone.get_info())
delivery_drone.take_off(100)
delivery_drone.deliver_package()  # В воздухе
print("calculate_route:", delivery_drone.calculate_route("Склад", "Дом"))
delivery_drone.perform_emergency_landing()
print("После emergency_landing:", delivery_drone.get_info())
delivery_drone.charge(50)
print("После charge:", delivery_drone.get_info())