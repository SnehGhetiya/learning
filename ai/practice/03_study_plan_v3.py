name = input("Your name: ").strip().title()
target_role = input("Target role: ").strip()
hours_per_week = float(input("Hours per week: "))
total_hours = 180

if not name:
    name = "Friend"

if hours_per_week <= 0:
    print("Hours must be more than 0")
elif hours_per_week > 80:
    print("It is very hard to study more than 80 hours per week")
else:
    weeks = total_hours / hours_per_week
    
    print("=" * 36)
    print(f"Study plan for {name} as {target_role}")
    print(f"Weeks to finish: {weeks:.1f}")

    if weeks > 52:
        print("Pace: over a year. Can you find more time?")
    elif weeks > 26:
        print("Pace: steady, six months to a year.")
    else:
        print("Pace: fast track, under six months!")

    if hours_per_week > 40:
        print("Warning: over 40 hours a week. Plan some rest too.")

    # BUG EXPLANATION: 
    # The original condition `if "ai" in target_role.lower():` triggers for "Maintenance Manager" 
    # because the substring "ai" is present inside the word "mAIntenance". 
    # It blindly matches the letters anywhere in the string, leading to a false positive.
    if " ai " in target_role.lower() or target_role.lower().startswith("ai ") or target_role.lower() == "ai":
        print("AI role: Modules 3 and 4 will matter most.")

    print("=" * 36)