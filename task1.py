# Step 1: Create a dictionary of employees
employees = {
    'Alice': 30000,
    'Bob': 25000,
    'Charlie': 40000,
    'David': 20000,
    'Eve': 35000
}

# Step 2: Compute the total salary of employees
total_salary = sum(employees.values())
print(f"Total salary of employees: {total_salary}")

# Step 3: Find the minimum and maximum salaries
min_salary = min(employees.values())
max_salary = max(employees.values())
print(f"Minimum salary: {min_salary}")
print(f"Maximum salary: {max_salary}")

# Step 4: Find the employee who is drawing the highest salary
highest_salary_employee = max(employees, key=employees.get)
print(f"Employee with the highest salary: {highest_salary_employee} ({employees[highest_salary_employee]})")

# Step 5: List employee names whose salary is greater than a dynamic input
threshold = int(input("Enter the salary threshold: "))
filtered_employees = [name for name, salary in employees.items() if salary > threshold]
print(f"Employees with salary greater than {threshold}: {', '.join(filtered_employees)}")
print("Hi this is devops lab")
print("This is my second trail")