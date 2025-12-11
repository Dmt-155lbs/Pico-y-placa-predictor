from utils.validators import validate_license_plate

class LicensePlate:
    def __init__(self, plate_number: str):
        # Clean the input (Upper case and remove extra spaces)
        self.plate_number = plate_number.upper().strip()
        
        # Call our manual validator function
        is_valid, error_msg = validate_license_plate(self.plate_number)
        
        if not is_valid:
            # If invalid, we crash intentionally so the CLI knows something is wrong
            raise ValueError(f"{error_msg} (Got: '{self.plate_number}')")

    def get_last_digit(self) -> int:
        """
        Returns the last digit of the plate as an integer.

        """
        return int(self.plate_number[-1])