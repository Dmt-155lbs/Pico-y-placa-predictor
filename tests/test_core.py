import unittest
from src.LicensePlate import LicensePlate
from src.PicoPlacaPredictor import PicoPlacaPredictor

class TestPicoPlaca(unittest.TestCase):

    # Test 1: License Plate Logic
    def test_last_digit_extraction(self):
        # We expect PBX-1234 to give us 4
        plate = LicensePlate("PBX-1234")
        self.assertEqual(plate.get_last_digit(), 4)
        
        # We expect ABC-987 to give us 7
        plate2 = LicensePlate("ABC-987")
        self.assertEqual(plate2.get_last_digit(), 7)

    # Test 2: The Rules Engine (Monday Restriction)
    def test_monday_restriction(self):
        # Mondays: Plates ending in 1 & 2 are RESTRICTED
        # Hours: 07:00 - 09:30 and 16:00 - 19:30
        
        predictor = PicoPlacaPredictor()
        plate = LicensePlate("PBX-0001") # Ends in 1
        
        # Case A: Monday at 8:00 AM (Should be Restricted/False)
        can_drive = predictor.predict(plate, "2025-12-08", "08:00") 
        # Note: 2025-12-08 is a Monday
        self.assertFalse(can_drive, "Plate ending in 1 should be restricted on Monday morning")

    # Test 3: The Rules Engine (Allowed Time)
    def test_allowed_time(self):
        # Even if it's Monday, 12:00 PM is free
        predictor = PicoPlacaPredictor()
        plate = LicensePlate("PBX-0001")
        
        can_drive = predictor.predict(plate, "2025-12-08", "12:00")
        self.assertTrue(can_drive, "Plate ending in 1 should be allowed on Monday at noon")

if __name__ == '__main__':
    unittest.main()