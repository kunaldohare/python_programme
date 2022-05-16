##data="90"
##print(data)
##print(type(data))

##data="netzwerk"
##print(data)
##print(type(data))

##data=('academy')
##print(data)
##print(type(data))

##data='academy'
##print(data)
##print(type(data))

##data=("academy")
##print(data)
##print(type(data))
##      
##data="""this is programming langauage"""
##print(data)
##print(type(data))
##
##data='''this is programming language'''
##print(data)
##print(type(data))

##'''Below line is used for declearing string data'''

##data='''India is my country \
##and i love my country'''
##print(data)
##print(type(data))

##data="Hello Saad \nHello Saad"
##print(data)

x = 75
def myfunc():
    global x
    x = x + 1
    print(x)
myfunc()
print(x)












name="dhoni"
age=33
##data = "My captain plays even at the age of"

##data= "My captain" +name+ " plays even at the age of" +age
##print(data)
''' Integer cannot be concatenate int to str'''

##data="My captain " +name+" plays even at the age of " + str(age)
##print(data)
''' here in these two lines str(age) is used to concatenate integer with string'''

##data= "My captain %s plays even at the age of %d"%(name,age)
##print(data)
'''Here in these two lines of code %s is for storing string and %d is for integer and %(name,age) is for string and integer value'''

##data= "My  captain %s plays even at the age of %d"%(name,name)
##print(data)
''' In these two lines if we run we get type error as %d format: a real number is required, not str'''

##data= "My  captain %s plays even at the age of %d"%(age,age)
##print(data)

##data= "My  captain {} plays even at the age of {}".format(name,age)
##print(data)

##data= f"My  captain {name} plays even at the age of {age}"
##print(data)

##data= "%s %d"%(name,age)
##print(data)











