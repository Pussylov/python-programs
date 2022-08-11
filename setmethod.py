b = set()
print(type(b))
# putting the values in the set
b.add(4)
b.add(5)
# cannot add list and dict 
#hashable : something which can be changed 
# sets are unordered,un indexed
print(b)

#find the length of the set 
print(b.__len__())# length of the set

# remove the element from the set
b.remove(5)
print(b)

# removes random number
print(b.pop())
print(b)
