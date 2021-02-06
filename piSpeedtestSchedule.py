import speedtest
from datetime import datetime
import pandas as pd
import schedule
import time

s = speedtest.Speedtest()

megabit = 1000000

speedColumns = ['Time','Month','Weekday','Day','Year','Hour','Download','Upload']
df = pd.DataFrame(columns=speedColumns)

def getSpeeds():
    speedDict = {}

    today = datetime.today()
    date = today.strftime("%m/%d/%y")
    dayOfWeek = today.strftime('%A')
    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    currentMonth = now.strftime('%B')
    dayOfMonth = datetime.today().day
    currentYear = now.year
    currentHour = now.hour

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
    speedDict['Day'] = dayOfMonth 
    speedDict['Year'] = currentYear
    speedDict['Hour'] = currentHour
    speedDict['Download'] = downloadMbps
    speedDict['Upload'] = uploadMbps

    global df
    df = df.append(speedDict,ignore_index=True)

    df.to_csv('Test file.csv')
    print('Speeds gathered, dataframe updated, saved to csv.')

schedule.every().minute.at(":15").do(getSpeeds)

while True:
    schedule.run_pending()
    time.sleep(1)