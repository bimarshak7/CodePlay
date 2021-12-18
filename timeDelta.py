from datetime import datetime, timedelta

#Check if the string starts with "The" and ends with "Spain":
T1 = "Sun 10 May 2015 13:54:36 -0700"
T2 = "Sun 10 May 2015 13:54:36 -0000"
T3 = "Sat 02 May 2015 19:54:36 +0530"
T4 = "Fri 01 May 2015 13:54:36 -0000"

def time_delta(t1,t2):
  zone1 = t1.split(' ')[5]
  zone2 = t2.split(' ')[5]
  
  date1 = datetime.strptime(t1[:24],"%a %d %b %Y %H:%M:%S")
  date2 = datetime.strptime(t2[:24],"%a %d %b %Y %H:%M:%S")
  if zone1[0]=='+':
        date1-=timedelta(hours=int(t1[26:28]),minutes=int(t1[28:]))
  else:
        date1+=timedelta(hours=int(t1[26:28]),minutes=int(t1[28:]))

  if zone2[0]=='+':
        date2-=timedelta(hours=int(t2[26:28]),minutes=int(t2[28:]))
  else:
        date2+=timedelta(hours=int(t2[26:28]),minutes=int(t2[28:]))

  return str(int(abs((date1-date2).total_seconds())))


print(time_delta(T1,T2))
