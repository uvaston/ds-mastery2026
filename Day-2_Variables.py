"""
DS Mastery 2026 - Day 2
Variables + Data Types + Comments
Complete working examples from chapter
"""

# ========================================
# VARIABLES - Python's Memory Boxes
# ========================================

# Basic variables (your Raj example)
Money = 5.2
Age = 28
Name = "Raj" 
Chocolate = "Dairy Milk"

print("Basic Variables:")
print(Money)
print(Age)
print(Name)
print(Chocolate)
print()  # Empty line

# Pro tip: Multiple print
print(Name, "has", Money, "Rs for", Chocolate)
print()

# Snake_case naming convention
money_raj = 5.2
chocolate_name = "Dairy Milk"
student_age = 20
print("Snake Case Examples:")
print("money_raj =", money_raj)
print("student_age =", student_age)
print()

# ========================================
# DATA TYPES - What Python sees
# ========================================

print("Data Types Demo:")
# Numbers (no quotes)
age = 28                    # int
pocket_money = 5.2         # float
print("age type:", type(age))
print("money type:", type(pocket_money))

# Text (quotes)
name = "Raj"               # str
print("name type:", type(name))
print()

# Complete types showcase
is_student = True          # bool
z = 3 + 4j                 # complex
scores = [85, 92, 78]      # list
marks = (10, 20, 30)       # tuple
student = {"name": "Raj"}  # dict
unique_ids = {101, 102}    # set

print("All Types:")
print("bool:", type(is_student))
print("complex:", type(z))
print("list:", type(scores))
print("tuple:", type(marks))
print("dict:", type(student))
print("set:", type(unique_ids))
print()

# ========================================
# COMMENTS - Explain WHY (not what)
# ========================================

"""
Multi-line comment example:
Step 1: Raj's initial pocket money
Step 2: Extra earnings from chores
Step 3: Total available for chocolate
"""

# Raj's pocket money (Dairy Milk costs 5 Rs)
pocket_money = 5.2  

# Extra money earned helping neighbor
extra_money = 10.0

# Total money - now can buy bigger chocolate!
total = pocket_money + extra_money  # 15.2 total
print("Comments Example:")
print("Total money:", total)  # Output: 15.2

print("\n" + "="*50)
print("DS Mastery 2026 - Day 2 Complete!")
print("Tomorrow: Operators + Input")
print("GitHub: github.com/yourusername/ds-mastery2026")
