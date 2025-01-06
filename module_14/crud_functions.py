import sqlite3 as sq


PATH_TO_DATABASE = 'module_14/not_telegram.db'


################ для модуля 14.4 #####################
def initiate_db():
    with sq.connect(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS Products (
                    id INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    description TEXT,
                    price INTEGER NOT NULL,
                    img TEXT
                    )
                """)
        #таблица юзеров для  модуля 14.5 (в БД создана ещё в модуле 14.1)
        cur.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER,
                balance INTEGER NOT NULL
                )
            """)
        
        
def add_product(title, description, price, img):
    with sq.connect(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO Products (title, description, price, img)
                    VALUES (?, ?, ?, ?)
                """, (title, description, price, img))
        conn.commit()
        
def get_all_products():
    with sq.connect(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("""
                    SELECT title, description, price, img FROM Products
                """)
        return cur.fetchall()

################ для модуля 14.5 #####################
def add_user(username, email, age, balance=1000):
    with sq.connect(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("""
                    INSERT INTO Users (username, email, age, balance)
                    VALUES (?, ?, ?, ?)
                """, (username, email, age, balance))
        conn.commit()

def is_included(username):
    with sq.connect(PATH_TO_DATABASE) as conn:
        cur = conn.cursor()
        cur.execute("""
                    SELECT username FROM Users WHERE username = :Username
                """, {"Username": username})
        return cur.fetchone()


if __name__ == '__main__':
    initiate_db()

    #заполнение БД, таблицы Products
    # for number in range(1, 5):
    #     with open(f'module_14/img/{number}.jpg', 'rb') as f:
    #         img = f.read()
    #         add_product(title=f'Продукт {number}', description=f'Описание продукта {number}', price=number*100, img=img)

