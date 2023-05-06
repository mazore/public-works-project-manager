from datetime import datetime


def parse_datetime(str):
    no_timezone = ' '.join(str.split(' ')[:-1])
    if not no_timezone:
        return datetime.min
    return datetime.strptime(no_timezone, r'%m/%d/%Y @ %I:%M %p')


def format_datetime(dt):
    if dt == datetime.min:
        return None
    return datetime.strftime(dt, r'%B %d %Y, %I:%M %p').replace(' 0', ' ')
