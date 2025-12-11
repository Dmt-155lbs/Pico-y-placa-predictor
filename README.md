# Pico y Placa Predictor

A robust, object-oriented Python application that predicts whether a vehicle is restricted from circulation according to the "Pico y Placa" traffic regulations in Ecuador.

## Description

"Pico y Placa" is a driving restriction policy in Ecuador intended to mitigate traffic congestion during peak hours. This tool allows users to verify if a vehicle is allowed on the road based on three key inputs:
1.  **License Plate:** Validates the format and extracts the last digit.
2.  **Date:** Determines the day of the week.
3.  **Time:** Checks if the requested time falls within restricted windows.

## Restriction Rules

The application implements the following standard regulations:

| Day of Week | Restricted Plate (Last Digit) | Restricted Hours             |
|-------------|-------------------------------|------------------------------|
| Monday      | 1, 2                          | 07:00–09:30 and 16:00–19:30 |
| Tuesday     | 3, 4                          | 07:00–09:30 and 16:00–19:30 |
| Wednesday   | 5, 6                          | 07:00–09:30 and 16:00–19:30 |
| Thursday    | 7, 8                          | 07:00–09:30 and 16:00–19:30 |
| Friday      | 9, 0                          | 07:00–09:30 and 16:00–19:30 |
| Sat & Sun   | None                          | No restrictions              |


### Prerequisites
* Python 3.8 or higher

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/pico-placa-predictor.git](https://github.com/Dmt-155lbs/pico-placa-predictor.git)
    ```

2.  Run the application:
    ```bash
    python cli.py
    ```

### Usage Example
The program runs interactively. Follow the on-screen prompts to enter your data.

```text
Enter the license plate (e.g., PBX-1234): PBX-1234
Enter the date (YYYY-MM-DD): 2025-12-12
Enter the time (HH:MM): 08:30

---------------- RESULT ----------------
The car can be on the road. Sui
----------------------------------------
```
## Project Structure
```
Pico-y-placa-predictor/
├── cli.py                   # Main entry point (Handles user input)
├── src/                     # Core Business Logic
│   ├── LicensePlate.py      # Entity: Handles plate data and invokes validation
│   └── PicoPlacaPredictor.py # Engine: Applies the rules to the data
├── utils/                   # Shared Utilities
│   └── validators.py        # Helpers: Manual validation for plates, dates, and times
└── tests/                   # Automated Quality Assurance
    └── test_core.py         # Unit tests covering standard scenarios and edge cases

```

## Testing

To verify the logic and ensure reliability, run the automated test suite. This covers valid inputs, edge cases, and invalid data handling.
```bash
python -m unittest tests.test_core
```
## Author
Daniel Martínez





