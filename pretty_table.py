from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Subjects',['Mathematics',"Physics","Chemistry"])
table.add_column('Marks Obtained',[90,88,77])

print(table)