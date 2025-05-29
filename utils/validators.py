import re
import dateparser
from datetime import datetime
from email_validator import validate_email, EmailNotValidError


def validate_email_address(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def validate_phone_number(phone: str) -> bool:
    pattern = re.compile(r"^\+?\d{7,15}$")
    return bool(pattern.match(phone.strip()))


def parse_and_validate_date(date_str: str) -> str | None:
    dt = dateparser.parse(date_str)
    if dt and dt.date() >= datetime.today().date():
        return dt.strftime("%Y-%m-%d")
    return None
