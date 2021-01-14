import speedtest
import schedule

s = speedtest.Speedtest()

megabit = 1000000

def GetInternetSpeed():
    print('Getting your speeds, hot rod.')
    download = s.download()
    upload = s.upload()
    downloadMbps = round(download/megabit,1)
    uploadMbps = round(upload/megabit,1)
    print('My download speed is:', downloadMbps)
    print('My upload speed is:', uploadMbps)

schedule.every(15).minutes.do(GetInternetSpeed)

while True:
    schedule.run_pending()
    time.sleep(1)