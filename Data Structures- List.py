#===================================================
#Python data type vs Data Structure 
#===================================================
# NOTE: You need to execute the code only once. Shortcut = Shift + Enter

#If we assign only one value, we call it data types 

#example: 

a =5
b =5.5
c='nit'
d = True 
e = i+2j

#data Structure -- user assigned more than 1 value is called datastructure 

#List , Tuple , set, dict, range
'''
1. List is defined using [] (square brackets)
#2. Lis t is growable 
#3. append() will allow user to add the element or value at the end of the list 
#4.You can declare multiple datatype inside the list. 
#5. List allows duplicates and it will append it to the end of the list. 
#6..append takes only one argument
#7. Index() return the index value 
#8. insert() insert the value before index . insert always we need to pass 2 arguemnt
# 9. extend()- extend from one list to another list 
# 10. copy list.
# 11. pop() by default it will remove  & print the last element value 
#     pop(3) it will remove only 3rd index position value  
#     pop() is index wise elimination 
# 12. remove() not index 

'''
l =[] 

#=============list and Tuple===============
l =[]
l

#In python we use .call the function
l1 = [ 10, 20, 30, 40]
print(l1) # OP: [ 10, 20, 30, 40]

print(len(l1))  # OP : 4 

print (l) #OP : []
print(l1) # OP: [ 10, 20, 30, 40]

l == l1 #OP: False 
l!=l1 #OP: True 
l.append(100)
l.append(100)
l.append(12.50)
l.append(True)
l.append(1+2j)
l.append([1,2,3])

print (l) # OP: [100, 100, 12.5, True, (1+2j), [1, 2, 3]]

print(100 in l ) #OP: True ( List Membership)
print(1000 in l ) #OP: False ( List Membership)


l.append(100) #Op: [100, 100, 12.5, True, (1+2j), [1, 2, 3], 100] 
# list allows duplicates. 

print (l) # OP: [100, 100, 12.5, True, (1+2j), [1, 2, 3], 100]
print(l1) #OP: [10, 20, 30, 40]

print(len(l)) # OP: 8
print(len(l1)) #OP: 4 

l.append(10,20) #OP: TypeError: list.append() takes exactly one argument (2 given)

l.count (100) # OP: 2 

l.count(12.5)  # OP:1

l.count(1000) # OP: 0


l2 = l1.copy() 

print (l) # OP: [100, 100, 12.5, True, (1+2j), [1, 2, 3], 100]
print(l1) #OP: [10, 20, 30, 4
print(l2) #OP: [10, 20, 30, 40]


l1.append(50)
print(l1) #OP: [10, 20, 30, 40, 50]
print(l2) #OP: [10, 20, 30, 40]


l2. clear() #clears the list but not the variables 

print (l) # OP: [100, 100, 12.5, True, (1+2j), [1, 2, 3], 100]
print(l1) #OP: [10, 20, 30, 4
print(l2) # OP: []

l.extend(l1) # Extends l data to l1
print(l) # OP: [100, 100, 12.5, True, (1+2j), [1, 2, 3], 100, 10, 20, 30, 40, 50]

l.index(10) #OP: 7 
l.index(100) # OP: 0 ( Even though they are multiple 100, it will give first index of 100)

l1.insert(1, 15 ) #Insert value in the index 1 and move index 1 value to right 
print(l1) # OP: [10, 15, 15, 20, 30, 40, 50]

l1.(4, 25)
print(l1) #  [10, 15, 15, 20, 25, 30, 40, 50]


l.pop() # The last element will be eliminated OP: 50


l.pop () #OP: 40 

l.pop(4) # Op 

l.remove(True) 
print (l) #  OP: [100, 100, 12.5, [1, 2, 3], 100, 10, 20, 30]

l.remove(True)  # If the values doesn't exist. We will get below error 
                # ValueError: list.remove(x): x not in list
