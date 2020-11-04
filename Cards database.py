import sqlite3
conn = sqlite3.connect("computer_cards.db")

result = conn.execute("SELECT * FROM computer WHERE ram = 512 ORDER BY cost")

computers = result.fetchall()

for computer in computers:
	print(computer)
	
conn.close()