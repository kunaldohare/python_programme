#Python is unstructured programming
#Python can be made as structured programming if it follows class principle
#class is collection of objects
#object is real world entity
#class is kind of template or wrapper to hold things
#object is anything which takes memory.
#class is mainly to give the property of inheritance or exter

##var = "saad"
##print(var)
##
##def fun():
##    print("welcome")
##
##fun()

#But from line no 9 to 15 this is unstructured way of defininf data we cannot use it into another python program for that we have to use the concept of class.
#class helps in saving  unwanted memory consumption

# here in defining class we can see both the function and variable are sitting in side the class.

##class My_class:
##
##    var = "Saad"
##
##    def fun():
##        print("welcome")  #Here we are defining data into structured way which means lesser memory consumption and more effective.
    
##print(My_class.var)
##My_class.fun()

##class My_class:
##
##    var = "Saad"
##    var1 = "david"
##
##    def fun():
##       print("welcome")

#My is called object refrence of the "My_Class"
# This the shortest way of using class.

##My = My_class
##print(My.var)
##My.fun()
#here from line no 32 to 42 this is class without constructor

##class My_class:
##    def new(name):
##        print("hello")
##
##    def fun(name,age):
##        print("welcome")
##        
##My = My_class
##My.fun("saad",23)
##My.new("saad")
            
        

##class My_Class:
##    
##    def __init__(self,name,age):
##        
##        self.name = name
##        self.age = age
##        
##    def new(self):
##          print(self.name)
##      
##
##    def fun(self):
##         print(self.name,self.age)
        
                
##my = My_Class('saad',23)
#My_class is called as constructor class
#My is called object reference with single instant memory(single 
#My_class() will have one hidden object inside
#Whenever you create constructor,an attribute called _init_ is created automatically
#We can use that _init_ if we need to initialize the data inside the class.
#attribute or magic method or dunder method is anythin that contain double underscore on either side.
#self is similar to My
#My is the object reference for external class
#self is the object reference for internal class
##my.new()
##my.fun()


##class My_Class:
##
##        def __init__(self,name,age,country):
##
##            self.name = name
##            self.age  = age
##            self.country = country
##
##        def new(self):
##             print("hello")
##             print(self.name)
##
##        def fun(self):
##
##             print("welcome")
##             print(self.name,self.age,self.country)
##             
##my = My_Class("saad",23,"India")
##my.new()
##my.fun()


##class My_class:
##
##    def __init__(self):
##        print("hello saad")
##
##    def fun(self):
##        print("dhoni")
##
##    def fun(self):
##        print("welcome to python")
##
##my = My_class()   
##my.fun()

 #Here we can see that overiding takes place and it will print the last fun.

##class My_class:
##
##    def __init__(self):
##        print("hello saad")
##
##    def fun(self):
##        print("dhoni")
##
##    def fun(self):
##        print("welcome to python")
##
##my = My_class()   
##my.fun()

#Access specifier - It can be Public ,Private or Protected but in python we dont have protected.
#Till now what we are seeing is public access specifier as the function sitting inside the class is easily accessible from outside

##class My_class:
##
##    def __init__(self):
##        print("hello saad")
##
##    def fun(self):
##        print("dhoni")
##
##    def __new(self):
##        print("welcome to python")
##        
##
##my = My_class()   
##my.fun()
#Here if we put double underscore before new function on the left hand side that function becomes private access specifier or data hiding takes place.
'''Example of Inheritance'''
  
##class My_class:
##
##    def __init__(self,name,age):
##
##        self.name = name
##        self.age  = age
##        
##    def one(self):
##        print("one",self.name)
##
##class Second_class(My_class): #This is the syntax of single inheritance that is inside my Second class we are inheriting our parent class.
##
##    def two(self):
##        print("two",self.name,self.age)
##
##my = Second_class("dhoni",33)
###In line no 175 we are not creating constructor for parent class because then we cannot call the funcion inside the child.So alwys we will create from lower one that is for child
##my.one()
##my.two()
    
'''Here we have same function name in both the parent and child class'''        
class My_class:

    def __init__(self,name,age):

        self.name = name
        self.age  = age
       
    def two(self):
        print("one",self.name)

class Second_class(My_class):
    
    def two(self):
        
        print("two",self.name,self.age)

my = Second_class("dhoni",33)
my.two()
#Here we can see that when running from line no 182 to 199 the fun which is inside the child class is executing not the fun which is in the parent class.
#It is because due to the property of inheritance that is whatever the constructor you have created the function which is inside that get the preference first executes,
# so if we need to call the function inside the parent we need to create object reference for the parent class.
my_parent = My_class("dhoni",34)
my_parent.two()
#This is called polymerpism means that if we want to call a function of a specfic class we need to create constructor of that particular class.

##class A:
##    
##    def fun(self):
##        print("a")
##
##class B(A):
##    def fun(self):
##        print("b")
##       
##class C(A):
##    def fun(self):
##        print("c")
##        
##class D(C,B):
##    def fun(self):
##        print("d")
##        
##d = D()
##d.fun()
##d_parent = C()
##d.fun()
#Here principle of inheritance works.

##class A:
##    
##    def fun(self):
##        print("a")
##
##class B(A):
##    def fun(self):
##        print("b")
##       
##class C(A):
##    def fun(self):
##        print("c")
##        
##class D(C,B):
##    pass
##    def fun(self):
##       print("d")
##        
##d = D()
##d.fun()
 #Here if we run from line no 230 to line no 249 we get c as output because it works on aalgorithm called
 #Method Resolution Orde
 # This will do nearby search in version latest version of python
 #But in older version that is 2 and all it will do deep search.


##class My_class:
##    def __init__(self,name,country):
##         self.name = name
##         self.country = country
##         
##    def new(self):
##        print("one")
##
##class Second_class(My_class):
##
##    def fun(self):
##        print("two",self.name)
##
##class Third_class(My_class):
##
##    def fun(self):
##        print("third",self.name,self.country)
##
##my = Third_class("saad","India")
##my.new()
##my.fun()
##
##my_parent = Second_class("saad","India")


    
    
    
    





        
        
 






























