start_hour = int(input("Starting time (hours): "))
start_minute = int(input("Starting time (minutes): "))
duration_minutes = int(input("Event duration (minutes): "))
start_minute += duration_minutes
start_hour += start_minute // 60
start_minute %= 60
start_hour %= 24

print(start_hour, ":", start_minute, sep="")
