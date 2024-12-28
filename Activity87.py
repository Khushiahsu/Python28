#Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.
class bird:
    def __init__(self):
        print('The bird is ready!')
    def word(self):
        print('The birds are nice')
    def supe(self):
        print('The birds are yellow')
class penguin(bird):
    def __init__(self):
        super().__init__()
        print('Now the penguin is ready!')
    def word(self):
        print('The penguins are nice!')
    def supe(self):
        print('The penguins are yellow')
    def run(self):
        print("RUNNNNNN!!!!")
obj3 = penguin()
obj3.word()
obj3.supe()
obj3.run()
        
        