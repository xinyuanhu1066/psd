from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from user_manager import add_student, view_students

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Add Student")
    print("4. View All Students")
    print("5. Search User by Name")
    print("6. Delete User by ID")
    print("7. Exit")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-7): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name: ")
            address = input("Enter address: ")
            add_student(name, address)
        elif choice == '4':
            students = view_students()
            for student in students:
                print(student)
        elif choice == '5':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '6':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
