

start_hour = int(input("Starting time (hours): "))
start_minute = int(input("Starting time (minutes): "))
duration_minutes = int(input("Event duration (minutes): "))

# Calculate the total minutes from the start time and the duration
total_minutes = start_minute + duration_minutes

# Calculate the new hours and minutes
end_hour = (start_hour + (total_minutes // 60)) % 24
end_minute = total_minutes % 60

# Print the end time in the desired format
print(f"The event will end at {end_hour}:{end_minute}")
