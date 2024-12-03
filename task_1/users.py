import sqlite3

connection = sqlite3.connect('users.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    second_name TEXT,
    age INTEGER,
    email TEXT)
    '''
)


def polychenie(user_id):
    data = cursor.execute(
        f'''
        SELECT * FROM users
        where id = {user_id}
        ''')
    return list(data)


def sending(first_name, second_name, age, email):
    cursor.execute(
        '''
    INSERT INTO users(first_name,second_name,age,email) 
    VALUES (?,?,?,?)
    ''', (first_name, second_name, age, email))
    connection.commit()


