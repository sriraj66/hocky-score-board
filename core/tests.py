import time

import threading


def timer(seconds):
    while seconds >= 0:
        # Format the remaining time as "MM:SS"
        minutes = seconds // 60
        seconds_remaining = seconds % 60
        time_formatted = f"{minutes:02d}:{seconds_remaining:02d}"
        print(time_formatted, end="\r")  # Print on the same line
        time.sleep(1)  # Pause for 1 second
        seconds -= 1


input_seconds = int(input("Enter the number of seconds: "))
t1 = threading.Thread(target=timer,args=(input_seconds,))
t1.start()
print("Timer has finished!")
