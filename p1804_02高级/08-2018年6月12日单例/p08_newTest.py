
class Car(object):
    def __init__(self):
        print ("init")
    def __new__(cls):
        print ('new')
        return object.__new__(cls)

Car()

