from dateutil import easter


def get_easter(year, type_calendar):
    easter_day = easter.esater(year, type_calendar)
    return easter_day

