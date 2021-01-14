import speedtest
import schedule

s = speedtest.Speedtest()

megabit = 1000000

defGetInternetSpeed():
    print('Getting your speeds, hot rod.')
    download = s.download()
    upload = s.upload()
    downloadMbps = download/megabit
    uploadMbps = upload/megabit
    print('My download speed is:', downloadMbps)
    print('My upload speed is:', uploadMbps)

schedule.every(15).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)