'''
Problem Of The Day - 3/19/2025

Part 1: Creating an Employee and Manager classes

Employee Class:
- Attributes:
--- name
--- salary
- Methods:
--- get_salary(): Returns salary.

Manager Class:
- Inherits from Employee
- Has an additional attribute bonus (float)
- Overrides get_salary() to return salary + bonus.

Part 2: Modify the Employee and Manager classes to include performance reviews.

Employee Class Adds:
- add_review(review): Adds a performance review to the list.
- print_reviews(): Prints all reviews.

Manager Class Adds:
- Can review other employees using review_employee(employee, review).

'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self._performance_reviews = []  

    def get_salary(self):
        return self.salary

    def add_review(self, review):
        self._performance_reviews.append(review)

    def print_reviews(self):
        print(f"Performance reviews for {self.name}:")
        for review in self._performance_reviews:
            print(f"- {review}")


class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

    def review_employee(self, employee, review):
        if isinstance(employee, Employee):
            employee.add_review(review)
        else:
            print("Error: Can only review Employee objects")


# Example Usage:
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
mgr = Manager("Charlie", 80000, 10000)

# Employee interactions
emp1.add_review("Great teamwork")
emp1.add_review("Needs to work on deadlines")

# Manager interactions
mgr.review_employee(emp1, "Shows strong leadership skills")
mgr.review_employee(emp2, "Excellent problem solver")

# Printing reviews
emp1.print_reviews()
emp2.print_reviews()

# Checking salaries
print(f"{emp1.name}'s Salary: ${emp1.get_salary()}")
print(f"{mgr.name}'s Salary with bonus: ${mgr.get_salary()}")
