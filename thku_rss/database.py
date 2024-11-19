import sqlite3

class database:
    def __init__(self, db_path:str):
	    self.cx = sqlite3.connect(db_path)
	    self.cu = self.cx.cursor()

    def create_table(self, table_name:str):
        self.cu.execute("CREATE TABLE IF NOT EXISTS '{}' ('TITLE' VARCHAR(200) NOT NULL, 'UPLOAD_DATE' DATE NOT NULL, 'LINK' VARCHAR(200) NOT NULL, PRIMARY KEY('TITLE'))".format(table_name))

    def get_item(self, title:str, table:str) -> tuple:
        return self.cu.execute("SELECT * FROM {} WHERE TITLE == '{}'".format(table, title)).fetchall()[0]

    def title_exists(self, title:str, table:str) -> bool:
        return len(self.cu.execute("SELECT * FROM {} WHERE TITLE == '{}'".format(table, title)).fetchall()) == 1

	
    def insert_item(self, item:tuple, table:str):
        self.cu.execute("INSERT INTO {} VALUES ('{}', '{}', '{}')".format(table, item[0], item[1], item[2]))
        self.cx.commit()
