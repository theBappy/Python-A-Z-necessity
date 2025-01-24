# import datetime
# import pytz

# dt_str = 'November 21 , 2024'
# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)

# dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))
# print(dt_mtn.strftime('%B %d , %Y'))

# dt_str = 'November 21 , 2024'
# dt = datetime.datetime.strptime(dt_str , '%B %d , %Y')
# print(dt)

# import pytz
# import datetime


# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_mtn = datetime.datetime.now()
# de_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)



# dt =datetime.datetime(2024, 11, 22, 12, 25, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# import datetime
# import pytz

# dt = datetime

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)



# dt = datetime.datetime(2024,11,22,12,34,45,100000)
# tdel = datetime.timedelta(hours=12)
# print(dt + tdel)

# print(t.date())
# print(t.time())
# print(t.year)
# t = datetime.time(9, 30, 45, 100000)
# print(t.hour)


# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=10)
# print(tday + tdelta)
# print(tday - tdelta)

# bday = datetime.date(2025,10,19)
# till_bday = bday - tday
# print(till_bday.total_seconds())



# Monday = 0 Sunday = 6 (weekday)
# Monday = 1 Sunday = 7 (isoweekday)
# import datetime

# tday = datetime.date.today()

# tdelta = datetime.timedelta(days=7)

# print(tday - tdelta)

# print(tday)
# print(tday.weekday())
# print(tday.isoweekday())


# import datetime

# pYear = datetime.date.today()
# print(pYear.year)
# print(pYear.day)
# print(pYear.weekday())
# print(pYear.isoweekday())


# tday = datetime.date.today()
# print(tday)

# d= datetime.date(2015,7,12)
# print(d)