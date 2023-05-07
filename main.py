import time

# Get input from user
print("Please enter the number of seconds for the timer to count down:")
user_input = int(input())

# Count down from user_input
for i in range(user_input, 0, -1):
    print(i)
    time.sleep(1)

# Print "Time's Up!" when timer reaches 0
print("Time's Up!")

# Stopwatch

import time

# Get input from user
print("Press Enter to start the stopwatch")
input()

# Initialize start time
start_time = time.time()

# Get input from user
print("Press Enter to stop the stopwatch")
input()

# Calculate and print time elapsed
end_time = time.time()
elapsed_time = end_time - start_time
print("Time elapsed:", round(elapsed_time, 2), "seconds")

# World Time

# Get the current time in UTC
import datetime

utc_time = datetime.datetime.utcnow()

# Print the current UTC time
print("The current UTC time is:", utc_time)

# Alarm App

import time
import datetime

# Get input from user
print("Please enter the time you would like the alarm to go off (HH:MM:SS):")
alarm_time = input()

# Convert the alarm time to a datetime object
alarm_time_dt = datetime.datetime.strptime(alarm_time, '%H:%M:%S')

# Print alarm time
print("Alarm set for", alarm_time)

# Calculate time until alarm goes off
time_until_alarm = alarm_time_dt - datetime.datetime.now()
time_until_alarm_secs = time_until_alarm.total_seconds()

# Wait until alarm time
time.sleep(time_until_alarm_secs)

# Print alarm message
print("Alarm! Wake up!")