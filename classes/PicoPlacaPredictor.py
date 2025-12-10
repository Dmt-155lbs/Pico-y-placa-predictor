from classes.LicensePlate import LicensePlate

class PicoPlacaPredictor:
    def __init__(self):
        pass

    def predict(self, plate: LicensePlate, date_str: str, time_str: str) -> bool:
        """
        Determines if the vehicle can be on the road.
        
        """
        return True