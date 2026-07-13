class Shaxs:
    __num_shaxs = 0

    def __init__(self, name, idraqam, tyil, familya, jins):
        self.name = name
        self.idraqam = idraqam
        self.tyil = tyil
        self.familya = familya
        self.__jins = jins
        Shaxs.__num_shaxs += 1

    def get_info(self):
        return self.name, self.idraqam, self.tyil, self.familya

    @classmethod
    def shaxs(cls):
        return cls.__num_shaxs

    def get_jins(self):
        if self.__jins:
            return "erkak"
        else:
            return "Ayol"


class Talaba(Shaxs):
    __num_talaba = 0

    def __init__(self, name, idraqam, tyil, familya, jins, id, fanlar, kg):
        super().__init__(name, idraqam, tyil, familya, jins)
        self.id = id
        self.fanlar = []
        self.bosqich = 1
        self.__kg = kg
        Talaba.__num_talaba += 1

    def get_info(self):
        return (f"{self.bosqich} bosqich talabasi {self.name} {self.familya}\nPasport raqami {self.idraqam},  "
                f"{self.tyil}-yilda tug'ilgan ")

    @classmethod
    def talabalar_son(cls):
        return cls.__num_talaba

    def get_age(self, yil):
        age = yil - self.tyil
        return f"{age}  yoshda "

    def get_kg(self):
        return self.__kg

    def add_kg(self, kg):
        self.__kg += kg
        return self.__kg

    def fanga_yozil(self, Fan):
        self.fanlar.append(Fan)

    def remove_fan(self, Fan):
        if Fan in self.fanlar:
            self.fanlar.remove(Fan)
        else:
            print("Bu fanga yozilmagansiz")


shaxs1 = Shaxs("Ali", 212223, 2005, "Aliyev", True)
print(shaxs1.get_info())
print(shaxs1.get_jins())
talaba1 = Talaba(
    "Ali",
    212223,
    2005,
    "Aliyev",
    True,  # Erkak
    "T001",
    [],
    70
)

print(talaba1.get_jins())
print(talaba1.add_kg(40))
print(talaba1.talabalar_son())
print(shaxs1.shaxs())
