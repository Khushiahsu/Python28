#Write a program to create a parent class Person (attributes - name, id number) with a method display to display the attributes. Next, create a child class Employee (attributes - name, id number, salary, post). Access the attributes of parent class in child class. Then, create an object for child class and call the display method to display the name and id number.
class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print('Name :',self.name)
        print('Id :',self.id)
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post

        person.__init__(self,name,id)
obj2 = employee('Aarav','9128','5000','Intern')
obj2.display()

        