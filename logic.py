import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database # имя базы данных
        
    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''CREATE TABLE project
                                    (project_id INTEGER PRIMARY KEY,
                                    user_id INTEGER,
                                    project_name TEXT,
                                    description TEXT,
                                    url TEXT,
                                    status_id INTEGER,
                                    FOREIGN KEY(status_id) REFERENCES status(status_id))''')
            
            conn.execute('''CREATE TABLE skills
                                    (skills_id INTEGER PRIMARY KEY,
                                    skils_name TEXT,
                                    )''')
            
            conn.execute('''CREATE TABLE project_skills
                                    (skills_id INTEGER FFOREIGN KEY,
                                    project_id INTEGER FK,
                                    )''')
            
            conn.execute('''CREATE TABLE status
                                    (status_id INTEGER PRIMARY KEY,
                                    status_name TEXT,
                                    )''')
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            conn.commit()