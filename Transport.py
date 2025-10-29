class Transport:

    def __init__(
        self,
        id: str,
        current_location: str,
        current_speed: float = 0.0,
        battery_level: float = 100.0,
    ) -> None:
        self.id = id
        self.current_speed = max(0.0, float(current_speed))
        self.current_location = current_location
        self.battery_level = float(max(0.0, min(100.0, battery_level)))

    def move(self, new_location: str, speed: float) -> None:

        speed = max(0.0, float(speed))
        if self.battery_level < speed:
            print("Недостаточно заряда для поездки.")
            return

        self.current_location = new_location
        self.current_speed = speed
        self.battery_level = max(0.0, self.battery_level - speed)

    def charge(self, amount: float) -> None:
        amount = float(amount)
        self.battery_level = float(min(100.0, max(0.0, self.battery_level + amount)))

    def get_info(self) -> str:
        return (
            f"Transport[ID={self.id}] | "
            f"Скорость: {self.current_speed} | "
            f"Локация: {self.current_location} | "
            f"Заряд: {self.battery_level}%"
        )
