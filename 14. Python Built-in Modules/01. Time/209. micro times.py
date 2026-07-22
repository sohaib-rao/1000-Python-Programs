import time

def pomodoro_timer(minutes):
    print(f"Focus timer started for {minutes} minute(s)...")
    seconds = minutes * 60
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f" {mins:02d}:{secs:02d}"
        print(time_format, end='\r')
        time.sleep(1)
        seconds -= 1
        
    print("\nTime is up! Take a break. \a")

pomodoro_timer(1)