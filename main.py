import datetime
from playsound import playsound
import schedule
import time

try:
    def action():
        return playsound("wakeup-alarm-tone-21497.mp3")


    now_min = datetime.datetime.now().minute
    now_hr = datetime.datetime.now().hour
    print(now_hr, ":", now_min)

    in_hr = input("Input hour(24hr clock): ")
    in_min = input("Input min: ")
    in_time = in_hr + ":" + in_min

    print("Alarm will set for {} : {}".format(in_hr, in_min))
    schedule.every().day.at(in_time).do(action)

    while True:
        schedule.run_pending()
        time.sleep(1)

except KeyboardInterrupt:
    print("Alarm was stopped")