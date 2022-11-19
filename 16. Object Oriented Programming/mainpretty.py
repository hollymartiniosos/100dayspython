import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")
print(table)

table.align["Type"] = "r"

print(table)

