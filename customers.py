from database import get_connection


def add_customer():
    name = input("Enter customer name: ")

    if name == "":
        print("Customer name cannot be empty!")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO customers (name, phone, email)
        VALUES (%s, %s, %s)
    """

    cursor.execute(query, (name, phone, email))

    connection.commit()

    cursor.close()
    connection.close()

    print("Customer added successfully!")


def view_customers():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM customers"

    cursor.execute(query)

    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    cursor.close()
    connection.close()

def update_customer():
    customer_id = input("Enter customer ID to update: ")
    name = input("Enter new customer name: ")
    phone = input("Enter new phone number: ")
    email = input("Enter new email: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE customers
        SET name = %s, phone = %s, email = %s
        WHERE id = %s
    """

    cursor.execute(query, (name, phone, email, customer_id))

    connection.commit()

    cursor.close()
    connection.close()

    print("Customer updated successfully!")


def delete_customer():
    customer_id = input("Enter customer ID to delete: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = "DELETE FROM customers WHERE id = %s"

    cursor.execute(query, (customer_id,))

    connection.commit()

    cursor.close()
    connection.close()

    print("Customer deleted successfully!")


def search_customer():
    search_name = input("Enter customer name to search: ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT * FROM customers
        WHERE name LIKE %s
    """

    cursor.execute(query, (f"%{search_name}%",))

    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    cursor.close()
    connection.close()