import sqlite3
conn = sqlite3.connect("computer_cards.db")

def create(name, cores, cpu_speed, ram, cost):
	insert_sql = "INSERT INTO computer(name, cores, cpu_speed, ram, cost) VALUES ('{}', '{}', '{}', '{}', '{}')".format(name,cores,cpu_speed,ram,cost)
	
	conn.execute(insert_sql)
	
	conn.commit()
	
def read(name):
	select_sql = "SELECT * from computer WHERE name = '{}'".format(name)
	result = conn.execute(select_sql)
	
	return result.fetchone()

def update(cores, cpu_speed, ram, cost, name):
	update_sql = "UPDATE computer SET cores = {}, cpu_speed = {}, ram = {}, cost = {} WHERE name = '{}'".format(cores,cpu_speed,ram,cost,name)
	
	conn.execute(update_sql)
	
	conn.commit()
	
	
def delete(name):
	delete_sql = "DELETE FROM computer WHERE name = '{}'".format(name)
	
	conn.execute(delete_sql)
	
	conn.commit()
		
command = input("Do you want to create, read, update or delete a card?")

if command.lower() == "create":
	name = input("Name >")
	cores = input("Cores >")
	cpu_speed = input("CPU speed (GHz) >")
	ram = input("RAM (MB) >")
	cost = input("Cost ($) >")

	create(name, cores, cpu_speed, ram, cost)
	
	print("Your card has been created")

elif command.lower() == "read":
	name = input("Enter the name of the card that you want to read. >")

	card = read(name)

	print(card)

elif command.lower() == "update":
	name = input("Enter the name of the card that you want to update >")
	cores = input("Cores >")
	cpu_speed = input("CPU speed (GHz) >")
	ram = input("RAM (MB) >")
	cost = input("Cost ($) >")
	
	update(cores, cpu_speed, ram, cost, name)
	
	print("Your card has been updated")
	
elif command.lower() == "delete":
	name = input("Enter the name of the card that you want to delete. >")
	
	delete(name)
	
	print("Your card has been deleted.")
	
all_computers = conn.execute("SELECT * FROM computer")
computers = all_computers.fetchall()

for computer in computers:
	print(computer)
	
conn.close()