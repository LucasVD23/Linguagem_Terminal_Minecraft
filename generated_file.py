from EntitiesTable import EntitiesTable, Player, Mob

entities_table = EntitiesTable()

player1 = Player("player1")
print('Summoned new Player')
entities_table.add_entity(player1)

player2 = Player("player2")
print('Summoned new Player')
entities_table.add_entity(player2)

mob1 = Mob("mob1")
print("Summoned new Skeleton")
entities_table.add_entity(mob1)

players = entities_table.get_all_players()
for player in players:
	print('Given [WoodenSword] * 3 to ' + player.name)
print('Your game mode has been updated to Adventure Mode')
print("Changing to clear weather")
print("Set the time to 1000")
print('Teleported player1 to 2, 2, 2')
print("Set game difficulty to peaceful")
