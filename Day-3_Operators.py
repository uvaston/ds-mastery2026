"""
DS Mastery 2026 - Day 3: Operators + Input()
GitHub: github.com/uvaston/ds-mastery2026
"""

print("=== ARITHMETIC OPERATORS ===")
pocket = 50.0
earned = 30.0
total = pocket + earned
taxed = total * 1.18
print(f"Pocket + Earned: ₹{total}")
print(f"After 18% tax: ₹{taxed:.2f}")
print()

print("=== ASSIGNMENT SHORTCUTS ===")
a = 10
a += 5      # a = a + 5
a *= 2      # a = a * 2
print(f"a after shortcuts: {a}")  # 30
print()

print("=== RELATIONAL ===")
salary = 55000
threshold = 50000
print(f"High salary? {salary > threshold}")  # True
print()

print("=== IDENTITY (Your Twins Example!) ===")
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(f"x == y: {x == y}")      # True (same values)
print(f"x is y: {x is y}")      # False (different objects)
print(f"x is z: {x is z}")      # True (same object!)
print(f"IDs: id(x)={id(x)}, id(z)={id(z)}")
print()

print("=== MEMBERSHIP ===")
skills = ["Python", "Pandas", "SQL"]
print("'Python' in skills:", "Python" in skills)  # True
print("5 in [1,2,3]:", 5 in [1,2,3])            # False
print()

print("=== LOGICAL OPERATORS ===")
a, b, c = 5, 6, 5
print("AND:", (a==b) and (a==c))  # False
print("OR: ", (a==b) or (a==c))   # True
print("NOT:", not(a==b))          # True
print()

print("=== DYNAMIC INPUT CALCULATOR ===")
pocket_input = float(input("Enter pocket money ₹"))
earned_input = float(input("Enter earned today ₹"))
total_dynamic = (pocket_input + earned_input) * 1.18
print(f"Total after tax: ₹{total_dynamic:.2f}")
print()

print("=== EXPRESSION (BODMAS) ===")
result = (10 + 5) * 2 / 3
print(f"(10+5)*2/3 = {result}")  # 10.0
print()

print("\n🎉 DS Mastery 2026 - Day 3 COMPLETE!")
print("Tomorrow: Day 4 Lists")
print("GitHub: github.com/uvaston/ds-mastery2026")
