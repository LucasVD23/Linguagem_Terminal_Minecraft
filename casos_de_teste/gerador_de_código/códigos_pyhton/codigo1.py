from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

mob1 = Mob("mob1")
print("Summoned new Skeleton")
entities_table.add_entity(mob1)

print('Given [DiamondBoots] * 3 to player1')
entities_table.kill_entity(player1.name)
print('Killed ' + player1.name)
entities_table.kill_entity(mob1.name)
print('Killed ' + mob1.name)
