from datetime import datetime


def period_in_days(start_date, end_date):
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')
    timedelta = end.date() - start.date()

    return timedelta.days + 1