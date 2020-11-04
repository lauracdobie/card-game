import sqlite3
from random import randint
from time import time
conn = sqlite3.connect("computer_cards.db")

def read(name):
	select_sql = "SELECT * from computer WHERE name = '{}'".format(name)
	result = conn.execute(select_sql)
	
	return result.fetchone()

def read_all_cards():
	result = conn.execute("SELECT * FROM computer")
	return result.fetchall()

def insert_picked(name):
	insert_sql = "INSERT INTO picked(name, time) VALUES ('{}', {})".format(name, time())
	conn.execute(insert_sql)
	conn.commit()
	
def read_last_picked():
	result = conn.execute("SELECT * FROM picked ORDER BY time DESC")
	return result.fetchone()
	
def pick_card():
	cards = read_all_cards()
	
	last_picked_card = read_last_picked()
	
	random_card = cards[randint(0, len(cards) - 1)]

	while random_card[0] == last_picked_card[0]:
		random_card = cards[randint(0, len(cards) - 1)]

	insert_picked(random_card[0])
	return random_card


def read_all_picked():
	result = conn.execute("SELECT * FROM picked")
	return result.fetchall()

def card1_name():
	picked = read_all_picked()
	card1 = picked[len(picked) - 2]
	
	return card1[0]

def card2_name():
	picked = read_all_picked()
	card2 = picked[len(picked) - 1]
	
	return card2[0]
	
#print(card1_name())
#print(card2_name())

def get_card1():
	card1 = card1_name()
	cards = read_all_cards()
	for card in cards:
		if card[0] == card1:
			return(card)

def get_card2():
	card2 = card2_name()
	cards = read_all_cards()
	for card in cards:
		if card[0] == card2:
			return(card)
			
#print(get_card1())
#print(get_card2())

def log_card1_winner():
	card1 = card1_name()
	card2  = card2_name()
	
	insert_sql = "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card1, card2, card1)
	conn.execute(insert_sql)
	conn.commit()
	
def log_card2_winner():
	card1 = card1_name()
	card2  = card2_name()
	
	insert_sql = "INSERT INTO result(card1, card2, winner) VALUES ('{}', '{}', '{}')".format(card1, card2, card2)
	conn.execute(insert_sql)
	conn.commit()
	
def compare_feature():
	card1_wins = 0
	card2_wins = 0
	
	card1 = get_card1()
	card2 = get_card2()
	
	card1_name = card1[0]
	card2_name = card2[0]
	
	feature = int(input("What do you want to play on? Type 1 for cores, 2 for CPU speed, 3 for RAM, or 4 for cost > "))
	
	
	if card1[feature] > card2[feature]:
		log_card1_winner()
		print(str(card1_name) + " wins! Woop woop!")
		card1_wins +=1
		print("This card has won " + str(card1_wins) + " times.")
	elif card1[feature] < card2[feature]:
		log_card2_winner()
		print(str(card2_name) + " wins! Huzzah!")
		card2_wins +=1
		print("This card has won " + str(card2_wins) + " times.")
	else:
		print("It's a tie!")
		
# compare_feature()
		
def play_game():
	player1_card = pick_card()
	print(player1_card)
	
	player2_card = pick_card()
	print(player2_card)
	
	compare_feature()
	
play_game()
	
	
	
conn.close()

			







