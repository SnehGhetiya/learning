# Review fixes (2026-10-06). Your original code is kept in "# YOUR VERSION" comments
# above each fixed part, so you can compare. Fixes:
#   - every function now uses 4-space indentation (some used 2 or 3)
#   - ask_numebr -> ask_number, with a docstring
#   - ask_hours commented out (nothing calls it after ask_number)
#   - stray ";" removed in skills_below
#   - skills_below called twice (default limit=3 and limit=5), with the limit in each label
#   - count_words called on two postings

# YOUR VERSION (2-space indent):
# def print_line(char="-", width=40):
#   """Print a divider line. Both parameters have defaults."""
#   print(char * width)
def print_line(char="-", width=40):
    """Print a divider line. Both parameters have defaults."""
    print(char * width)

# YOUR VERSION (2-space indent):
# def ask_name():
#   """Ask for a name. Return "Friend" if it's left blank."""
#   name = input("Your name: ").strip().title()
#   if not name:
#     name = "Friend"
#   return name
def ask_name():
    """Ask for a name. Return "Friend" if it's left blank."""
    name = input("Your name: ").strip().title()
    if not name:
        name = "Friend"
    return name

# YOUR VERSION (no longer used, ask_number replaces it):
# def ask_hours():
#   """Keep asking until the answer is between 1 and 80, then return it."""
#   while True:
#     hours = float(input("Hours per week (1-80): "))
#     if 1 <= hours <= 80:
#       return hours
#     print("Please enter a number from 1 to 80.")

# YOUR VERSION (typo in the name, no docstring, 2-space indent):
# def ask_numebr(prompt, low, high):
#   while True:
#     value = float(input(prompt))
#     if low <= value <= high:
#       return value
#     print(f"Please enter a value from {low} to {high}")
def ask_number(prompt, low, high):
    """Keep asking until the answer is between low and high, then return it as a float."""
    while True:
        value = float(input(prompt))
        if low <= value <= high:
            return value
        print(f"Please enter a value from {low} to {high}")

# YOUR VERSION (3-space indent, called ask_numebr):
# def ask_skills():
#    """Return a dict of skill -> level."""
#    skills = {}
#    while True:
#      skill = input("Add a skill (blank to finish): ").strip().lower()
#      if not skill:
#        return skills
#      skills[skill] = int(ask_numebr("Level 1-5: ", 1, 5))
def ask_skills():
    """Return a dict of skill -> level."""
    skills = {}
    while True:
        skill = input("Add a skill (blank to finish): ").strip().lower()
        if not skill:
            return skills
        skills[skill] = int(ask_number("Level 1-5: ", 1, 5))

# YOUR VERSION (3-space indent):
# def summarise(modules):
#    """Return two values: the total hours and the largest hours."""
#    total = 0
#    top_hours = 0
#    for module in modules:
#      total += module["hours"]
#      if module["hours"] > top_hours:  # noqa: PLR1730
#        top_hours = module["hours"]
#    return total, top_hours
def summarise(modules):
    """Return two values: the total hours and the largest hours."""
    total = 0
    top_hours = 0
    for module in modules:
        total += module["hours"]
        if module["hours"] > top_hours:  # noqa: PLR1730
            top_hours = module["hours"]
    return total, top_hours

# YOUR VERSION (4 spaces, then 6 inside the loop):
# def modules_with_hours(modules, hours):
#     """Return a list of the names of every module with exactly this many hours."""
#     modules_with_top_hours = []
#     for module in modules:
#       if module["hours"] == hours:
#         modules_with_top_hours.append(module["name"])
#     return modules_with_top_hours
def modules_with_hours(modules, hours):
    """Return a list of the names of every module with exactly this many hours."""
    modules_with_top_hours = []
    for module in modules:
        if module["hours"] == hours:
            modules_with_top_hours.append(module["name"])
    return modules_with_top_hours

def is_ai_role(role):
    """Return True if the role contains an AI keyword as a whole word."""
    words = role.lower().replace("-", " ").replace("/", " ").split()
    return bool({"ai", "ml", "llm"} & set(words))

# YOUR VERSION (stray ";", no docstring, 2-space indent):
# def skills_below(skills, limit=3):
#   skills_below_limit = [];
#   for skill, level in skills.items():
#     if level < limit:
#       skills_below_limit.append(skill)
#   return skills_below_limit
def skills_below(skills, limit=3):
    """Return a list of the skill names whose level is below limit."""
    skills_below_limit = []
    for skill, level in skills.items():
        if level < limit:
            skills_below_limit.append(skill)
    return skills_below_limit

# YOUR VERSION (no docstring, 2-space indent):
# def count_words(text):
#   word_count = {}
#   for word in text.split():
#     word_count[word] = word_count.get(word, 0) + 1
#   return word_count
def count_words(text):
    """Return a dict of word -> how many times it appears in text."""
    word_count = {}
    for word in text.split():
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

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
ai_skills = {"python", "llm apis", "rag", "evals", "pytorch"}

name = ask_name()
target_role = input("Target role: ").strip()
# YOUR VERSION: hours_per_week = ask_numebr("Hours per week (1-80): ", 1, 80)
hours_per_week = ask_number("Hours per week (1-80): ", 1, 80)
my_skills = ask_skills()

total, top_hours = summarise(modules)  # unpack the returned tuple
weeks = total / hours_per_week

# YOUR VERSION (one posting only):
# posting = "python rag python evals rag python"
posting_1 = "python rag python evals rag python"
posting_2 = "pytorch python evals llm apis python"

print_line("=")
print(f"Study plan for {name} as {target_role}")
print(f"{len(modules)} modules, {total} hours, {weeks:.1f} weeks")
print_line()
for i in range(len(modules)):
    module = modules[i]
    status = progress.get(module["name"], "not started")
    print(f"{i + 1}. {module['name']} ({module['hours']} h): {status}")

longest = modules_with_hours(modules, top_hours)
print(f"Longest: {' and '.join(longest)} ({top_hours} h)")

if is_ai_role(target_role):
    have = set(my_skills)
    print_line()
    print("AI role: Modules 3 and 4 will matter most.")
    print(f"Skills you have: {', '.join(sorted(ai_skills & have))}")
    print(f"Skills to learn: {', '.join(sorted(ai_skills - have))}")

# YOUR VERSION (only limit=5, label doesn't say which limit, same-type nested quotes):
# print(f"Skills below limit: {", ".join(skills_below(my_skills, limit=5))}")
# print(count_words(posting))
print_line()
print(f"Skills below 3: {', '.join(skills_below(my_skills))}")
print(f"Skills below 5: {', '.join(skills_below(my_skills, limit=5))}")
print(f"Posting 1 words: {count_words(posting_1)}")
print(f"Posting 2 words: {count_words(posting_2)}")
print_line("=")
