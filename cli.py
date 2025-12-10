from classes.LicensePlate import LicensePlate
from classes.PicoPlacaPredictor import PicoPlacaPredictor

def run():

    input_plate = "PBX-1234"
    input_date = "2025-12-12"
    input_time = "08:30"
    
    print(f"Checking for Plate: {input_plate}, Date: {input_date}, Time: {input_time}")

    plate_obj = LicensePlate(input_plate)
    predictor = PicoPlacaPredictor()

    can_drive = predictor.predict(plate_obj, input_date, input_time)

    if can_drive:
        print("The car can be on the road. Sui")
    else:
        print("The car cannot be on the road.")

if __name__ == "__main__":
    run()