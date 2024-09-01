class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def save_to_database(self):
        print(f"Saving {self.name} to database.")

    def print_report(self):
        print(f"Printing report for {self.name}, position: {self.position}")

# Menggunakan kelas Employee
employee = Employee("Fadli Shidqi F", "Developer")
employee.save_to_database()
employee.print_report()
