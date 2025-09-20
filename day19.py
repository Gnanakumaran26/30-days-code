import datetime
import time

print("⏰ Alarm Clock - Day 19")

# Ask user for alarm time
alarm_time = input("Enter alarm time (HH:MM in 24hr format): ")

print(f"✅ Alarm set for {alarm_time} ...")

while True:
    # Current time
    now = datetime.datetime.now().strftime("%H:%M")
    
    if now == alarm_time:
        print("\n🔔 Wake up! Alarm ringing! 🔔")
        break
    
    time.sleep(30)  # check every 30 seconds
