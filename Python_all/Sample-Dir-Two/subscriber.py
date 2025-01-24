import datetime
import math

goal_subs = 150000
current_subs = 85000
subs_to_go = goal_subs - current_subs


avs_subs_day = 200
days_to_go = math.ceil(subs_to_go / avs_subs_day)

today = datetime.date.today()

print(today + datetime.timedelta(days=days_to_go))
