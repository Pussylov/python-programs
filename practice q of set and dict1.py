#Q1 WAP to crete a dictionary of hindi words to english

myDict = {
    "Becharm": "fool",
    "papa": "father",
    "vastu": "mother",
    "ishtar": "god"
} 
print("options are ",myDict.keys())
a = input("enter the word\n")
print("the meaning of your word is :",myDict.get(a))
