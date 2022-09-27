from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

print("Changing to sunny weather")
print('Teleported player1 to 2, 2, <missing NUM_INT>')
print("Set game difficulty to veryhard")
