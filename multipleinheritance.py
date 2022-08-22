class Elite:
    season= 3
    languAge="spanish"

class strangerThings: 
    season = 4
    language = "english"

class Dark(Elite,strangerThings):
    season =2
    languages="german"

jonathan=Dark()
print(jonathan.language)
