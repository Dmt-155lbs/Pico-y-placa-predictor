from datetime import datetime

def validate_license_plate(plate: str) -> bool:
    """
    Validates the format of a license plate.
    
    :param plate: The license plate string to validate.
    :return: (bool, str) -> (is_valid, error_message)
    """
    if len(plate) not in [7, 8]:
        return False, "License plate must be 7 or 8 characters long."
    if plate[3] != '-':
        return False, "License plate must have a '-' after the letters."
    if not plate[:3].isalpha():
        return False, "License plate must start with 3 letters."
    if not plate[4:].isdigit():
        return False, "License plate must end with 4 digits."
    return True, ""

def validate_date(date_text: str):
    """
    Validates date string manually (YYYY-MM-DD).
    Returns: (bool, str or datetime)
    """
    # 1. Basic length check
    if len(date_text) != 10:
        return False, "Date must be in format YYYY-MM-DD."
    
    # 2. Check separators
    if date_text[4] != '-' or date_text[7] != '-':
        return False, "Date must assume YYYY-MM-DD format with hyphens."

    # 3. Validate actual existence of date (handles Feb 30, etc.)
    try:
        dt = datetime.strptime(date_text, "%Y-%m-%d")
        return True, dt
    except ValueError:
        return False, "Invalid calendar date."

def validate_time(time_text: str):
    """
    Validates time string manually (HH:MM).
    Returns: (bool, str or datetime_time)
    """
    if len(time_text) != 5:
        return False, "Time must be in format HH:MM."
    
    if time_text[2] != ':':
        return False, "Time must have a colon ':' separator."

    try:
        # We parse it to verify hours are 0-23 and minutes 0-59
        t = datetime.strptime(time_text, "%H:%M").time()
        return True, t
    except ValueError:
        return False, "Invalid time. Hours must be 00-23, Minutes 00-59."
