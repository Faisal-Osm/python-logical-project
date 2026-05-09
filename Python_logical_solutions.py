# ============================================================
# Q1 - Student Management System using OOPs
# ============================================================

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        if self.marks >= 40:
            return "Pass"
        else:
            return "Fail"

student1 = Student("Rahul", 75)
print(f"Student: {student1.name}")
print(f"Marks: {student1.marks}")
print(f"Result: {student1.is_pass()}")


# ============================================================
# Q2 - Banking App: Total Balance from Deposits
# ============================================================

def total_balance(deposits):
    total = 0
    for amount in deposits:
        total += amount
    return total

deposits = [1000, 2500, 3000]
print(f"\nDeposits: {deposits}")
print(f"Total Balance: ₹{total_balance(deposits)}")


# ============================================================
# Q3 - Calculator: Square of a Number
# ============================================================

def calculate_square(num):
    result = num ** 2
    print(f"\nSquare of {num} = {result}")
    return result

calculate_square(7)


# ============================================================
# Q4 - Online Exam: Print Passing Marks (>= 40)
# ============================================================

marks = [35, 78, 90, 45, 22, 60]
print("\nPassing marks from the list:")
for mark in marks:
    if mark >= 40:
        print(mark)


# ============================================================
# Q5 - Fitness App: Print Even Numbers up to n
# ============================================================

n = 20  # You can change this value
print(f"\nEven numbers from 1 to {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")
print()


# ============================================================
# Q6 - Company Bonus Eligibility
# ============================================================

salary = int(input("\nEnter employee salary: ₹"))
if salary > 30000:
    print("Bonus Eligible ✅")
else:
    print("Not Eligible ❌")