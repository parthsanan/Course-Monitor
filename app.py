import schedule
import time 
from main import Course_Monitor

schedule.every(30).minutes.do(Course_Monitor)

while 1:
    schedule.run_pending()
    time.sleep(1)
