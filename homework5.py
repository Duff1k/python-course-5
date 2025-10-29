# Домашнее задание: Система "Умный транспорт" (финальный вариант с проверками и изменёнными строками)
class Transport:
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100):
        self.id = str(id)
        self.current_speed = current_speed if current_speed >= 0 else 0
        self.current_location = str(current_location)
        bl = int(battery_level)
        self.battery_level = 0 if bl < 0 else (100 if bl > 100 else bl)

    def move(self, new_location, new_speed):
        try:
            speed = int(new_speed)
        except (TypeError, ValueError):
            print("Ошибка: значение скорости должно быть числом.")
            return
        if speed < 0:
            print("Ошибка: отрицательная скорость недопустима.")
            return

        required_charge = speed  # 1% заряда на 1 ед. скорости
        if self.battery_level >= required_charge:
            self.current_location = str(new_location)
            self.current_speed = speed
            self.battery_level -= required_charge
        else:
            print("Недостаточно заряда аккумулятора для движения.")

    def charge(self, amount):
        # Подзарядка с проверками и ограничением до 100%
        try:
            delta = int(amount)
        except (TypeError, ValueError):
            print("Ошибка: величина зарядки должна быть числом.")
            return

        self.current_speed = 0
        self.battery_level = max(0, min(100, self.battery_level + delta))

    def get_info(self):
        return (f"ID транспорта: {self.id}, "
                f"Текущая скорость: {self.current_speed}, "
                f"Место нахождения: {self.current_location}, "
                f"Уровень заряда: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, is_rented = False):
        super().__init__(id, current_speed, current_location, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, new_speed):
        if not self.is_rented:
            print("Самокат не активирован. Пожалуйста, начните аренду.")
            return
        return super().move(new_location, new_speed)


class Drone(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, altitude = 0):
        super().__init__(id, current_speed, current_location, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        try:
            h = int(height)
        except (TypeError, ValueError):
            print("Ошибка: высота взлёта должна быть числом.")
            return
        if h <= 0:
            print("Ошибка: высота взлёта должна быть положительной.")
            return
        self.altitude += h
        print(f"Дрон поднялся на высоту {self.altitude} м.")

    def land(self):
        self.altitude = 0
        self.current_speed = 0
        print("Дрон успешно приземлился.")

    def move(self, new_location, new_speed):
        if self.altitude <= 0:
            print("Ошибка: дрон находится на земле, взлетите перед полётом.")
            return

        try:
            speed = int(new_speed)
        except (TypeError, ValueError):
            print("Ошибка: значение скорости должно быть числом.")
            return
        if speed < 0:
            print("Ошибка: отрицательная скорость недопустима.")
            return

        required_charge = speed
        if self.battery_level >= required_charge:
            self.current_location = str(new_location)
            self.current_speed = speed
            self.battery_level -= required_charge
            print(f"Дрон направляется в точку '{new_location}' на высоте {self.altitude} м.")
        else:
            print("Недостаточно заряда для выполнения полёта.")


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Построен маршрут: из '{from_location}' в '{to_location}'."


class EmergencyLanding:
    def perform_emergency_landing(self):
        if hasattr(self, 'altitude'):
            self.altitude = 0
        if hasattr(self, 'current_speed'):
            self.current_speed = 0
        if hasattr(self, 'battery_level'):
            self.battery_level = 5
        print("Выполнена аварийная посадка дрона!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, altitude = 0):
        super().__init__(id, current_speed, current_location, battery_level, altitude)
        self.package = None

    def load_package(self, package):
        self.package = package
        print(f"Груз '{package}' успешно загружен.")

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Груз '{self.package}' доставлен получателю.")
                self.package = None
            else:
                print("Нет груза для доставки.")
        else:
            print("Дрон должен приземлиться перед доставкой.")

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Груз: {self.package if self.package else 'Отсутствует'}"
        return base_info + package_info


# Тестирование
if __name__ == "__main__":
    print("=== Проверка электросамоката ===")
    scooter = ElectricScooter("A01", current_location="Дом")
    print(scooter.get_info())

    scooter.move("Парк", 20)  # без аренды
    scooter.is_rented = True
    scooter.move("Парк", 20)
    print(scooter.get_info())

    scooter.charge(15)
    print("После зарядки:", scooter.get_info())
    print()

    print("=== Проверка дрона ===")
    drone = Drone("B01", current_location="Склад №1")
    print(drone.get_info())

    drone.move("Магазин", 10)  # без взлёта
    drone.take_off(50)
    drone.move("Магазин", 10)
    print(drone.get_info())

    drone.land()
    print("После посадки:", drone.get_info())
    print()

    print("=== Проверка дрона-доставки ===")
    delivery_drone = DeliveryDrone("D01", current_location="База доставки")
    print(delivery_drone.get_info())

    delivery_drone.take_off(100)
    delivery_drone.load_package("Пицца и напиток")
    print(delivery_drone.calculate_route("База доставки", "Адрес клиента"))
    delivery_drone.move("Адрес клиента", 18)

    delivery_drone.deliver_package()  # нельзя в воздухе
    delivery_drone.land()
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())

    delivery_drone.perform_emergency_landing()
    print("После аварийной посадки:", delivery_drone.get_info())
