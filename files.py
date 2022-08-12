# a = open('sample.txt','r')
# # a = open('sample.txt') by default it used read mode
# data = a.read(6)# reads first fve character
# print(data)
# a.close()
#  # to read lines we use readline()
# #  mode are read(r) write(w) append(a) update(+)


f=open('this.text','a')
f.write("hello there")
f.close()