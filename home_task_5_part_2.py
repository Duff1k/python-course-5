from home_task_5_part_1 import Drone


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    def perfom_emergency_landing(self):
        self.current_speed = 0
        self.altitude = 0
        self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, current_speed=0, current_location='', battery_level=100, altitude=0, package=None):
        super().__init__(current_speed, current_location, battery_level, altitude)
        self.package = package


    def load_package(self, loading_package):
        self.package = loading_package


    def deliver_package(self):
        if self.altitude == 0:
            print(f'Посылка {self.package} доставлена!')
            self.package = None
        else:
            print("Внимание дрон еще в воздухе!")


    def get_info(self):
        return (f"ID: {self.id}; "
                f"Скорость: {self.current_speed}; "
                f"Местоположение: {self.current_location}; "
                f"Заряд: {self.battery_level}; "
                f"Посылка: {self.package}")


#Тест дрона доставщика и миксинов
delivery_drone = DeliveryDrone(0, 'Офис')
print(delivery_drone.get_info())
delivery_drone.load_package('Документы')
print(delivery_drone.get_info())
print(delivery_drone.calculate_route('Офис', 'Парк'))
print(delivery_drone.get_info())
print(delivery_drone.take_off(10))
print(delivery_drone.deliver_package())
print(delivery_drone.get_info())
print(delivery_drone.move('Парк', 50))
print(delivery_drone.land())
print(delivery_drone.deliver_package())
print(delivery_drone.get_info())

print('')
delivery_drone2 = DeliveryDrone(0, 'Офис')
print(delivery_drone2.get_info())
delivery_drone2.load_package('Фото')
delivery_drone2.perfom_emergency_landing()
print(delivery_drone2.get_info())