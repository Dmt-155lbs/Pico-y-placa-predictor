from datetime import datetime

def parse_datetime(date_str: str, time_str: str) -> datetime:
    """
    Parses string date and time inputs into a single datetime object.
    
    :param date_str: The date in "YYYY-MM-DD" format.
    :param time_str: The time in "HH:MM" format.
    :return: A datetime object representing the combined inputs.
    :raises ValueError: If the format does not match.
    """
    full_date_str = f"{date_str} {time_str}"
    return datetime.strptime(full_date_str, "%Y-%m-%d %H:%M")