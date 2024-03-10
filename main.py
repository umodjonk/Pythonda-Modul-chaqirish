class Transport:
    def __init__(self,module,brend):
        self=module
        self=brend

    def speed(self):
        pass

    def ves(self):
        pass

    def Kuch(self):
        pass

class Car(Transport):
    def speed(self):
        return "S/460"
    def ves(self):
        return "4.2 t"

    def Kuch(self):
        return "800.o"

class Bout(Transport):
    def speed(self):
        return "S/380"

    def ves(self):
        return "200000.o"


class Airfly(Transport):
    def speed(self):
        return "S/1800"

    def ves(self):
        return "30 t"

    def Kuch(self):
        return "2000000.o"

car=Car('Sport',"Bugatti")
bout=Bout("matlida","Boin")
airfily=Airfly('b30','Boin')

print(car.speed())
print(bout.speed())
print(airfily.speed())

