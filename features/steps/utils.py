import datetime


def calculate_date(days):
    calculated_date = datetime.datetime.today().timestamp() + (3600 * 24 * days)
    return datetime.datetime.fromtimestamp(calculated_date).strftime("%Y-%m-%d")