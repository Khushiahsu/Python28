#Write a Python program to implement Inheritance by creating a Parent Class Vehicle with a constructor that has details like name, maximum speed, and mileage. Then, create a Child Class Bus that inherits Class Vehicle. Finally, showcase Inheritance to display the details of the Vehicle Bus named - School Volvo.
class vehicle:
    def __init__(self,name,speed,mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage
class bus(vehicle):
    pass
obj1 = bus('School Volvo','45mph','1l')
print('Name :',obj1.name)
print('Speed :',obj1.speed)
print('Mileage :',obj1.mileage)
