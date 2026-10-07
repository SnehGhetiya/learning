name = input("Your name: ").strip().title()

if not name:
    name = "Friend"

target_role = input("Target role: ").strip()

while True:
    hours_per_week = float(input("Hours per week (1-80): "))
    if 1 <= hours_per_week <= 80:
        break
    print("Please enter a number from 1 to 80.")

my_skills = {}
while True:
    skill = input("Add a skill (blank to finish): ").strip().lower()
    if not skill:
        break
    level = int(input("Level 1-5: "))
    my_skills[skill] = level

modules = [
    {"name": "Python basics", "hours": 40},
    {"name": "Python for web and APIs", "hours": 25},
    {"name": "LLM fundamentals", "hours": 45},
    {"name": "LangChain and LangGraph", "hours": 25},
    {"name": "Classic ML", "hours": 30},
    {"name": "Neural networks", "hours": 35},
    {"name": "Fine-tuning", "hours": 25},
    {"name": "Capstone", "hours": 45},
]
progress = {"Python basics": "in progress"}

total_hours = 0
longest = ("", 0)  # a tuple: (name, hours) of the best so far

for module in modules:
    total_hours += module["hours"]
    if module["hours"] > longest[1]:
        longest = (module["name"], module["hours"])

weeks = total_hours / hours_per_week

print("=" * 40)
print(f"Study plan for {name} as {target_role}")
print(f"{len(modules)} modules, {total_hours} hours, {weeks:.1f} weeks")
print("-" * 40)

for i in range(len(modules)):
    module = modules[i]
    status = progress.get(module["name"], "not started")
    print(f"{i + 1}. {module['name']} ({module['hours']} h): {status}")

longest_name, longest_hours = longest
print(f"Longest module: {longest_name} ({longest_hours} h)")

# Second loop: now that we know the top hours, collect every module that has them.
tied = []
for module in modules:
    if module["hours"] == longest_hours:
        tied.append(module["name"])

if len(tied) > 1:
    print(f"Tied for longest: {' and '.join(tied)}")

words = target_role.lower().replace("-", " ").replace("/", " ").split()
ai_keywords = {"ai", "ml", "llm"}
if ai_keywords & set(words):
    ai_skills = {"python", "llm apis", "rag", "evals", "pytorch"}
    print("-" * 40)
    print("AI role: Modules 3 and 4 will matter most.")
    print(f"Skills you have: {', '.join(sorted(ai_skills & set(my_skills)))}")
    print(f"Skills to learn: {', '.join(sorted(ai_skills - set(my_skills)))}")

for skill, level in my_skills.items():
    if level < 3:
        print(f"Skill {skill}: to practise")
print("=" * 40)

posting = "python rag python evals rag python"
counts = {}

for word in posting.split():
    counts[word] = counts.get(word, 0) + 1

print(counts)
