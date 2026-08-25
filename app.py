from auth import register_user, login_user
from customers import (
    add_customer,
    view_customers,
    update_customer,
    delete_customer,
    search_customer
)
from leads import add_lead, view_leads, update_lead_status


while True:

    print("\n===== Business CRM System =====")
    print("1. Register")
    print("2. Login")
    print("3. Add Customer")
    print("4. View Customers")
    print("5. Update Customer")
    print("6. Delete Customer")
    print("7. Search Customer")
    print("8. Add Lead")
    print("9. View Leads")
    print("10. Update Lead Status")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register_user()

    elif choice == "2":
        login_user()

    elif choice == "3":
        add_customer()

    elif choice == "4":
        view_customers()

    elif choice == "5":
        update_customer()

    elif choice == "6":
        delete_customer()

    elif choice == "7":
        search_customer()

    elif choice == "8":
        add_lead()

    elif choice == "9":
        view_leads()

    elif choice == "10":
        update_lead_status()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")