from datetime import datetime, timedelta
a = '10:00'

print(type(a))

dat = timedelta(hours=int(a.split(':')[0]),minutes=int(a.split(':')[1]))

convt = dat.total_seconds() + 10 
print(convt)

