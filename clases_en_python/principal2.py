from player import Player
from player import Sorcered
from player import Knight

sorcered = Sorcered()          #llamada a Sorcered el cual heredo valores de la clase Player
sorcered.vocation = "noce"    #ya tiene un valor por defecto en la superclase Sorcered

knight = Knight(hit_points=500,mana=2500)
knight.spell = "Ultra_SHIT"


print(sorcered)
print(knight)