class Employee:

    count = 0
    def __init__(self, name, branch, salary):
        self.name = name
        self.branch = branch
        self.salary = salary
        Employee.count+=1

    def display(self):
        print("Employee count %d " %Employee.count)

    def empDetails(self):
        print("name : ", self.name , "\nbranch : ", self.branch, "\nsalary : ", self.salary)


e1 = Employee("Naveen", "Cse", 123455)
e1.display()
e1.empDetails()
