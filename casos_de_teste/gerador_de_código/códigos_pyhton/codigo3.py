from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

p1 = Player("p1")
print('Summoned new Player')
entities_table.add_entity(p1)

print("Set the time to 15000")
print('Your game mode has been updated to Creative Mode')
print("Changing to snow weather")
print("Set game difficulty to easy")
print('Given [WoodenAxe] * 2 to p1')
entities_table.kill_entity(p1.name)
print('Killed ' + p1.name)
end1 = Mob("end1")
print("Summoned new Enderman")
entities_table.add_entity(end1)

entities_table.kill_entity(end1.name)
print('Killed ' + end1.name)
