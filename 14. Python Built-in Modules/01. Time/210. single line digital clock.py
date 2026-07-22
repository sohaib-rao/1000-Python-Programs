import time
from datetime import datetime

while True:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f" LIVE CLOCK: {current_time}", end="\r")
        time.sleep(1)