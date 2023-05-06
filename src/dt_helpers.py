from datetime import datetime


def parse_datetime(str):
    no_timezone = ' '.join(str.split(' ')[:-1])
    if not no_timezone:
        return datetime.min
    return datetime.strptime(no_timezone, r'%m/%d/%Y @ %I:%M %p')


def format_date(dt):
    if dt == datetime.min:
        return None
    return datetime.strftime(dt, r'%b %d %Y').replace(' 0', ' ')


def format_time(dt):
    if dt == datetime.min:
        return None
    return datetime.strftime(dt, r'%I:%M %p').strip('0')
