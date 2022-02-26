import re
from datetime import datetime


def varify_name(name) -> bool:
    """
    if name is valid will return True
    a valid name is a name that starts with Capital latter and contains at least 2 letters
    All other letters should be lowered cased
    :param name: a string
    :return: True if name is valid
    """
    pattern = re.compile(r'^[A-Z][a-z]+$')
    return pattern.match(name) is not None


def get_current_year() -> int:
    """
    :return: the current year as an integer
    """
    today = datetime.today()
    return today.year
