from datetime import datetime
import pytz
tz_SG = pytz.timezone('Asia/Singapore') 
now = datetime.now(tz_SG)

print(now.hour)

print(type(now.hour))


print(now.weekday())


print(now)