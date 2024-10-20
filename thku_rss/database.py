import sqlite3

class database:
	def __init__(self, db_path:str):
		self.cx = sqlite3.connect(db_path)
		self.cu = self.cx.cursor()

	def get_item(self, title:str, table:str) -> tuple:
		return self.cu.execute("SELECT * FROM {} WHERE TITLE == '{}'".format(table, title)).fetchall()[0]


	def title_exists(self, title:str, table:str) -> bool:
		return len(self.cu.execute("SELECT * FROM {} WHERE TITLE == '{}'".format(table, title)).fetchall()) == 1

	
	def insert_item(self, item:tuple, table:str):
		self.cu.execute("INSERT INTO {} VALUES ('{}', '{}', '{}', '{}')".format(table, item[0], item[1], item[2], item[3]))
		self.cx.commit()
