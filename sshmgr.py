#!/usr/bin/env python3
from getch import *
from os import system

CONN_DB_PATH = "sshmgr-db"

def load_conns():
	conns = []
	with open(CONN_DB_PATH) as f:
		conns = [l.strip() for l in f.readlines()]
	return conns

def create_new(conns):
	name = input("Name the new connection: ")
	conns.append(name)

	save_conns(conns)

def save_conns(conns):
	with open(CONN_DB_PATH, 'w') as f:
		for conn in conns:
			f.write("{:s}\n".format(conn))

def get_connection(conns, c):
	try:
		num = int(c)
	except ValueError:
		print("Selection needs to be a number!")
		return False

	if num < 1 or num > len(conns):
		print("Selection not in range!")
		return False
	
	selection = conns[num - 1]
	return selection

def connect(connection):
	system("screen ssh {}".format(connection))
	
def delete_conn(conns):
	c = input("Which connection should be removed? ")
	deleted = get_connection(conns, c)
	if not deleted:
		print("Nothing was deleted.")
		getch()
		return

	conns = [conn for conn in conns if conn != deleted]
	save_conns(conns)	

def main():
	running = True
	while running:
		conns = load_conns()
		system("clear")

		print("Select connection: ")
		for i,conn in enumerate(conns):
			print("({:d}) {:s}".format(i + 1, conn))
		print("(n) New connection")
		print("(d) Delete connection")
		print("(q) Quit")

		c = getch()

		if (c == "q"):
			return
		elif (c == "d"):
			delete_conn(conns)
		elif (c == "n"):
			create_new(conns)
		else:
			connection = get_connection(conns, c)
			if not connection:
				print("Select a valid connection.")
				getch()
			else:
				connect(connection)
				return

if __name__ == "__main__":
	main()
