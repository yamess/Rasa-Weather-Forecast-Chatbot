import datetime
from typing import Optional, Tuple
from pyowm.owm import OWM


reg = OWM("not-actually-used-key").city_id_registry()


def text_to_coordinate(text_city: str) -> Tuple[float, float]:
    """
    Parse city name to coordinate

    :param text_city: str, city name
    :return: latitude, longitude
    """

    list_of_locations = reg.locations_for(text_city)

    # Select the first one (maybe incorrect)
    city = list_of_locations[0]

    return city.lat, city.lon


def text_to_date(text_date: str) -> Optional[datetime.date]:
    """
    Convert text based date info into datetime object.
    If the convert is not supported, it will return None

    :param text_date:
    :return: date time
    """

    today = datetime.datetime.now()
    one_more_day = datetime.timedelta(days=1)

    if text_date == "today":
        return today.date()

    if text_date == "tomorrow":
        return (today + one_more_day).date()

    if text_date == "the day after tomorrow":
        return (today + one_more_day * 2).date()

    # not supported
    if text_date in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
        return None

    # not supported
    if text_date in ["yesterday"]:
        return None

    # anything else
    return None
