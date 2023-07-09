def days_in_hours(days: int) -> int:
    return days * 24


def hours_to_minutes(hours: int) -> int:
    return hours * 60


def minutes_to_seconds(minutes: int) -> int:
    return minutes * 60


def seconds_to_days(seconds: int) -> int:
    return int(seconds / (60 * 60 * 24))
