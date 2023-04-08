# 1
# Task 1
import datetime

date = datetime.date(2015, 6, 16)
week_number = date.isocalendar()[1]
print(week_number)


# Task 2
year = 2015
week_number = 50

first_day_of_year = datetime.date(year, 1, 1)

days_to_first_monday = (7 - first_day_of_year.weekday()) % 7

first_monday = first_day_of_year + datetime.timedelta(days=days_to_first_monday)
date = first_monday + datetime.timedelta(weeks=week_number-1)

print(date.strftime("%a %d %B %H:%M:%S %Y"))


# Task 3
year = 2023

first_day_of_year = datetime.date(year, 1, 1)

sundays = [first_day_of_year + datetime.timedelta(days=i) for i in range(7 - first_day_of_year.weekday(), 366, 7)]

for sunday in sundays:
    print(sunday.strftime("%Y-%m-%d"))


# Task 4
def addYears(date_obj, years):
    try:
        new_date = date_obj.replace(year=date_obj.year + years)

        if date_obj.month == 2 and date_obj.day == 29 and not datetime.date(date_obj.year + years, 2, 29):
            new_date = new_date.replace(day=28)

        return new_date

    except ValueError:
        # Если будет високосный год
        return None


print(addYears(datetime.date(2015, 1, 1), -1))
print(addYears(datetime.date(2015, 1, 1), 0))
print(addYears(datetime.date(2015, 1, 1), 2))


# 2
# Task 1
import pytz

gmt_time = datetime.datetime.utcnow()

local_tz = pytz.timezone('Asia/Almaty')
local_time = datetime.datetime.now(local_tz)

print(f"Время по Гринвичу: {gmt_time}")
print(f"Местное время: {local_time}")


# Task 2
date1 = datetime.date(2023, 4, 1)
date2 = datetime.date(2023, 4, 10)

delta = date2 - date1

print(f"Количество дней между датами: {delta.days}")


# Task 3
date1 = datetime.datetime(2023, 4, 1, 10, 30, 0)
date2 = datetime.datetime(2023, 4, 10, 15, 45, 30)

delta = date2 - date1

days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f"Разница между датами: {days} дней, {hours} часов, {minutes} минут, {seconds} секунд")


# Task 4
import calendar

year = 2023
month = 4

cal = calendar.monthcalendar(year, month)

html = '<table border="1">\n<tr><th colspan="7">{0} {1}</th></tr>\n'.format(calendar.month_name[month], year)

html += '<tr><th>Пн</th><th>Вт</th><th>Ср</th><th>Чт</th><th>Пт</th><th>Сб</th><th>Вс</th></tr>\n'

for week in cal:
    html += '<tr>'
    for day in week:
        if day == 0:
            html += '<td>&nbsp;</td>'
        else:
            html += '<td>{0}</td>'.format(day)
    html += '</tr>\n'

html += '</table>'

print(html)


# Regular expressions
# Task 1
import re

emails = ['example1@gmail.com', 'example2@yahoo.com', 'example3@hotmail.com']
domains = []

for email in emails:
    domain = re.findall('@([\w.]+)', email)
    domains.extend(domain)

print(domains)


# Task 2
text = 'apple banana cat dog elephant'

vowels = 'aeiou'
pattern = rf'\b[{vowels}]\w*'

words = re.findall(pattern, text, flags=re.IGNORECASE)
print(words)


# Task 3
text = 'apple, banana; cat dog   elephant'

split_pattern = ',|;|\s+'

words = re.split(split_pattern, text)
print(words)




