from datetime import datetime, timedelta


def days_in_hours(days: int) -> int:
    return days * 24


def hours_to_minutes(hours: int) -> int:
    return hours * 60


def minutes_to_seconds(minutes: int) -> int:
    return minutes * 60


def seconds_to_days(seconds: int) -> int:
    return int(seconds / (60 * 60 * 24))


def get_current_date() -> list:
    """
    :return: [year, month, day]
    """
    res = []
    today = str(datetime.now())
    res.append(int(today[0:4]))  # Year
    res.append(int(today[5:7]))  # Month
    res.append(int(today[8:10]))  # Day
    return res


def get_future_date_in(days: int) -> list:
    """
    :param days:
    :return: [year, month, day]
    """
    res = []
    d = str(datetime.now() + timedelta(days=days))
    res.append(int(d[0:4]))  # Year
    res.append(int(d[5:7]))  # Month
    res.append(int(d[8:10]))  # Day
    return res
