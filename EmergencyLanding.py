class EmergencyLanding:

    def perform_emergency_landing(self) -> None:
        try:
            self.altitude = 0.0
        except AttributeError:
            pass
        try:
            self.current_speed = 0.0
        except AttributeError:
            pass
        try:
            self.battery_level = 5.0
        except AttributeError:
            pass
        print("Аварийная посадка!")
