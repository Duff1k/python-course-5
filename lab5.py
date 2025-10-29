class Transport:
    def __init__(self, code: str, location: str = "Стоянка"):
        self.code = code
        self.speed = 0
        self.place = location
        self.battery = 100

    def move(self, destination: str, velocity: float):
        if self.battery <= 0:
            print("Транспорт не может двигаться — батарея разряжена.")
            return

        if self.battery < velocity:
            print("Недостаточно заряда для движения с такой скоростью.")
            return

        self.place = destination
        self.speed = velocity
        self.battery = max(0, self.battery - velocity)

    def charge(self, value: float):
        self.battery = min(100, self.battery + value)
        print(f"Заряд увеличен до {self.battery}%.")

    def get_info(self) -> str:
        return (f"[{self.code}] Местоположение: {self.place}, "
                f"Скорость: {self.speed} км/ч, Заряд: {self.battery:.1f}%")


# ==========================================================

class ElectricScooter(Transport):
    def __init__(self, scooter_id: str, location: str = "Пункт проката"):
        super().__init__(scooter_id, location)
        self.rented = False

    def move(self, destination: str, velocity: float):
        if not self.rented:
            print("Самокат не арендован, движение невозможно.")
            return
        super().move(destination, velocity)


# ==========================================================

class Drone(Transport):
    def __init__(self, drone_id: str, base_location: str = "База"):
        super().__init__(drone_id, base_location)
        self.height = 0

    def take_off(self, meters: float):
        self.height += meters
        print(f"Дрон поднялся на {self.height} м.")

    def land(self):
        self.height = 0
        print("Дрон приземлился.")

    def move(self, destination: str, velocity: float):
        if self.height <= 0:
            print("Дрон должен быть в воздухе для полёта.")
            return

        if self.battery < velocity:
            print("Недостаточно заряда для полёта.")
            return

        self.place = destination
        self.speed = velocity
        self.battery = max(0, self.battery - velocity)
        print(f"Дрон движется к '{destination}' на высоте {self.height} м.")


# ==========================================================

class GPSNavigator:
    def build_route(self, start: str, end: str):
        return f"Маршрут: из '{start}' в '{end}'."


class EmergencyLanding:
    def emergency_land(self):
        self.height = 0
        self.speed = 0
        self.battery = 5
        print("Выполнена аварийная посадка! Остаток заряда: 5%.")


# ==========================================================

class DeliveryDrone(Drone, GPSNavigator, EmergencyLanding):
    def __init__(self, code: str, location: str = "Склад №1"):
        super().__init__(code, location)
        self.parcel = None

    def load(self, package_name: str):
        self.parcel = package_name
        print(f"Посылка '{package_name}' успешно загружена.")

    def deliver(self):
        if self.height > 0:
            print("Дрон должен быть на земле для выдачи посылки.")
            return
        if not self.parcel:
            print("Нет посылки для доставки.")
            return
        print(f"Посылка '{self.parcel}' доставлена получателю.")
        self.parcel = None

    def get_info(self):
        info = super().get_info()
        return info + f", Текущая посылка: {self.parcel if self.parcel else 'отсутствует'}"


# ==========================================================
# Пример использования
# ==========================================================

if __name__ == "__main__":
    print("=== Проверка Transport ===")
    t = Transport("T100", "Центральная площадь")
    print(t.get_info())
    t.move("Парк", 15)
    print(t.get_info())
    t.charge(10)

    print("\n=== Проверка ElectricScooter ===")
    s = ElectricScooter("S202")
    print(s.get_info())
    s.move("Улица Абая", 8)
    s.rented = True
    s.move("Улица Абая", 8)
    print(s.get_info())

    print("\n=== Проверка Drone ===")
    d = Drone("D303", "Аэродром")
    print(d.get_info())
    d.take_off(40)
    d.move("Центр", 20)
    print(d.get_info())
    d.land()

    print("\n=== Проверка DeliveryDrone ===")
    dd = DeliveryDrone("DD404", "Склад")
    print(dd.get_info())
    print(dd.build_route("Склад", "Проспект Мира"))
    dd.load("Ноутбук")
    dd.take_off(60)
    dd.move("Проспект Мира", 25)
    dd.land()
    dd.deliver()
    print(dd.get_info())

    print("\n=== Проверка аварийной посадки ===")
    dd.take_off(80)
    dd.move("Новый район", 30)
    dd.emergency_land()
    print(dd.get_info())
