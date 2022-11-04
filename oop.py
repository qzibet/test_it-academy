from abc import abstractmethod


class Axe:
    damage = 10
    strength = 10

    def __init__(self, rang):
        if rang == 'C':
            self.damage += 5

        elif rang == 'B':
            self.damage += 10
        
        elif rang == 'A':
            self.damage += 20

        elif rang == 'S':
            self.damage += 100
    
    @classmethod
    def change_url(cls, url):
        print('azazazaza')
        cls.base_url = url


class Katana:
    damage = 10
    strength = 7

    def __init__(self, rang):
        if rang == 'C':
            self.damage += 7

        elif rang == 'B':
            self.damage += 12
        
        elif rang == 'A':
            self.damage += 24

        elif rang == 'S':
            self.damage += 120


class Person:
    age = 17
    hp = 10
    lvl = 1
    base_url = 'instagram.com'

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def get_item(self, item):
        self.damage += item.damage

    @classmethod
    def change_age(cls, age):
        cls.age = age
    
    @classmethod
    def change_url(cls, url):
        cls.base_url = url
    
    @staticmethod
    def get_person_info(name, age):
        print('Просто класс человека, который мы можем дополнять')

    
    def level_up(self):
        self.damage += 15
        self.hp += 10
        self.lvl += 1
        print("Вы подняли свой lvl, ура!!!")

    

    def fast_level_up(self):
        self.damage += 1000
        self.hp += 1000
        self.lvl += 1
        print("Вы подняли свой lvl, ура!!!")



class Elf(Person, Axe):
    age = 600
    hp = 1000
    mana = 1000
    lvl = 1

    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def level_up(self):
        self.damage += 15
        self.hp += 10
        self.lvl += 1
        print("Вы подняли свой lvl, ура!!!")



Vadim = Person('Вадим', 10)
Azis = Person('Азис', 10)
admin = Person.level_up()

Person.change_age(30)


print(admin)
print(Vadim.age)
print(Azis.age)