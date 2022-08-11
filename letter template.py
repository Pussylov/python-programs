letter='''Dear <|name|>,
you are selected !

Date:<|DATE|>
'''
name = input("Enter your name\n")
date= input("Enter date  ")
letter = letter.replace("<|name|>", name)
letter = letter.replace("<|DATE|>",date)
print(letter)