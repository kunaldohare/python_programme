##var = {}
##print(var)
##print(type(var))

##var ={"dhoni",33}
##print(var)
##print(type(var))

#dictionary always exist with a key pair.

##var ={"name":"dhoni", "age":33}
##print(var)
##print(type(var))

##var ={"name":"dhoni", "age":33}
##print(var[0])
#No index based direct data retrieval in dictionary

#In dictionary datas are manipulated or used via key
#Dictionary is called key value pair
#because each data we use needs to be stored with specfic key
# storing data with key is generally called as "Hashing" or "HashTable"

##var ={"name":"dhoni", "age":33}
##print(var["age"])

##var = {"name":"dhoni", "age":33}
##var["name"] = "kohli"
##print(var)
#Dictionary is mutable type

##var ={"name":"dhoni", "age":33,"name":"arjun"}
##print(var)

#keys should always be unique otherwise it will rewrite
#Dictionary is " Un ordered Collection"

##var ={"name":"dhoni", 9:33,98.9:"arjun",("a","b"):"veena",True:"rahul"}
##var["name"] = "kohli"
##print(var)

##var = {"name":"dhoni"}
##var["country"] = "india"
##print(var)
# Data is added in this way to dictionary

##var = {"name":"dhoni","team":"csk"}
##output = var["team"]
##print(output)

##var = {"name":"dhoni","team":"csk"}
##var1 = {"age":33}
##output = var + var1
##print(output)
#We cannot concatenate dictionary using +sign

##var = {"name":"dhoni","team":"csk"}
##var1 = {"age":33}
##var2 = {"lan":"eng"}
##output = {**var,**var1,**var2}
##print(output)
# SO we concatenate dictionary using **syntax

var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
print(var)

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var["team"][1]
##print(output)

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##var["name"][1] = "rohit"
##print(var)

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var["country"]
##print(output)
##print(welcome)

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var.get("country")
##print(output)
##print("welcome")

##var = {"name":["dhoni","kohli"],"team":("csk","rcb"),"sports":{"cricket":["sachin","dravid"]}}
##output = var.get("country","sorry key not found")
##print(output)
##print("welcome")




























    
