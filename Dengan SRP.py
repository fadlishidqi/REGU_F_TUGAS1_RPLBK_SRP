class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class EmployeeDatabase:
    def save_to_database(self, employee):
        print(f"Saving {employee.name} to database.")

class EmployeeReport:
    def print_report(self, employee):
        print(f"Printing report for {employee.name}, position: {employee.position}")

# Menggunakan kelas-kelas terpisah
employee = Employee("Fadli Shidqi F", "Developer")
db = EmployeeDatabase()
report = EmployeeReport()

db.save_to_database(employee)
report.print_report(employee)
