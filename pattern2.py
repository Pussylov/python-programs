# a=int(input("enter the number of pattern you want"))

# for i in range(a):
#     print("1"*(i+1))

a=5
for i in range(a):
    print("* "*(a-i))

a=5
for i in range (a):
    print(" "*(a-i),end=" ")
    print("* "*(i+1))