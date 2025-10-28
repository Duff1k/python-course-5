import math

class Transport:
    def __init__(self, transport_id, initial_location):
        self.id = transport_id
        self.current_speed = 0
        self.current_location = initial_location
        self.battery_level = 100 

    def move(self, new_location, speed):
        required_battery = speed #Мы уменьшаем батарею на каждую единицу скорости, поэтому необходимый заряд батареи равен заданной скорости
        
        if self.battery_level < required_battery:
            print("Недостаточно заряда для поездки.")
        else:
            self.current_speed = speed
            self.current_location = new_location
            # Уменьшаем заряд, но не ниже 0
            self.battery_level = max(0, self.battery_level - required_battery)
            print(f"[{self.id}] Перемещение в '{self.current_location}' со скоростью {self.current_speed} км/ч.")

    def charge(self, amount):
        self.battery_level = min(100, self.battery_level + amount)
        print(f"[{self.id}] Батарея заряжена до {self.battery_level}%.")

    def get_info(self):
        return (f"ID: {self.id} | Место: {self.current_location} | "
                f"Скорость: {self.current_speed} км/ч | "
                f"Заряд: {self.battery_level}%")

class ElectricScooter(Transport):
    def __init__(self, transport_id, initial_location):
        super().__init__(transport_id, initial_location)
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"[{self.id}] Самокат арендован.")
        else:
            print(f"[{self.id}] Самокат уже был арендован.")

    def return_scooter(self):
        if self.is_rented:
            self.is_rented = False
            self.current_speed = 0 # Остановка при возврате
            print(f"[{self.id}] Самокат сдан с аренды.")
        else:
            print(f"[{self.id}] Самокат не был арендован.")

    def move(self, new_location, speed):
        if not self.is_rented:
            print(f"[{self.id}] Самокат не арендован. Движение невозможно.")
        else:
            super().move(new_location, speed)

class Drone(Transport):
    def __init__(self, transport_id, initial_location):
        super().__init__(transport_id, initial_location)
        self.altitude = 0  

    def take_off(self, height):
        self.altitude = height
        print(f"[{self.id}] Дрон взлетел. Высота: {self.altitude} м.")

    def land(self):
        self.altitude = 0
        self.current_speed = 0
        print(f"[{self.id}] Дрон приземлился.")

    def move(self, new_location, speed):
        if self.altitude <= 0:
            print(f"[{self.id}] Дрон на земле. Сначала нужно взлететь.")
            return

        # Проверяем батарею (логика дублируется из родителя, 
        # так как нам нужно вставить свою логику *до* и *после* родительской)
        required_battery = speed
        if self.battery_level < required_battery:
            print("Недостаточно заряда для поездки.")
        else:
            self.current_speed = speed
            self.current_location = new_location
            self.battery_level = max(0, self.battery_level - required_battery)
            print(f"[{self.id}] Дрон летит в {self.current_location} на высоте {self.altitude} м.")

class GPSNavigator:
    def calculate_route(self, from_location, to_location):
        return f"[GPS] Проложен маршрут из {from_location} в {to_location}."

class EmergencyLanding:
    def perform_emergency_landing(self):
        print(f"[{self.id}] Аварийная посадка!")
        self.altitude = 0
        self.current_speed = 0
        self.battery_level = 5 

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, transport_id, initial_location):
        super().__init__(transport_id, initial_location)
        self.package = None

    def load_package(self, package_name):
        if self.altitude == 0:
            self.package = package_name
            print(f"[{self.id}] Посылка '{self.package}' загружена.")
        else:
            print(f"[{self.id}] Невозможно загрузить посылку в полете.")

    def deliver_package(self):
        if self.altitude == 0:
            if self.package:
                print(f"Посылка '{self.package}' доставлена!")
                self.package = None
            else:
                print(f"[{self.id}] Нет посылки для доставки.")
        else:
            print(f"[{self.id}] Невозможно доставить посылку. Дрон должен приземлиться.")

    def get_info(self):
        base_info = super(Drone, self).get_info() 
        package_info = f"Посылка: {'нет' if self.package is None else self.package}"
        altitude_info = f"Высота: {self.altitude} м"
        
        return f"{base_info} | {altitude_info} | {package_info}"


#Клиентский код
print("=" * 40)
print("--- 1. Тест Transport ---")
print("=" * 40)
car = Transport("T-100", "Гараж")
print(car.get_info())
car.move("Магазин", 50) 
print(car.get_info())
car.move("Дом", 60)      
car.charge(30)          
print(car.get_info())
car.move("Дом", 60)      
print(car.get_info())

print("\n" + "=" * 40)
print("--- 2. Тест ElectricScooter ---")
print("=" * 40)
scooter = ElectricScooter("S-01", "Парковка А")
print(scooter.get_info())
scooter.move("Кафе", 20) 
scooter.rent()
scooter.move("Кафе", 20) 
print(scooter.get_info())
scooter.return_scooter()
print(scooter.get_info())

print("\n" + "=" * 40)
print("--- 3. Тест Drone ---")
print("=" * 40)
drone = Drone("D-500", "База")
print(drone.get_info())
drone.move("Точка X", 30) 
drone.take_off(50)
print(drone.get_info())
drone.move("Точка X", 30)
print(drone.get_info())
drone.land()
print(drone.get_info())

print("\n" + "=" * 40)
print("--- 4. Тест DeliveryDrone (Множественное наследование) ---")
print("=" * 40)
delivery_bot = DeliveryDrone("DD-007", "Склад")
print(delivery_bot.get_info()) 

# 1. Методы GPS (Mixin)
print(delivery_bot.calculate_route(delivery_bot.current_location, "Клиент А"))

# 2. Методы DeliveryDrone (Загрузка)
delivery_bot.load_package("Пицца Пепперони")
print(delivery_bot.get_info())

# 3. Методы Drone (Полет)
delivery_bot.take_off(100)
delivery_bot.move("Клиент А", 40) 
print(delivery_bot.get_info())

# 4. Методы DeliveryDrone (Доставка)
delivery_bot.deliver_package()
delivery_bot.land()
delivery_bot.deliver_package() 
print(delivery_bot.get_info()) 

# 5. Методы EmergencyLanding (Mixin)
delivery_bot.charge(100) 
delivery_bot.take_off(200)
delivery_bot.move("Точка Y", 50) 
print(f"Перед аварией: {delivery_bot.get_info()}")
delivery_bot.perform_emergency_landing()
print(f"После аварии: {delivery_bot.get_info()}") 