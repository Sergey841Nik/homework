import sqlite3 as sq


with sq.connect('module_14/not_telegram.db') as conn:
    cur = conn.cursor()
    # Код из предыдущего задания
    # cur.execute("""
    #             CREATE TABLE IF NOT EXISTS Users (
    #             id INTEGER PRIMARY KEY,
    #             username TEXT NOT NULL,
    #             email TEXT NOT NULL,
    #             age INTEGER,
    #             balance INTEGER NOT NULL
    #             )
    #         """)
    # for i in range(1, 11):
    #     cur.execute("""
    #                 INSERT INTO Users (username, email, age, balance)
    #                 VALUES (?, ?, ?, ?)
    #                 """, (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

    # cur.execute("""
    #             UPDATE Users SET balance =:Balance
    #             WHERE id % 2 <> 0
    #             """, {"Balance": 500})
    
    # for i in range(1, 11, 3):
    #     cur.execute("""
    #                 DELETE FROM Users
    #                 WHERE id = :id
    #                 """, {"id": i})

    # cur.execute("""
    #             SELECT username, email, age, balance 
    #             FROM Users 
    #             WHERE age <> 60
    #             """)
    
    # users = cur.fetchall() 
    # for user in users:
    #     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

    # Удаление пользователя с id=6
    cur.execute("""
                DELETE FROM Users
                WHERE id = 6
                """)
    
    # Подсчёт кол-ва всех пользователей
    cur.execute("SELECT COUNT(*) FROM Users")
    total_users = cur.fetchone()[0]
    
    # Подсчёт суммы всех балансов
    cur.execute("SELECT SUM(balance) FROM Users")
    all_balances = cur.fetchone()[0]

    print(all_balances / total_users)
    
    conn.commit()
    
    
    
    