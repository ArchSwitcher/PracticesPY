import player
import trolls


# knight = player.Knight(hit_points=80,mana=20)
# sorcered = player.Sorcered(hit_points=40,mana=80)
# druid= player.Druid(hit_points = 60, mana=75)
# paladin = player.Paladin(hit_points = 150, mana = 50)
# ultra_Druid = player.Druid()

# ultra_Druid.vocation = "Ultra Druid"
# ultra_Druid.spell = "ULTRA_INSTIC"

# print(knight)
# print(sorcered)
# print(druid)
# print(paladin)
# print(ultra_Druid, "injustice shit xD \n \n")

# 

troll_type = int(input("1 2 3:"))

if troll_type == 1:
    troll = trolls.icetroll(hit_points=50,type_troll = "ICETROLL")
elif troll_type == 2:
    troll = trolls.Swamp_Troll(hit_points = 150,type_troll = "SWAMPTROLL")
elif troll_type == 3:
    troll = trolls.Island_troll(hit_points = 300,type_troll = "ISLANDTROLL")


print(troll)
