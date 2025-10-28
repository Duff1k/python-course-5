class Transport:
    def __init__(self, id, current_speed=0, current_location="стоянка", battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, new_location, new_speed):
        battery_change = new_speed

        if self.battery_level >= battery_change:
            self.current_location = new_location
            self.current_speed = new_speed
            self.battery_level = max(0, self.battery_level - battery_change)
            print(f"{self.id} едет около {new_location} со скоростью {new_speed} км/ч.\n")
        else:
            print("Недостаточно заряда для поездки.\n")

    def parking(self):  # сделала метод парковки чтобы после перемещения снизить скорость до 0
        self.current_speed = 0
        print("Транспорт припаркован.\n")

    def charge(self, battery_change):
        if self.current_speed == 0:
            self.battery_level = min(100, self.battery_level + battery_change)
            print(f"{self.id} зарядился на {battery_change}%. Текущий заряд: {self.battery_level}%\n")
        else:
            print("Припаркуйтесь!\n")

    def get_info(self):
        return (f"ID: {self.id}\nСкорость: {self.current_speed} км/ч\n"
                f"Местоположение: {self.current_location}\nЗаряд: {self.battery_level}%\n")


class ElectricScooter(Transport):
    def __init__(self, id, is_rented=False):
        super().__init__(id)
        self.is_rented = is_rented

    def move(self, new_location, new_speed):
        if self.is_rented:
            super().move(new_location, new_speed)
        else:
            print("Самокат не арендован.\n")


class Drone(Transport):
    def __init__(self, id, altitude=0):
        super().__init__(id)
        self.altitude = altitude

    def move(self, new_location, new_speed):
        if self.altitude > 0:
            battery_change = new_speed
            if self.battery_level >= battery_change:
                self.current_location = new_location
                self.current_speed = new_speed
                self.battery_level = max(0, self.battery_level - battery_change)
                print(f"Дрон летит в {new_location} на высоте {self.altitude} м.\n")
            else:
                print("Недостаточно заряда для полета.\n")
        else:
            print("Сначала нужно взлететь.\n")

    def take_off(self, altitude):
        self.altitude = altitude
        print(f"Дрон на высоте {altitude} м.\n")

    def land(self):
        self.altitude = 0
        print("Дрон приземлился.\n")
        self.parking()  # снизим скорость до 0
        # не стала тут(в классе дрон) переопределять метод parking, чтобы от задания не отходить


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        print(f"Проложен маршрут из {from_location} в {to_location}.\n")


class EmergencyLanding:
    def perform_emergency_landing(self):
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, package=None):
        super().__init__(id)
        self.package = package

    def load_package(self, package_name):
        if self.altitude == 0:
            self.package = package_name
            print(f"Посылка '{package_name}' загружена в дрон {self.id}.\n")
        else:
            print("Дрон в воздухе.\n")

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!\n")
                self.package = None
            else:
                print("Нет посылки для доставки.\n")
        else:
            print("Дрон в воздухе.\n")

    def get_info(self):
        return super().get_info() + (f"Высота: {self.altitude} м\n"
                                     f"Посылка: {self.package if self.package else 'нет'}\n")


if __name__ == "__main__":
    print(50 * "-")
    print('Поехали на машине из вокзала на почту и заряжаемся')
    print(50 * "-")

    transport = Transport("Car1", 20, "вокзал", 60)
    print(transport.get_info())
    transport.move("почта", 50)
    transport.parking()
    transport.charge(50)
    print(transport.get_info())

    print(50 * "-")
    print('Поехали на скутере в магазин без аренды, потом одумались и арендовали скутер')
    print(50 * "-")

    scooter = ElectricScooter("Scooter1")
    print(scooter.get_info())
    scooter.move("магазин", 15)
    scooter.is_rented = True
    scooter.move("магазин", 15)
    print(scooter.get_info())
    scooter.parking()
    scooter.is_rented = False

    print(50 * "-")
    print('Поехали на скутере в деревню за город и не посмотрели на заряд')
    print(50 * "-")

    scooter_low_charge = ElectricScooter("Scooter2", True)
    scooter_low_charge.battery_level = 10
    print(scooter_low_charge.get_info())
    scooter_low_charge.move("деревня", 20)

    print(50 * "-")
    print('Дрон полетел в офис')
    print(50 * "-")

    drone = Drone("Drone1", 0)
    print(drone.get_info())
    drone.move("офис", 30)
    drone.take_off(50)
    drone.move("офис", 30)
    print(drone.get_info())
    drone.land()
    print(drone.get_info())

    print(50 * "-")
    print('Дрон доставляет айфон домой')
    print(50 * "-")

    delivery_drone = DeliveryDrone("Delivery1")
    print(delivery_drone.get_info())
    delivery_drone.calculate_route("склад", "дом")
    delivery_drone.load_package("айфон")
    print(delivery_drone.get_info())
    delivery_drone.take_off(100)
    delivery_drone.move("дом", 40)
    print(delivery_drone.get_info())
    delivery_drone.perform_emergency_landing()
    print(delivery_drone.get_info())
    delivery_drone.deliver_package()
    print(delivery_drone.get_info())
