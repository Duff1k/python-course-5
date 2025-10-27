class Transport:
    """
    Базовый класс для всех видов транспорта.
    """
    def __init__(self, id, current_location, current_speed=0, battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, speed):
        """
        Изменяет местоположение и скорость, уменьшая заряд батареи.
        """
        required_charge = speed
        if self.battery_level >= required_charge:
            self.current_location = new_location
            self.current_speed = speed
            self.battery_level = max(0, self.battery_level - required_charge)
            print(f"Транспорт {self.id} перемещается в {self.current_location}.")
        else:
            print("Недостаточно заряда для поездки.")

    def charge(self, amount):
        """
        Увеличивает заряд батареи.
        """
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Батарея заряжена. Текущий уровень: {self.battery_level}%.")

    def get_info(self):
        """
        Возвращает строку с общей информацией о транспорте.
        """
        return (f"ID: {self.id}, Скорость: {self.current_speed} км/ч, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")

class ElectricScooter(Transport):
    """
    Класс для электросамоката, наследуется от Transport.
    """
    def __init__(self, id, current_location, is_rented=False):
        super().__init__(id, current_location)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        """
        Переопределенный метод движения: самокат движется только в аренде.
        """
        if self.is_rented:
            super().move(new_location, speed)
        else:
            print("Самокат не арендован.")

class Drone(Transport):
    """
    Класс для дрона, наследуется от Transport.
    """
    def __init__(self, id, current_location, altitude=0):
        super().__init__(id, current_location)
        self.altitude = altitude

    def take_off(self, height):
        """
        Увеличивает высоту полёта.
        """
        self.altitude += height
        print(f"Дрон {self.id} взлетел на высоту {self.altitude} м.")

    def land(self):
        """
        Устанавливает высоту в 0.
        """
        self.altitude = 0
        self.current_speed = 0
        print(f"Дрон {self.id} приземлился.")

    def move(self, new_location, speed):
        """
        Переопределенный метод движения: дрон летит только если высота > 0.
        """
        if self.altitude > 0:
            super().move(new_location, speed)
            print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        else:
            print("Дрон должен сначала взлететь.")

class GPSNavigator:
    """
    Миксин для навигации.
    """
    def calculate_route(self, from_location, to_location):
        """
        Возвращает строку с информацией о маршруте.
        """
        return f"Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    """
    Миксин для выполнения аварийной посадки.
    """
    def perform_emergency_landing(self):
        """
        Устанавливает высоту и скорость в 0, заряд батареи до 5%.
        """
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    """
    Класс для дрона-доставщика с множественным наследованием.
    """
    def __init__(self, id, current_location, package=None):
        super().__init__(id, current_location)
        self.package = package

    def load_package(self, package_name):
        """
        Загружает посылку.
        """
        self.package = package_name
        print(f"Посылка '{self.package}' загружена на дрон.")

    def deliver_package(self):
        """
        Доставляет посылку, если дрон на земле.
        """
        if self.altitude == 0 and self.package is not None:
            print(f"Посылка '{self.package}' доставлена!")
            self.package = None
        else:
            if self.package is None:
                print("Нет посылки для доставки.")
            else:
                print("Для доставки посылки необходимо приземлиться.")

    def get_info(self):
        """
        Возвращает расширенную информацию, включая данные о посылке.
        """
        base_info = super().get_info()
        package_info = f"Посылка: {'Нет' if self.package is None else self.package}"
        return f"{base_info}, {package_info}"


if __name__ == "__main__":
    # 1. Демонстрация базового класса Transport
    print("--- 🚗 Демонстрация Transport ---")
    car = Transport(id="T-001", current_location="Парковка А")
    print(car.get_info())
    car.move(new_location="Центр города", speed=50)
    print(car.get_info())
    car.charge(20)
    print(car.get_info())
    car.move("Склад", speed=90)


    # 2. Демонстрация класса ElectricScooter
    print("--- 🛴 Демонстрация ElectricScooter ---")
    scooter = ElectricScooter(id="S-123", current_location="Парк Горького")
    print(scooter.get_info())
    scooter.move("Красная площадь", speed=15)
    scooter.is_rented = True
    print("Самокат арендован.")
    scooter.move("Красная площадь", speed=15)
    print(scooter.get_info())
    scooter.is_rented = False
    print("Аренда завершена.")


    # 3. Демонстрация класса Drone
    print("--- 🚁 Демонстрация Drone ---")
    simple_drone = Drone(id="D-01", current_location="База")
    print(simple_drone.get_info())
    simple_drone.move("Точка Б", speed=100)
    simple_drone.take_off(50)
    simple_drone.move("Точка Б", speed=100)
    print(simple_drone.get_info())
    simple_drone.land()
    print(simple_drone.get_info())


    # 4. Демонстрация класса DeliveryDrone
    print("--- 📦 Демонстрация DeliveryDrone ---")
    delivery_drone = DeliveryDrone(id="DD-555", current_location="Склад")
    print(delivery_drone.get_info())
    print(delivery_drone.calculate_route(from_location="Склад", to_location="Дом клиента"))
    delivery_drone.load_package("Новый смартфон")
    delivery_drone.deliver_package()
    delivery_drone.take_off(100)
    delivery_drone.move("Дом клиента", speed=80)
    print(delivery_drone.get_info())
    delivery_drone.land()
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())
    delivery_drone.take_off(150)
    print("Обнаружена неисправность...")
    delivery_drone.perform_emergency_landing()
    print(delivery_drone.get_info())