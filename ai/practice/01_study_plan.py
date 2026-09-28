# Study plan calculator: how long will this course take me?
hours_per_week = 10
total_hours = 180
total_minutes = hours_per_week * 60

weeks = total_hours / hours_per_week
print("Weeks to finish:", weeks)
print("Whole months:", weeks // 4)
print("Minutes per week:", total_minutes)
print("Leftover weeks:", weeks % 4)
