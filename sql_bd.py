import sqlite3
class DateBaseSQL():
    db_name : str = "SQL.db" #наименование базы данных
    def __init__(self, name = None):
        self.con = sqlite3.connect(name or self.db_name) #подключаемся к бд
        self.cur = self.con.cursor() #создаём курсор к которому будем обращаться
        self.create_table() #ссылка на метод класса

    def set(self, name, score):
        db_score = self.get(name=name) #ссылка на метод
        if score is not None or score > db_score:
            self.cur.execute(f'DELETE FROM stocks WHERE name="{name}"') # удаляем из stocks где имя = переменной name
            self.cur.execute(f"INSERT INTO stocks VALUES ('{name}', {score})") #вставляем в stocks значения
            self.con.commit()# подтверждаем действие
    def get(self, name=None, limit =5):
        if name:

            rows = self,cur.execute(f'SELECT score FROM stocks WHERE name= "{name}" ORDER BY score')
            rows = list(rows)

            return rows [0] [0] if rows else None
        scores = list(self.cur.execute(f'SELECT * FROM stocks ORDER BY score DESC LIMIT {limit}'))
        return scores

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS stocks (name. text, score int)''')
        self.con.commit()
