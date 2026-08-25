import bcrypt
from database import get_connection


def register_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    password_bytes = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO users (username, password_hash)
        VALUES (%s, %s)
    """

    cursor.execute(query, (username, hashed_password))

    connection.commit()

    cursor.close()
    connection.close()

    print("User registered successfully!")

def login_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT password_hash, role
        FROM users
        WHERE username = %s
    """

    cursor.execute(query, (username,))

    user = cursor.fetchone()

    if user is None:
        print("Username not found!")
    else:
        stored_hash = user[0].encode("utf-8")
        role = user[1]

        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            print("Login successful!")
            print("Role:", role)
        else:
            print("Incorrect password!")

    cursor.close()
    connection.close()

