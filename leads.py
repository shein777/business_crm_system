from database import get_connection


def add_lead():
    customer_name = input("Enter customer name: ")
    status = input("Enter lead status (New/Contacted/Closed): ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO leads (customer_name, status)
        VALUES (%s, %s)
    """

    cursor.execute(query, (customer_name, status))

    connection.commit()

    cursor.close()
    connection.close()

    print("Lead added successfully!")


def view_leads():
    connection = get_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM leads"

    cursor.execute(query)

    leads = cursor.fetchall()

    for lead in leads:
        print(lead)

    cursor.close()
    connection.close()


def update_lead_status():
    lead_id = input("Enter lead ID: ")
    new_status = input("Enter new status (New/Contacted/Closed): ")

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        UPDATE leads
        SET status = %s
        WHERE id = %s
    """

    cursor.execute(query, (new_status, lead_id))

    connection.commit()

    cursor.close()
    connection.close()

    print("Lead status updated successfully!")