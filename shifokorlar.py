class Person:
    def __init__(self, ism, familiya, ssn):
        self.ism = ism
        self.familiya = familiya
        self.ssn = ssn

class NoSuchDoctor(Exception):
    pass

class Doctor(Person):
    def __init__(self, ism, familiya, ssn, id, mutaxassisligi):
        super().__init__(ism, familiya, ssn)
        self.id = id
        self.mutaxassisligi = mutaxassisligi

    def getID(self):
        return self.id

    def getMutaxassisligi(self):
        return self.mutaxassisligi

class Clinic:
    def __init__(self):
        self.shifokorlar = []

    def addDoctor(self, shifokor):
        self.shifokorlar.append(shifokor)

    def getDoctor(self, id):
        for shifokor in self.shifokorlar:
            if shifokor.getID() == id:
                return shifokor
        raise NoSuchDoctor("Shifokor topilmadi")


clinic = Clinic()


shifokor1 = Doctor("Ismi", "Familiyasi", "SSN raqami", "Shifokor ID raqami", "Mutaxassisligi")
clinic.addDoctor(shifokor1)

try:
    shifokor = clinic.getDoctor("Shifokor ID raqami")
    print(shifokor.ism, shifokor.familiya, shifokor.getMutaxassisligi())
except NoSuchDoctor as e:
    print("Shifokor topilmadi:", str(e))
