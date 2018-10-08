class Singleton(object): # is safer to keep object notation otherwise singleton patter is not correctily 
                         # implemanted if you omit the reference to  object
    __instance = None
    def __new__(cls, val=None):
        if Singleton.__instance is None:
           Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance 
         
s = Singleton()

s.val = 'chips'

print s.val

f = Singleton()

s==f

# f.val = 333
print f.val
print s.val  


class Borg(object):
    """docstring for Borg"""
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

b = Borg()
c = Borg()

b.ddd = "test"

print b.ddd
print c.ddd   

c.ddd = "patata"

print b.ddd
print c.ddd     