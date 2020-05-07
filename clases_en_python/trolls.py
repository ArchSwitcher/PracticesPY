class Troll:
    type_troll = "Troll"
    color = "Red"
    mana = 50
    movement_speed = 75
    
    def __init__(self, **kwargs):
        self.hit_points = kwargs.get("hit_points",30)
        self.type_troll = kwargs.get("type_troll","Troll")
        
    def __str__(self):
        return "type_troll: {} \n   color: {} \n   hit_points: {} \n   mana: {} \n   movement_speed: {} \n   spell: {}".format(self.type_troll,self.color,self.hit_points,self.mana,self.movement_speed,self.spell)
    

class icetroll(Troll):
    color = "Blank_Blue"
    hit_points = 75
    mana = 350
    movement_speed = 30
    spell = "Ice Garou"

class Island_troll(Troll):
    color = "Black_Red"
    hit_points = 90
    mana = 400
    movement_speed = 35
    spell = "peak Garou"

class Swamp_Troll(Troll):
    color = "Dark_Green"
    hit_points = 110
    mana = 500
    movement_speed = 123
    spell = "ultra Garou"

class Normal_troll(Troll):
    pass


# TODO:
# icetroll
# islandTroll
# swamptroll

#return "the {} have {} hit points, yield {} experience points and they carry {}, ".format(self.vocation, self.hit_points, self.experience_points, self.droped_objects) + ("is " if (self.is_paralyzable) else "is not ") + "paralyzable, " + ("is " if (self.is_summonable) else "is not ") + "summonable, " + ("is " if (self.is_convencible) else "is not ") + "convencible.\n"