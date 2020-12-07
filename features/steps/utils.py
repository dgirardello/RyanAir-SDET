import datetime


def calculate_date(days, weekday=None):

    if weekday is not None:
        weekday = str(weekday).capitalize()
        week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        week_day_today = datetime.datetime.now().weekday()
        if week_days.index(weekday) > week_day_today:
            days += len(week_days) - week_day_today - 1
        elif week_days.index(weekday) < week_day_today:
            days += week_day_today - week_days.index(weekday)

    calculated_date = datetime.datetime.today().timestamp() + (3600 * 24 * days)
    return datetime.datetime.fromtimestamp(calculated_date).strftime("%Y-%m-%d")