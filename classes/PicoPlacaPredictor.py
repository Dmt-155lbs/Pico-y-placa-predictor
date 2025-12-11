from classes.LicensePlate import LicensePlate
from datetime import datetime

class PicoPlacaPredictor:
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
        """Helper to check if time is within restricted windows."""
        current_time = time_obj.time()
        
        # Morning Window: 07:00 - 09:30
        morning_start = datetime.strptime("07:00", "%H:%M").time()
        morning_end = datetime.strptime("09:30", "%H:%M").time()

        # Afternoon Window: 16:00 - 19:30
        evening_start = datetime.strptime("16:00", "%H:%M").time()
        evening_end = datetime.strptime("19:30", "%H:%M").time()

        if (morning_start <= current_time <= morning_end) or \
           (evening_start <= current_time <= evening_end):
            return True
        return False

    def predict(self, plate: LicensePlate, date_str: str, time_str: str) -> bool:
        """
        Determines if the vehicle can be on the road.
        
        """
        # 1. Parse Data: Combining date and time strings to create a datetime object
        try:
            full_date_str = f"{date_str} {time_str}"
            dt_obj = datetime.strptime(full_date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Error: Invalid Date/Time format. Use YYYY-MM-DD and HH:MM")
            return False

        # 2. Check Weekend (Saturday=5, Sunday=6)
        day_of_week = dt_obj.weekday()
        if day_of_week >= 5:
            return True # Free to drive on weekends

        # 3. Check Plate Restriction
        last_digit = plate.get_last_digit()
        restricted_digits = self.RESTRICTIONS.get(day_of_week, [])

        if last_digit in restricted_digits:
            # 4. If plate is restricted today, check the TIME
            if self._is_time_restricted(dt_obj):
                return False # RESTRICTED
        
        return True
        