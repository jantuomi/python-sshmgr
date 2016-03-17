#!/usr/bin/env python3
from os import system
from sshmgr.utils.getch import getch
import os.path
import argparse

class Manager:

	CONN_DB_PATH = os.path.join(os.path.expanduser("~"), ".sshmgr-db")
	
	def __init__(self):
		pass

	def load_conns(self):
		conns = []
		try:
			with open(self.CONN_DB_PATH) as f:
				conns = [l.strip() for l in f.readlines()]
		except FileNotFoundError:
			with open(self.CONN_DB_PATH, 'w') as f:
				conns = []
		except:
			print("Could not load connections from file. ({:s})".format(self.CONN_DB_PATH))
			getch()

		return conns

	def create_new(self, conns):
		name = input("Name the new connection: ")
		conns.append(name)

		self.save_conns(conns)

	def save_conns(self, conns):
		with open(self.CONN_DB_PATH, 'w') as f:
			for conn in conns:
				f.write("{:s}\n".format(conn))

	def get_connection(self, conns, c):
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

	def connect(self, connection):
		system("screen ssh {}".format(connection))
		
	def delete_conn(self, conns):
		c = input("Which connection should be removed? ")
		deleted = self.get_connection(conns, c)
		if not deleted:
			print("Nothing was deleted.")
			getch()
			return

		conns = [conn for conn in conns if conn != deleted]
		self.save_conns(conns)	

	def run(self):
		running = True
		while running:
			conns = self.load_conns()
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
				self.delete_conn(conns)
			elif (c == "n"):
				self.create_new(conns)
			else:
				connection = self.get_connection(conns, c)
				if not connection:
					print("Select a valid connection.")
					getch()
				else:
					self.connect(connection)
					return

def start():
	parser = argparse.ArgumentParser(description="Simple text GUI tool for managing SSH connections.")
	parser.add_argument('--db-path', help="set the path to the data file", default="~/.sshmgr-db")
	args = parser.parse_args()

	Manager.CONN_DB_PATH = os.path.expanduser(args.db_path)

	s = Manager()
	s.run()

if __name__ == "__main__":
	start()
