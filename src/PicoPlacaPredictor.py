from src.LicensePlate import LicensePlate
from datetime import datetime
from utils.validators import validate_date, validate_time

class PicoPlacaPredictor:
    """
    The main engine for determining driving restrictions based on 
    Pico y Placa regulations.
    """

    def __init__(self):
        # Define the Rules clearly
        # Monday=0, Sunday=6
        self.RESTRICTIONS = {
            0: [1, 2], # Monday
            1: [3, 4], # Tuesday
            2: [5, 6], # Wednesday
            3: [7, 8], # Thursday
            4: [9, 0], # Friday
        }
    
    def _is_time_restricted(self, check_time) -> bool:
        """
        Internal helper to check if a specific time falls within restricted windows.

        :param check_time: The datetime object containing the time to check.
        :return: True if the time is inside a restriction window, False otherwise.
        """
        """Helper to check if time is within restricted windows."""

        morning_start = datetime.strptime("07:00", "%H:%M").time()
        morning_end = datetime.strptime("09:30", "%H:%M").time()
        evening_start = datetime.strptime("16:00", "%H:%M").time()
        evening_end = datetime.strptime("19:30", "%H:%M").time()

        return (morning_start <= check_time <= morning_end) or \
               (evening_start <= check_time <= evening_end)

    def predict(self, plate: LicensePlate, date_str: str, time_str: str) -> bool:
        """
        Determines whether a vehicle can be on the road based on its plate 
        and the current date/time.

        :param plate: The LicensePlate object containing the vehicle's info.
        :param date_str: Date string in "YYYY-MM-DD" format.
        :param time_str: Time string in "HH:MM" format.
        :return: True if the vehicle is allowed to drive, False if restricted.
        """
        
        # 1. Validate and Parse Date
        valid_date, dt_obj = validate_date(date_str)
        if not valid_date:
            raise ValueError(dt_obj) # Return the error message

        # 2. Validate and Parse Time
        valid_time, time_obj = validate_time(time_str)
        if not valid_time:
            raise ValueError(time_obj)

        # 3. Check Weekend (Saturday=5, Sunday=6)
        # Note: dt_obj from validators is a datetime, so we can use .weekday()
        if dt_obj.weekday() >= 5:
            return True 

        # 4. Check Plate Restriction
        last_digit = plate.get_last_digit()
        restricted_digits = self.RESTRICTIONS.get(dt_obj.weekday(), [])

        if last_digit in restricted_digits:
            # 5. Check Time
            if self._is_time_restricted(time_obj):
                return False 
        
        return True
        