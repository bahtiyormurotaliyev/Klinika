class Person:
    def __init__(self, ism, familiya, ssn):
        self.ism = ism
        self.familiya = familiya
        self.ssn = ssn

class NoSuchPatient(Exception):
    pass

class Clinic:
    def __init__(self):
        self.bemorlar = []

    def addPatient(self, bemor):
        self.bemorlar.append(bemor)

    def getPatient(self, ssn):
        for bemor in self.bemorlar:
            if bemor.ssn == ssn:
                return bemor
        raise NoSuchPatient("Bemor topilmadi")

    def removePatient(self, ssn):
        for bemor in self.bemorlar:
            if bemor.ssn == ssn:
                self.bemorlar.remove(bemor)
                return
        raise NoSuchPatient("Bemor topilmadi")

    def updatePatient(self, ssn, ism, familiya):
        for bemor in self.bemorlar:
            if bemor.ssn == ssn:
                bemor.ism = ism
                bemor.familiya = familiya
                return
        raise NoSuchPatient("Bemor topilmadi")


clinic = Clinic()

bemor1 = Person("Abdushukr", "Abuqodirov", "203")
clinic.addPatient(bemor1)

try:
    bemor = clinic.getPatient("203")
    print(bemor.ism, bemor.familiya)
except NoSuchPatient as e:
    print("Bemor topilmadi:", str(e))


try:
    clinic.removePatient("203")
except NoSuchPatient as e:
    print("Bemor topilmadi:", str(e))

try:
    clinic.updatePatient("204", "ALi", "Saliyev")
except NoSuchPatient as e:
    print("Bemor topilmadi:", str(e))
