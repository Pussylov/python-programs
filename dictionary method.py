myDict = {
"fast" : "in a quick manner",
"slow" :  "traveler",
"anotherDict": {"preet":"traveler"},
"marks": [45,90],
1:2
}
# print(list(myDict.keys()))
# print(myDict.values())# print the values of my dict
# print(myDict.items())# print all the (key,value) of the dictionary
updateDict = {
    "Arjit": "singer",
    "slow": "dancer"
} # it updates the (key,value)
myDict.update(updateDict)
print(myDict)
print(myDict.get("slow2"))# return none
print(myDict["slow2"]) #return error
