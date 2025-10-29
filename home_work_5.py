class Transport:
    def __init__(self, id, current_speed=0, current_location="", battery_level=100):
        self.id = id
        self.current_speed = current_speed
        self.current_location = current_location
        self.battery_level = battery_level
    
    def move(self, new_location, new_speed):
        battery_consumption = new_speed
        
        if self.battery_level >= battery_consumption:
            self.current_location = new_location
            self.current_speed = new_speed
            self.battery_level = max(0, self.battery_level - battery_consumption)
            print(f"Транспорт {self.id} переместился в {new_location} со скоростью {new_speed} км/ч")
        else:
            print("Недостаточно заряда для поездки.")
    
    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Транспорт {self.id} заряжен до {self.battery_level}%")
    
    def get_info(self):
        return f"ID: {self.id}, Скорость: {self.current_speed} км/ч, Местоположение: {self.current_location}, Заряд: {self.battery_level}%"


class ElectricScooter(Transport):
    def __init__(self, id, current_speed=0, current_location="", battery_level=100, is_rented=False):
        super().__init__(id, current_speed, current_location, battery_level)
        self.is_rented = is_rented
    
    def move(self, new_location, new_speed):
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        
        super().move(new_location, new_speed)
    
    def rent(self):
        self.is_rented = True
        print(f"Самокат {self.id} арендован")
    
    def return_scooter(self):
        self.is_rented = False
        print(f"Самокат {self.id} возвращен")


class Drone(Transport):
    def __init__(self, id, current_speed=0, current_location="", battery_level=100, altitude=0):
        super().__init__(id, current_speed, current_location, battery_level)
        self.altitude = altitude
    
    def move(self, new_location, new_speed):
        if self.altitude > 0:
            self.current_location = new_location
            self.current_speed = new_speed
            battery_consumption = new_speed
            self.battery_level = max(0, self.battery_level - battery_consumption)
            print(f"Дрон летит в {new_location} на высоте {self.altitude} м.")
        else:
            print("Дрон не может лететь - он на земле")
    
    def take_off(self, height):
        self.altitude = height
        print(f"Дрон {self.id} взлетел на высоту {height} м")
    
    def land(self):
        self.altitude = 0
        print(f"Дрон {self.id} приземлился")


class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"Проложен маршрут из {from_location} в {to_location}."


class EmergencyLanding:
    def perform_emergency_landing(self):
        if hasattr(self, 'altitude'):
            self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5
        print("Аварийная посадка!")


class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, id, current_speed=0, current_location="", battery_level=100, altitude=0, package=None):
        Drone.__init__(self, id, current_speed, current_location, battery_level, altitude)
        self.package = package
    
    def load_package(self, package_name):
        self.package = package_name
        print(f"Посылка '{package_name}' загружена в дрон {self.id}")
    
    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!")
                self.package = None
            else:
                print("Нет посылки для доставки")
        else:
            print("Предупреждение: Дрон должен быть на земле для доставки посылки")
    
    def get_info(self):
        base_info = super().get_info()
        package_info = f", Посылка: {self.package if self.package else 'Нет'}"
        return base_info + package_info


# Клиентский код - демонстрация работы всех классов
print("." * 50)
print("Демонстрация системы 'Умный траниспорт'")
print("." * 50)

print("\n" + "."*30)
print("Базовый класс TRANSPORT")
print("."*30)

transport1 = Transport("T001", 0, "Гараж", 80)
print(transport1.get_info())
transport1.move("Центр города", 30)
transport1.charge(25)
print(transport1.get_info())

print("\n" + "."*30)
print("Класс ELECTRIC SCOOTER")
print("."*30)

scooter = ElectricScooter("ES001", 0, "Станция А", 50)
print(scooter.get_info())

# Попытка поехать без аренды
scooter.move("Парк", 15)

# Аренда и поездка
scooter.rent()
scooter.move("Парк", 15)
scooter.charge(30)
print(scooter.get_info())

scooter.return_scooter()

print("\n" + "."*30)
print("Класс DRONE")
print("."*30)

drone = Drone("D001", 0, "База", 75)
print(drone.get_info())

# Попытка полететь без взлета
drone.move("Торговый центр", 20)

# Взлет и полет
drone.take_off(50)
drone.move("Торговый центр", 20)
print(drone.get_info())

drone.land()
print(drone.get_info())

print("\n" + "."*30)
print("Класс DELIVERY DRONE")
print("."*30)

delivery_drone = DeliveryDrone("DD001", 0, "Склад", 90)
print(delivery_drone.get_info())

# Демонстрация методов из миксинов
route = delivery_drone.calculate_route("Склад", "Улица Ленина, 10")
print(route)

# Загрузка посылки и доставка
delivery_drone.load_package("Смартфон")
delivery_drone.take_off(30)
delivery_drone.move("Улица Ленина, 10", 25)
print(delivery_drone.get_info())

# Попытка доставить в воздухе
delivery_drone.deliver_package()

# Доставка на земле
delivery_drone.land()
delivery_drone.deliver_package()
print(delivery_drone.get_info())

# Демонстрация аварийной посадки
delivery_drone.take_off(40)
delivery_drone.perform_emergency_landing()
print(delivery_drone.get_info())

print("\n" + "."*30)
print("Тестирование предельных случаев")
print("."*30)

# Тест с низким зарядом
low_battery_scooter = ElectricScooter("ES002", 0, "Точка А", 5)
low_battery_scooter.rent()
low_battery_scooter.move("Точка Б", 10)  # Должен быть отказ из-за низкого заряда

# Тест зарядки выше 100%
transport2 = Transport("T002", 0, "База", 95)
transport2.charge(10)
print(transport2.get_info())
