# Домашнее задание по объектно-ориентированному программированию
# Домашнее задание: Система "Умный транспорт"
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
            print("Скорость должна быть числом.")
        if speed < 0:
            print("Скорость не может быть отрицательной.")


        required_charge = speed   # уменьшение заряда на 1% за каждую единицу скорости , поэтому необходимый заряд батареи равен заданной скорости
        if self.battery_level >= required_charge:
            self.current_location = str(new_location)
            self.current_speed = speed
            self.battery_level -= required_charge
        else:
            print("Недостаточно заряда для поездки.")

    def charge(self, amount):
        self.current_speed = 0
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
        self.battery_level = min(100, self.battery_level + amount)

    def get_info(self):
        return (f"ID: {self.id}, Скорость: {self.current_speed}, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, is_rented = False):
        super().__init__(id, current_speed, current_location, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, new_speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        return super().move(new_location, new_speed)


class Drone(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, altitude = 0):
        super().__init__(id, current_speed, current_location, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height

    def land(self):
        self.altitude = 0
        self.current_speed = 0

    def move(self, new_location, new_speed):
        if self.altitude <= 0:
            print("Дрон не может лететь – он на земле.")
            return


        required_charge = new_speed
        if self.battery_level >= required_charge:
            self.current_location = new_location
            self.current_speed = new_speed
            self.battery_level -= required_charge
            print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        else:
            print("Недостаточно заряда для полета.")


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    def perform_emergency_landing(self):
        if hasattr(self, 'altitude'):
            self.altitude = 0
        if hasattr(self, 'current_speed'):
            self.current_speed = 0
        if hasattr(self, 'battery_level'):
            self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, altitude = 0):
        super().__init__(id, current_speed, current_location, battery_level, altitude)
        self.package = None

    def load_package(self, package):
        self.package = package
        print(f"Посылка '{package}' загружена.")

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!")
                self.package = None
            else:
                print("Нет посылки для доставки.")
        else:
            print("Дрон должен быть на земле для доставки.")

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'Нет'}"
        return base_info + package_info


# Клиентский код
if __name__ == "__main__":
    print("Тестирование Электроскутера")
    scooter = ElectricScooter("A01", current_location = "Работа")
    print(scooter.get_info())

    scooter.move("Ближайшая от работы станция Метро", 25)  # Попытка поехать без аренды
    scooter.is_rented = True
    scooter.move("Ближайшая от работы станция Метро", 25)
    print(scooter.get_info())

    scooter.charge(20)
    print("После зарядки: ", scooter.get_info())
    print()

    print("Тестирование Дрона")
    drone = Drone("B01", current_location = "офис Яндекс лавка")
    print(drone.get_info())

    drone.move("Склад", 10)  # Попытка лететь без взлёта
    drone.take_off(75)
    drone.move("Склад", 10)
    print(drone.get_info())

    drone.land()
    print("После посадки: ", drone.get_info())
    print()

    print("Тестирование Доставки дрона")
    delivery_drone = DeliveryDrone("D01", current_location = "офис Яндекс лавка")
    print(delivery_drone.get_info())

    delivery_drone.take_off(80)
    delivery_drone.load_package("Кофе с крусаном")
    print(delivery_drone.calculate_route("Яндекс лавка", "Дом клиента"))
    delivery_drone.move("Дом клиента", 15)

    delivery_drone.deliver_package()  # Не может доставить в воздухе
    delivery_drone.land()
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())

    delivery_drone.perform_emergency_landing()
    print("После аварийной посадки:", delivery_drone.get_info())