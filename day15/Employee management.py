# Employee Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"


# Dictionary to store employees
employees = {}


# Function to add employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")

    try:
        salary = float(input("Enter Salary: "))
    except ValueError:
        print("❌ Invalid salary! Please enter a number.")
        return

    emp = Employee(emp_id, name, salary)
    employees[emp_id] = emp
    print("✅ Employee added successfully!")


# Function to display employees
def display_employees():
    if not employees:
        print("No employees found.")
        return

    print("\n--- Employee List ---")
    for emp in employees.values():   # Loop used here
        print(emp.display())


# Function to save data to file
def save_to_file():
    with open("employees.txt", "w") as file:
        for emp in employees.values():
            file.write(emp.display() + "\n")

    print("💾 Data saved to file successfully!")


# Main Program Loop
while True:
    print("\n1. Add Employee")
    print("2. Display Employees")
    print("3. Save to File")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        save_to_file()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("❌ Invalid choice! Try again.")
