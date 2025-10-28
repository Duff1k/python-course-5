class Transport:
    """Базовый класс для всех видов транспорта"""

    def __init__(self, id, current_speed=0, current_location="", battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, speed):
        """Перемещает транспорт в новое местоположение"""
        required_charge = speed

        if self.battery_level < required_charge:
            print(f"Недостаточно заряда для поездки. Требуется: {required_charge}%, доступно: {self.battery_level}%")
            return False

        self.current_location = new_location
        self.current_speed = speed
        self.battery_level = max(0, self.battery_level - required_charge)
        return True

    def charge(self, amount):
        """Заряжает батарею"""
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Транспорт {self.id} заряжен на {amount}%. Текущий заряд: {self.battery_level}%")

    def get_info(self):
        """Возвращает информацию о транспорте"""
        return (f"ID: {self.id}, Скорость: {self.current_speed} км/ч, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    """Класс электросамоката"""

    def __init__(self, id, current_speed=0, current_location="", battery_level=100, is_rented=False):
        super().__init__(id, current_speed, current_location, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        """Перемещает самокат, если он арендован"""
        if not self.is_rented:
            print("Самокат не арендован.")
            return False

        return super().move(new_location, speed)

    def rent(self):
        """Арендовать самокат"""
        self.is_rented = True
        print(f"Самокат {self.id} арендован.")

    def return_scooter(self):
        """Вернуть самокат"""
        self.is_rented = False
        self.current_speed = 0
        print(f"Самокат {self.id} возвращен.")


class Drone(Transport):
    """Базовый класс дрона"""

    def __init__(self, id, current_speed=0, current_location="", battery_level=100, altitude=0):
        super().__init__(id, current_speed, current_location, battery_level)
        self.altitude = altitude

    def move(self, new_location, speed):
        """Перемещает дрон, если он в воздухе"""
        if self.altitude <= 0:
            print("Дрон не может лететь - он на земле.")
            return False

        result = super().move(new_location, speed)
        if result:
            print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        return result

    def take_off(self, altitude):
        """Взлетает на заданную высоту"""
        if self.battery_level < 10:
            print("Недостаточно заряда для взлета.")
            return

        self.altitude = altitude
        print(f"Дрон {self.id} взлетел на высоту {altitude} м.")

    def land(self):
        """Приземляет дрон"""
        self.altitude = 0
        self.current_speed = 0
        print(f"Дрон {self.id} приземлился.")


# Миксины (примеси)
class GPSNavigator:
    """Миксин для навигации"""

    def calculate_route(self, from_location, to_location):
        """Рассчитывает маршрут"""
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    """Миксин для аварийной посадки"""

    def perform_emergency_landing(self):
        """Выполняет аварийную посадку"""
        if hasattr(self, 'altitude'):
            self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    """Класс дрона-доставщика с множественным наследованием"""

    def __init__(self, id, current_speed=0, current_location="", battery_level=100, altitude=0):
        super().__init__(id, current_speed, current_location, battery_level, altitude)
        self.package = None

    def load_package(self, package_name):
        """Загружает посылку"""
        if self.altitude > 0:
            print("Невозможно загрузить посылку - дрон в воздухе!")
            return False

        self.package = package_name
        print(f"Посылка '{package_name}' загружена в дрон {self.id}.")
        return True

    def deliver_package(self):
        """Доставляет посылку"""
        if self.altitude > 0:
            print("Невозможно доставить посылку - дрон в воздухе!")
            return False

        if not self.package:
            print("Нет посылки для доставки!")
            return False

        print(f"Посылка '{self.package}' доставлена!")
        self.package = None
        return True

    def get_info(self):
        """Возвращает расширенную информацию о дроне-доставщике"""
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'нет'}"
        return base_info + package_info


# Клиентский код - демонстрация работы всех классов
def main():
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ СИСТЕМЫ УМНОГО ТРАНСПОРТА")
    print("=" * 50)

    # 1. Тестирование базового класса Transport
    print("\n1. ТЕСТИРОВАНИЕ БАЗОВОГО КЛАССА TRANSPORT")
    print("-" * 40)

    transport = Transport("T001", current_location="Гараж")
    print(transport.get_info())

    transport.move("Центр города", 20)
    print(transport.get_info())

    transport.charge(15)
    print(transport.get_info())

    # 2. Тестирование ElectricScooter
    print("\n2. ТЕСТИРОВАНИЕ ELECTRICSCOOTER")
    print("-" * 40)

    scooter = ElectricScooter("ES001", current_location="Станция А")
    print(scooter.get_info())

    # Попытка поехать без аренды
    scooter.move("Парк", 15)

    # Аренда и поездка
    scooter.rent()
    scooter.move("Парк", 15)
    print(scooter.get_info())

    # Возврат самоката
    scooter.return_scooter()
    print(scooter.get_info())

    # 3. Тестирование Drone
    print("\n3. ТЕСТИРОВАНИЕ DRONE")
    print("-" * 40)

    drone = Drone("D001", current_location="База")
    print(drone.get_info())

    # Попытка полететь без взлета
    drone.move("Точка Б", 30)

    # Взлет и полет
    drone.take_off(50)
    drone.move("Точка Б", 30)
    print(drone.get_info())

    # Приземление
    drone.land()
    print(drone.get_info())

    # 4. Тестирование DeliveryDrone
    print("\n4. ТЕСТИРОВАНИЕ DELIVERYDRONE")
    print("-" * 40)

    delivery_drone = DeliveryDrone("DD001", current_location="Склад")
    print(delivery_drone.get_info())

    # Тестирование GPS навигации
    route = delivery_drone.calculate_route("Склад", "Клиент А")
    print(route)

    # Загрузка посылки
    delivery_drone.load_package("Смартфон XYZ")
    print(delivery_drone.get_info())

    # Попытка доставить посылку без взлета/полета
    delivery_drone.deliver_package()

    # Полный цикл доставки
    delivery_drone.take_off(100)
    delivery_drone.move("Адрес клиента", 40)
    print(delivery_drone.get_info())

    delivery_drone.land()
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())

    # Тестирование аварийной посадки
    print("\n5. ТЕСТИРОВАНИЕ АВАРИЙНОЙ ПОСАДКИ")
    print("-" * 40)

    emergency_drone = DeliveryDrone("ED001", current_speed=60, battery_level=80, altitude=150)
    print(emergency_drone.get_info())

    emergency_drone.perform_emergency_landing()
    print(emergency_drone.get_info())

    # 6. Дополнительные тесты
    print("\n6. ДОПОЛНИТЕЛЬНЫЕ ТЕСТЫ")
    print("-" * 40)

    # Тест разряда батареи
    test_scooter = ElectricScooter("TEST001", current_location="Точка А", battery_level=10)
    test_scooter.rent()
    test_scooter.move("Точка Б", 15)  # Должен не хватить заряда
    print(test_scooter.get_info())

    # Тест зарядки
    test_scooter.charge(50)
    test_scooter.move("Точка Б", 15)
    print(test_scooter.get_info())


if __name__ == "__main__":
    main()