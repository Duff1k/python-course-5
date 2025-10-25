class Transport:

    def __init__(self, transport_id, current_speed=0, current_location="", battery_level=100):
        self.id = transport_id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, new_speed):
        battery_consumption = new_speed
        self.current_location = new_location
        self.current_speed = new_speed
        print(f"Местоположение: {self.current_location}, текущая скорость: {self.current_speed}")
        self.battery_level = max(0, self.battery_level - battery_consumption)
        if self.battery_level < 1:
            print("Недостаточно заряда для поездки.") #я исхожу из того, что заряд измеряется ВО ВРЕМЯ поездки, а не ДО поездки. В условии задания не очень понятно.
            return False
        return True

    def charge(self, charge_increase):
        self.battery_level = min(100, self.battery_level + charge_increase)
        print(f"Заряд увеличен на {charge_increase}%. Уровень заряда: {self.battery_level}%")

    def get_info(self):
        return (f"ID: {self.id}, Скорость: {self.current_speed} км/ч, "
                f"Местоположение: {self.current_location}, Заряд: {self.battery_level}%")


class ElectricScooter(Transport):
    def __init__(self, transport_id, current_speed=0, current_location="", battery_level=100, is_rented=False):
        super().__init__(transport_id, current_speed, current_location, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, new_speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return False
        return super().move(new_location, new_speed)

class Drone(Transport):
    def __init__(self, transport_id, current_speed=0, current_location="", battery_level=100, altitude=0):
        super().__init__(transport_id, current_speed, current_location, battery_level)
        self.altitude = altitude

    def move(self, new_location, new_speed):
        if self.altitude <= 0:
            print("Дрон не взлетел. Используйте take_off()")
            return False

        if super().move(new_location, new_speed):
            print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
            return True
        return False

    def take_off(self, altitude):
        self.altitude = altitude


    def land(self):
        self.altitude = 0
        print("Дрон приземлился.")

class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    def perform_emergency_landing(self):
        if hasattr(self, 'battery_level') and self.battery_level <= 5:
            if hasattr(self, 'altitude'):
                self.altitude = 0
            self.current_speed = 0
            print("Аварийная посадка!")

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, transport_id, current_speed=0, current_location="", battery_level=100, altitude=0, package=None):
        super().__init__(transport_id, current_speed, current_location, battery_level, altitude)
        self.package = package

    def load_package(self, package_name):
        self.package = package_name
        print(f"Посылка '{package_name}' загружена в дрон {self.id}.")

    def deliver_package(self):
        if self.altitude != 0:
            print("Ошибка: Дрон должен быть на земле для доставки!")
            return False

        print(f"Посылка '{self.package}' доставлена!")
        self.package = None
        return True

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'нет'}"
        return base_info + package_info

def main():
    print("\nДЕМОНСТРАЦИЯ СИСТЕМЫ УМНОГО ТРАНСПОРТА")
    print("=" * 20)

    print("\n1. БАЗОВЫЙ ТРАНСПОРТ")
    print("-" * 20)
    transport = Transport("КН007", 0, "Точка А", 80)
    print(transport.get_info())
    transport.move("Точка Б", 60)
    print(transport.get_info())
    transport.charge(25)
    print(transport.get_info())

    print("\n2. ЭЛЕКТРОСАМОКАТ")
    print("-" * 20)
    scooter1 = ElectricScooter("KY007", 0, "ТОчка В", 80, is_rented=False)
    print(f"Создан неарендованный самокат: {scooter1.get_info()}")

    #Попытка поехать без аренды
    scooter1.move("Точка Г", 50)

    scooter2 = ElectricScooter("KY008", 0, "Точка Д", 80, is_rented=True)
    print(f"\nСоздан арендованный самокат: {scooter2.get_info()}")

    #Попытка поехать с арендой
    scooter2.move("Точка Е", 50)

    print("\n3. ДРОН")
    print("-" * 20)
    drone = Drone("D001", 0, "Точка Ж", 80)
    print(drone.get_info())

    drone.move("Точка З", 20)

    drone.take_off(10)
    drone.move("Точка И", 20)
    print(drone.get_info())

    drone.land()
    print(drone.get_info())

    print("\n4. ДРОН-ДОСТАВЩИК")
    print("-" * 20)
    delivery_drone = DeliveryDrone("DD001", 0, "Склад", 29)
    print(delivery_drone.get_info())

    # Навигация
    route = delivery_drone.calculate_route("Склад", "Адрес доставки")
    print(route)

    # Загрузка посылки
    delivery_drone.load_package("Смартфон")
    # print(delivery_drone.get_info())

    # Попытка доставить в воздухе
    delivery_drone.take_off(30)
    delivery_drone.deliver_package()

    # Успешная доставка
    delivery_drone.land()
    delivery_drone.deliver_package()
    # print(delivery_drone.get_info())

    # Аварийная посадка
    delivery_drone.take_off(40)
    delivery_drone.move("Парк", 25)
    delivery_drone.perform_emergency_landing()
    print(delivery_drone.get_info())


if __name__ == "__main__":
    main()