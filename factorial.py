# n = int(input("enter the factorial number : "))
# product=1
# for i in range(n):
#     product = product*(i+1)
# print(product)
def preet(n):
    product=1
    for i in range(n):
        product = product*(i+1)
    return product 
print(preet(5))

#recursive 
def factorial_recursive(n):
    if n ==0 or n ==1:
        return 1
    return n*factorial_recursive(n-1)
f=factorial_recursive(5)
print(f)