class Greetings:
    name="Manoj"
    def __init__(self):
        self.x="Hello"
        self.__z="Good afternoon"
    def getx(self):
        return self.x+self.name
    def getz(self):
        return self.__z+self.name
g= Greetings()
print(g.getx())
print(g.name+g.getz())