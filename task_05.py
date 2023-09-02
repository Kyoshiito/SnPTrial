import datetime


def date_in_future(integer):
    date_now = datetime.datetime.today()
    if isinstance(integer, int):
        future_date = (date_now + datetime.timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')
        return future_date
    else:
        return date_now.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))
