class singleton:
    singletoninstance = None

    @staticmethod
    def getinstance():
        if(singletoninstance == None):
            singletone()
        return singletoninstance
        
    def __init__(self):
        if(singletoninstance == None):
            singleton.singletoninstance = self
        else:
            raise Exception ("there are more than 1 instance")
