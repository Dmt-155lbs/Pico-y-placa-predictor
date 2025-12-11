from src.LicensePlate import LicensePlate
from datetime import datetime
from utils.validators import parse_datetime

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
    
    def _is_time_restricted(self, time_obj) -> bool:
        """
        Internal helper to check if a specific time falls within restricted windows.

        :param time_obj: The datetime object containing the time to check.
        :return: True if the time is inside a restriction window, False otherwise.
        """
        """Helper to check if time is within restricted windows."""

        current_time = time_obj.time()
        
        morning_start = datetime.strptime("07:00", "%H:%M").time()
        morning_end = datetime.strptime("09:30", "%H:%M").time()
        evening_start = datetime.strptime("16:00", "%H:%M").time()
        evening_end = datetime.strptime("19:30", "%H:%M").time()

        if (morning_start <= current_time <= morning_end) or \
           (evening_start <= current_time <= evening_end):
            return True
        return False

    def predict(self, plate: LicensePlate, date_str: str, time_str: str) -> bool:
        """
        Determines whether a vehicle can be on the road based on its plate 
        and the current date/time.

        :param plate: The LicensePlate object containing the vehicle's info.
        :param date_str: Date string in "YYYY-MM-DD" format.
        :param time_str: Time string in "HH:MM" format.
        :return: True if the vehicle is allowed to drive, False if restricted.
        """
        
        try:
            dt_obj = parse_datetime(date_str, time_str)
        except ValueError:
            print("Error: Invalid Date/Time format. Use YYYY-MM-DD and HH:MM")
            return False

        # 1. Check Weekend (Saturday=5, Sunday=6)
        day_of_week = dt_obj.weekday()
        if day_of_week >= 5:
            return True # Free to drive on weekends

        # 2. Check Plate Restriction
        last_digit = plate.get_last_digit()
        restricted_digits = self.RESTRICTIONS.get(day_of_week, [])

        if last_digit in restricted_digits:
            # 3. If plate is restricted today, check the TIME
            if self._is_time_restricted(dt_obj):
                return False # RESTRICTED
        
        return True
        