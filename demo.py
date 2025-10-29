# -*- coding: utf-8 -*-
from Transport import Transport
from ElectricScooter import ElectricScooter
from Drone import Drone
from DeliveryDrone import DeliveryDrone


def demo():
    t = Transport(id="T-001", current_location="Склад")
    print(t.get_info())
    t.move("Порт", 20)
    print(t.get_info())
    t.charge(15)
    print(t.get_info())
    t.move("Центр", 200)
    print(t.get_info())

    s = ElectricScooter(id="E-101", current_location="Парк")
    print(s.get_info())
    s.move("Мост", 10)
    s.is_rented = True
    s.move("Мост", 10)
    print(s.get_info())

    d = Drone(id="D-202", current_location="Ангар")
    print(d.get_info())
    d.move("Точка А", 10)
    d.take_off(50)
    print(d.get_info())
    d.move("Точка А", 10)
    print(d.get_info())
    print("Посадка...")
    d.land()
    print(d.get_info())

    dd = DeliveryDrone(id="DD-303", current_location="Хаб")
    print(dd.get_info())
    print(dd.calculate_route("Хаб", "Склад 7"))
    dd.load_package("Документы")
    dd.deliver_package()
    print(dd.get_info())
    dd.load_package("Посылка-42")
    dd.take_off(30)
    dd.move("Адрес клиента", 15)
    dd.deliver_package()
    dd.perform_emergency_landing()
    dd.deliver_package()
    print(dd.get_info())


if __name__ == "__main__":
    demo()
