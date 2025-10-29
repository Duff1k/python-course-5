class Transport:
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level

    def move(self, location, speed):
        current_speed = int(speed)
        needed_charge = speed
        if self.battery_level >= needed_charge:
            self.current_location = location
            self.current_speed = current_speed
            self.battery_level -= needed_charge
            print(f"Поездка завершена, оставшийся заряд батареи: {self.battery_level}")
        else:
            print("Поездка невозможна, слишком низкий заряд батареи")

    def charge(self, charge_battery):
        if (charge_battery + self.battery_level) >= 100:
            self.battery_level = 100
        else:
            self.battery_level = self.battery_level + charge_battery

    def get_info(self):
        return (f"id: {self.id}, cкорость: {self.current_speed}, местоположение: {self.current_location}, заряд батареи: {self.battery_level}")


class ElectricScooter(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, is_rented = False):
        super().__init__(id, current_speed, current_location, battery_level)
        self.is_rented = is_rented

    def move(self, location, speed):
        if not self.is_rented:
            print("Вы не можете поехать, т.к. самокат не арендован")
            return
        return super().move(location, speed)


class Drone(Transport):
    def __init__(self, id, current_speed = 0, current_location = "", battery_level = 100, altitude = 0):
        super().__init__(id, current_speed, current_location, battery_level)
        self.altitude = altitude

    def take_off(self, height):
        self.altitude += height

    def land(self):
        self.altitude = 0
        print("Посадка выполнена успешно")

    def move(self, location, speed):
        if self.altitude <= 0:
            print("Движение невозможно, увеличьте высоту полета")
            return
        required_charge = speed
        if self.battery_level >= required_charge:
            self.current_location = location
            self.current_speed = speed
            self.battery_level -= required_charge
            print(f"Дрон летит в {location} на высоте {self.altitude}м.")
        else:
            print("Полет невозможен, слишком низкий заряд батареи")


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        print (f"Проложен маршрут из {from_location} в {to_location}")


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

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!")
                self.package = None
            else:
                print("Доставка не запланирована")
        else:
            print("Доставка невозможна, дрон находится на высоте")

    def get_info(self):
        transport_info = super().get_info()
        package_info = f"Посылка: {self.package if self.package else 'Нет'}"
        return transport_info + package_info


if __name__ == "__main__":
    print("<Тест класса ElectricScooter>")

    scooter = ElectricScooter("1", current_location = "Метро Каширская")
    print(scooter.get_info())

    print("- Тест поездки без аренды")
    scooter.move("НИЯУ МИФИ", 15)

    print("- Тест поездки c арендой")
    scooter.is_rented = True
    scooter.move("Парк Нагатино-Садовники", 20)

    print("- Тест зарядки в пределах 100%")
    scooter.charge(5)
    print(scooter.get_info())

    print("- Тест зарядки более 100%")
    scooter.charge(50)
    print(scooter.get_info())
    print()

    print("<Тест класса Drone>")
    drone = Drone("2", current_location = "Точка Кипения НИЯУ МИФИ")
    print(drone.get_info())

    print("- Тест полета на 0 высоте")
    drone.move("НИЯУ МИФИ", 20)

    print("- Тест полета с набором высоты")
    drone.take_off(30)
    drone.move("НИЯУ МИФИ", 20)
    print(drone.get_info())

    print("- Тест посадки")
    drone.land()
    print()

    print("<Тест класса DeliveryDrone>")
    delivery_drone = DeliveryDrone("3", current_location = "Пятерочка")
    print(delivery_drone.get_info())

    print("- Тест доставки, когда дрон на определенной высоте")
    delivery_drone.take_off(45)
    delivery_drone.deliver_package()

    print("- Тест доставки, когда дрон на 0 высоте")
    delivery_drone.land()
    delivery_drone.load_package("Манго")
    delivery_drone.calculate_route("Пятерочка", "Общежитие")
    print(delivery_drone.get_info())
    delivery_drone.deliver_package()

    print("- Тест аварийной посадки")
    delivery_drone.perform_emergency_landing()
    print(delivery_drone.get_info())