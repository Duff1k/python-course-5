import itertools


class Transport:
    id_transport = itertools.count(1)


    def __init__(self, current_speed=0, current_location='', battery_level=100):
        self.id = str(next(Transport.id_transport))
        self.current_speed = current_speed
        self.current_location = current_location
        if battery_level <= 100:
            self.battery_level = battery_level
        else:
            self.battery_level = 100
            print("Максимальный уровень заряда 100%")


    def move(self, location, speed): #надо дописать
        if (abs(self.current_speed - speed) > self.battery_level):
            print("Недостаточно заряда для поездки.")
        else:
            self.current_location = location
            self.battery_level = self.battery_level - abs(self.current_speed - speed)
            self.current_speed = speed
        return self.current_location, self.current_speed, self.battery_level


    def charge(self, charging):
        if (self.battery_level + charging > 100):
            print("Батарея не может быть заряжена выше 100%")
        else:
            self.battery_level += charging
        return f"Заряд: {self.battery_level}"


    def get_info(self):
        return (f"ID: {self.id}; "
                f"Скорость: {self.current_speed}; "
                f"Местоположение: {self.current_location}; "
                f"Заряд: {self.battery_level}")


class ElectricScooter(Transport):
    def __init__(self, current_speed=0, current_location='', battery_level=100, is_rented=False):
        super().__init__(current_speed, current_location, battery_level)
        self.is_rented = is_rented


    def move(self, location, speed):
        if (self.is_rented == False):
            print("Самокат не арендован.")
        else:
            if (abs(self.current_speed - speed) > self.battery_level):
                print("Недостаточно заряда для поездки.")
            else:
                self.current_location = location
                self.battery_level = self.battery_level - abs(self.current_speed - speed)
                self.current_speed = speed
        return self.current_location, self.current_speed, self.battery_level, self.is_rented


    def rent(self):
        self.is_rented = True
        return "Самокат арендован"


    def simple(self):
        self.is_rented = False
        return "Самокат сдан"


class Drone(Transport):
    def __init__(self, current_speed=0, current_location='', battery_level=100, altitude=0):
        super().__init__(current_speed, current_location, battery_level)
        self.altitude = altitude


    def take_off(self, height):
        self.altitude += height
        return f"Дрон взлетел на высоту {self.altitude} м."


    def land(self):
        self.altitude = 0
        return "Дрон сел."


    def move(self, location, speed):
        if (self.altitude == 0):
            print("Дрон не может передвигаться не взлетев.")
        else:
            if (self.battery_level - abs(self.current_speed - speed) < 0):
                print("Недостаточно заряда для поездки.")
            else:
                self.current_location = location
                self.battery_level = self.battery_level - abs(self.current_speed - speed)
                self.current_speed = speed
                print(f"Дрон летит в {self.current_location} на высоте {self.altitude} м.")
        return self.current_location, self.current_speed, self.battery_level, self.altitude


#Тест класса транспорт
client_transport = Transport(30, 'Главная улица')
print(client_transport.get_info())
print(client_transport.move('Дом', 150))
print(client_transport.move('Дом', 101))
print(client_transport.charge(101))
print(client_transport.charge(50))
print("")


#Тест электроскутера
print("Тест класса Электроскутер")
client_electricscooter = ElectricScooter(20, 'Дома', 160)
print(client_electricscooter.get_info())
print(client_electricscooter.move('Работа', 150))
print(client_electricscooter.rent())
print(client_electricscooter.move('Работа', 150))
print(client_electricscooter.move('Работа', 0))
print(client_electricscooter.simple())
print(client_electricscooter.move('Работа', 0))
print("")


#Тест дрона
print("Тест класса Дрон")
client_drone = Drone(20, 'Мак', 90)
print(client_drone.get_info())
print(client_drone.move('Работа', 150))
print(client_drone.take_off(10))
print(client_drone.move('Работа', 50))
print(client_drone.move('Пункт выдачи', 0))
print(client_drone.land())
print("")
