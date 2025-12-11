from src.LicensePlate import LicensePlate
from src.PicoPlacaPredictor import PicoPlacaPredictor
import sys

def run():

    input_plate = input("Enter the license plate (e.g. ABC-1234): ")
    input_date = input("Enter the date (YYYY-MM-DD): ")
    input_time = input("Enter the time (HH:MM): ")
    
    print(f"Checking for Plate: {input_plate}, Date: {input_date}, Time: {input_time}")

    try:
        plate_obj = LicensePlate(input_plate)
        predictor = PicoPlacaPredictor()

        can_drive = predictor.predict(plate_obj, input_date, input_time)

        if can_drive:
            print("The car can be on the road. Sui")
        else:
            print("The car cannot be on the road.")

    except ValueError as e:
        print(f"\n ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n UNEXPECTED ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run()