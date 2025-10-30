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
        self.battery_level -= required_charge
        if self.battery_level < 0:
            self.battyre_level = 0
    def charge(self, amount):
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100
    def get_info(self):
        return (f"ID: {self.id}, "
                f"Скорость: {self.current_speed}, "
                f"Местоположение: {self.current_location}, "
                f"Заряд: {self.battery_level}%")
    
class ElectricScooter(Transport):
    def __init__(self, id, current_location, current_speed = 0, battery_level = 100, is_rented = False):
        super().__init__(id, current_location, current_speed, battery_level)
        self.is_rented = is_rented

    def move(self, new_location, speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)    

class Drone(Transport):
    def __init__(self, id, current_location, current_speed = 0, battery_level = 100, altitude = 0):
        super().__init__(id, current_location, current_speed, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height

    def land(self):
        self.altitude = 0
        self.current_speed = 0

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print("Дрон не может перемещаться, так как высота 0")
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
    def __init__(self, id, current_location, current_speed = 0, battery_level = 100, altitude = 0, package = None):
        super().__init__(id, current_location, current_speed, battery_level, altitude)
        self.package = package

    def load_package(self, package_name):
        self.package = package_name
        print(f"Посылка {self.package} загружена")

    def deliver_package(self):
        if self.package is None:
            print("Нет посылки для доставки.")
            return
        if self.altitude == 0:
            print(f"Посылка {self.package} доставлена")
        else:
            print(f"Поссылку невозможно доставить, так как дрон не на земле.")

    def get_info(self):
        based_info = super().get_info()
        return f"{based_info}, Высота: {self.altitude}, Посылка: {self.package}"

if __name__ == "__main__":
    print("=== Транспорт ===")
    transport = Transport(id="T-1", current_location="Точка посадки")
    print("Общая информация:", transport.get_info())
    transport.move("Центр", 10)
    print("После move:", transport.get_info())
    transport.charge(15)
    print("После зарядки:", transport.get_info())
    transport.move("Порт", 120)  # намеренно: заряда не хватит

    print("\n=== ELECTRIC SCOOTER ===")
    scooter = ElectricScooter(id="S-2", current_location="Парковка")
    print("Общая информация:", scooter.get_info())
    scooter.move("Парк", 5)  # не арендован
    scooter.is_rented = True
    scooter.move("Парк", 5)
    print("После аренды и поездки:", scooter.get_info())

    print("\n=== DRONE ===")
    drone = Drone(id="D-3", current_location="Склад-А")
    print("Общая информация:", drone.get_info())
    drone.move("Точка-B", 15)  # высота 0 — не поедет
    drone.take_off(50)
    drone.move("Точка-B", 15)  # теперь полетит
    print("После передвижения:", drone.get_info())
    drone.land()
    print("После приземления", drone.get_info())

    print("\n=== DELIVERY DRONE ===")
    del_drone = DeliveryDrone(id="DD-4", current_location="Склад")
    print("Общая информация:", del_drone.get_info())
    print(del_drone.calculate_route("Хаб", "Пункт-1"))
    del_drone.load_package("Документы")
    del_drone.take_off(20)
    del_drone.deliver_package()  # попытка в воздухе — должно предупредить
    del_drone.perform_emergency_landing()  # высота=0, скорость=0, батарея=5%
    del_drone.deliver_package()  # теперь на земле — доставит
    print("После доставки:", del_drone.get_info())
    # Попробуем снова маршрут и перелёт с малым зарядом
    del_drone.charge(50)  # подзарядим до 55%
    del_drone.take_off(10)
    del_drone.move("Пункт-1", 3)  # полетит, потратит 3%
    print(del_drone.get_info())

    
