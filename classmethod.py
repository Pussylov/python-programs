class loosers:
    work="nothing"
    confidence=100

    @classmethod
    def changeconfidence(cls,con):
        cls.confidence=con

     
gottago=loosers()
print(gottago.confidence)
gottago.changeconfidence(200)
print(loosers.confidence)