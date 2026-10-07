name = input("Your name: ").strip().title()
if not name:
    name = "Friend"
target_role = input("Your target role: ").strip()

while True:
    hours_per_week = float(input("Hours per week (1-80): "))
    if 1 <= hours_per_week <= 80:
        break
    print("Please enter a number from 1 to 80.")

my_skills = []

while True:
    skill = input("Add a skill (blank to finish): ").strip()
    if not skill:
        break
    my_skills.append(skill)

modules = ["Python basics", "Python for web and APIs", "LLM fundamentals",
           "LangChain and LangGraph", "Classic ML", "Neural networks",
           "Fine-tuning", "Capstone"]
module_hours = [40, 25, 45, 25, 30, 35, 25, 45]

total_hours = 0
for hours in module_hours:
    total_hours += hours
weeks = total_hours / hours_per_week

print("=" * 40)
print(f"Study plan for {name} as {target_role}")
print(f"{len(modules)} modules, {total_hours} hours, {weeks:.1f} weeks")
if my_skills:
    print(f"My skills: {', '.join(my_skills)}")
print("-" * 40)

for i in range(len(modules)):
    print(f"{i + 1}. {modules[i]} ({module_hours[i]} h)")

words = target_role.lower().replace("-", " ").replace("/", " ").split()
ai_keywords = ["ai", "ml", "llm"]

is_ai_role = False
for keyword in ai_keywords:
    if keyword in words:
        is_ai_role = True
        break

if is_ai_role:
    print("-" * 40)
    print("AI role: Modules 3 and 4 will matter most.")

# Find the longest module without max(): keep the "best so far".
longest_hours = 0
longest_name = ""
for i in range(len(module_hours)):
    if module_hours[i] > longest_hours:
        longest_hours = module_hours[i]
        longest_name = modules[i]

print("-" * 40)
print(f"Longest module: {longest_name} ({longest_hours} h)")
print("=" * 40)
