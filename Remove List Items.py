thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
thislist2 = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist2.remove("banana")
print(thislist2)
thislist3 = ["apple", "banana", "cherry"]
thislist3.pop(1)
print(thislist3)
thislist4 = ["apple", "banana", "cherry"]
thislist4.pop()
print(thislist4)
thislist5 = ["apple", "banana", "cherry"]
del thislist5[0]
print(thislist5)
"""
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".
"""
thislist6= ["apple", "banana", "cherry"]
thislist6.clear()
print(thislist6)