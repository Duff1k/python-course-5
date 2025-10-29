class Transport:
    def __init__(self, id: str, current_location: str, current_speed: int = 0, battery_level: int = 100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location: str, speed: int):
        required_battery = speed
        if self.battery_level < required_battery:
            print("--Недостаточно заряда для поездки--")
            return

        self.battery_level -= required_battery
        if self.battery_level < 0:
            self.battery_level = 0

        self.current_speed = speed
        self.current_location = new_location

    def charge(self, amount: int):
        self.current_speed = 0
        self.battery_level += amount
        if self.battery_level > 100:
            self.battery_level = 100

    def get_info(self):
        return ( f"ID: {self.id}, "
        f"Скорость: {self.current_speed}, "
        f"Местоположение: {self.current_location}, "
        f"Заряд: {self.battery_level}%"
    )

transport = Transport(id="Transport", current_location="АСЭ")
print(transport.get_info())
transport.move("метро Дмитровская", 60)
print(transport.get_info())
transport.charge(15)
print(transport.get_info())

class ElectricScooter(Transport):
    def __init__(self, id: str, current_location: str, is_rented: bool = False):
        super().__init__(id, current_location)
        self.is_rented = is_rented

    def move(self, new_location: str, speed: int):
        if not self.is_rented:
            print("--Самокат не арендован--")
            return
        super().move(new_location, speed)

scooter = ElectricScooter(id="Scooter", current_location="Остановка")
print(scooter.get_info())
scooter.move("Кинотеатр", 20)
scooter.is_rented = True
scooter.move("Кинотеатр", 20)
print(scooter.get_info())

class Drone(Transport):
    def __init__(self, id: str, current_location: str, altitude: int = 0):
        super().__init__(id, current_location)
        self.altitude = altitude

    def take_off(self, height: int):
        self.altitude += height

    def land(self):
        self.altitude = 0
        self.current_location = "Земля"
        self.current_speed = 0

    def move(self, new_location: str, speed: int):
        if self.altitude <= 0:
            print("Дрон не может лететь: высота равна 0.")
            return

        super().move(new_location, speed)
        print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")

drone = Drone(id="Drone", current_location="Парк")
print(drone.get_info())
drone.move("Небо", 10)
drone.take_off(100)
drone.move("Небо", 20)
print(drone.get_info())
drone.land()
print(drone.get_info())

class GPSNavigator:
    def calculate_route(self, from_location: str, to_location: str):
        return f"Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    def perform_emergency_landing(self):
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id: str, current_location: str, altitude: int = 0, package: str = None):
        super().__init__(id, current_location, altitude)
        self.package = package

    def load_package(self, package: str):
        self.package = package

    def deliver_package(self):
        if (self.altitude != 0) and (self.package != None):
            print(f"Посылка {self.package} доставлена!")
            self.package = None
        elif (self.package == None):
            print(f"Посылки нет")
        elif self.altitude == 0:
            print(f"Не взлетели")

    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'нет'}"
        return base_info + package_info

delivery_drone = DeliveryDrone(id="DeliveryDrone", current_location="Магазин")
print(delivery_drone.get_info())
print(delivery_drone.calculate_route("Магазин", "Адрес доставки"))
delivery_drone.deliver_package()
delivery_drone.load_package("Хлеб")
print(delivery_drone.get_info())
delivery_drone.deliver_package()
delivery_drone.load_package("Хлеб")
delivery_drone.altitude = 100
print(delivery_drone.get_info())
delivery_drone.deliver_package()
delivery_drone.land()
print(delivery_drone.get_info())
print(delivery_drone.calculate_route("Адрес доставки", "Магазин"))
delivery_drone.perform_emergency_landing()
print(delivery_drone.get_info())