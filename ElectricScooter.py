from Transport import Transport

class ElectricScooter(Transport):

    def __init__(
        self,
        id: str,
        current_location: str,
        is_rented: bool = False,
        current_speed: float = 0.0,
        battery_level: float = 100.0,
    ) -> None:
        super().__init__(
            id=id,
            current_location=current_location,
            current_speed=current_speed,
            battery_level=battery_level,
        )
        self.is_rented = bool(is_rented)

    def move(self, new_location: str, speed: float) -> None:
        if not self.is_rented:
            print("Самокат не арендован.")
            return
        super().move(new_location, speed)
