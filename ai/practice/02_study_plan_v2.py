name = input("Your name: ").strip().title()
target_role = input("Your target role: ").strip().upper()
hours_per_week = float(input("Hours per week: "))
total_hours = 180

weeks = total_hours / hours_per_week
minutes_per_week = hours_per_week * 60

print("=" * 30)
print(f"Study plan for {name}")
print(f"Target role: {target_role}")
print(f"Minutes per week: {minutes_per_week:.0f}")
print(f"Weeks to finish:  {weeks:.1f}")
print(f"Whole months:     {weeks // 4:.0f}")
print(f"Leftover weeks:   {weeks % 4:.0f}")
print("=" * 30)
