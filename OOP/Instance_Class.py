class Foo:
    @classmethod    #This is class method decorator and uses class as argument
    def hi(cls):
        print(cls.__name__)

my_object=Foo()
my_object.hi()

class Bar:
    @staticmethod   #This is static method decorator and does not take any arguments
    def hi():
        print("I don't have any arguments")
    
object2=Bar()
object2.hi()