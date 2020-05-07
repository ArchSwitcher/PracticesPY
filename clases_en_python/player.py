class Player:
    vocation = "No vocation"
    spell = "Puff"
    movement_speed = 50

    def __init__ (self,**kwargs):
        self.name = input("Escribe tu  nombre: ")
        self.hit_points = kwargs.get("hit_points",50)
        self.mana = kwargs.get("mana",75)


    def __str__(self):
        return "User Name: {} \n  is: {} \n mana: {} \n hit_points: {} \n Spell: {} \n Movement_speed: {} \n".format(self.name, self.vocation,self.mana, self.hit_points, self.cast_spell(), self.movement_speed)

    def cast_spell(self):
        return self.spell
    

class Sorcered(Player):
    vocation = "Sorcered"
    spell = "Speliadum"
    movement_speed = 20

    def cast_spell(self):
        return "{} Injustice health ".format(self.spell)


class Knight(Player):
    vocation = "Knight"
    spell = "Ultra_punch"
    movement_speed = 60


class Druid(Player):
    vocation = "Druid"    
    spell = "Friendly_health"
    movement_speed = 40


class Paladin(Player):
    vocation = "Paladin"
    spell = "Double_punch"
    movement_speed = 100

class nada(Player):
    pass
