from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

mob1 = Mob("mob1")
print("Summoned new Creeper")
entities_table.add_entity(mob1)

print('Your game mode has been updated to Survival Mode')
print('Given [IronSword] * 1 to player1')
entities_table.kill_entity(mob1.name)
print('Killed ' + mob1.name)
print('Teleported player1 to 2, 2, 2')
print("Set the time to 1000")
print("Set game difficulty to hard")
print("Changing to rain weather")
