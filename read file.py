a = open('poem.txt','r')
data = a.read()
if 'twinkle' in data:
    print("true")
else:
    print("false")
print(data)
a.close()