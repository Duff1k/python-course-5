#Базовый класс и простое наследование

class Transport:
    def __init__(self, id, current_location="Неизвестно", current_speed=0, battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, speed):
        if self.battery_level <= 0:
            print("Недостаточно заряда для поездки.")
            return

        needed_charge = speed
        if self.battery_level < needed_charge:
            print("Недостаточно заряда для поездки.")
            return

        self.current_speed = speed
        self.current_location = new_location
        old_charge = self.battery_level  # Сохраняем заряд до поездки
        self.battery_level -= needed_charge
        if self.battery_level < 0:
            self.battery_level = 0
        print(f"Транспорт {self.id} переместился в {new_location} со скоростью {speed} км/ч.")
        print(f"Заряд уменьшился с {old_charge}% до {self.battery_level}% (-{old_charge - self.battery_level}%).")

    def charge(self, value):
        old_charge = self.battery_level  # Заряд до подзарядки
        self.battery_level = min(100, self.battery_level + value)
        added = self.battery_level - old_charge  # Реально добавленный заряд
        print(f"Транспорт {self.id} заряжен на +{added}%. Текущий уровень: {self.battery_level}%.")

    def get_info(self):
        return (f"ID: {self.id}, Скорость: {self.current_speed} км/ч, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")

#Класс ElectricScooter
class ElectricScooter(Transport):
    def __init__(self, id, current_location="Неизвестно", current_speed=0, battery_level=100, is_rented=False):
        super().__init__(id, current_location, current_speed, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)

#Класс Drone
class Drone(Transport):
    def __init__(self, id, current_location="Неизвестно", current_speed=0, battery_level=100, altitude=0):
        super().__init__(id, current_location, current_speed, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height
        print(f"Дрон {self.id} взлетел на высоту {self.altitude} м.")

    def land(self):
        self.altitude = 0
        print(f"Дрон {self.id} приземлился.")

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не может двигаться — он на земле.")
            return
        if self.battery_level <= 0:
            print("Недостаточно заряда для полета.")
            return
        old_charge = self.battery_level
        self.current_speed = speed
        self.current_location = new_location
        self.battery_level -= speed
        if self.battery_level < 0:
            self.battery_level = 0
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        print(f"Заряд уменьшился с {old_charge}% до {self.battery_level}% (-{old_charge - self.battery_level}%).")

#Множественное наследование

class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    def perform_emergency_landing(self):
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка! Высота и скорость сброшены, заряд установлен на 5%.")

#Класс DeliveryDrone
class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, current_location="Неизвестно", current_speed=0, battery_level=100, altitude=0, package=None):
        super().__init__(id, current_location, current_speed, battery_level, altitude)
        self.package = package

    def load_package(self, package_name):
        self.package = package_name
        print(f"Посылка '{package_name}' загружена.")

    def deliver_package(self):
        if self.altitude != 0:
            print("Невозможно доставить посылку: дрон находится в воздухе.")
            return
        if self.package is None:
            print("Нет посылки для доставки.")
            return
        print(f"Посылка '{self.package}' доставлена!")
        self.package = None

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'нет'}"
        return base_info + package_info


# Клиентский код

print("=== Транспорт ===")
t = Transport("T001")
print(t.get_info())
t.move("Станция B", 20)
t.charge(10)
print(t.get_info())

print("\n=== Электросамокат ===")
s = ElectricScooter("S001", "Площадь", is_rented=False)
s.move("Улица Ленина", 10)  # Не арендован
s.is_rented = True
s.move("Улица Ленина", 10)
print(s.get_info())

print("\n=== Дрон ===")
d = Drone("D001", "Склад")
d.move("Парк", 15)  # На земле
d.take_off(50)
d.move("Парк", 15)
d.land()
print(d.get_info())

print("\n=== Дрон доставки ===")
dd = DeliveryDrone("DD001", "Склад 1")
print(dd.calculate_route("Склад 1", "Дом клиента"))
dd.load_package("Телефон")
dd.take_off(100)
dd.move("Дом клиента", 20)
dd.perform_emergency_landing()
dd.deliver_package()
print(dd.get_info())
