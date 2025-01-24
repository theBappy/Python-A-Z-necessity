# import datetime

# x = datetime.datetime(2025, 1, 5)
# print(x.strftime("%V"))

# x = datetime.datetime( 2025, 1, 5)
# print(x)

# x = datetime.datetime.now()

# print(x.year)
# # print(x.weekday)
# print(x.strftime("%A"))


# x = datetime.datetime.now()
# print(x)



# import datetime
# import pytz

# dt_mtn = datetime.datetime.now(tz=pytz.timezone('US/Mountain'))

# print(dt_mtn.strftime('%B %d, %Y'))

# dt_str = 'January 05, 2025'
# dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
# print(dt)

# Strftime (converts a datetime to string)
# Strpfime (convert a string to datetime)



# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# # print(dt_utcnow)

# dt_mtn = datetime.datetime.now()
# mtn_tz = pytz.timezone('US/Mountain')
# dt_mtn = mtn_tz.localize(dt_mtn)
# print(dt_mtn)

# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)


# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

# for tz in pytz.all_timezones:
#     print(tz)


# dt = datetime.datetime(2025, 1, 5, 6, 6, 45, tzinfo=pytz.UTC)
# print(dt)


# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()



# print(dt_today)
# print(dt_now)
# print(dt_utcnow)


# t = datetime.datetime(2016,7,12,12,30,45,100000)

# tdelta = datetime.timedelta(hours=12)

# print(t + tdelta)

# print(t)
# print(t.date())
# print(t.time())
# print(t.year)
# print(t.hour)
# print(t.month)

# t = datetime.time(9, 30 , 45, 100000)
# print(t)
# print(t.hour)
# print(t.minute)
# print(t.second)
# print(t.microsecond)

# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)


# print(tday - tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

# bday = datetime.date(2025,10,19)
# till_bday = bday - tday
# print(till_bday.days)
# print(till_bday.total_seconds())

# tdelta = datetime.timedelta(days=15)
# print(tday + tdelta)

# tdelta = datetime.timedelta(days=7)

# print(tday + tdelta)



# tday = datetime.date.today()
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(tday.weekday())  # Monday = 0, Sunday = 6
# print(tday.isoweekday()) # Monday = 1, Sunday = 7


# tday = datetime.date.today()
# print(tday)
# tday = datetime.date.today()
# print(tday)

# tday = datetime.date.today()
# print(tday)

# tday = datetime.date.today()
# print(tday)

# tday = datetime.date.today()
# print(tday)
# d = datetime.date(2025, 5, 1)
# print(d)

# d = datetime.date(2025,1,5)
# print(d)

# d = datetime.date(2016, 7, 12)
# print(d)

