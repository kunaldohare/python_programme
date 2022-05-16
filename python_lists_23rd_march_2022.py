'''In python anything enclosed under square bracket is a list'''
''' In list any type of data can be stored'''
##var = []
##print(type(var))

##var = ["a","b",2,4,5.6]
##print(var[4])

##var = ["a","b",2,4,5.6]
##var[0] = "dhoni"
##print(var)

##var = ["a","B"]
##var1 = [1,2]
##print(var+var1)
# we can do list concatenation

##var = ["a","b",2,4,5.6]
##print(dir(var))

##var = ["a","b",2,4,5.6]
##var[0] = "dhoni"
##print(var)

'''insert function puts data into the provided index of list without deleting ,instead that data moves to next index''' 
##var = ["a","b",2,4,5.6]
##var.insert(0,"dhoni")
##print(var)

##var = ["a","b",2,4,5.6]
##var.insert(10,"dhoni")
##print(var)# Here it will not give error and it justs enter dhoni after the last index of the list

##var = ["a","b",2,4,5.6]
##var.remove("b") # remove function will remove the data from the parent list 
##print(var)

##var = ["a","b",2,4,5.6]
##var.pop(2)
##print(var)
 
''' append function add data after the last possible index'''
##var = ["a","b",2,4,5.6]
##var.append("dhoni")
##print(var)

##var = ["a","b",2,4,5.6]
##var.append("dhoni","kohli")
##print(var)
'''here if we run line no 33,34,35 we get error because append can take only one argument'''
'''list.append() takes exactly one argument (2 given)'''

##var = ["a","b",2,4,5.6]
##var.append(["dhoni","kohli"])
##print(var)

'extend method add multiple elements at the same time at the end of the list.
##var = ["a","b",2,4,5.6]
##var.extend([8,"age",4])
##print(var)

##var = ["a","b",2,4,5.6]
##var.extend("captain")
##print(var)

'sort function is used only for same data type of data and it will sort the list in alphabetical order.
##var = ["ant","india","bat","cricket","zoom"]
##var.sort()
##print(var)

##var = ["ant","india","bat","cricket","zoom"]
##var.sort(reverse=True)
##print(var)

##var = ["ant","india","bat","cricket","zoom"]
##output = sorted(var)
##print(output)

##var = [1,"a",3,4,5]
##var.clear()
##print(var)
'var.clear returns none value and its used to erase all the elements of list.

##var = [1,"a",3,4,5]
##var.remove("a")
##print(var)
'It removes an item from the list

##var = ["ant","india","bat","cricket","zoom",2,3,4,9]
##output = var.index("ant")
##print(output)

var = ["a","b",2,4,5.6]
var.remove(2)
for i in range(0,len(var)):
    print(var[i], end =" ")












