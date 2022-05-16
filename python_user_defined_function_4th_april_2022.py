##print("Hello")
##print("Welcome to my programming")

##def My_Fun(): # Function definition without argument or paramter or signature
##    print("Hello")
##    print("Welcome to my programming")
    
##My_Fun() # Calling Function     
  
##def My_Fun(name):   # Function definition with argument or paramter or signature
##    print("Hello",name)
##    print("Welcome to my programming")
    
##My_Fun("rahul")  #Calling Function
##My_Fun("kohli")
##My_Fun(4) # It can take any data type because it is just a variable

#To restrict data types :

##def My_Fun(name):# Function definition with argument or paramter or signature
##    if isinstance(name,str):
##        print("Hello",name)
##        print("Welcome to my programming")

##My_Fun(7) #Here we can see when calling function it is not printing because we have restricted the data type to str

##def My_Fun(name,country):# Function definition with more than one argument or paramter or signature
##    if isinstance(name,str):
##        print("Hello",name, "from",country)
##        print("Welcome to my programming")

##My_Fun("dhoni") # when we call function here in line no 32 we will get type error because My_Fun() missing 1 required positional argument: 'country'
##My_Fun("dhoni","India")
##My_Fun("dhoni",4) #Here when calling function it will not give error because here for country we have not resticted data typ

#To restrict data type of both the given argument
    #Method 1 
##def My_Fun(name,country):
##    if isinstance(name,str) and isinstance(country,str):
##        print("Hello",name, "from",country)
##        print("Welcome to my programming")

##My_Fun("David Warner","Australia") # Here we see when calling function we have given both the arguments as strings.

# method 2
##def My_Fun(name,country):
##    if isinstance(name,str):
##        if isinstance(country,int):
##            print("Hello",name, "from",country)
##            print("Welcome to my programming")
##
##My_Fun("saad",4)
            
       
##def My_Fun(name,country):  #Function definition with  keyword argument or paramter or signature
##    if isinstance(name,str):
##        if isinstance(country,int):
##            print("Hello",name, "from",country)
##            print("Welcome to my programming")

##My_Fun(name = "saad", country = 4)


##def My_Fun(name,country = ""):  #Function definition with  default argument or paramter or signature
##    if isinstance(name,str):
##        if isinstance(country,str):
##            print("Hello",name, "from",country)
##            print("Welcome to my programming")


##My_Fun("kohli") # Here in calling fucntion even if we are not providing the country argument it is taking the default value of the argument.
##My_Fun("Ricky","India") # Here in calling function it is not taking the default argument because we are providing the argument.

# Default Argument means  that you gonna keep as a part of function definition
# Keyword argument means keyword you gonna supply to the function definition through function calling


##def My_Fun(name = "Ricky",country = None):    #Function definition with  default argument or paramter or signature
##        print("Hello",name, "from",country)
##        print("Welcome to my programming")
        
#Calling Function
##My_Fun()
##My_Fun("kohli")
##My_Fun("warner","australia")

##def My_Fun(name = "Ricky",country):    #Function definition with  default argument or paramter or signature
##        print("Hello",name, "from",country)
##        print("Welcome to my programming")

#Calling Function
##My_Fun()    # Here it will throw error because default is before non default.     


##def Student_Passes(*names):
##
##    print(names)
##
##Student_Passes("kohli")
##Student_Passes("kohli","Warner")

# *args means it can take any no of arguments
# Output will be in the form of tupple.

##def Student_Passes(**names):
##
##    print(names)
##
##Student_Passes()
##Student_Passes(captain = "dhoni")
##Student_Passes(name = "kohli" ,age = "Warner")

# **args means data with keys
# output will be in the form of dictionary

##def Student_Marks(eng,maths,student_name):
##    total = eng+maths
##    return

##Student_Marks(90,80,"dhoni") #Here in line no 120 when we call function it will give nothing  because when we have return statement we have to use print
##print(Student_Marks(90,80,"dhoni"))


##def Student_Marks(eng,maths,student_name):
##    total = eng+maths
##    return
##
##output = Student_Marks(90,80,"dhoni")
##print(output)
# Here it is returning none because we have not given anything in the return statement its just a emty return.


##def Student_Marks(eng,maths,student_name):
##    total = eng+maths
##    return
##    print("welcome")
##
##output = Student_Marks(90,80,"dhoni")
##print(output)
                   #return IS THE LAST EXECUTABLE STATEMENT OF ANY FUNCTION.
#Return statement is not mandatory.

##def Student_Marks(eng,maths,student_name):
##    total = eng+maths
##    return total

##output = Student_Marks(90,80,"dhoni") # Here when calling function we can see function is returning because we have given return total.
##print(output)

 #We can have n no of return statement

##def Student_Marks(eng,maths,student_name):
##    total = eng+maths
##    return total,student_name
##
##output = Student_Marks(90,80,"dhoni") 
##print(output)

#SCOPING - IT MEANS HOW DATA ARE ACCESSED.

##var = 100 #External Variable(Global)
##def fun():
##    var = 10
##    print(var) #Internal Variable

##print(var)
##fun()
##print(var)

var = 100 #External Variable(Global)
def fun():
    global var
    var = 10 # Internal variable
    print(var)

print(var)
fun()
print(var)

#to make all the variable work on a common principle without any local or global response.

##count = 0
##def fun():
##    global count
##    print("hello",count)
##    count = count + 1 
##    if count == 101:
##        return
##    fun()
##
##fun()

##count = 0
##def fun():
##    global count
##    print("hello",count)
##    count = count + 1 
##    if count < 100:
##        fun()
##        
##fun()

count = 0
def fun():
    global count
    print("hello",count)
    count = count + 1 
    while count < 100:
       fun()
       
fun()



























