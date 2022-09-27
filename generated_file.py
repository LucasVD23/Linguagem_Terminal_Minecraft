from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

player2 = Player("player2")
print('Summoned new Player')
entities_table.add_entity(player2)

player3 = Player("player3")
print('Summoned new Player')
entities_table.add_entity(player3)

mob1 = Mob("mob1")
print("Summoned new Spider")
entities_table.add_entity(mob1)

mob2 = Mob("mob2")
print("Summoned new Enderman")
entities_table.add_entity(mob2)

print('Given [IronSword] * 1 to player1')
print('Given [IronHelmet] * 1 to player2')
print('Given [IronChestplate] * 1 to player2')
print('Given [IronLeggings] * 1 to player2')
print('Given [IronBoots] * 1 to player2')
entities_table.kill_entity(mob1.name)
print('Killed ' + mob1.name)
entities_table.kill_entity(mob2.name)
print('Killed ' + mob2.name)
print("Set the time to 1000")
