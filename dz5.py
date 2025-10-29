class Transport:
    def __init__(self, id, current_location, current_speed=0, battery_level=100):
        self.id = str(id)
        self.current_speed = current_speed
        self.current_location = str(current_location)
        self.battery_level = battery_level

    def move(self, new_location, speed):
        if speed < 0:
            print("Скорость не может быть отрицательной.")
            return

        required_charge = speed
        if self.battery_level < required_charge:
            print("Недостаточно заряда для поездки.")
            return

        self.current_location = new_location
        self.current_speed = speed
        self.battery_level = max(0, self.battery_level - required_charge)

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)

    def get_info(self):
        return (f"ID: {self.id}, Скорость: {self.current_speed}, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, id, current_location, current_speed=0, battery_level=100, is_rented=False):
        super().__init__(id, current_location, current_speed, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)


class Drone(Transport):
    def __init__(self, id, current_location, current_speed=0, battery_level=100, altitude=0):
        super().__init__(id, current_location, current_speed, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height

    def land(self):
        self.altitude = 0

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не может лететь – он на земле.")
            return

        required_charge = speed
        if self.battery_level < required_charge:
            print("Недостаточно заряда для полета.")
            return

        self.current_location = new_location
        self.current_speed = speed
        self.battery_level -= required_charge
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
    def __init__(self, id, current_location, current_speed=0, battery_level=100, altitude=0):
        super().__init__(id, current_location, current_speed, battery_level, altitude)
        self.package = None

    def load_package(self, package):
        self.package = package
        print(f"Посылка '{package}' загружена.")

    def deliver_package(self):
        if self.altitude > 0:
            print("Дрон должен быть на земле для доставки.")
            return

        if not self.package:
            print("Нет посылки для доставки.")
            return

        print(f"Посылка '{self.package}' доставлена!")
        self.package = None

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'Нет'}"
        return base_info + package_info

if __name__ == "__main__": # клиентский код
    print("=" * 60)
    print("ТЕСТИРОВАНИЕ ВСЕХ КЛАССОВ И МЕТОДОВ")
    print("=" * 60)

    print("\n--- ТЕСТ КЛАССА Transport ---")
    transport1 = Transport("T-001", "Склад")
    print("Создан транспорт:", transport1.get_info())

    transport1.move("Парк", 20)
    print("После перемещения:", transport1.get_info())

    transport1.charge(15)
    print("После зарядки:", transport1.get_info())

    print("\n--- ТЕСТ КЛАССА ElectricScooter ---")
    scooter1 = ElectricScooter("ES-001", "Метро")
    print("Создан самокат:", scooter1.get_info())

    scooter1.move("Торговый центр", 15)

    scooter1.is_rented = True
    scooter1.move("Торговый центр", 15)
    print("После поездки:", scooter1.get_info())

    scooter1.charge(10)
    print("После зарядки:", scooter1.get_info())

    print("\n--- ТЕСТ КЛАССА Drone ---")
    drone1 = Drone("D-001", "База")
    print("Создан дрон:", drone1.get_info())

    drone1.move("Парк", 30)

    drone1.take_off(50)
    drone1.move("Парк", 30)
    print("После полета:", drone1.get_info())

    drone1.land()
    print("После посадки:", drone1.get_info())

    print("\n--- ТЕСТ КЛАССА DeliveryDrone ---")
    delivery_drone1 = DeliveryDrone("DD-001", "Склад доставки")
    print("Создан дрон доставки:", delivery_drone1.get_info())

    route = delivery_drone1.calculate_route("Склад", "Дом клиента")
    print("Маршрут:", route)

    delivery_drone1.load_package("Важные документы")
    print("После загрузки:", delivery_drone1.get_info())

    delivery_drone1.take_off(100)
    delivery_drone1.move("Дом клиента", 40)
    print("В полете:", delivery_drone1.get_info())

    delivery_drone1.deliver_package()

    delivery_drone1.land()
    delivery_drone1.deliver_package()
    print("После доставки:", delivery_drone1.get_info())

    delivery_drone1.perform_emergency_landing()
    print("После аварийной посадки:", delivery_drone1.get_info())