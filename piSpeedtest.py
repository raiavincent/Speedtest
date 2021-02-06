import speedtest
from datetime import datetime
import pandas as pd

s = speedtest.Speedtest()

megabit = 1000000

speedDict = {}

today = datetime.today()
date = today.strftime("%m/%d/%y")
dayOfWeek = today.strftime('%A')
print(dayOfWeek)
now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
print(currentTime)
print(date)
# currentMonth = datetime.now().month
currentMonth = now.strftime('%B')
print(currentMonth)
dayOfMonth = datetime.today().day
print(dayOfMonth)
currentYear = now.year
print(currentYear)
currentHour = now.hour
print(currentHour)


print('Getting your speeds, hot rod.')
download = s.download()
upload = s.upload()
downloadMbps = round(download/megabit,1)
uploadMbps = round(upload/megabit,1)
print('My download speed is:', downloadMbps,'Mbps.')
print('My upload speed is:', uploadMbps,'Mbps.')

speedDict['Time'] = currentTime
speedDict['Month'] = currentMonth
speedDict['Weekday'] = dayOfWeek
speedDict['Day'] = dayOfMonth # possibly find a better key for this
speedDict['Year'] = currentYear
speedDict['Hour'] = currentHour
speedDict['Download'] = downloadMbps
speedDict['Upload'] = uploadMbps
print(speedDict) 

speedColumns = ['Time','Month','Weekday','Day','Year','Hour','Download','Upload']
df = pd.DataFrame(columns=speedColumns)
df = df.append(speedDict,ignore_index=True)
print(df)