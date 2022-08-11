math=int(input("enter your marks"))
science=int(input("enter your marks"))
french=int(input("enter your marks"))
if(math<33 or science<33 or  french<33):
    print("you are fail")
elif((math+science+french)/3 <40):
    print("you are fail")
else:
    print("you are pass")
