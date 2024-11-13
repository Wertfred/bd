import sqlite3

def init_db():
    conn = sqlite3.connect('pass.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pass (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fio TEXT UNIQUE NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_user(fio, status):
    conn = sqlite3.connect('pass.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO pass(fio, status) 
                      VALUES (?, ?)''', (fio, status))
    conn.commit()
    conn.close()

def update_user(id, fio, status):
    conn = sqlite3.connect('pass.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pass SET fio = ?, status = ?
        WHERE id = ?
    ''', (fio, status, id))
    conn.commit()
    conn.close()

def delete_user(id):
    conn = sqlite3.connect('pass.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM pass WHERE id = ?', (id))
    conn.commit()
    conn.close()

def print_id(id):
    conn = sqlite3.connect('pass.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM pass WHERE id = ?', (id))
    data = cursor.fetchone()
    conn.close()
    return data

if __name__ == '__main__':
    init_db()

    zapros = input("Введите функцию update,delete,insert,print: ")
    while zapros != "exit":
        if zapros == "update":
            id = (input("Введите id для обновления: "))
            fio = input("Введите новое ФИО: ")
            status = input("Введите новую должность: ")
            update_user(id, fio, status)

        elif zapros == "delete":
            id = (input("Введите id для удаления: "))
            delete_user(id) 
        elif zapros == "insert":
            fio=input("Введите ФИО: ")
            status=input("Введите должность: ")
            insert_user(fio, status)

        elif zapros == "print":
            id = (input("Введите id пользователя: "))
            data = print_id(id)  
            if data:
                print("Данные пользователя:")
                print(f"ID: {data[0]}")
                print(f"ФИО: {data[1]}")
                print(f"должность: {data[2]}")
            else:
                print(f"Пользователь с id {id} не найден.")
        elif zapros == "exit":
                break
        zapros = input("Введите функцию update,delete,insert,print: ")
            