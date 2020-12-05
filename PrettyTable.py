# Create relational tables in Python

# pip install prettytable

from prettytable import PrettyTable

# Specify the Column Name while initializing the Table
myTable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# Add rows
myTable.add_row(["Leanord", "X", "B", "91.2%"])
myTable.add_row(["Penny", "X", "C", "63.5%"])
myTable.add_row(["Howard", "X", "A", "90.23%"])
myTable.add_row(["Bernadette", "Y", "D", "92.7%"])
myTable.add_row(["Sheldon", "Y", "A", "98.2%"])
myTable.add_row(["Raj", "Y", "B", "88.1%"])
myTable.add_row(["Amy", "Y", "A", "95.0%"])
print(myTable)
