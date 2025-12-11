class LicensePlate:
    def __init__(self, plate_number: str):
        self.plate_number = plate_number

    def get_last_digit(self) -> int:
        """
        Returns the last digit of the plate as an integer.

        """
        return int(self.plate_number[-1])